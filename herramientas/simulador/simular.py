"""Simulador de balance de los arquetipos de inicio (niveles 1 a 19).

Lee los datos de la carpeta datos/ (los mismos CSV que se importarán a las
DataTables de Unreal) y compara cuánto daño hace cada arquetipo con cada arma en
dos pruebas:

  - Jefe: 20 minutos golpeando un objetivo de vida casi infinita.
  - Caza: matar 1.000 mobs de 1.000 de vida (el daño que sobra al matar se pierde).

Uso:
  python3 simular.py             muestra los resultados
  python3 simular.py --calibrar  recalcula el daño de las armas y los hechizos
                                 para igualar al arma de referencia y lo guarda
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


def combatir(perfil, conversion, parametros, vidas, limite_s=None, azar=None):
    """Pelea contra una lista de objetivos (sus vidas) uno detrás de otro.

    Devuelve el tiempo empleado, el daño útil, el daño perdido al rematar y los
    usos de cada acción. Los golpes blancos dañan al empezar el golpe; los
    hechizos, al terminar de lanzarlos. Con `azar` (un random.Random) cada golpe
    tira su crítico; sin él, se usa el valor esperado.
    """
    s = secundarias(perfil["arquetipo"], conversion, parametros)
    intervalo = float(perfil["arma"]["segundos_entre_golpes"])
    dano_arma = float(perfil["arma"]["dano"])
    con_ataque_basico = perfil["arquetipo"]["ataque_basico"] == "1"
    habilidades = perfil["habilidades"]
    listo = {h["nombre"]: 0.0 for h in habilidades}  # cuándo sale del enfriamiento
    usos = {}
    t, util, perdido, indice = 0.0, 0.0, 0.0, 0
    vida = vidas[0]

    while indice < len(vidas) and (limite_s is None or t < limite_s):
        disponibles = [h for h in habilidades if listo[h["nombre"]] <= t]
        if disponibles:
            # Prioridad: el hechizo de más daño que esté disponible.
            h = max(disponibles, key=lambda h: float(h["dano"]) * float(h["golpes"]))
            listo[h["nombre"]] = t + float(h["enfriamiento"])
            t += float(h["lanzamiento"])
            n = float(h["golpes"])
            dano = (float(h["dano"]) + s["plano"]) * n * s["base"] * s["habilidad"]
            nombre = h["nombre"]
        elif con_ataque_basico:
            dano = (dano_arma + s["plano"]) * s["base"]
            nombre = "golpe blanco"
            t += intervalo
        elif listo:
            t = min(listo.values())  # esperar a que salga un hechizo
            continue
        else:
            break
        if azar is None:
            dano *= s["critico"]
        elif azar.random() < s["probabilidad_critico"]:
            dano *= s["multiplicador_critico"]
        usos[nombre] = usos.get(nombre, 0) + 1
        util += min(dano, vida)
        perdido += max(dano - vida, 0)
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
    vidas = [parametros["vida_mob"]] * int(parametros["numero_mobs"])
    azar = random.Random(int(parametros["semilla"])) if parametros["critico_aleatorio_en_caza"] else None
    return combatir(perfil, conversion, parametros, vidas, azar=azar)


def calibrar(parametros, armas, arquetipos, conversion, habilidades):
    """Ajusta el daño de cada arma (y de los hechizos de quien no usa el arma)
    para que su daño por segundo contra el jefe iguale al del arma de referencia.
    El daño contra el jefe es lineal en esos valores, así que basta con dos
    pruebas por perfil para despejar el valor exacto."""
    lista = list(perfiles(armas, arquetipos, habilidades))
    referencia = next(p for p in lista if p["arma"]["arma"] == parametros["arma_referencia"])
    objetivo = prueba_jefe(referencia, conversion, parametros)["dps"]

    for perfil in lista:
        if perfil is referencia:
            continue
        if perfil["arquetipo"]["ataque_basico"] == "1":
            ajustables = [perfil["arma"]]
        else:
            ajustables = perfil["habilidades"]
        originales = [float(a["dano"]) for a in ajustables]
        resultados = []
        for factor in (1, 2):
            for a, v in zip(ajustables, originales):
                a["dano"] = str(v * factor)
            resultados.append(prueba_jefe(perfil, conversion, parametros)["dps"])
        pendiente = resultados[1] - resultados[0]
        factor = 1 + (objetivo - resultados[0]) / pendiente
        for a, v in zip(ajustables, originales):
            a["dano"] = f"{v * factor:.1f}"

    escribir("armas.csv", armas)
    escribir("habilidades.csv", habilidades)
    print(f"Calibrado a {objetivo:.2f} de daño por segundo ({parametros['arma_referencia']}).")
    print("Guardado en datos/armas.csv y datos/habilidades.csv.\n")


def informe(parametros, armas, arquetipos, conversion, habilidades):
    filas = []
    for perfil in perfiles(armas, arquetipos, habilidades):
        filas.append((perfil, prueba_jefe(perfil, conversion, parametros),
                      prueba_caza(perfil, conversion, parametros)))
    media_dps = sum(j["dps"] for _, j, _ in filas) / len(filas)
    media_caza = sum(c["tiempo"] for _, _, c in filas) / len(filas)

    print(f"Nivel 1 · jefe: {parametros['duracion_jefe_s'] / 60:.0f} min · caza: "
          f"{parametros['numero_mobs']:.0f} mobs de {parametros['vida_mob']:.0f} de vida\n")
    rapido = min(c["tiempo"] for _, _, c in filas)
    print(f"{'Arquetipo':<24}{'Arma':<14}{'s/golpe':>8}{'Daño':>7}{'DPS jefe':>10}{'vs media':>10}"
          f"{'Golpes/mob':>11}{'s/mob':>7}{'Caza (min)':>11}{'vs media':>10}{'vs + rápido':>12}{'Perdido':>9}")
    for perfil, jefe, caza in filas:
        a = perfil["arma"]
        con_arma = perfil["arquetipo"]["ataque_basico"] == "1"
        golpes = sum(caza["usos"].values()) / parametros["numero_mobs"]
        print(f"{perfil['arquetipo']['nombre']:<24}{a['arma'] if con_arma else 'solo hechizos':<14}"
              f"{(a['segundos_entre_golpes'] if con_arma else '—'):>8}{(a['dano'] if con_arma else '—'):>7}"
              f"{jefe['dps']:>10.2f}{(jefe['dps'] / media_dps - 1) * 100:>+9.1f}%"
              f"{golpes:>11.2f}{caza['tiempo'] / parametros['numero_mobs']:>7.2f}"
              f"{caza['tiempo'] / 60:>11.1f}{(caza['tiempo'] / media_caza - 1) * 100:>+9.1f}%"
              f"{(caza['tiempo'] / rapido - 1) * 100:>+11.1f}%"
              f"{caza['perdido'] / (caza['util'] + caza['perdido']) * 100:>8.1f}%")

    dps = [j["dps"] for _, j, _ in filas]
    tiempos = [c["tiempo"] for _, _, c in filas]
    print(f"\nDiferencia máxima entre perfiles · jefe: {(max(dps) / min(dps) - 1) * 100:.1f} %"
          f" · caza: {(max(tiempos) / min(tiempos) - 1) * 100:.1f} %")
    print("'Perdido' = daño que sobra al rematar a cada mob en la prueba de caza.")

    print("\nUsos en la prueba del jefe:")
    for perfil, jefe, _ in filas:
        usos = ", ".join(f"{n} x{v}" for n, v in jefe["usos"].items())
        print(f"  {perfil['arquetipo']['nombre']} ({perfil['arma']['arma']}): {usos}")
    if habilidades:
        print("\nHechizos:")
        for h in habilidades:
            print(f"  {h['nombre']} ({h['arquetipo']}): {h['dano']} de daño base, "
                  f"{h['enfriamiento']} s de enfriamiento, {h['lanzamiento']} s de lanzamiento")


def main():
    datos = cargar()
    if "--calibrar" in sys.argv:
        calibrar(*datos)
    informe(*datos)


if __name__ == "__main__":
    main()
