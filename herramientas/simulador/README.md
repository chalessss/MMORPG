# Simulador de balance

Compara los tres arquetipos de inicio (niveles 1 a 19) con cada arma que pueden elegir:

- **Físico cuerpo a cuerpo** (reparto base del Combatiente, 5/1/4): espada larga o espada corta; golpes blancos más golpe doble y golpe al suelo.
- **Físico a distancia** (reparto base del Atacante, 2/2/6): arco; golpes blancos más disparo cargado y ráfaga triple.
- **Mágico** (reparto base del Mago, 1/7/2): nunca pega con el bastón; solo lanza un hechizo fuerte y, mientras se recarga, tres débiles.

Pruebas:

- **Jefe**: 20 minutos golpeando un objetivo de 50 millones de vida.
- **Caza en combate puro**: matar 1.000 mobs de 420 de vida (±10 %), solo daño. El daño que sobra al rematar cada mob se pierde, así que penaliza los golpes grandes. No se gasta una habilidad en un mob que muere con un golpe blanco.
- **Caza real**: lo mismo, pero el cuerpo a cuerpo camina hasta cada mob, el de distancia pega gratis mientras el mob se acerca, el mob devuelve golpes, las habilidades gastan maná y se descansa para recuperar vida y maná.

```
python3 herramientas/simulador/simular.py             # resultados
python3 herramientas/simulador/simular.py --calibrar  # recalcula el daño de armas y hechizos y lo guarda
```

`--calibrar` deja el arma de referencia (espada larga) como está y ajusta el daño de las demás armas, y el de los hechizos del mágico, para que todos tarden lo mismo en la caza en combate puro. Las habilidades de los físicos se definen como % del daño del arma y suben o bajan con ella.

Solo necesita Python 3, sin librerías extra. Todos los valores están en `datos/` (CSV), los mismos que más adelante se importarán a las DataTables de Unreal:

| Archivo | Contenido |
|---|---|
| `arquetipos.csv` | Reparto base de STR/INT/AGI, si usa ataque básico, si pega a distancia y qué armas puede llevar |
| `armas.csv` | Segundos entre golpe y golpe, daño por golpe y estadísticas que suma el arma |
| `habilidades.csv` | Habilidades de cada arquetipo: daño de cada golpe (en múltiplos del arma o en puntos), enfriamiento, duración y coste de maná |
| `conversion.csv` | Cuánto da cada punto de STR, INT y AGI |
| `parametros.csv` | Arma de referencia, jefe, mobs (vida, daño, ritmo), desplazamiento, vida y maná base, descansos, crítico base y azar |

Supuestos de esta versión (ver `docs/ESTADISTICAS.md`): nivel 1, sin pociones; una habilidad sin tiempo de lanzamiento ocupa el hueco de un golpe blanco. La caza real tarda un par de minutos en calcularse. En el jefe el crítico cuenta por su valor esperado; en la caza cada golpe tira su crítico con una semilla fija.
