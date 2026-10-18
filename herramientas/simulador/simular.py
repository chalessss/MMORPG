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
    conversion = {}
    for c in leer("conversion.csv"):
        conversion.setdefault(c["estadistica"], {})[c["secundaria"]] = float(c["por_punto"])
    habilidades = leer("habilidades.csv")
    return parametros, armas, conversion, habilidades, leer("clases.csv")


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


def simular_clase(clase, parametros, armas, conversion, habilidades):
    arma = armas[clase["arma"]]
    velocidad, dano_arma = float(arma["velocidad"]), float(arma["dano"])
    propias = [h for h in habilidades if h["clase_id"] in (clase["id"], "*")]
    ataques = [h for h in propias if h["tipo"] == "dano"]
    mejoras = [h for h in propias if h["tipo"] == "mejora"]

    base = {e: float(clase[e]) for e in ("str", "int", "agi")}
    duracion = parametros["duracion_s"]
    t = 0.0
    listo = {h["nombre"]: 0.0 for h in propias}  # cuándo sale del enfriamiento
    activa_hasta = {h["nombre"]: -1.0 for h in mejoras}
    total = {"ataque básico": 0.0}
    golpes = {"ataque básico": 0}
    # Parte del daño de habilidades que sale de su daño base (sin el plano de AGI):
    # sirve para calcular cuánto habría que subir o bajar las habilidades.
    habilidades_base = 0.0

    while t < duracion:
        principales = dict(base)
        for m in mejoras:
            if activa_hasta[m["nombre"]] > t and m["efecto"].startswith("principal+"):
                principales[clase["estadistica_principal"]] += float(m["efecto"].split("+")[1])
        s = secundarias(principales, conversion, parametros)

        # Prioridad: mantener las mejoras, luego la habilidad de más daño disponible,
        # y si no hay ninguna, ataque básico.
        mejora = next((m for m in mejoras if activa_hasta[m["nombre"]] <= t and listo[m["nombre"]] <= t), None)
        if mejora:
            activa_hasta[mejora["nombre"]] = t + float(mejora["lanzamiento"]) + float(mejora["duracion"])
            listo[mejora["nombre"]] = t + float(mejora["enfriamiento"])
            t += float(mejora["lanzamiento"])
            continue

        disponibles = [h for h in ataques if listo[h["nombre"]] <= t]
        if disponibles:
            h = max(disponibles, key=lambda h: float(h["dano"]))
            dano = (float(h["dano"]) + s["plano"]) * s["base"] * s["habilidad"] * s["critico"]
            total[h["nombre"]] = total.get(h["nombre"], 0) + dano
            habilidades_base += float(h["dano"]) * s["base"] * s["habilidad"] * s["critico"]
            golpes[h["nombre"]] = golpes.get(h["nombre"], 0) + 1
            listo[h["nombre"]] = t + float(h["enfriamiento"])
            t += float(h["lanzamiento"])
        else:
            dano = (dano_arma + s["plano"]) * s["base"] * s["critico"]
            total["ataque básico"] += dano
            golpes["ataque básico"] += 1
            t += 1 / velocidad
    return total, golpes, habilidades_base


def main():
    parametros, armas, conversion, habilidades, clases = cargar()
    resultados = []
    for clase in clases:
        total, golpes, habilidades_base = simular_clase(clase, parametros, armas, conversion, habilidades)
        resultados.append((clase, total, golpes, sum(total.values()), habilidades_base))

    media = sum(r[3] for r in resultados) / len(resultados)
    duracion = parametros["duracion_s"]
    print(f"Muñeco de entrenamiento · {duracion / 60:.0f} minutos · nivel 1 · sin defensa\n")
    print(f"{'Clase':<22}{'Arma':<9}{'Daño total':>12}{'DPS':>8}{'vs media':>10}{'Básicos':>9}")
    for clase, total, golpes, suma, _ in resultados:
        print(f"{clase['clase']:<22}{clase['arma']:<9}{suma:>12,.0f}{suma / duracion:>8.1f}"
              f"{(suma / media - 1) * 100:>+9.1f}%{total['ataque básico'] / suma * 100:>8.0f}%")
    extremos = [r[3] for r in resultados]
    print(f"\nDiferencia entre la clase más fuerte y la más débil: {(max(extremos) / min(extremos) - 1) * 100:.1f} %")

    print("\nDesglose por fuente de daño:")
    for clase, total, golpes, suma, _ in resultados:
        partes = ", ".join(f"{n} {d / suma * 100:.0f}% ({golpes[n]} golpes)" for n, d in total.items())
        print(f"  {clase['clase']}: {partes}")

    print("\nAjuste del daño de las habilidades para que todas las clases igualen la media:")
    for clase, total, golpes, suma, habilidades_base in resultados:
        factor = (media - (suma - habilidades_base)) / habilidades_base
        print(f"  {clase['clase']}: x{factor:.2f} ({(factor - 1) * 100:+.0f} %)")


if __name__ == "__main__":
    main()
