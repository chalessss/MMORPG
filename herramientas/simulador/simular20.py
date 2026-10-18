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
    }


def combatir(f, p, grupos, limite_s=None, sin_dano=False, vida_inicial_pct=100, azar=None):
    """Pelea contra una lista de grupos de mobs (cada grupo, una lista de vidas)
    que llegan uno detrás de otro; todos los mobs de un grupo pegan a la vez.
    Devuelve el tiempo, los mobs muertos, el daño hecho y lo gastado."""
    azar = azar or random.Random(int(p["semilla"]))
    esp = f["esp"]["especializacion"]
    recurso = f["esp"]["recurso"]
    area_roba = esp in str(p.get("robo_vida_en_area", "")).split("|")
    con_basico = f["esp"]["ataque_basico"] == "1"
    a_distancia = f["esp"]["a_distancia"] == "1"
    activas = [h for h in f["habilidades"] if h["tipo"] in ("dano", "area", "zona", "canal", "cura", "escudo")]
    listo = {h["nombre"]: 0.0 for h in activas}

    def mejora(h, base):
        return base ** (num(h["nivel_habilidad"], 1) - 1)

    def coste(h):
        return round(num(h["coste_mana_pct"]) * f["mana"] / 100 * mejora(h, 1 + p["mejora_coste_pct"] / 100))

    e = {"t": 0.0, "vida": f["vida"], "mana": f["mana"], "dano": 0.0, "muertes": 0, "muertos": 0,
         "pociones_vida": 0, "pociones_mana": 0, "descanso": 0.0, "curado": 0.0, "usos": {}}
    r = {"ira": 0.0, "energia": 100.0, "foco": 0.0, "trance": 0.0, "trance_hasta": -1.0, "esencia": 0.0}
    estado = {"ocupado": 0.0, "pendiente": None, "canal": None, "escudo": 0.0, "escudo_hasta": -1.0,
              "energia_desgarro": 0.0}
    pocion = {"vida": 0.0, "mana": 0.0}
    zonas, sangrados = [], []

    def beber(tipo):
        if pocion[tipo] > e["t"]:
            return
        maximo = f["vida"] if tipo == "vida" else f["mana"]
        e[tipo] = min(maximo, e[tipo] + p[f"pocion_{tipo}"])
        e[f"pociones_{tipo}"] += 1
        pocion[tipo] = e["t"] + p["enfriamiento_pocion_s"]

    def golpe(base, es_habilidad, magico=False, porcentaje=None):
        """Daño de un impacto (sin crítico). Con `porcentaje`, el % de la habilidad
        se aplica al golpe entero (arma + daño plano), como en las de área."""
        if porcentaje is None:
            d = (base + f["plano"]) * f["base"] * f["mult_dano"]
        else:
            d = (f["dano_arma"] + f["plano"]) * porcentaje * f["base"] * f["mult_dano"]
        if es_habilidad:
            d *= f["habilidad"]
        if magico:
            d *= f["mult_hechizos"]
            if e["t"] < r["trance_hasta"]:
                d *= 1 + p["trance_dano_pct"] / 100
        return d

    def pegar(mob, d, roba=True):
        if azar.random() < f["prob_critico"]:
            d *= f["mult_critico"]
        d = round(d)
        util = min(d, max(mob["vida"], 0))
        mob["vida"] -= d
        e["dano"] += util
        # El robo de vida solo cuenta en el objetivo principal (no en cada mob del área),
        # salvo para quien lo tiene en área (el Combatiente: cuantos más mobs, más aguanta).
        if (roba or area_roba) and f["robo_vida"] and not sin_dano:
            e["vida"] = min(f["vida"], e["vida"] + util * f["robo_vida"])

    def contar_hechizo():
        if recurso == "trance" and e["t"] >= r["trance_hasta"]:
            r["trance"] += p["trance_por_hechizo"]
            if r["trance"] >= 100:
                r["trance"] = 0
                r["trance_hasta"] = e["t"] + p["trance_duracion_s"]
        if recurso == "esencia":
            r["esencia"] = min(100, r["esencia"] + 5)

    vivos = []

    def empezar_grupo(vidas):
        vivos.clear()
        for i, v in enumerate(vidas):
            remoto, ciclo = TIPOS_MOB[(e["muertos"] + i) % len(TIPOS_MOB)]
            espera = 0 if remoto else (p["acercamiento_mob_s"] if a_distancia else p["desplazamiento_melee_s"])
            vivos.append({"vida": v, "max": v, "proximo": e["t"] + espera, "ciclo": ciclo, "n": 0})
        if not a_distancia:
            estado["ocupado"] = e["t"] + p["desplazamiento_melee_s"]  # camina hasta el grupo

    def morir():
        e["muertes"] += 1
        e["t"] += p["penalizacion_muerte_s"]
        e["vida"], e["mana"] = f["vida"], f["mana"]
        for m in vivos:
            m["vida"] = m["max"]
            m["proximo"] = e["t"] + 1
        estado.update(pendiente=None, canal=None, ocupado=e["t"])
        zonas.clear()
        sangrados.clear()

    def resolver(accion):
        """Aplica el daño de una habilidad (al terminar de lanzarla)."""
        h, mult, objetivo = accion
        nombre = h["nombre"]
        e["usos"][nombre] = e["usos"].get(nombre, 0) + 1
        magico = h["unidad"] == "puntos"
        if h["tipo"] == "cura":
            cura = f["vida"] * num(h["valor"]) / 100 * f["apoyo"] * (1 + r["esencia"] * 0.3 / 100)
            r["esencia"] = 0
            antes = e["vida"]
            e["vida"] = min(f["vida"], e["vida"] + cura)
            e["curado"] += e["vida"] - antes
            return
        if h["tipo"] == "escudo":
            estado["escudo"] = f["vida"] * num(h["valor"]) / 100 * f["apoyo"]
            estado["escudo_hasta"] = e["t"] + num(h["duracion"])
            return
        objetivos = [m for m in vivos if m["vida"] > 0] if h["tipo"] == "area" else [objetivo]
        for valor in h["golpes"].split("|"):
            if h["tipo"] == "area" and h["unidad"] == "arma":
                d = golpe(0, True, porcentaje=num(valor))
            else:
                d = golpe(num(valor) * (f["dano_arma"] if h["unidad"] == "arma" else 1), True, magico)
            d *= mult * mejora(h, 1 + p["mejora_dano_pct"] / 100)
            for i, m in enumerate(objetivos):
                if m["vida"] > 0:
                    pegar(m, d, roba=i == 0)
        if h["mecanica"] == "desgarro":
            # El sangrado depende de la Energía gastada (100 / 70 / 50 % del arma en 6 s).
            gastada = estado["energia_desgarro"]
            tramo = 1.0 if gastada >= 70 else 0.7 if gastada >= 40 else 0.5
            sangrados.append({"mob": objetivo, "dano": golpe(f["dano_arma"] * tramo / 6, True), "fin": e["t"] + 6,
                              "proximo": e["t"] + 1})
        if magico:
            contar_hechizo()

    def elegir():
        """Siguiente acción cuando el personaje está libre."""
        objetivo = next((m for m in vivos if m["vida"] > 0), None)
        if objetivo is None:
            return None
        n = sum(1 for m in vivos if m["vida"] > 0)
        en_peligro = any(m["proximo"] <= e["t"] + 2 for m in vivos if m["vida"] > 0) and not sin_dano
        candidatas = []
        for h in activas:
            nombre = h["nombre"]
            if listo[nombre] > e["t"]:
                continue
            c = coste(h)
            if c > e["mana"]:
                if c <= f["mana"]:
                    beber("mana")
                continue
            tipo, mec = h["tipo"], h["mecanica"]
            if tipo == "cura":
                if e["vida"] < f["vida"] * 0.6 and not sin_dano:
                    return (h, 1.0, objetivo, 1e9)
                continue
            if tipo == "escudo":
                if en_peligro and e["t"] >= estado["escudo_hasta"]:
                    return (h, 1.0, objetivo, 1e9)
                continue
            if num(h["coste_vida_pct"]) and e["vida"] - f["vida"] * num(h["coste_vida_pct"]) / 100 < f["vida"] * 0.5:
                continue
            mult = 1.0
            golpes = sum(num(g) for g in h["golpes"].split("|")) * (f["dano_arma"] if h["unidad"] == "arma" else 1)
            if mec == "requiere_ira" and r["ira"] < p["coste_ira_fisura"]:
                continue
            if mec == "requiere_energia" and (r["energia"] < p["coste_energia_cuchillas"] or n < 2):
                continue
            if mec == "desgarro":
                if r["energia"] < 70:
                    continue
            if mec == "remate" and objetivo["vida"] < objetivo["max"] * p["remate_umbral_pct"] / 100:
                golpes = p["remate_dano"] * f["dano_arma"]
            if mec == "embate":
                if r["ira"] < 60:
                    continue
            valor = golpes * (n if tipo in ("area", "zona", "canal") else 1)
            if tipo == "canal":
                valor *= num(h["valor"])
            if tipo == "zona":
                valor *= num(h["duracion"])
            candidatas.append((h, mult, objetivo, valor))
        if not candidatas:
            return None
        h, mult, objetivo, valor = max(candidatas, key=lambda c: c[3])
        blanco = f["dano_arma"] if con_basico else 0
        if con_basico and valor <= blanco:
            return None
        # No se gasta una habilidad de un solo objetivo si un golpe blanco ya lo mata.
        if con_basico and h["tipo"] == "dano" and objetivo["vida"] <= golpe(f["dano_arma"], False) and n == 1:
            return None
        return (h, mult, objetivo, valor)

    def lanzar(accion):
        h, mult, objetivo, _ = accion
        listo[h["nombre"]] = e["t"] + num(h["enfriamiento"])
        e["mana"] -= coste(h)
        if num(h["coste_vida_pct"]):
            e["vida"] -= f["vida"] * num(h["coste_vida_pct"]) / 100
        mec = h["mecanica"]
        if mec == "remate" and objetivo["vida"] < objetivo["max"] * p["remate_umbral_pct"] / 100:
            listo[h["nombre"]] = e["t"] + p["remate_enfriamiento"]
            h = dict(h, golpes=str(p["remate_dano"]))
        # Recurso secundario que potencia la habilidad.
        if recurso == "ira_golpe" and h["tipo"] != "cura":
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
            estado["energia_desgarro"] = r["energia"]
            r["energia"] = 0
        if mec == "certero":
            mult *= 1 + r["foco"] * p["foco_por_punto_pct"] / 100
            r["foco"] = 0
        if h["tipo"] == "zona":
            # No interrumpe: cae en la zona mientras el personaje sigue pegando.
            e["usos"][h["nombre"]] = e["usos"].get(h["nombre"], 0) + 1
            zonas.append({"h": h, "fin": e["t"] + num(h["duracion"]), "proximo": e["t"] + 1, "mult": mult})
            return
        if h["tipo"] == "canal":
            ticks = int(num(h["valor"]))
            e["usos"][h["nombre"]] = e["usos"].get(h["nombre"], 0) + 1
            estado["canal"] = {"h": h, "quedan": ticks, "cada": num(h["duracion"]) / ticks,
                               "proximo": e["t"] + num(h["duracion"]) / ticks, "mult": mult}
            estado["ocupado"] = e["t"] + num(h["duracion"])
            return
        lanzamiento = num(h["lanzamiento"]) * f["celeridad"]
        if h["unidad"] == "arma" and con_basico:
            # Sin tiempo de lanzamiento, la habilidad ocupa el hueco de un golpe blanco.
            lanzamiento = lanzamiento or f["intervalo"]
        estado["pendiente"] = (h, mult, objetivo)
        estado["ocupado"] = e["t"] + max(lanzamiento, PASO)

    indice = 0
    empezar_grupo(grupos[0])
    if vida_inicial_pct < 100:
        for m in vivos:
            m["vida"] = m["max"] * vida_inicial_pct / 100
    while limite_s is None or e["t"] < limite_s:
        e["t"] += PASO
        t = e["t"]
        e["vida"] = min(f["vida"], e["vida"] + f["regen_vida"] * PASO)
        e["mana"] = min(f["mana"], e["mana"] + f["regen_mana"] * PASO)
        if recurso == "energia":
            r["energia"] = min(100, r["energia"] + (p["energia_regen"] + p["energia_regen_por_agi"] * f["puntos"]["agi"]) * PASO)
        # Golpes de los mobs.
        if not sin_dano:
            for m in vivos:
                if m["vida"] > 0 and m["proximo"] <= t:
                    bruto = p["dano_mob"] * m["ciclo"][m["n"] % len(m["ciclo"])]
                    m["n"] += 1
                    m["proximo"] += p["intervalo_mob_s"]
                    d = max(1, round(bruto * (1 - f["defensa"] / 100) - f["armadura"] / p["armadura_por_punto_de_dano"]))
                    if t < estado["escudo_hasta"] and estado["escudo"] > 0:
                        absorbido = min(d, estado["escudo"])
                        estado["escudo"] -= absorbido
                        d -= absorbido
                    e["vida"] -= d
                    if recurso == "ira_recibida":
                        r["ira"] = min(100, r["ira"] + p["ira_por_golpe_recibido"])
            if e["vida"] < f["vida"] * p["usar_pocion_vida_pct"] / 100:
                beber("vida")
            if e["vida"] <= 0:
                morir()
                if e["muertes"] >= MUERTES_MAXIMAS:
                    break  # no puede con este tipo de caza
                continue
        # Zonas, sangrados y canalizaciones.
        for z in zonas:
            if z["proximo"] <= t <= z["fin"] + 1e-9:
                z["proximo"] += 1
                d = golpe(0, True, porcentaje=num(z["h"]["golpes"])) * z["mult"]
                for i, m in enumerate(vivos):
                    if m["vida"] > 0:
                        pegar(m, d, roba=i == 0)
        zonas[:] = [z for z in zonas if z["fin"] > t]
        for s in sangrados:
            if s["proximo"] <= t <= s["fin"] + 1e-9:
                s["proximo"] += 1
                if s["mob"]["vida"] > 0:
                    pegar(s["mob"], s["dano"])
        sangrados[:] = [s for s in sangrados if s["fin"] > t]
        canal = estado["canal"]
        if canal and canal["proximo"] <= t + 1e-9:
            canal["proximo"] += canal["cada"]
            canal["quedan"] -= 1
            d = golpe(num(canal["h"]["golpes"]), True, magico=True) * canal["mult"]
            for i, m in enumerate(vivos):
                if m["vida"] > 0:
                    pegar(m, d, roba=i == 0)
            if canal["quedan"] <= 0:
                estado["canal"] = None
                contar_hechizo()
        # Acción del personaje.
        if t >= estado["ocupado"] and estado["canal"] is None:
            if estado["pendiente"]:
                resolver(estado["pendiente"])
                estado["pendiente"] = None
            accion = elegir() if any(m["vida"] > 0 for m in vivos) else None
            if accion:
                lanzar(accion)
            elif con_basico and any(m["vida"] > 0 for m in vivos):
                objetivo = next(m for m in vivos if m["vida"] > 0)
                pegar(objetivo, golpe(f["dano_arma"], False))
                e["usos"]["golpe blanco"] = e["usos"].get("golpe blanco", 0) + 1
                if recurso == "ira_golpe":
                    r["ira"] = min(100, r["ira"] + p["ira_por_golpe"])
                if recurso == "foco":
                    r["foco"] = min(p["foco_maximo"], r["foco"] + p["foco_por_disparo"])
                estado["ocupado"] = t + f["intervalo"]
        # ¿Grupo terminado?
        if all(m["vida"] <= 0 for m in vivos):
            e["muertos"] += len(vivos)
            indice += 1
            if indice >= len(grupos):
                break
            zonas.clear()
            # Descanso si la vida (o el maná de quien depende de él) quedó baja.
            bajo = p["descansar_bajo_pct"] / 100
            if e["vida"] < f["vida"] * bajo or (not con_basico and e["mana"] < f["mana"] * bajo):
                mult = p["multiplicador_regen_descanso"]
                dt = max((f["vida"] - e["vida"]) / (f["regen_vida"] * mult), (f["mana"] - e["mana"]) / (f["regen_mana"] * mult))
                e["t"] += dt
                e["descanso"] += dt
                e["vida"], e["mana"] = f["vida"], f["mana"]
            empezar_grupo(grupos[indice])
    e["tiempo"] = e["t"]
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
        normal = combatir(f, p, [[p["vida_jefe"]]], p["duracion_jefe_s"], sin_dano=True)
        remate = combatir(f, p, [[p["vida_jefe"]]], p["duracion_jefe_s"], sin_dano=True,
                          vida_inicial_pct=p["remate_umbral_pct"] - 1)
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
