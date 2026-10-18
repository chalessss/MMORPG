"""Simulador de las especializaciones del nivel 20 (aproximación por rol).

Desde el nivel 20 no se busca paridad: el simulador solo sirve de referencia de
que cada rol cumple su papel (docs/ESTADISTICAS_NIVEL_20.md, 1.0d). Lee los
datos de datos/nivel20/ y prueba cada especialización en:

  - Caza individual: mobs de uno en uno.
  - Conglomerados: grupos de 6 y de 12 mobs que pegan todos a la vez y se
    matan en área (todos los mobs del grupo entran en cada habilidad de área).
  - Jefe: 20 minutos contra un objetivo de vida casi infinita, por encima y por
    debajo del 20 % de vida (fase de remate).

Uso:
  python3 simular20.py           muestra los resultados
  python3 simular20.py --ficha   muestra la ficha de estadísticas del nivel 20
"""

import csv
import random
import sys
from pathlib import Path

DATOS = Path(__file__).parent / "datos" / "nivel20"
PASO = 0.1  # segundos por paso de la simulación
MUERTES_MAXIMAS = 20  # si muere tantas veces, se da por hecho que no puede con esa caza

# Tipos de mob en rotación: (a distancia, ciclo de golpes).
TIPOS_MOB = [(False, (1, 1, 2)), (True, (1, 1, 2)), (False, (1, 1, 2)), (True, (1, 1, 2))]
# Grupos que se prueban en la caza en grupo.
GRUPOS = [("Trío", ["combatiente", "mago", "invocador"]),
          ("Grupo de 5", ["combatiente", "invocador", "mago", "atacante", "asesino"])]
# Qué habilidades base usa cada especialización (habilidades 1-4).
GRUPO_BASE = {"luchador": "melee", "combatiente": "melee", "asesino": "melee",
              "atacante": "rango", "mago": "magico", "invocador": "magico"}


def leer(nombre):
    with open(DATOS / nombre, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(texto, defecto=None):
    try:
        return float(texto)
    except (TypeError, ValueError):
        return 0.0 if defecto is None else defecto


def cargar():
    parametros = {p["parametro"]: num(p["valor"], p["valor"]) for p in leer("parametros.csv")}
    armas = {a["arma"]: a for a in leer("armas.csv")}
    return parametros, armas, leer("especializaciones.csv"), leer("conversion.csv"), leer("habilidades.csv")


def habilidades_de(esp, habilidades):
    """Las 8 habilidades de una especialización: las 1-4 de su clase de inicio
    (con las que sustituya) y las 5-8 propias."""
    base = {h["ranura"]: h for h in habilidades if h["especializacion"] == GRUPO_BASE[esp]}
    for h in habilidades:
        if h["especializacion"] == esp:
            base[h["ranura"]] = h
    return [base[r] for r in sorted(base)]


def ficha(esp, parametros, armas, conversion, habilidades):
    """Estadísticas del nivel 20: los 370 puntos repartidos según la
    especialización y convertidos con su pasiva de especialización."""
    p = parametros
    reparto = {e: num(esp[e]) for e in ("str", "agi", "int")}
    puntos = {e: round(p["puntos_totales"] * v / sum(reparto.values())) for e, v in reparto.items()}
    por_punto = {}
    for c in conversion:
        if c["especializacion"] in ("todas", esp["especializacion"]):
            por_punto[(c["estadistica"], c["secundaria"])] = num(c["por_punto"])
    s = {}
    for (estadistica, secundaria), valor in por_punto.items():
        s[secundaria] = s.get(secundaria, 0) + puntos[estadistica] * valor
    lista = habilidades_de(esp["especializacion"], habilidades)
    pasivas = {h["tipo"]: h for h in lista}
    critico = s.get("critico_pct", 0) + (3 if "Ojo de Halcón" in [h["nombre"] for h in lista] else 0)
    if "arma_critico" in pasivas:
        critico += num(pasivas["arma_critico"]["valor"])
    defensa = s.get("defensa_fisica_pct", 0)
    armadura = p["armadura"]
    if "arma_defensa" in pasivas:
        defensa += num(pasivas["arma_defensa"]["valor"])
        armadura += 500
    arma = armas[esp["arma"]]
    intervalo = num(arma["segundos_entre_golpes"])
    if "arma_velocidad" in pasivas:
        intervalo *= 1 - num(pasivas["arma_velocidad"]["valor"]) / 100
    regen_mana = p["regen_mana_base"] + s.get("regen_mana", 0)
    if "arma_hechizos" in pasivas:
        regen_mana *= 1.2
    if "arma_apoyo" in pasivas:
        # La pasiva de arma del Invocador también da maná por segundo por cada punto de INT.
        regen_mana += p["apoyo_regen_mana_por_int"] * puntos["int"]
    regen_vida = p["regen_vida_base"] + s.get("regen_vida", 0)
    if "robo_vida" in pasivas and pasivas["robo_vida"]["nombre"] == "Sed de sangre":
        regen_vida += 0.1 * puntos["str"]
    mult_dano = 1.0
    if "arma_dano" in pasivas:
        mult_dano += num(pasivas["arma_dano"]["valor"]) / 100
    mult_hechizos = 1.0
    if "arma_hechizos" in pasivas:
        mult_hechizos += num(pasivas["arma_hechizos"]["valor"]) / 100
    return {
        "esp": esp, "puntos": puntos, "habilidades": lista, "pasivas": pasivas,
        "vida": round(p["vida_base"] + s.get("vida", 0)),
        "mana": round(p["mana_base"] + s.get("mana", 0)),
        "regen_vida": round(regen_vida * 5) / 5, "regen_mana": round(regen_mana * 5) / 5,
        "defensa": defensa, "armadura": armadura,
        "plano": s.get("dano_base", 0), "base": 1 + s.get("dano_base_pct", 0) / 100,
        "habilidad": 1 + s.get("dano_habilidad_pct", 0) / 100,
        "prob_critico": min(p["critico_base_pct"] + critico, p["tope_critico_pct"]) / 100,
        "mult_critico": 1 + min(p["critico_aumentado_base_pct"] + s.get("critico_aumentado_pct", 0),
                                p["tope_critico_aumentado_pct"]) / 100,
        "arma": arma, "intervalo": intervalo, "dano_arma": num(arma["dano"]),
        "mult_dano": mult_dano, "mult_hechizos": mult_hechizos,
        "robo_vida": num(pasivas["robo_vida"]["valor"]) / 100 if "robo_vida" in pasivas else 0,
        "celeridad": 1 - num(pasivas["celeridad"]["valor"]) / 100 if "celeridad" in pasivas else 1,
        "apoyo": 1 + num(pasivas["arma_apoyo"]["valor"]) / 100 if "arma_apoyo" in pasivas else 1,
        "mult_amenaza": p["amenaza_tanque_mult"] if esp["recurso"] == "ira_recibida" else 1,
        # Pasiva de arma del Invocador: más daño contra monstruos (no contra jefes).
        "contra_monstruos": 1 + p["apoyo_dano_monstruos_pct"] / 100 if "arma_apoyo" in pasivas else 1,
    }


class Personaje:
    """Un personaje dentro de un combate: sus estadísticas (la ficha), lo que le
    queda de vida y maná, sus recursos y lo que está haciendo."""

    def __init__(self, f, combate, controla_agro=False):
        self.f, self.c, self.p = f, combate, combate.p
        # Con control del agro, no lanza áreas que le quitarían el agro al tanque.
        self.controla_agro = controla_agro
        self.recurso = f["esp"]["recurso"]
        self.con_basico = f["esp"]["ataque_basico"] == "1"
        self.a_distancia = f["esp"]["a_distancia"] == "1"
        self.activas = [h for h in f["habilidades"] if h["tipo"] in ("dano", "area", "zona", "canal", "cura", "escudo")]
        self.listo = {h["nombre"]: 0.0 for h in self.activas}
        self.e = {"vida": f["vida"], "mana": f["mana"], "dano": 0.0, "muertes": 0, "pociones_vida": 0,
                  "pociones_mana": 0, "curado": 0.0, "escudado": 0.0, "golpes_recibidos": 0, "usos": {}}
        self.r = {"ira": 0.0, "energia": 100.0, "foco": 0.0, "trance": 0.0, "trance_hasta": -1.0, "esencia": 0.0}
        self.estado = {"ocupado": 0.0, "pendiente": None, "canal": None, "escudo": 0.0, "escudo_hasta": -1.0,
                       "energia_desgarro": 0.0, "caido_hasta": -1.0}
        self.pocion = {"vida": 0.0, "mana": 0.0}

    @property
    def nombre(self):
        return self.f["esp"]["nombre"]

    def vivo(self):
        return self.c.t >= self.estado["caido_hasta"]

    def mejora(self, h, base):
        return base ** (num(h["nivel_habilidad"], 1) - 1)

    def coste(self, h):
        """Coste de maná: un valor exacto (hechizos de Mago e Invocador) y/o un % del
        maná máximo (el resto), que sube con cada nivel de la habilidad."""
        base = num(h["coste_mana"]) + num(h["coste_mana_pct"]) * self.f["mana"] / 100
        return round(base * self.mejora(h, 1 + self.p["mejora_coste_pct"] / 100))

    def usar(self, nombre):
        self.e["usos"][nombre] = self.e["usos"].get(nombre, 0) + 1

    def beber(self, tipo):
        if self.pocion[tipo] > self.c.t:
            return
        maximo = self.f["vida"] if tipo == "vida" else self.f["mana"]
        self.e[tipo] = min(maximo, self.e[tipo] + self.p[f"pocion_{tipo}"])
        self.e[f"pociones_{tipo}"] += 1
        self.pocion[tipo] = self.c.t + self.p["enfriamiento_pocion_s"]

    def golpe(self, base, es_habilidad, magico=False, porcentaje=None):
        """Daño de un impacto (sin crítico). Con `porcentaje`, el % de la habilidad
        se aplica al golpe entero (arma + daño plano), como en las de área."""
        f = self.f
        if porcentaje is None:
            d = (base + f["plano"]) * f["base"] * f["mult_dano"]
        else:
            d = (f["dano_arma"] + f["plano"]) * porcentaje * f["base"] * f["mult_dano"]
        if es_habilidad:
            d *= f["habilidad"]
        if not self.c.jefe:
            d *= f["contra_monstruos"]
        if magico:
            d *= f["mult_hechizos"]
            if self.c.t < self.r["trance_hasta"]:
                d *= 1 + self.p["trance_dano_pct"] / 100
        return d

    def pegar(self, mob, d, robo=1.0):
        if self.c.azar.random() < self.f["prob_critico"]:
            d *= self.f["mult_critico"]
        d = round(d)
        util = min(d, max(mob["vida"], 0))
        mob["vida"] -= d
        self.e["dano"] += util
        # Amenaza (aggro): cada punto de daño suma amenaza en ese mob (el tanque, multiplicada).
        mob["amenaza"][self] = mob["amenaza"].get(self, 0) + util * self.f["mult_amenaza"]
        # El robo de vida cuenta en cada mob golpeado; algunas habilidades lo reducen (robo < 1).
        if self.f["robo_vida"] and not self.c.sin_dano:
            self.e["vida"] = min(self.f["vida"], self.e["vida"] + util * self.f["robo_vida"] * robo)

    def curar(self, cantidad):
        antes = self.e["vida"]
        self.e["vida"] = min(self.f["vida"], self.e["vida"] + cantidad)
        return self.e["vida"] - antes

    def escudar(self, cantidad, duracion, sumar=False):
        if sumar and self.c.t < self.estado["escudo_hasta"]:
            self.estado["escudo"] += cantidad
        else:
            self.estado["escudo"] = cantidad
        self.estado["escudo_hasta"] = max(self.estado["escudo_hasta"], self.c.t + duracion)

    def contar_hechizo(self):
        r = self.r
        if self.recurso == "trance" and self.c.t >= r["trance_hasta"]:
            r["trance"] += self.p["trance_por_hechizo"]
            if r["trance"] >= 100:
                r["trance"] = 0
                r["trance_hasta"] = self.c.t + self.p["trance_duracion_s"]
        if self.recurso == "esencia":
            r["esencia"] = min(100, r["esencia"] + 5)

    def recibir(self, d):
        """Recibe el golpe de un mob (ya con defensa y armadura)."""
        if self.c.t < self.estado["escudo_hasta"] and self.estado["escudo"] > 0:
            absorbido = min(d, self.estado["escudo"])
            self.estado["escudo"] -= absorbido
            d -= absorbido
        self.e["vida"] -= d
        self.e["golpes_recibidos"] += 1
        if self.recurso == "ira_recibida":
            self.r["ira"] = min(100, self.r["ira"] + self.p["ira_por_golpe_recibido"])

    def resolver(self, accion):
        """Aplica el efecto de una habilidad (al terminar de lanzarla)."""
        h, mult, objetivo = accion
        f, p, c = self.f, self.p, self.c
        self.usar(h["nombre"])
        magico = h["unidad"] == "puntos"
        if h["tipo"] == "cura":
            # Cura un % de la vida máxima del aliado; si cura a otro, el Invocador se cura
            # la mitad de ese % (o, si no le falta vida, se la da a otro aliado al que le falte).
            pct = num(h["valor"]) / 100 * f["apoyo"] * (1 + self.r["esencia"] * 0.3 / 100)
            self.r["esencia"] = 0
            curado = objetivo.curar(objetivo.f["vida"] * pct)
            if objetivo is not self:
                otro = self if self.e["vida"] < f["vida"] else c.mas_herido(excluir=(objetivo,))
                if otro:
                    curado += otro.curar(otro.f["vida"] * pct / 2)
            self.e["curado"] += curado
            # Curar también genera amenaza en todos los mobs (una parte de lo curado).
            for m in c.vivos:
                if m["vida"] > 0:
                    m["amenaza"][self] = m["amenaza"].get(self, 0) + curado * p["amenaza_cura_pct"] / 100
            return
        if h["tipo"] == "escudo":
            # Sobre un aliado: el aliado recibe el escudo entero y quien lo lanza una parte.
            cantidad = f["vida"] * num(h["valor"]) / 100 * f["apoyo"]
            objetivo.escudar(cantidad, num(h["duracion"]))
            self.e["escudado"] += cantidad
            if objetivo is not self:
                self.escudar(cantidad * p["escudo_propio_pct"] / 100, num(h["duracion"]))
            return
        objetivos = [m for m in c.vivos if m["vida"] > 0] if h["tipo"] == "area" else [objetivo]
        for valor in h["golpes"].split("|"):
            if h["tipo"] == "area" and h["unidad"] == "arma":
                d = self.golpe(0, True, porcentaje=num(valor))
            else:
                d = self.golpe(num(valor) * (f["dano_arma"] if h["unidad"] == "arma" else 1), True, magico)
            d *= mult * self.mejora(h, 1 + p["mejora_dano_pct"] / 100)
            for m in objetivos:
                if m["vida"] > 0:
                    self.pegar(m, d, num(h.get("robo_vida_pct"), 100) / 100)
        if h["nombre"] in str(p["habilidades_provocan"]).split("|"):
            # Provocación: todos los mobs a su alcance le atacan a él durante unos segundos,
            # tengan la amenaza que tengan; después vuelven con quien más amenaza tenga.
            for m in c.vivos:
                if m["vida"] > 0:
                    m["provocado_hasta"], m["provocador"] = c.t + p["provocacion_s"], self
                    if p["provocacion_iguala_amenaza"]:
                        # Provocación clásica: su amenaza sube hasta la más alta de ese mob.
                        m["amenaza"][self] = max([m["amenaza"].get(self, 0)] + list(m["amenaza"].values()))
        if h["mecanica"] == "desgarro":
            # El sangrado depende de la Energía gastada (100 / 70 / 50 % del arma en 6 s).
            gastada = self.estado["energia_desgarro"]
            tramo = 1.0 if gastada >= 70 else 0.7 if gastada >= 40 else 0.5
            c.sangrados.append({"quien": self, "mob": objetivo, "dano": self.golpe(f["dano_arma"] * tramo / 6, True),
                                "fin": c.t + 6, "proximo": c.t + 1})
        if magico:
            self.contar_hechizo()

    def elegir(self):
        """Siguiente acción cuando el personaje está libre."""
        f, p, c, e, r = self.f, self.p, self.c, self.e, self.r
        objetivo = c.objetivo_para(self)
        if objetivo is None:
            return None
        n = sum(1 for m in c.vivos if m["vida"] > 0)
        candidatas = []
        for h in self.activas:
            nombre = h["nombre"]
            if self.listo[nombre] > c.t:
                continue
            coste = self.coste(h)
            if coste > e["mana"]:
                if coste <= f["mana"]:
                    self.beber("mana")
                continue
            tipo, mec = h["tipo"], h["mecanica"]
            if tipo == "cura":
                herido = c.mas_herido()
                if herido and herido.e["vida"] < herido.f["vida"] * p["curar_bajo_pct"] / 100 and not c.sin_dano:
                    return (h, 1.0, herido, 1e9)
                continue
            if tipo == "escudo":
                # Se escuda a quien están golpeando los mobs (a sí mismo, o al más golpeado si es apoyo).
                golpeado = c.mas_golpeado()
                if f.get("apoyo", 1) > 1:
                    destino = golpeado
                else:
                    destino = self if any(c.objetivo_de(m) is self for m in c.vivos if m["vida"] > 0) else None
                if (destino and not c.sin_dano and c.t >= destino.estado["escudo_hasta"]
                        and any(m["proximo"] <= c.t + 2 for m in c.vivos if m["vida"] > 0)):
                    return (h, 1.0, destino, 1e9)
                continue
            if num(h["coste_vida_pct"]) and e["vida"] - f["vida"] * num(h["coste_vida_pct"]) / 100 < f["vida"] * 0.5:
                continue
            mult = 1.0
            golpes = sum(num(g) for g in h["golpes"].split("|")) * (f["dano_arma"] if h["unidad"] == "arma" else 1)
            if mec == "requiere_ira" and r["ira"] < p["coste_ira_fisura"]:
                continue
            if mec == "requiere_energia" and (r["energia"] < p["coste_energia_cuchillas"] or n < 2):
                continue
            if mec == "desgarro" and r["energia"] < 70:
                continue
            if mec == "remate" and objetivo["vida"] < objetivo["max"] * p["remate_umbral_pct"] / 100:
                golpes = p["remate_dano"] * f["dano_arma"]
            # Solo, el Embate se guarda para cuando hay Ira; en grupo es su provocación y se usa en cuanto está.
            if mec == "embate" and r["ira"] < 60 and len(c.equipo) == 1:
                continue
            # Valor = daño estimado (con las estadísticas) por segundo que ocupa al personaje.
            magico = h["unidad"] == "puntos"
            if tipo in ("area", "zona") and h["unidad"] == "arma":
                por_golpe = sum(self.golpe(0, True, porcentaje=num(g)) for g in h["golpes"].split("|"))
            elif tipo == "zona":
                por_golpe = self.golpe(num(h["golpes"]) - f["plano"], True, magico=True)
            elif tipo == "canal":
                por_golpe = self.golpe(num(h["golpes"]) - f["plano"], True, magico=True) * num(h["valor"])
            elif mec == "remate" and golpes == p["remate_dano"] * f["dano_arma"]:
                por_golpe = self.golpe(golpes, True)
            else:
                por_golpe = sum(self.golpe(num(g) * (f["dano_arma"] if h["unidad"] == "arma" else 1), True, magico)
                                for g in h["golpes"].split("|"))
            if tipo == "zona":
                por_golpe *= num(h["valor"]) or num(h["duracion"])
            if self.controla_agro:
                ocupa_s = num(h["duracion"]) if tipo in ("canal", "zona") else num(h["lanzamiento"]) * f["celeridad"]
                if tipo in ("area", "zona", "canal"):
                    # Respeta la provocación: el área solo si todos los mobs siguen provocados
                    # por el tanque durante lo que tarda; si no, pausa (hechizos a un objetivo).
                    if any(m["vida"] > 0 and c.t + ocupa_s > m["provocado_hasta"] and c.quitaria_agro(self, por_golpe, m)
                           for m in c.vivos):
                        continue
                elif c.t + ocupa_s > objetivo["provocado_hasta"] and c.quitaria_agro(self, por_golpe, objetivo):
                    continue
            valor = por_golpe * (n if tipo in ("area", "zona", "canal") else 1)
            ocupa = (num(h["duracion"]) if tipo == "canal" else num(h["lanzamiento"]) if tipo == "zona"
                     else num(h["lanzamiento"]) * f["celeridad"] or (f["intervalo"] if self.con_basico else PASO))
            candidatas.append((h, mult, objetivo, valor / ocupa if ocupa else float("inf")))
        if not candidatas:
            return None
        h, mult, objetivo, valor = max(candidatas, key=lambda x: x[3])
        blanco = self.golpe(f["dano_arma"], False) / f["intervalo"] if self.con_basico else 0
        if self.con_basico and valor <= blanco:
            return None
        # No se gasta una habilidad de un solo objetivo si un golpe blanco ya lo mata.
        if self.con_basico and h["tipo"] == "dano" and objetivo["vida"] <= self.golpe(f["dano_arma"], False) and n == 1:
            return None
        return (h, mult, objetivo, valor)

    def lanzar(self, accion):
        h, mult, objetivo, _ = accion
        f, p, c, e, r = self.f, self.p, self.c, self.e, self.r
        self.listo[h["nombre"]] = c.t + num(h["enfriamiento"])
        e["mana"] -= self.coste(h)
        if num(h["coste_vida_pct"]):
            e["vida"] -= f["vida"] * num(h["coste_vida_pct"]) / 100
        mec = h["mecanica"]
        if mec == "remate" and objetivo["vida"] < objetivo["max"] * p["remate_umbral_pct"] / 100:
            self.listo[h["nombre"]] = c.t + p["remate_enfriamiento"]
            h = dict(h, golpes=str(p["remate_dano"]))
        # Recurso secundario que potencia la habilidad.
        if self.recurso == "ira_golpe" and h["tipo"] != "cura":
            mult *= 1 + r["ira"] * p["ira_por_punto_pct"] / 100
            r["ira"] = 0
        if mec == "requiere_ira":
            r["ira"] -= p["coste_ira_fisura"]
        if mec == "embate":
            mult *= 1 + r["ira"] * p["embate_por_ira_pct"] / 100
            r["ira"] = 0
        if mec == "requiere_energia":
            r["energia"] -= p["coste_energia_cuchillas"]
        if mec == "desgarro":
            self.estado["energia_desgarro"] = r["energia"]
            r["energia"] = 0
        if mec == "certero":
            mult *= 1 + r["foco"] * p["foco_por_punto_pct"] / 100
            r["foco"] = 0
        if h["tipo"] == "zona":
            # No interrumpe: tras su lanzamiento (si tiene) cae en la zona mientras el
            # personaje sigue con otras cosas. `valor` = número de impactos (si no, uno por segundo).
            self.usar(h["nombre"])
            impactos = num(h["valor"]) or num(h["duracion"])
            cada = num(h["duracion"]) / impactos
            c.zonas.append({"quien": self, "h": h, "fin": c.t + num(h["duracion"]), "proximo": c.t + cada,
                            "cada": cada, "mult": mult})
            if num(h["lanzamiento"]):
                self.estado["ocupado"] = c.t + num(h["lanzamiento"]) * f["celeridad"]
            if h["unidad"] == "puntos":
                self.contar_hechizo()
            return
        if h["tipo"] == "canal":
            ticks = int(num(h["valor"]))
            self.usar(h["nombre"])
            self.estado["canal"] = {"h": h, "quedan": ticks, "cada": num(h["duracion"]) / ticks,
                                    "proximo": c.t + num(h["duracion"]) / ticks, "mult": mult}
            self.estado["ocupado"] = c.t + num(h["duracion"])
            return
        lanzamiento = num(h["lanzamiento"]) * f["celeridad"]
        if h["unidad"] == "arma" and self.con_basico:
            # Sin tiempo de lanzamiento, la habilidad ocupa el hueco de un golpe blanco.
            lanzamiento = lanzamiento or f["intervalo"]
        self.estado["pendiente"] = (h, mult, objetivo)
        self.estado["ocupado"] = c.t + max(lanzamiento, PASO)

    def paso(self):
        """Un paso de tiempo: regenera, canaliza y, si está libre, actúa."""
        f, p, c, e, r, estado = self.f, self.p, self.c, self.e, self.r, self.estado
        if not self.vivo():
            return
        e["vida"] = min(f["vida"], e["vida"] + f["regen_vida"] * PASO)
        e["mana"] = min(f["mana"], e["mana"] + f["regen_mana"] * PASO)
        if self.recurso == "energia":
            r["energia"] = min(100, r["energia"] + (p["energia_regen"] + p["energia_regen_por_agi"] * f["puntos"]["agi"]) * PASO)
        canal = estado["canal"]
        if canal and canal["proximo"] <= c.t + 1e-9:
            canal["proximo"] += canal["cada"]
            canal["quedan"] -= 1
            # Los impactos de una canalización no suman el daño plano de la AGI (sería
            # sumarlo una vez por impacto y por mob).
            d = self.golpe(num(canal["h"]["golpes"]) - f["plano"], True, magico=True) * canal["mult"]
            for m in c.vivos:
                if m["vida"] > 0:
                    self.pegar(m, d, num(canal["h"].get("robo_vida_pct"), 100) / 100)
            if canal["quedan"] <= 0:
                estado["canal"] = None
                self.contar_hechizo()
        # Poción de maná en cuanto baja de la mitad (si no está en enfriamiento).
        if e["mana"] < f["mana"] * p["usar_pocion_mana_pct"] / 100:
            self.beber("mana")
        if c.t >= estado["ocupado"] and estado["canal"] is None:
            if estado["pendiente"]:
                self.resolver(estado["pendiente"])
                estado["pendiente"] = None
            hay_mobs = any(m["vida"] > 0 for m in c.vivos)
            accion = self.elegir() if hay_mobs else None
            if accion:
                self.lanzar(accion)
            elif self.con_basico and hay_mobs:
                objetivo = c.objetivo_para(self)
                self.pegar(objetivo, self.golpe(f["dano_arma"], False))
                self.usar("golpe blanco")
                if self.recurso == "ira_golpe":
                    r["ira"] = min(100, r["ira"] + p["ira_por_golpe"])
                if self.recurso == "foco":
                    r["foco"] = min(p["foco_maximo"], r["foco"] + p["foco_por_disparo"])
                estado["ocupado"] = c.t + f["intervalo"]


class Combate:
    """Uno o varios personajes contra una lista de grupos de mobs (cada grupo, una
    lista de vidas) que llegan uno detrás de otro. Todos los mobs pegan al
    personaje que tiene el aggro: el tanque (Combatiente) si lo hay; si no, el
    primero de la lista. Con `jefe`, el objetivo es un jefe (no cuentan los bonos
    contra monstruos); con `sin_dano`, los mobs no pegan."""

    def __init__(self, fichas, p, sin_dano=False, jefe=False, azar=None, controla_agro=False):
        self.p, self.sin_dano, self.jefe = p, sin_dano, jefe
        self.azar = azar or random.Random(int(p["semilla"]))
        self.t = 0.0
        self.vivos, self.zonas, self.sangrados = [], [], []
        self.muertos, self.descanso, self.caidas = 0, 0.0, 0
        # El control del agro es cosa de los demás: el tanque siempre pega todo lo que puede.
        self.equipo = [Personaje(f, self, controla_agro and f["esp"]["recurso"] != "ira_recibida") for f in fichas]
        # Orden del aggro: el tanque primero; después cuerpo a cuerpo; después el resto.
        self.aggro = sorted(self.equipo, key=lambda a: (a.recurso != "ira_recibida", a.a_distancia))

    def objetivo_de_mobs(self):
        """A quién va un mob que nadie ha tocado todavía: el tanque primero."""
        return next((a for a in self.aggro if a.vivo()), None)

    def objetivo_de(self, m):
        """A quién ataca un mob: a quien le provocó (mientras dure) o a quien más amenaza tiene."""
        if self.t < m["provocado_hasta"] and m["provocador"] and m["provocador"].vivo():
            return m["provocador"]
        candidatos = [(v, a) for a, v in m["amenaza"].items() if a.vivo() and v > 0]
        if candidatos:
            return max(candidatos, key=lambda x: x[0])[1]
        return self.objetivo_de_mobs()

    def mas_golpeado(self):
        """El personaje al que atacan más mobs ahora mismo."""
        cuenta = {}
        for m in self.vivos:
            if m["vida"] > 0:
                a = self.objetivo_de(m)
                if a:
                    cuenta[a] = cuenta.get(a, 0) + 1
        return max(cuenta, key=cuenta.get, default=None)

    def objetivo_para(self, quien):
        """A qué mob pega un personaje: el tanque, a los que se le escapan; con control del
        agro, a uno provocado por el tanque (si lo hay); si no, al primero que quede vivo."""
        vivos = [m for m in self.vivos if m["vida"] > 0]
        if quien.recurso == "ira_recibida" and len(self.equipo) > 1:
            # El tanque va primero a por los mobs que se le escapan (atacan a otro).
            sueltos = [m for m in vivos if self.objetivo_de(m) is not quien]
            if sueltos:
                return sueltos[0]
        if quien.controla_agro:
            provocados = [m for m in vivos if self.t < m["provocado_hasta"]]
            if provocados:
                return provocados[0]
        return vivos[0] if vivos else None

    def quitaria_agro(self, quien, dano_por_mob, solo=None):
        """¿Algún mob que no esté provocado pasaría a atacar a `quien` si le hace ese daño?
        Con `solo`, se mira únicamente ese mob (habilidades de un objetivo)."""
        for m in ([solo] if solo else self.vivos):
            if m["vida"] <= 0:
                continue
            # Aunque el mob esté provocado, al acabar la provocación iría a por quien más
            # amenaza tenga: se compara con la mayor amenaza de los demás.
            otros = max((v for a, v in m["amenaza"].items() if a is not quien and a.vivo()), default=0)
            if m["amenaza"].get(quien, 0) + dano_por_mob * quien.f.get("mult_amenaza", 1) > otros:
                return True
        return False

    def mas_herido(self, excluir=()):
        heridos = [a for a in self.equipo if a.vivo() and a not in excluir and a.e["vida"] < a.f["vida"]]
        return min(heridos, key=lambda a: a.e["vida"] / a.f["vida"], default=None)

    def empezar_grupo(self, vidas):
        objetivo = self.objetivo_de_mobs()
        self.vivos.clear()
        for i, v in enumerate(vidas):
            remoto, ciclo = TIPOS_MOB[(self.muertos + i) % len(TIPOS_MOB)]
            espera = 0 if remoto else (self.p["acercamiento_mob_s"] if objetivo.a_distancia
                                       else self.p["desplazamiento_melee_s"])
            self.vivos.append({"vida": v, "max": v, "proximo": self.t + espera, "ciclo": ciclo, "n": 0,
                               "amenaza": {}, "provocado_hasta": -1.0, "provocador": None})
        for a in self.equipo:
            if not a.a_distancia:
                a.estado["ocupado"] = self.t + self.p["desplazamiento_melee_s"]  # camina hasta el grupo

    def caer(self, quien):
        """Muere un personaje. Si era el último en pie, el grupo entero cae: se pierde
        tiempo, todos vuelven con todo lleno y los mobs se recuperan."""
        p = self.p
        quien.e["muertes"] += 1
        quien.estado.update(pendiente=None, canal=None, escudo=0.0)
        if any(a.vivo() for a in self.equipo if a is not quien):
            quien.estado["caido_hasta"] = self.t + p["penalizacion_muerte_s"]
            for m in self.vivos:
                m["amenaza"].pop(quien, None)
            quien.e["vida"], quien.e["mana"] = quien.f["vida"], quien.f["mana"]
            return
        self.caidas += 1
        self.t += p["penalizacion_muerte_s"]
        for a in self.equipo:
            a.e["vida"], a.e["mana"] = a.f["vida"], a.f["mana"]
            a.estado.update(pendiente=None, canal=None, ocupado=self.t, caido_hasta=-1.0)
        for m in self.vivos:
            m["vida"] = m["max"]
            m["proximo"] = self.t + 1
            m.update(amenaza={}, provocado_hasta=-1.0, provocador=None)
        self.zonas.clear()
        self.sangrados.clear()

    def pelear(self, grupos, limite_s=None, vida_inicial_pct=100):
        p = self.p
        indice = 0
        self.empezar_grupo(grupos[0])
        if vida_inicial_pct < 100:
            for m in self.vivos:
                m["vida"] = m["max"] * vida_inicial_pct / 100
        while limite_s is None or self.t < limite_s:
            self.t += PASO
            t = self.t
            # Golpes de los mobs: cada uno a quien tiene su agro.
            if not self.sin_dano:
                golpeados = []
                for m in self.vivos:
                    if m["vida"] > 0 and m["proximo"] <= t:
                        bruto = p["dano_mob"] * m["ciclo"][m["n"] % len(m["ciclo"])]
                        m["n"] += 1
                        m["proximo"] += p["intervalo_mob_s"]
                        objetivo = self.objetivo_de(m)
                        if objetivo:
                            f = objetivo.f
                            objetivo.recibir(max(1, round(bruto * (1 - f["defensa"] / 100)
                                                          - f["armadura"] / p["armadura_por_punto_de_dano"])))
                            if objetivo not in golpeados:
                                golpeados.append(objetivo)
                cayo_el_grupo = False
                for objetivo in golpeados:
                    if objetivo.e["vida"] < objetivo.f["vida"] * p["usar_pocion_vida_pct"] / 100:
                        objetivo.beber("vida")
                    if objetivo.e["vida"] <= 0 and objetivo.vivo():
                        caidas = self.caidas
                        self.caer(objetivo)
                        if self.caidas > caidas:
                            cayo_el_grupo = True
                            break
                if cayo_el_grupo:
                    if self.caidas >= MUERTES_MAXIMAS:
                        break  # no puede con este tipo de caza
                    continue
            # Zonas y sangrados.
            for z in self.zonas:
                if z["proximo"] <= t + 1e-9 and z["proximo"] <= z["fin"] + 1e-9:
                    z["proximo"] += z["cada"]
                    a, h = z["quien"], z["h"]
                    if h["unidad"] == "puntos":
                        # Impactos mágicos: sin el daño plano de la AGI en cada impacto.
                        d = a.golpe(num(h["golpes"]) - a.f["plano"], True, magico=True) * z["mult"]
                    else:
                        d = a.golpe(0, True, porcentaje=num(h["golpes"])) * z["mult"]
                    for m in self.vivos:
                        if m["vida"] > 0:
                            a.pegar(m, d, num(h.get("robo_vida_pct"), 100) / 100)
                    if h["mecanica"] == "escudo_aliados" and not self.sin_dano:
                        # Cada impacto escuda a los aliados (no a quien la lanza) con el daño que hace.
                        for aliado in self.equipo:
                            if aliado.vivo() and aliado is not a:
                                aliado.escudar(d, p["escudo_estrellas_s"], sumar=True)
                                a.e["escudado"] += d
            self.zonas[:] = [z for z in self.zonas if z["proximo"] <= z["fin"] + 1e-9]
            for s in self.sangrados:
                if s["proximo"] <= t <= s["fin"] + 1e-9:
                    s["proximo"] += 1
                    if s["mob"]["vida"] > 0:
                        s["quien"].pegar(s["mob"], s["dano"])
            self.sangrados[:] = [s for s in self.sangrados if s["fin"] > t]
            for a in self.equipo:
                a.paso()
            # ¿Grupo terminado?
            if all(m["vida"] <= 0 for m in self.vivos):
                self.muertos += len(self.vivos)
                indice += 1
                if indice >= len(grupos):
                    break
                self.zonas.clear()
                # Descanso si a alguien le quedó poca vida (o poco maná a quien depende de él).
                bajo = p["descansar_bajo_pct"] / 100
                mult = p["multiplicador_regen_descanso"]
                if any(a.e["vida"] < a.f["vida"] * bajo or (not a.con_basico and a.e["mana"] < a.f["mana"] * bajo)
                       for a in self.equipo):
                    dt = max(max((a.f["vida"] - a.e["vida"]) / (a.f["regen_vida"] * mult),
                                 (a.f["mana"] - a.e["mana"]) / (a.f["regen_mana"] * mult)) for a in self.equipo)
                    self.t += dt
                    self.descanso += dt
                    for a in self.equipo:
                        a.e["vida"], a.e["mana"] = a.f["vida"], a.f["mana"]
                self.empezar_grupo(grupos[indice])
        return self


def combatir(f, p, grupos, limite_s=None, sin_dano=False, vida_inicial_pct=100, azar=None, jefe=False):
    """Un solo personaje: devuelve sus resultados con el tiempo, los mobs muertos y el descanso."""
    c = Combate([f], p, sin_dano=sin_dano, jefe=jefe, azar=azar).pelear(grupos, limite_s, vida_inicial_pct)
    e = dict(c.equipo[0].e)
    e.update(tiempo=c.t, muertos=c.muertos, descanso=c.descanso, muertes=c.caidas)
    return e


def grupos_de(p, tamano):
    azar = random.Random(int(p["semilla"]))
    vidas = [round(p["vida_mob"] * (1 + azar.uniform(-0.1, 0.1))) for _ in range(int(p["mobs_por_prueba"]))]
    return [vidas[i:i + tamano] for i in range(0, len(vidas), tamano)]


def informe(parametros, armas, especializaciones, conversion, habilidades):
    p = parametros
    fichas = [ficha(esp, p, armas, conversion, habilidades) for esp in especializaciones]
    print(f"Nivel 20 · mob de {p['vida_mob']:.0f} de vida y {p['dano_mob']:.0f} de daño · "
          f"{p['mobs_por_prueba']:.0f} mobs por prueba\n")
    print("1) Jefe: daño por segundo durante 20 minutos (sin recibir daño)\n")
    print(f"{'Especialización':22}{'Por encima del 20 %':>21}{'Remate (< 20 %)':>17}")
    for f in fichas:
        normal = combatir(f, p, [[p["vida_jefe"]]], p["duracion_jefe_s"], sin_dano=True, jefe=True)
        remate = combatir(f, p, [[p["vida_jefe"]]], p["duracion_jefe_s"], sin_dano=True,
                          vida_inicial_pct=p["remate_umbral_pct"] - 1, jefe=True)
        print(f"{f['esp']['nombre']:22}{normal['dano'] / p['duracion_jefe_s']:>21.0f}"
              f"{remate['dano'] / p['duracion_jefe_s']:>17.0f}")
    for tamano in (1, 6, 12):
        print(f"\n2) Caza: grupos de {tamano} mob{'s' if tamano > 1 else ''}"
              f"{' (todos pegan a la vez)' if tamano > 1 else ''}\n")
        print(f"{'Especialización':22}{'Mobs/hora':>10}{'Muertes':>9}{'Poc. vida':>10}{'Poc. maná':>10}"
              f"{'Descanso':>10}  Usos")
        for f in fichas:
            r = combatir(f, p, grupos_de(p, tamano))
            horas = r["tiempo"] / 3600
            usos = ", ".join(f"{k} ×{v}" for k, v in sorted(r["usos"].items(), key=lambda x: -x[1]))
            if r["muertes"] >= MUERTES_MAXIMAS:
                print(f"{f['esp']['nombre']:22}{'no puede':>10}{r['muertes']:>9}  (muere {r['muertes']} veces "
                      f"tras matar {r['muertos']} mobs)")
                continue
            print(f"{f['esp']['nombre']:22}{r['muertos'] / horas:>10.0f}{r['muertes']:>9}{r['pociones_vida']:>10}"
                  f"{r['pociones_mana']:>10}{r['descanso'] / r['tiempo'] * 100:>9.0f}%  {usos}")
    print("\n3) En grupo (aproximación): 12 mobs que no le pegan (el tanque los aguanta)\n")
    print(f"{'Especialización':22}{'Mobs/hora':>10}{'Daño/s total':>14}")
    for f in fichas:
        if f["esp"]["recurso"] == "ira_recibida":
            print(f"{f['esp']['nombre']:22}  es quien recibe los golpes (su Ira sale de ahí): ver grupos de 12")
            continue
        r = combatir(f, p, grupos_de(p, 12), sin_dano=True)
        print(f"{f['esp']['nombre']:22}{r['muertos'] / (r['tiempo'] / 3600):>10.0f}{r['dano'] / r['tiempo']:>14.0f}")
    print("\n4) Grupo completo: el Combatiente provoca con Embate y lo alterna con Fisura; fuera de la provocación "
          "cada mob ataca a quien más amenaza tiene\n")
    por_id = {f["esp"]["especializacion"]: f for f in fichas}
    for nombre, ids in GRUPOS:
        equipo = [por_id[i] for i in ids]
        for controla in (False, True):
            print(f"{nombre}: {', '.join(f['esp']['nombre'] for f in equipo)} · "
                  f"{'con' if controla else 'sin'} control del agro")
            print(f"{'Mobs':>6}{'Mobs/hora':>11}{'Por miembro':>13}{'Caídas':>8}{'Descanso':>10}"
                  f"{'Curado/s':>10}{'Escudo/s':>10}{'Golpes al tanque':>18}  Muertes · reparto del daño")
            for tamano in (1, 6, 12):
                c = Combate(equipo, p, controla_agro=controla).pelear(grupos_de(p, tamano))
                if c.caidas >= MUERTES_MAXIMAS:
                    print(f"{tamano:>6}{'no puede':>11}  (el grupo cae {c.caidas} veces tras matar {c.muertos} mobs)")
                    continue
                horas = c.t / 3600
                total = sum(a.e["dano"] for a in c.equipo) or 1
                curado = sum(a.e["curado"] for a in c.equipo) / c.t
                escudo = sum(a.e["escudado"] for a in c.equipo) / c.t
                muertes = ", ".join(f"{a.nombre} {a.e['muertes']}" for a in c.equipo if a.e["muertes"]) or "nadie"
                reparto = ", ".join(f"{a.nombre} {a.e['dano'] / total * 100:.0f} %" for a in c.equipo)
                golpes = sum(a.e["golpes_recibidos"] for a in c.equipo) or 1
                al_tanque = c.aggro[0].e["golpes_recibidos"] / golpes * 100
                print(f"{tamano:>6}{c.muertos / horas:>11.0f}{c.muertos / horas / len(equipo):>13.0f}{c.caidas:>8}"
                      f"{c.descanso / c.t * 100:>9.0f}%{curado:>10.0f}{escudo:>10.0f}{al_tanque:>17.0f}%"
                      f"  muertes: {muertes} · {reparto}")
            print()
    print("Caídas = veces que cae el grupo entero · muertes = veces que muere cada uno (vuelve a los 30 s) · "
          "Por miembro = mobs/hora entre los miembros (la experiencia se reparte)")
    print("\nMobs/hora = mobs muertos por hora de caza (la experiencia es por mob) · Descanso = % del tiempo sentado")


def mostrar_ficha(parametros, armas, especializaciones, conversion, habilidades):
    print(f"{'Especialización':22}{'STR':>5}{'AGI':>5}{'INT':>5}{'Vida':>7}{'Reg/5s':>7}{'Maná':>7}{'Reg/5s':>7}"
          f"{'Defensa':>9}{'Armadura':>9}{'Crítico':>9}{'+Crítico':>9}{'Golpe':>7}")
    for esp in especializaciones:
        f = ficha(esp, parametros, armas, conversion, habilidades)
        golpe = round((f["dano_arma"] + f["plano"]) * f["base"] * f["mult_dano"]) if f["dano_arma"] else 0
        print(f"{esp['nombre']:22}{f['puntos']['str']:>5}{f['puntos']['agi']:>5}{f['puntos']['int']:>5}"
              f"{f['vida']:>7}{round(f['regen_vida'] * 5):>7}{f['mana']:>7}{round(f['regen_mana'] * 5):>7}"
              f"{f['defensa']:>8.1f}%{f['armadura']:>9.0f}{f['prob_critico'] * 100:>8.1f}%"
              f"{(f['mult_critico'] - 1) * 100:>8.1f}%{golpe:>7}")


def main():
    datos = cargar()
    if "--ficha" in sys.argv:
        mostrar_ficha(*datos)
    else:
        informe(*datos)


if __name__ == "__main__":
    main()
