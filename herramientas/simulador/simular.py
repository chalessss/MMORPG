"""Simulador de daño contra un muñeco de entrenamiento (nivel 1).

Lee los datos de balance de la carpeta datos/ (los mismos CSV que se importarán
a las DataTables de Unreal) y calcula cuánto daño hace cada clase golpeando a un
muñeco sin defensa durante la duración configurada.

Uso: python3 simular.py
"""

import csv
from pathlib import Path

DATOS = Path(__file__).parent / "datos"


def leer(nombre):
    with open(DATOS / nombre, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cargar():
    parametros = {p["parametro"]: float(p["valor"]) for p in leer("parametros.csv")}
    armas = {a["arma"]: a for a in leer("armas.csv")}
    arquetipos = {a["arquetipo"]: a for a in leer("arquetipos.csv")}
    conversion = {}
    for c in leer("conversion.csv"):
        conversion.setdefault(c["estadistica"], {})[c["secundaria"]] = float(c["por_punto"])
    return parametros, armas, arquetipos, conversion, leer("habilidades.csv"), leer("clases.csv")


def secundarias(principales, conversion, parametros):
    """Convierte STR/INT/AGI en las estadísticas secundarias que usa el combate."""
    s = {}
    for estadistica, puntos in principales.items():
        for secundaria, por_punto in conversion.get(estadistica, {}).items():
            s[secundaria] = s.get(secundaria, 0) + puntos * por_punto
    probabilidad = (parametros["critico_base_pct"] + s.get("critico_pct", 0)) / 100
    multiplicador = parametros["multiplicador_critico_base"] + s.get("critico_aumentado_pct", 0) / 100
    return {
        "plano": s.get("dano_base", 0),
        "base": 1 + s.get("dano_base_pct", 0) / 100,
        "habilidad": 1 + s.get("dano_habilidad_pct", 0) / 100,
        # Valor esperado del crítico: así el resultado no depende del azar.
        "critico": 1 + min(probabilidad, 1) * (multiplicador - 1),
    }


def simular_clase(clase, parametros, armas, arquetipos, conversion, habilidades):
    """Devuelve el daño por fuente, los golpes por fuente y la parte del daño de
    habilidades que sale de su escala de arma (para calcular ajustes)."""
    arma = armas[clase["arma"]]
    velocidad, dano_arma = float(arma["velocidad"]), float(arma["dano"])
    con_ataque_basico = arquetipos[clase["arquetipo"]]["ataque_basico"] == "1"
    propias = [h for h in habilidades if h["arquetipo"] == clase["arquetipo"]]
    if not parametros["usar_habilidades"]:
        propias = []

    s = secundarias({e: float(clase[e]) for e in ("str", "int", "agi")}, conversion, parametros)
    duracion = parametros["duracion_s"]
    t = 0.0
    listo = {h["nombre"]: 0.0 for h in propias}  # cuándo sale del enfriamiento
    total, golpes = {}, {}
    habilidades_escala = 0.0

    while t < duracion:
        # Prioridad: la habilidad de más daño disponible; si no hay, ataque básico.
        disponibles = [h for h in propias if listo[h["nombre"]] <= t]
        if disponibles:
            h = max(disponibles, key=lambda h: float(h["escala_arma"]) * float(h["golpes"]))
            n = float(h["golpes"])
            multiplicadores = s["base"] * s["habilidad"] * s["critico"]
            escala = float(h["escala_arma"]) * dano_arma * n * multiplicadores
            dano = escala + s["plano"] * n * multiplicadores
            total[h["nombre"]] = total.get(h["nombre"], 0) + dano
            golpes[h["nombre"]] = golpes.get(h["nombre"], 0) + 1
            habilidades_escala += escala
            listo[h["nombre"]] = t + float(h["enfriamiento"])
            # Sin tiempo de lanzamiento, la habilidad ocupa el hueco de un golpe blanco.
            t += float(h["lanzamiento"]) or 1 / velocidad
        elif con_ataque_basico:
            dano = (dano_arma + s["plano"]) * s["base"] * s["critico"]
            total["golpe blanco"] = total.get("golpe blanco", 0) + dano
            golpes["golpe blanco"] = golpes.get("golpe blanco", 0) + 1
            t += 1 / velocidad
        elif listo:
            t = min(listo.values())  # esperar a que salga una habilidad
        else:
            break
    return total, golpes, habilidades_escala


def main():
    parametros, armas, arquetipos, conversion, habilidades, clases = cargar()
    resultados = []
    for clase in clases:
        total, golpes, escala = simular_clase(clase, parametros, armas, arquetipos, conversion, habilidades)
        resultados.append({"clase": clase, "total": total, "golpes": golpes,
                           "suma": sum(total.values()), "escala": escala})

    media = sum(r["suma"] for r in resultados) / len(resultados)
    duracion = parametros["duracion_s"]
    modo = "con habilidades" if parametros["usar_habilidades"] else "solo golpes blancos"
    print(f"Muñeco de entrenamiento · {duracion / 60:.0f} minutos · nivel 1 · sin defensa · {modo}\n")
    print(f"{'Clase':<22}{'Arquetipo':<11}{'Arma':<8}{'Daño total':>11}{'DPS':>7}{'vs media':>10}{'Blancos':>9}")
    for r in resultados:
        c, suma = r["clase"], r["suma"]
        blancos = r["total"].get("golpe blanco", 0) / suma * 100
        print(f"{c['clase']:<22}{c['arquetipo']:<11}{c['arma']:<8}{suma:>11,.0f}{suma / duracion:>7.1f}"
              f"{(suma / media - 1) * 100:>+9.1f}%{blancos:>8.0f}%")
    sumas = [r["suma"] for r in resultados]
    print(f"\nDiferencia entre la clase más fuerte y la más débil: {(max(sumas) / min(sumas) - 1) * 100:.1f} %")

    print("\nDesglose por fuente de daño:")
    for r in resultados:
        partes = ", ".join(f"{n} {d / r['suma'] * 100:.0f}% ({r['golpes'][n]} veces)" for n, d in r["total"].items())
        print(f"  {r['clase']['clase']}: {partes}")

    if not parametros["usar_habilidades"]:
        return
    # Las habilidades de cada arquetipo se ajustan para igualar la media del arquetipo
    # de referencia. El daño es lineal en la escala de las habilidades, así que el
    # factor sale directo.
    referencia = next(a for a, d in arquetipos.items() if d["referencia"] == "1")
    grupo_ref = [r for r in resultados if r["clase"]["arquetipo"] == referencia]
    objetivo = sum(r["suma"] for r in grupo_ref) / len(grupo_ref)
    print(f"\nAjuste de las habilidades de cada arquetipo para igualar la media de '{referencia}':")
    for arquetipo in arquetipos:
        grupo = [r for r in resultados if r["clase"]["arquetipo"] == arquetipo]
        escala = sum(r["escala"] for r in grupo)
        if arquetipo == referencia or not grupo or not escala:
            continue
        factor = (objetivo * len(grupo) - sum(r["suma"] - r["escala"] for r in grupo)) / escala
        print(f"  {arquetipos[arquetipo]['nombre']}: multiplicar la escala_arma de sus habilidades por {factor:.2f}")


if __name__ == "__main__":
    main()
