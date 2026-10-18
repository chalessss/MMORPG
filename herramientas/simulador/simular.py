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
    probabilidad = (parametros["critico_base_pct"] + s.get("critico_pct", 0)) / 100
    multiplicador = parametros["multiplicador_critico_base"] + s.get("critico_aumentado_pct", 0) / 100
    return {
        "plano": s.get("dano_base", 0),
        "base": 1 + s.get("dano_base_pct", 0) / 100,
        "habilidad": 1 + s.get("dano_habilidad_pct", 0) / 100,
        "probabilidad_critico": min(probabilidad, 1),
        "multiplicador_critico": multiplicador,
        # Valor esperado del crítico, para las pruebas sin azar.
        "critico": 1 + min(probabilidad, 1) * (multiplicador - 1),
    }


def perfiles(armas, arquetipos, habilidades):
    """Cada combinación de arquetipo y arma que puede elegir un jugador."""
    por_nombre = {a["arma"]: a for a in armas}
    for arquetipo in arquetipos:
        for arma in arquetipo["armas"].split("|"):
            yield {
                "arquetipo": arquetipo,
                "arma": por_nombre[arma],
                "habilidades": [h for h in habilidades if h["arquetipo"] == arquetipo["arquetipo"]],
            }


def golpes_de(habilidad, dano_arma, s):
    """Daño de cada golpe de una habilidad, sin crítico."""
    golpes = []
    for valor in habilidad["golpes"].split("|"):
        base = float(valor) * dano_arma if habilidad["unidad"] == "arma" else float(valor)
        golpes.append((base + s["plano"]) * s["base"] * s["habilidad"])
    return golpes


def combatir(perfil, conversion, parametros, vidas, limite_s=None, azar=None):
    """Pelea contra una lista de objetivos (sus vidas) uno detrás de otro.

    Devuelve el tiempo empleado, el daño útil, el daño perdido al rematar y los
    usos de cada acción. Con `azar` (un random.Random) cada golpe tira su
    crítico; sin él, se usa el valor esperado.
    """
    s = secundarias(perfil["arquetipo"], conversion, parametros)
    intervalo = float(perfil["arma"]["segundos_entre_golpes"])
    dano_arma = float(perfil["arma"]["dano"])
    con_ataque_basico = perfil["arquetipo"]["ataque_basico"] == "1"
    habilidades = perfil["habilidades"]
    golpes = {h["nombre"]: golpes_de(h, dano_arma, s) for h in habilidades}
    blanco = (dano_arma + s["plano"]) * s["base"]
    # El remate más barato: un golpe blanco o, si no hay, la habilidad más débil.
    remate = blanco if con_ataque_basico else min((sum(g) for g in golpes.values()), default=0)
    ahorrar = parametros["ahorrar_habilidades"]
    listo = {h["nombre"]: 0.0 for h in habilidades}  # cuándo sale del enfriamiento
    usos = {}
    t, util, perdido, indice = 0.0, 0.0, 0.0, 0
    vida = vidas[0]

    while indice < len(vidas) and (limite_s is None or t < limite_s):
        disponibles = [h for h in habilidades if listo[h["nombre"]] <= t]
        if ahorrar and vida <= remate:
            # Al mob le queda poco: no se gasta una habilidad con enfriamiento largo.
            baratas = [h for h in disponibles if sum(golpes[h["nombre"]]) <= remate]
            disponibles = baratas if baratas or con_ataque_basico else disponibles
        if disponibles:
            # Prioridad: la habilidad de más daño que esté disponible.
            h = max(disponibles, key=lambda h: sum(golpes[h["nombre"]]))
            nombre, danos = h["nombre"], golpes[h["nombre"]]
            listo[nombre] = t + float(h["enfriamiento"])
            # Sin tiempo de lanzamiento, la habilidad ocupa el hueco de un golpe blanco.
            t += float(h["lanzamiento"]) or intervalo
        elif con_ataque_basico:
            nombre, danos = "golpe blanco", [blanco]
            t += intervalo
        elif listo:
            t = min(listo.values())  # esperar a que salga un hechizo
            continue
        else:
            break
        usos[nombre] = usos.get(nombre, 0) + 1
        for dano in danos:
            if azar is None:
                dano *= s["critico"]
            elif azar.random() < s["probabilidad_critico"]:
                dano *= s["multiplicador_critico"]
            # Si el mob muere a mitad de una habilidad, los golpes que quedan se pierden.
            util += min(dano, max(vida, 0))
            perdido += max(dano - max(vida, 0), 0)
            vida -= dano
        if vida <= 0:
            indice += 1
            if indice < len(vidas):
                vida = vidas[indice]
                t += parametros["desplazamiento_s"]
    return {"tiempo": t, "util": util, "perdido": perdido, "usos": usos}


def prueba_jefe(perfil, conversion, parametros):
    r = combatir(perfil, conversion, parametros, [parametros["vida_jefe"]], parametros["duracion_jefe_s"])
    r["dps"] = r["util"] / parametros["duracion_jefe_s"]
    return r


def prueba_caza(perfil, conversion, parametros):
    azar_vidas = random.Random(int(parametros["semilla"]))
    variacion = parametros["variacion_vida_mob_pct"] / 100
    vidas = [parametros["vida_mob"] * (1 + azar_vidas.uniform(-variacion, variacion))
             for _ in range(int(parametros["numero_mobs"]))]
    azar = random.Random(int(parametros["semilla"])) if parametros["critico_aleatorio_en_caza"] else None
    return combatir(perfil, conversion, parametros, vidas, azar=azar)


def calibrar(parametros, armas, arquetipos, conversion, habilidades):
    """Ajusta el daño de cada arma (y de los hechizos de quien no usa el arma)
    para que tarde lo mismo en la caza que el arma de referencia. Las
    habilidades que dependen del arma suben o bajan con ella. Como el tiempo de
    caza va a saltos (golpes por mob), se busca el factor por bisección."""
    lista = list(perfiles(armas, arquetipos, habilidades))
    referencia = next(p for p in lista if p["arma"]["arma"] == parametros["arma_referencia"])
    objetivo = prueba_caza(referencia, conversion, parametros)["tiempo"]

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
                fila[campo] = f"{v * factor:.1f}" if redondear else str(v * factor)

        bajo, alto = 0.2, 5.0
        for _ in range(40):
            medio = (bajo + alto) / 2
            aplicar(medio)
            if prueba_caza(perfil, conversion, parametros)["tiempo"] > objetivo:
                bajo = medio
            else:
                alto = medio
        aplicar((bajo + alto) / 2, redondear=True)

    escribir("armas.csv", armas)
    escribir("habilidades.csv", habilidades)
    print(f"Calibrado a {objetivo / 60:.1f} min de caza ({parametros['arma_referencia']}).")
    print("Guardado en datos/armas.csv y datos/habilidades.csv.\n")


def informe(parametros, armas, arquetipos, conversion, habilidades):
    filas = []
    for perfil in perfiles(armas, arquetipos, habilidades):
        filas.append((perfil, prueba_jefe(perfil, conversion, parametros),
                      prueba_caza(perfil, conversion, parametros)))
    media_dps = sum(j["dps"] for _, j, _ in filas) / len(filas)
    media_caza = sum(c["tiempo"] for _, _, c in filas) / len(filas)
    rapido = min(c["tiempo"] for _, _, c in filas)
    n = parametros["numero_mobs"]

    print(f"Nivel 1 · caza: {n:.0f} mobs de {parametros['vida_mob']:.0f} de vida "
          f"(±{parametros['variacion_vida_mob_pct']:.0f} %) · jefe: {parametros['duracion_jefe_s'] / 60:.0f} min\n")
    print(f"{'Arquetipo':<24}{'Arma':<14}{'s/golpe':>8}{'Daño':>7}{'Acciones/mob':>13}{'s/mob':>7}"
          f"{'Caza (min)':>11}{'vs media':>10}{'vs + rápido':>12}{'Perdido':>9}{'DPS jefe':>10}{'vs media':>10}")
    for perfil, jefe, caza in filas:
        a = perfil["arma"]
        con_arma = perfil["arquetipo"]["ataque_basico"] == "1"
        acciones = sum(caza["usos"].values()) / n
        print(f"{perfil['arquetipo']['nombre']:<24}{a['arma'] if con_arma else 'solo hechizos':<14}"
              f"{(a['segundos_entre_golpes'] if con_arma else '—'):>8}{(a['dano'] if con_arma else '—'):>7}"
              f"{acciones:>13.2f}{caza['tiempo'] / n:>7.2f}"
              f"{caza['tiempo'] / 60:>11.1f}{(caza['tiempo'] / media_caza - 1) * 100:>+9.1f}%"
              f"{(caza['tiempo'] / rapido - 1) * 100:>+11.1f}%"
              f"{caza['perdido'] / (caza['util'] + caza['perdido']) * 100:>8.1f}%"
              f"{jefe['dps']:>10.2f}{(jefe['dps'] / media_dps - 1) * 100:>+9.1f}%")

    dps = [j["dps"] for _, j, _ in filas]
    tiempos = [c["tiempo"] for _, _, c in filas]
    print(f"\nDiferencia máxima entre perfiles · caza: {(max(tiempos) / min(tiempos) - 1) * 100:.1f} %"
          f" · jefe: {(max(dps) / min(dps) - 1) * 100:.1f} %")
    print("'Perdido' = daño que sobra al rematar a cada mob en la prueba de caza.")

    print("\nReparto del daño contra el jefe (sin crítico):")
    for perfil, jefe, _ in filas:
        s = secundarias(perfil["arquetipo"], conversion, parametros)
        dano_arma = float(perfil["arma"]["dano"])
        aporte = {}
        for nombre, veces in jefe["usos"].items():
            if nombre == "golpe blanco":
                por_uso = (dano_arma + s["plano"]) * s["base"]
            else:
                h = next(h for h in perfil["habilidades"] if h["nombre"] == nombre)
                por_uso = sum(golpes_de(h, dano_arma, s))
            aporte[nombre] = (veces, por_uso, veces * por_uso)
        total = sum(v[2] for v in aporte.values())
        partes = ", ".join(f"{n} x{v[0]} ({v[1]:.0f} por uso, {v[2] / total * 100:.0f} %)" for n, v in aporte.items())
        print(f"  {perfil['arquetipo']['nombre']} ({perfil['arma']['arma']}): {partes}")


def main():
    datos = cargar()
    if "--calibrar" in sys.argv:
        calibrar(*datos)
    informe(*datos)


if __name__ == "__main__":
    main()
