"""Simulador de balance de los arquetipos de inicio (niveles 1 a 19).

Lee los datos de la carpeta datos/ (los mismos CSV que se importarán a las
DataTables de Unreal) y compara cada arquetipo con cada arma en dos pruebas:

  - Caza: matar 1.000 mobs. El daño que sobra al rematar cada mob se pierde.
  - Jefe: 20 minutos golpeando un objetivo de vida casi infinita.

Uso:
  python3 simular.py             muestra los resultados
  python3 simular.py --calibrar  recalcula el daño de las armas y los hechizos
                                 para que todos tarden lo mismo en la caza que
                                 el arma de referencia, y lo guarda
  python3 simular.py --calibrar-real  sube el daño de las armas cuerpo a cuerpo
                                 para igualar a los de distancia en la caza
                                 real (con caminata), y lo guarda
  python3 simular.py --niveles   caza real nivel a nivel con mobs que escalan
  python3 simular.py --ficha     guarda la ficha de estadísticas por nivel en resultados/
  python3 simular.py --calibrar-mana  ajusta el % de maná de las habilidades para el
                                 objetivo de pociones de maná del último nivel
"""

import csv
import random
import sys
from pathlib import Path

DATOS = Path(__file__).parent / "datos"


def leer(nombre):
    with open(DATOS / nombre, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def escribir(nombre, filas):
    with open(DATOS / nombre, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(filas)


def numero(texto):
    try:
        return float(texto)
    except ValueError:
        return texto


def cargar():
    parametros = {p["parametro"]: numero(p["valor"]) for p in leer("parametros.csv")}
    conversion = {}
    for c in leer("conversion.csv"):
        conversion.setdefault(c["estadistica"], {})[c["secundaria"]] = float(c["por_punto"])
    return parametros, leer("armas.csv"), leer("arquetipos.csv"), conversion, leer("habilidades.csv")


def secundarias(arquetipo, conversion, parametros):
    """Convierte STR/INT/AGI en las estadísticas secundarias que usa el combate."""
    s = {}
    for estadistica in ("str", "int", "agi"):
        for secundaria, por_punto in conversion.get(estadistica, {}).items():
            s[secundaria] = s.get(secundaria, 0) + float(arquetipo[estadistica]) * por_punto
    # El crítico sube con el nivel (y con lo que den las estadísticas), hasta su tope.
    nivel = float(arquetipo.get("nivel", 1))
    probabilidad = min(parametros["critico_base_pct"] + parametros["critico_por_nivel_pct"] * (nivel - 1)
                       + s.get("critico_pct", 0), parametros["tope_critico_pct"]) / 100
    multiplicador = parametros["multiplicador_critico_base"] + min(
        parametros["critico_aumentado_base_pct"] + parametros["critico_aumentado_por_nivel_pct"] * (nivel - 1)
        + s.get("critico_aumentado_pct", 0), parametros["tope_critico_aumentado_pct"]) / 100
    return {
        "vida": s.get("vida", 0),
        "regen_vida": s.get("regen_vida", 0),
        "mana": s.get("mana", 0),
        "regen_mana": s.get("regen_mana", 0),
        "defensa_fisica_pct": s.get("defensa_fisica_pct", 0),
        "defensa_magica_pct": s.get("defensa_magica_pct", 0),
        "plano": s.get("dano_base", 0),
        "base": 1 + s.get("dano_base_pct", 0) / 100,
        "habilidad": 1 + s.get("dano_habilidad_pct", 0) / 100,
        "probabilidad_critico": min(probabilidad, 1),
        "multiplicador_critico": multiplicador,
        # Valor esperado del crítico, para las pruebas sin azar.
        "critico": 1 + min(probabilidad, 1) * (multiplicador - 1),
    }


def regen_cada_5s(por_segundo):
    """La regeneración se muestra cada 5 s, redondeada al entero más cercano."""
    return int(por_segundo * 5 + 0.5)


def perfiles(armas, arquetipos, habilidades):
    """Cada combinación de arquetipo y arma que puede elegir un jugador."""
    por_nombre = {a["arma"]: a for a in armas}
    for arquetipo in arquetipos:
        for arma in arquetipo["armas"].split("|"):
            # Las estadísticas que da el arma se suman al reparto base.
            con_arma = dict(arquetipo)
            for e in ("str", "int", "agi"):
                con_arma[e] = str(float(arquetipo[e]) + float(por_nombre[arma].get(f"bono_{e}") or 0))
            yield {
                "arquetipo": con_arma,
                "arma": por_nombre[arma],
                "habilidades": [h for h in habilidades if h["arquetipo"] == arquetipo["arquetipo"]],
            }


def vida_inicial(perfil, conversion, parametros):
    return parametros["vida_base"] + secundarias(perfil["arquetipo"], conversion, parametros)["vida"]


def golpes_de(habilidad, dano_arma, s):
    """Daño de cada golpe de una habilidad, sin crítico."""
    golpes = []
    for valor in habilidad["golpes"].split("|"):
        base = float(valor) * dano_arma if habilidad["unidad"] == "arma" else float(valor)
        golpes.append((base + s["plano"]) * s["base"] * s["habilidad"])
    return golpes


def combatir(perfil, conversion, parametros, vidas, limite_s=None, azar=None, supervivencia=False):
    """Pelea contra una lista de objetivos (sus vidas) uno detrás de otro.

    Con `azar` (un random.Random) cada golpe tira su crítico; sin él, se usa el
    valor esperado. Con `supervivencia`, además: el cuerpo a cuerpo camina hasta
    cada mob, al de distancia el mob tarda en llegar (golpes gratis), el mob
    devuelve golpes, las habilidades gastan maná y se descansa para recuperar
    vida y maná. Devuelve el tiempo empleado (y en qué se fue), el daño útil, el
    daño perdido al rematar y los usos de cada acción.
    """
    s = secundarias(perfil["arquetipo"], conversion, parametros)
    p = parametros
    intervalo = float(perfil["arma"]["segundos_entre_golpes"])
    dano_arma = float(perfil["arma"]["dano"])
    con_ataque_basico = perfil["arquetipo"]["ataque_basico"] == "1"
    a_distancia = perfil["arquetipo"]["a_distancia"] == "1"
    # Solo las habilidades desbloqueadas a este nivel: las de daño y las especiales
    # (pasivas y activas que no pegan).
    nivel = float(perfil["arquetipo"].get("nivel", 1))
    desbloqueadas = [h for h in perfil["habilidades"] if float(h.get("nivel_minimo") or 1) <= nivel]
    habilidades = [h for h in desbloqueadas if h.get("tipo", "dano") == "dano"]
    especial = {h["tipo"]: h for h in desbloqueadas if h.get("tipo", "dano") != "dano"}
    coste_vida = {h["nombre"]: round(vida_inicial(perfil, conversion, parametros) * float(h.get("coste_vida_pct") or 0) / 100)
                  if supervivencia else 0 for h in habilidades}
    robo_vida = float(especial["robo_vida"]["valor"]) / 100 if "robo_vida" in especial else 0.0
    furia, escudo = especial.get("furia"), especial.get("escudo")
    # Pasivas que suman crítico (sin pasar el tope).
    critico_extra = sum(float(h.get("critico_pct") or 0) for h in desbloqueadas) / 100
    if critico_extra:
        s = dict(s)
        s["probabilidad_critico"] = min(s["probabilidad_critico"] + critico_extra, parametros["tope_critico_pct"] / 100)
        s["critico"] = 1 + s["probabilidad_critico"] * (s["multiplicador_critico"] - 1)
    celeridad = 1 - float(especial["celeridad"]["valor"]) / 100 if "celeridad" in especial else 1.0
    activa = {"furia_hasta": -1.0, "furia_lista": 0.0, "escudo_hasta": -1.0, "escudo_resto": 0.0, "escudo_listo": 0.0}
    golpes = {h["nombre"]: golpes_de(h, dano_arma, s) for h in habilidades}
    blanco = (dano_arma + s["plano"]) * s["base"]
    # El remate más barato: un golpe blanco o, si no hay, la habilidad más débil.
    remate = blanco if con_ataque_basico else min((sum(g) for g in golpes.values()), default=0)
    listo = {h["nombre"]: 0.0 for h in habilidades}  # cuándo sale del enfriamiento

    vida_max = p["vida_base"] + s["vida"]
    mana_max = p["mana_base"] + s["mana"]
    # Pasivas que suben la regeneración de vida por cada punto de STR.
    extra_regen = sum(float(h.get("regen_vida_por_str") or 0) for h in desbloqueadas) * float(perfil["arquetipo"]["str"])
    regen_vida = regen_cada_5s(p["regen_vida_base"] + s["regen_vida"] + extra_regen) / 5
    regen_mana = regen_cada_5s(p["regen_mana_base"] + s["regen_mana"]) / 5
    # Coste de maná: una parte fija y una parte en % del maná máximo (así crece con el personaje).
    def coste_de(h):
        return round(float(h.get("coste_mana") or 0) + float(h.get("coste_mana_pct") or 0) * mana_max / 100)
    coste = {h["nombre"]: coste_de(h) if supervivencia else 0 for h in habilidades}
    # Una habilidad que cuesta más que todo el maná del personaje no se puede usar nunca.
    habilidades = [h for h in habilidades if coste[h["nombre"]] <= mana_max]
    if not habilidades and not con_ataque_basico:
        return {"tiempo": float("inf"), "util": 0.0, "perdido": 0.0, "usos": {}, "muertes": 0,
                "pociones_vida": 0, "pociones_mana": 0}
    defensa = {"fisico": s["defensa_fisica_pct"], "magico": s["defensa_magica_pct"]}
    armadura = p["armadura_por_nivel"] * nivel

    e = {"t": 0.0, "vida": vida_max, "mana": mana_max, "util": 0.0, "perdido": 0.0, "muertes": 0,
         "pegando": 0.0, "caminando": 0.0, "descansando": 0.0, "esperando_mana": 0.0, "muerto": 0.0,
         "dano_recibido": 0.0, "pociones_vida": 0, "pociones_mana": 0, "absorbido": 0.0, "curado": 0.0, "coste_vida": 0}
    pocion_lista = {"vida": 0.0, "mana": 0.0}  # cuándo sale del enfriamiento cada poción

    def beber(tipo):
        """Bebe una poción (instantánea) si están activadas y no está en enfriamiento."""
        if not (supervivencia and p["pociones"]) or pocion_lista[tipo] > e["t"]:
            return False
        maximo = vida_max if tipo == "vida" else mana_max
        e[tipo] = min(maximo, e[tipo] + p[f"pocion_{tipo}"])
        e[f"pociones_{tipo}"] += 1
        pocion_lista[tipo] = e["t"] + p["enfriamiento_pocion_s"]
        return True
    usos = {}
    # proximo_golpe None = el mob no está pegando; golpes = daño de cada ataque de su ciclo.
    mob = {"vida": 0.0, "proximo_golpe": None, "golpes": [], "ciclo": 0}

    def avanzar(dt, motivo, multiplicador_regen=1.0):
        """Pasa el tiempo: regenera y, si el mob está pegando, recibe sus golpes."""
        fin = e["t"] + dt
        while supervivencia and mob["proximo_golpe"] is not None and mob["proximo_golpe"] <= fin:
            regenerar(mob["proximo_golpe"] - e["t"], multiplicador_regen)
            e["t"] = mob["proximo_golpe"]
            dano_recibido = mob["golpes"][mob["ciclo"] % len(mob["golpes"])]
            mob["ciclo"] += 1
            if e["t"] < activa["escudo_hasta"] and activa["escudo_resto"] > 0:
                absorbido = min(dano_recibido, activa["escudo_resto"])
                activa["escudo_resto"] -= absorbido
                e["absorbido"] += absorbido
                dano_recibido -= absorbido
            e["vida"] -= dano_recibido
            e["dano_recibido"] += dano_recibido
            mob["proximo_golpe"] += p["intervalo_mob_s"]
            if 0 < e["vida"] < vida_max * p["usar_pocion_vida_pct"] / 100:
                beber("vida")
            if e["vida"] <= 0:
                return False
        regenerar(fin - e["t"], multiplicador_regen)
        e[motivo] += dt
        e["t"] = fin
        return True

    def regenerar(dt, multiplicador):
        if supervivencia:
            e["vida"] = min(vida_max, e["vida"] + regen_vida * multiplicador * dt)
            e["mana"] = min(mana_max, e["mana"] + regen_mana * multiplicador * dt)

    inicio = {}

    def empezar_mob(objetivo):
        vida, tipo = objetivo if isinstance(objetivo, tuple) else (objetivo, None)
        mob["vida"] = vida
        mob["ciclo"] = 0
        inicio["vida"], inicio["mana"] = e["vida"], e["mana"]
        if not supervivencia:
            mob["proximo_golpe"] = None
            return
        tipo = tipo or {"a_distancia": "0", "tipo_dano": "fisico", "ciclo": "1"}
        # En el juego todos los valores que se ven son enteros: cada golpe se redondea.
        # La armadura resta daño plano a cada golpe: 1 punto por cada 100 de armadura.
        mob["golpes"] = [max(1, int(p["dano_mob"] * float(m) * (1 - defensa[tipo["tipo_dano"]] / 100)
                                    - armadura / p["armadura_por_punto_de_dano"] + 0.5))
                         for m in tipo["ciclo"].split("|")]
        mob_a_distancia = tipo["a_distancia"] == "1"
        if mob_a_distancia:
            # Un mob a distancia empieza a pegar en cuanto empieza la pelea, también
            # mientras el cuerpo a cuerpo camina hacia él.
            mob["proximo_golpe"] = e["t"]
            if not a_distancia:
                avanzar(p["desplazamiento_melee_s"], "caminando")
        elif a_distancia:
            mob["proximo_golpe"] = e["t"] + p["acercamiento_mob_s"]
        else:
            avanzar(p["desplazamiento_melee_s"], "caminando")
            mob["proximo_golpe"] = e["t"]

    indice = 0
    empezar_mob(vidas[0])
    while indice < len(vidas) and (limite_s is None or e["t"] < limite_s):
        # Activas que no pegan: se usan antes que cualquier ataque si están listas.
        if furia and activa["furia_lista"] <= e["t"] and (not supervivencia or e["vida"] > vida_max / 2):
            activa["furia_hasta"] = e["t"] + float(furia["duracion"])
            activa["furia_lista"] = e["t"] + float(furia["enfriamiento"])
            usos[furia["nombre"]] = usos.get(furia["nombre"], 0) + 1
        if (supervivencia and escudo and activa["escudo_listo"] <= e["t"] and mob["proximo_golpe"] is not None
                and e["mana"] >= coste_de(escudo)):
            e["mana"] -= coste_de(escudo)
            activa["escudo_hasta"] = e["t"] + float(escudo["duracion"])
            activa["escudo_resto"] = vida_max * float(escudo["valor"]) / 100
            activa["escudo_listo"] = e["t"] + float(escudo["enfriamiento"])
            usos[escudo["nombre"]] = usos.get(escudo["nombre"], 0) + 1
            if not avanzar(float(escudo["lanzamiento"]), "pegando"):
                e["muertes"] += 1
                e["t"] += p["penalizacion_muerte_s"]
                e["muerto"] += p["penalizacion_muerte_s"]
                e["vida"], e["mana"] = vida_max, mana_max
                mob["proximo_golpe"] = None
                empezar_mob(vidas[indice])
            continue
        # Si una habilidad está lista pero falta maná, se bebe una poción de maná (si se puede).
        if supervivencia and any(listo[h["nombre"]] <= e["t"] and coste[h["nombre"]] > e["mana"] for h in habilidades):
            beber("mana")
        # Una habilidad que cuesta vida solo se usa si después queda más de un 25 % de colchón.
        disponibles = [h for h in habilidades if listo[h["nombre"]] <= e["t"] and coste[h["nombre"]] <= e["mana"]
                       and (not coste_vida[h["nombre"]] or e["vida"] - coste_vida[h["nombre"]] > vida_max * 0.25)]
        if p["ahorrar_habilidades"] and mob["vida"] <= remate:
            # Al mob le queda poco: no se gasta una habilidad con enfriamiento largo.
            baratas = [h for h in disponibles if sum(golpes[h["nombre"]]) <= remate]
            disponibles = baratas if baratas or con_ataque_basico else disponibles
        vivo = True
        if disponibles:
            # Prioridad: la habilidad de más daño que esté disponible.
            h = max(disponibles, key=lambda h: sum(golpes[h["nombre"]]))
            nombre, danos = h["nombre"], golpes[h["nombre"]]
            listo[nombre] = e["t"] + float(h["enfriamiento"])
            e["mana"] -= coste[nombre]
            e["vida"] -= coste_vida[nombre]
            e["coste_vida"] += coste_vida[nombre]
            if furia and e["t"] < activa["furia_hasta"]:
                # Furia: la habilidad pega más fuerte a cambio de vida.
                danos = [d * (1 + float(furia["valor"]) / 100) for d in danos]
                if supervivencia:
                    e["vida"] = max(1, e["vida"] - round(vida_max * float(furia["coste_vida_pct"]) / 100))
            # Sin tiempo de lanzamiento, la habilidad ocupa el hueco de un golpe blanco.
            duracion = float(h["lanzamiento"]) * celeridad or intervalo
        elif con_ataque_basico:
            nombre, danos, duracion = "golpe blanco", [blanco], intervalo
        elif listo:
            # Sin habilidad lista: esperar a la primera que se pueda lanzar, por
            # enfriamiento o por maná (lo que tarde más en cada una).
            esperas = []
            for h in habilidades:
                por_cd = max(listo[h["nombre"]] - e["t"], 0)
                falta = coste[h["nombre"]] - e["mana"]
                por_mana = falta / regen_mana if falta > 0 else 0
                esperas.append((max(por_cd, por_mana), por_mana > por_cd))
            espera, es_mana = min(esperas)
            if es_mana and beber("mana"):
                continue
            vivo = avanzar(max(espera, 1e-6), "esperando_mana" if es_mana else "pegando")
            nombre = None
        else:
            break

        if nombre:
            usos[nombre] = usos.get(nombre, 0) + 1
            vivo = avanzar(duracion, "pegando")
            if vivo:
                for dano in danos:
                    if azar is None:
                        dano *= s["critico"]
                    elif azar.random() < s["probabilidad_critico"]:
                        dano *= s["multiplicador_critico"]
                    if azar is not None:
                        dano = round(dano)  # con críticos reales cada golpe es un número entero
                    # Si el mob muere a mitad de una habilidad, los golpes que quedan se pierden.
                    util = min(dano, max(mob["vida"], 0))
                    e["util"] += util
                    if supervivencia and robo_vida:
                        curado = min(vida_max - e["vida"], util * robo_vida)
                        e["vida"] += curado
                        e["curado"] += curado
                    e["perdido"] += max(dano - max(mob["vida"], 0), 0)
                    mob["vida"] -= dano

        if not vivo:
            # Muerte: se pierde tiempo, se vuelve con todo lleno y el mob se recupera.
            e["muertes"] += 1
            e["t"] += p["penalizacion_muerte_s"]
            e["muerto"] += p["penalizacion_muerte_s"]
            e["vida"], e["mana"] = vida_max, mana_max
            mob["proximo_golpe"] = None
            empezar_mob(vidas[indice])
            continue

        if mob["vida"] <= 0:
            mob["proximo_golpe"] = None
            indice += 1
            if indice >= len(vidas):
                break
            if supervivencia and p["descansar"]:
                # Se descansa si no queda para aguantar otro mob como el último
                # (con margen) o si se baja del % mínimo.
                margen = p["margen_descanso"]
                gastado_vida = inicio["vida"] - e["vida"]
                gastado_mana = inicio["mana"] - e["mana"]
                necesita_mana = not con_ataque_basico
                if (e["vida"] < max(vida_max * p["descansar_bajo_vida_pct"] / 100, gastado_vida * margen)
                        or necesita_mana and e["mana"] < max(mana_max * p["descansar_bajo_mana_pct"] / 100,
                                                             gastado_mana * margen)):
                    multiplicador = p["multiplicador_regen_descanso"]
                    dt = max((vida_max - e["vida"]) / (regen_vida * multiplicador),
                             (mana_max - e["mana"]) / (regen_mana * multiplicador))
                    avanzar(dt, "descansando", multiplicador)
            elif not supervivencia:
                e["t"] += p["desplazamiento_s"]
            empezar_mob(vidas[indice])

    e["tiempo"] = e["t"]
    e["usos"] = usos
    return e


def prueba_jefe(perfil, conversion, parametros):
    r = combatir(perfil, conversion, parametros, [parametros["vida_jefe"]], parametros["duracion_jefe_s"])
    r["dps"] = r["util"] / parametros["duracion_jefe_s"]
    return r


def prueba_caza(perfil, conversion, parametros, supervivencia=None):
    azar_vidas = random.Random(int(parametros["semilla"]))
    variacion = parametros["variacion_vida_mob_pct"] / 100
    tipos = leer("mobs.csv")
    pesos = [float(t["proporcion"]) for t in tipos]
    vidas = []
    for i in range(int(parametros["numero_mobs"])):
        vida = round(parametros["vida_mob"] * (1 + azar_vidas.uniform(-variacion, variacion)))
        # Rotación fija (siempre se recibe daño intercalado) o tipo al azar.
        tipo = tipos[i % len(tipos)] if parametros["rotacion_mobs"] else azar_vidas.choices(tipos, pesos)[0]
        vidas.append((vida, tipo))
    azar = random.Random(int(parametros["semilla"])) if parametros["critico_aleatorio_en_caza"] else None
    if supervivencia is None:
        supervivencia = bool(parametros["supervivencia_en_caza"])
    return combatir(perfil, conversion, parametros, vidas, azar=azar, supervivencia=supervivencia)


def calibrar(parametros, armas, arquetipos, conversion, habilidades):
    """Ajusta el daño de cada arma (y de los hechizos de quien no usa el arma)
    para que tarde lo mismo en la caza que el arma de referencia, en combate puro
    (sin desplazamiento ni descansos: eso se compensa aparte). Las
    habilidades que dependen del arma suben o bajan con ella. Como el tiempo de
    caza va a saltos (golpes por mob), se busca el factor por bisección."""
    lista = list(perfiles(armas, arquetipos, habilidades))
    referencia = next(p for p in lista if p["arma"]["arma"] == parametros["arma_referencia"])
    objetivo = prueba_caza(referencia, conversion, parametros, supervivencia=False)["tiempo"]

    for perfil in lista:
        if perfil is referencia:
            continue
        if perfil["arquetipo"]["ataque_basico"] == "1":
            ajustables = [(perfil["arma"], "dano")]
        else:
            ajustables = [(h, "golpes") for h in perfil["habilidades"] if h["unidad"] == "puntos"]
        originales = [float(fila[campo]) for fila, campo in ajustables]

        def aplicar(factor, redondear=False):
            for (fila, campo), v in zip(ajustables, originales):
                fila[campo] = f"{v * factor:.0f}" if redondear else str(v * factor)

        bajo, alto = 0.2, 5.0
        for _ in range(40):
            medio = (bajo + alto) / 2
            aplicar(medio)
            if prueba_caza(perfil, conversion, parametros, supervivencia=False)["tiempo"] > objetivo:
                bajo = medio
            else:
                alto = medio
        aplicar((bajo + alto) / 2, redondear=True)

    escribir("armas.csv", armas)
    escribir("habilidades.csv", habilidades)
    print(f"Calibrado a {objetivo / 60:.1f} min de caza ({parametros['arma_referencia']}).")
    print("Guardado en datos/armas.csv y datos/habilidades.csv.\n")


def calibrar_real(parametros, armas, arquetipos, conversion, habilidades):
    """Sube o baja el daño de las armas cuerpo a cuerpo para que, en la caza real
    (caminando entre mobs), tarden lo mismo que la media de los perfiles a
    distancia. Las armas a distancia y los hechizos no se tocan."""
    lista = list(perfiles(armas, arquetipos, habilidades))
    distancia = [pf for pf in lista if pf["arquetipo"]["a_distancia"] == "1"]
    objetivo = sum(prueba_caza(pf, conversion, parametros, supervivencia=True)["tiempo"]
                   for pf in distancia) / len(distancia)
    for perfil in lista:
        if perfil in distancia:
            continue
        arma = perfil["arma"]
        original = float(arma["dano"])
        bajo, alto = 0.5, 3.0
        for _ in range(14):
            medio = (bajo + alto) / 2
            arma["dano"] = str(original * medio)
            if prueba_caza(perfil, conversion, parametros, supervivencia=True)["tiempo"] > objetivo:
                bajo = medio
            else:
                alto = medio
        arma["dano"] = f"{original * (bajo + alto) / 2:.0f}"
        print(f"{arma['arma']}: {original:g} -> {arma['dano']} de daño por golpe")
    escribir("armas.csv", armas)
    print(f"Igualado a {objetivo / 60:.1f} min de caza real (media de los perfiles a distancia).")
    print("Guardado en datos/armas.csv.\n")


def perfiles_nivel(armas, arquetipos, habilidades, nivel):
    """Perfiles a un nivel dado: cada nivel suma las estadísticas que da el arma
    de nivel 1 de ese arquetipo (la primera de su lista)."""
    por_nombre = {a["arma"]: a for a in armas}
    subidos = []
    for arquetipo in arquetipos:
        arma = por_nombre[arquetipo["armas"].split("|")[0]]
        subido = dict(arquetipo)
        subido["nivel"] = str(nivel)
        for e in ("str", "int", "agi"):
            subido[e] = str(float(arquetipo[e]) + (nivel - 1) * float(arma.get(f"bono_{e}") or 0))
        subidos.append(subido)
    return list(perfiles(armas, subidos, habilidades))


def condiciones_nivel(parametros, armas, arquetipos, conversion, habilidades, nivel):
    """Parámetros de la caza en un nivel: la vida del mob sube un % fijo por nivel
    (o, si es 0, como el daño por segundo medio de los perfiles) y su daño, como la
    vida media de los perfiles respecto al nivel 1."""
    p = dict(parametros)
    p["numero_mobs"] = parametros["numero_mobs_por_nivel"]

    def medias(n):
        lista = perfiles_nivel(armas, arquetipos, habilidades, n)
        vida = sum(vida_inicial(pf, conversion, p) for pf in lista) / len(lista)
        dps = 0 if parametros["crecimiento_vida_mob_pct"] else sum(
            prueba_jefe(pf, conversion, p)["dps"] for pf in lista) / len(lista)
        return dps, vida

    (dps1, vida1), (dps, vida) = medias(1), medias(nivel)
    if parametros["crecimiento_vida_mob_pct"]:
        p["vida_mob"] = round(parametros["vida_mob"] * (1 + parametros["crecimiento_vida_mob_pct"] / 100) ** (nivel - 1))
    else:
        p["vida_mob"] = round(parametros["vida_mob"] * dps / dps1)
    p["dano_mob"] = round(parametros["dano_mob"] * vida / vida1)
    return p


def niveles(parametros, armas, arquetipos, conversion, habilidades):
    """Caza real nivel a nivel con mobs que escalan (ver condiciones_nivel)."""
    escala = (f"vida del mob +{parametros['crecimiento_vida_mob_pct']:g} % por nivel" if parametros["crecimiento_vida_mob_pct"]
              else "vida del mob al ritmo del daño medio")
    print(f"Caza real nivel a nivel · {parametros['numero_mobs_por_nivel']:.0f} mobs por nivel · {escala}\n")
    cabecera = None
    for nivel in range(1, int(parametros["nivel_maximo_simulado"]) + 1):
        p = condiciones_nivel(parametros, armas, arquetipos, conversion, habilidades, nivel)
        lista = perfiles_nivel(armas, arquetipos, habilidades, nivel)
        cazas = [prueba_caza(pf, conversion, p, supervivencia=True) for pf in lista]
        nombres = [pf["arma"]["arma"] if pf["arquetipo"]["ataque_basico"] == "1" else "Mágico" for pf in lista]
        if cabecera is None:
            cabecera = f"{'Nivel':>5}{'Vida mob':>9}" + "".join(f"{n:>26}" for n in nombres) + f"{'Diferencia':>11}"
            print(cabecera)
            print(f"{'':>14}" + "".join(f"{'min · vida · maná · †':>26}" for _ in nombres))
        tiempos = [c["tiempo"] for c in cazas]
        celdas = "".join(f"{c['tiempo'] / 60:>10.1f}{c['pociones_vida']:>6}{c['pociones_mana']:>6}{c['muertes']:>4}"
                         for c in cazas)
        print(f"{nivel:>5}{p['vida_mob']:>9.0f}{celdas}{(max(tiempos) / min(tiempos) - 1) * 100:>10.1f}%")
    print("\nmin = minutos para matar los mobs del nivel · vida / maná = pociones bebidas de cada tipo · † = muertes")


def calibrar_mana(parametros, armas, arquetipos, conversion, habilidades):
    """Ajusta, por arquetipo, el % de maná que cuestan sus habilidades para que en el
    último nivel simulado beba el número objetivo de pociones de maná."""
    nivel = int(parametros["nivel_maximo_simulado"])
    p = condiciones_nivel(parametros, armas, arquetipos, conversion, habilidades, nivel)
    objetivo = parametros["objetivo_pociones_mana"]
    for arquetipo in arquetipos:
        propias = [h for h in habilidades if h["arquetipo"] == arquetipo["arquetipo"] and float(h.get("coste_mana_pct") or 0)]
        originales = [float(h["coste_mana_pct"]) for h in propias]

        def pociones(factor):
            for h, v in zip(propias, originales):
                h["coste_mana_pct"] = str(v * factor)
            lista = [pf for pf in perfiles_nivel(armas, arquetipos, habilidades, nivel)
                     if pf["arquetipo"]["arquetipo"] == arquetipo["arquetipo"]]
            return sum(prueba_caza(pf, conversion, p, supervivencia=True)["pociones_mana"] for pf in lista) / len(lista)

        bajo, alto = 0.1, 20.0
        for _ in range(25):
            medio = (bajo + alto) / 2
            if pociones(medio) < objetivo:
                bajo = medio
            else:
                alto = medio
        factor = (bajo + alto) / 2
        for h, v in zip(propias, originales):
            h["coste_mana_pct"] = f"{v * factor:.1f}"
        print(f"{arquetipo['nombre']}: " + ", ".join(f"{h['nombre']} {h['coste_mana_pct']} %" for h in propias)
              + f" → {pociones(1.0):.0f} pociones de maná en el nivel {nivel}")
    escribir("habilidades.csv", habilidades)
    print("Guardado en datos/habilidades.csv.\n")


def ficha(parametros, armas, arquetipos, conversion, habilidades):
    """Ficha cerrada de los niveles 1 al último simulado: estadísticas de cada
    perfil por nivel y escalado de los mobs. Se guarda en resultados/ como CSV."""
    p = parametros
    filas, mobs = [], []
    vida_media_1 = None
    for nivel in range(1, int(p["nivel_maximo_simulado"]) + 1):
        lista = perfiles_nivel(armas, arquetipos, habilidades, nivel)
        vidas = []
        for pf in lista:
            s = secundarias(pf["arquetipo"], conversion, p)
            con_arma = pf["arquetipo"]["ataque_basico"] == "1"
            dano_arma = float(pf["arma"]["dano"])
            vida = p["vida_base"] + s["vida"]
            vidas.append(vida)
            filas.append({
                "nivel": nivel,
                "perfil": pf["arquetipo"]["nombre"],
                "arma": pf["arma"]["arma"],
                "str": round(float(pf["arquetipo"]["str"])),
                "agi": round(float(pf["arquetipo"]["agi"])),
                "int": round(float(pf["arquetipo"]["int"])),
                "vida": round(vida),
                "regen_vida_5s": regen_cada_5s(p["regen_vida_base"] + s["regen_vida"]),
                "mana": round(p["mana_base"] + s["mana"]),
                "regen_mana_5s": regen_cada_5s(p["regen_mana_base"] + s["regen_mana"]),
                "armadura": round(p["armadura_por_nivel"] * nivel),
                "defensa_fisica_pct": round(s["defensa_fisica_pct"], 1),
                "defensa_magica_pct": round(s["defensa_magica_pct"], 1),
                "dano_arma": round(dano_arma) if con_arma else 0,
                "dano_base_pct": round((s["base"] - 1) * 100, 1),
                "dano_habilidad_pct": round((s["habilidad"] - 1) * 100, 1),
                "dano_plano": round(s["plano"]),
                "golpe_blanco": round((dano_arma + s["plano"]) * s["base"]) if con_arma else 0,
                "critico_pct": round(s["probabilidad_critico"] * 100, 1),
                "critico_extra_pct": round((s["multiplicador_critico"] - 1) * 100, 1),
            })
        vida_media = sum(vidas) / len(vidas)
        vida_media_1 = vida_media_1 or vida_media
        dano = round(p["dano_mob"] * vida_media / vida_media_1)
        crecimiento = p["crecimiento_vida_mob_pct"] / 100
        mobs.append({"nivel": nivel, "vida": round(p["vida_mob"] * (1 + crecimiento) ** (nivel - 1)),
                     "golpe_basico": dano, "golpe_potenciado": dano * 2})
    carpeta = Path(__file__).parent / "resultados"
    carpeta.mkdir(exist_ok=True)
    for nombre, datos in (("ficha_perfiles_1_19.csv", filas), ("ficha_mobs_1_19.csv", mobs)):
        with open(carpeta / nombre, "w", encoding="utf-8", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=list(datos[0].keys()), lineterminator="\n")
            escritor.writeheader()
            escritor.writerows(datos)
    print(f"Guardado en resultados/: ficha_perfiles_1_19.csv ({len(filas)} filas) y ficha_mobs_1_19.csv")


def informe(parametros, armas, arquetipos, conversion, habilidades):
    lista = list(perfiles(armas, arquetipos, habilidades))
    n = parametros["numero_mobs"]
    nombre = lambda perfil: (perfil["arma"]["arma"] if perfil["arquetipo"]["ataque_basico"] == "1"
                             else perfil["arquetipo"]["nombre"])
    print(f"Nivel 1 · caza: {n:.0f} mobs de {parametros['vida_mob']:.0f} de vida "
          f"(±{parametros['variacion_vida_mob_pct']:.0f} %) · jefe: {parametros['duracion_jefe_s'] / 60:.0f} min")

    # 1. Combate puro: solo daño, como se calibra.
    filas = [(pf, prueba_jefe(pf, conversion, parametros),
              prueba_caza(pf, conversion, parametros, supervivencia=False)) for pf in lista]
    rapido = min(c["tiempo"] for _, _, c in filas)
    print("\n1) Combate puro (sin desplazamiento, sin golpes del mob, sin maná)\n")
    print(f"{'Perfil':<14}{'Daño arma':>10}{'Acciones/mob':>13}{'s/mob':>7}{'Caza (min)':>11}"
          f"{'vs + rápido':>12}{'Perdido':>9}{'DPS jefe':>10}")
    for pf, jefe, caza in filas:
        con_arma = pf["arquetipo"]["ataque_basico"] == "1"
        print(f"{nombre(pf):<14}{(pf['arma']['dano'] if con_arma else '—'):>10}"
              f"{sum(caza['usos'].values()) / n:>13.2f}{caza['tiempo'] / n:>7.2f}{caza['tiempo'] / 60:>11.1f}"
              f"{(caza['tiempo'] / rapido - 1) * 100:>+11.1f}%"
              f"{caza['perdido'] / (caza['util'] + caza['perdido']) * 100:>8.1f}%{jefe['dps']:>10.2f}")
    tiempos = [c["tiempo"] for _, _, c in filas]
    print(f"Diferencia máxima en la caza: {(max(tiempos) / min(tiempos) - 1) * 100:.1f} %")

    # 2. Caza real: desplazamiento, golpes del mob, vida, maná y descansos.
    reales = [(pf, prueba_caza(pf, conversion, parametros, supervivencia=True)) for pf in lista]
    rapido = min(c["tiempo"] for _, c in reales)
    descanso = "con descansos" if parametros["descansar"] else "sin descansos"
    descanso += ", con pociones" if parametros["pociones"] else ", sin pociones"
    print(f"\n2) Caza real (desplazamiento, golpes del mob, vida y maná; {descanso})\n")
    print(f"{'Perfil':<14}{'Vida':>6}{'Reg/5s':>7}{'Maná':>6}{'Reg/5s':>7}{'Caza (min)':>11}{'vs + rápido':>12}"
          f"{'Pegando':>9}{'Caminando':>10}{'Descanso':>9}{'Sin maná':>9}{'Muerto':>8}{'Muertes':>8}{'Poc. vida':>10}{'Poc. maná':>10}{'Daño recibido/mob':>18}")
    for pf, c in reales:
        s = secundarias(pf["arquetipo"], conversion, parametros)
        t = c["tiempo"]
        print(f"{nombre(pf):<14}{parametros['vida_base'] + s['vida']:>6.0f}"
              f"{regen_cada_5s(parametros['regen_vida_base'] + s['regen_vida']):>7}"
              f"{parametros['mana_base'] + s['mana']:>6.0f}{regen_cada_5s(parametros['regen_mana_base'] + s['regen_mana']):>7}"
              f"{t / 60:>11.1f}{(t / rapido - 1) * 100:>+11.1f}%"
              f"{c['pegando'] / t * 100:>8.0f}%{c['caminando'] / t * 100:>9.0f}%"
              f"{c['descansando'] / t * 100:>8.0f}%{c['esperando_mana'] / t * 100:>8.0f}%"
              f"{c['muerto'] / t * 100:>7.0f}%{c['muertes']:>8}"
              f"{c['pociones_vida']:>10}{c['pociones_mana']:>10}{c['dano_recibido'] / n:>18.1f}")
    tiempos = [c["tiempo"] for _, c in reales]
    print(f"Diferencia máxima en la caza: {(max(tiempos) / min(tiempos) - 1) * 100:.1f} %")

    print("\nUsos en la caza real:")
    for pf, c in reales:
        print(f"  {nombre(pf)}: " + ", ".join(f"{k} x{v}" for k, v in c["usos"].items()))


def main():
    datos = cargar()
    if "--calibrar" in sys.argv:
        calibrar(*datos)
    if "--calibrar-real" in sys.argv:
        calibrar_real(*datos)
    if "--calibrar-mana" in sys.argv:
        calibrar_mana(*datos)
    if "--ficha" in sys.argv:
        ficha(*datos)
        return
    if "--niveles" in sys.argv:
        niveles(*datos)
        return
    informe(*datos)


if __name__ == "__main__":
    main()
