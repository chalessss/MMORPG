# Simulador de balance

Compara los tres arquetipos de inicio (niveles 1 a 19) con cada arma que pueden elegir:

- **Físico cuerpo a cuerpo** (reparto base del Combatiente, 5/1/4): espada larga o espada corta; golpes blancos más golpe doble y golpe al suelo.
- **Físico a distancia** (reparto base del Atacante, 2/2/6): arco; golpes blancos más disparo cargado y ráfaga triple.
- **Mágico** (reparto base del Mago, 1/7/2): nunca pega con el bastón; solo lanza un hechizo fuerte y, mientras se recarga, tres débiles.

Pruebas:

- **Jefe**: 20 minutos golpeando un objetivo de 50 millones de vida.
- **Caza en combate puro**: matar 1.000 mobs de 420 de vida (±10 %), solo daño. El daño que sobra al rematar cada mob se pierde, así que penaliza los golpes grandes. No se gasta una habilidad en un mob que muere con un golpe blanco.
- **Caza real**: lo mismo, pero el cuerpo a cuerpo camina hasta cada mob, el de distancia pega gratis mientras el mob se acerca, el mob devuelve golpes, las habilidades gastan maná, se beben pociones y (si está activado) se descansa para recuperar vida y maná.

```
python3 herramientas/simulador/simular.py             # resultados
python3 herramientas/simulador/simular.py --calibrar  # recalcula el daño de armas y hechizos y lo guarda
python3 herramientas/simulador/simular.py --calibrar-real  # sube el daño del cuerpo a cuerpo para igualar en la caza real
python3 herramientas/simulador/simular.py --niveles   # caza real del nivel 1 al 19 con mobs que escalan
python3 herramientas/simulador/simular.py --ficha     # guarda la ficha de estadísticas por nivel en resultados/
```

`--calibrar` deja el arma de referencia (espada larga) como está y ajusta el daño de las demás armas, y el de los hechizos del mágico, para que todos tarden lo mismo en la caza en combate puro. Las habilidades de los físicos se definen como % del daño del arma y suben o bajan con ella.

`--calibrar-real` deja el arco y el bastón como están y ajusta solo el daño de las armas cuerpo a cuerpo para que, caminando entre mobs, tarden lo mismo que la media de los de distancia. Ojo: volver a ejecutar `--calibrar` después iguala de nuevo todo en combate puro tomando la espada larga como referencia, y deshace esa compensación.

Solo necesita Python 3, sin librerías extra. Todos los valores están en `datos/` (CSV), los mismos que más adelante se importarán a las DataTables de Unreal:

| Archivo | Contenido |
|---|---|
| `arquetipos.csv` | Reparto base de STR/INT/AGI, si usa ataque básico, si pega a distancia y qué armas puede llevar |
| `armas.csv` | Segundos entre golpe y golpe, daño por golpe y estadísticas que suma el arma |
| `habilidades.csv` | Habilidades de cada arquetipo: daño de cada golpe (en múltiplos del arma o en puntos), enfriamiento, duración y coste de maná |
| `conversion.csv` | Cuánto da cada punto de STR, INT y AGI |
| `mobs.csv` | Tipos de mob (físico o mágico, cuerpo a cuerpo o a distancia), su ciclo de ataques y en qué proporción aparecen |
| `parametros.csv` | Arma de referencia, jefe, mobs (vida, daño, ritmo), desplazamiento, vida y maná base, descansos, pociones, crítico base y azar |

Supuestos de esta versión (ver `docs/ESTADISTICAS.md`): nivel 1; una habilidad sin tiempo de lanzamiento ocupa el hueco de un golpe blanco. La caza real tarda un par de minutos en calcularse. En el jefe el crítico cuenta por su valor esperado; en la caza cada golpe tira su crítico con una semilla fija.

## Nivel 20: especializaciones (`simular20.py`)

Aproximación por rol de las 6 especializaciones del nivel 20 (ver `docs/ESTADISTICAS_NIVEL_20.md`): no busca paridad, sino comprobar que cada rol cumple su papel.

```
python3 herramientas/simulador/simular20.py           # jefe, caza de uno en uno y conglomerados de 6 y 12 mobs
python3 herramientas/simulador/simular20.py --ficha   # ficha de estadísticas del nivel 20
```

Datos en `datos/nivel20/`:

| Archivo | Contenido |
|---|---|
| `especializaciones.csv` | Reparto base, arma, si pega con el arma o a distancia y recurso secundario |
| `armas.csv` | Segundos entre golpes y daño de cada arma |
| `conversion.csv` | Pasiva de especialización: qué da cada punto (`todas` = valor común; cada especialización sobrescribe lo suyo) |
| `habilidades.csv` | Las 8 habilidades: las 1-4 de la clase de inicio (`melee`, `rango`, `magico`) y las 5-8 de cada especialización |
| `parametros.csv` | Mob del nivel 20, puntos totales, crítico, pociones, recursos secundarios (Ira, Energía, Foco, Trance) y remate |

Simula en pasos de 0,1 s. En los conglomerados todos los mobs del grupo pegan a la vez y entran en las habilidades de área; si un personaje muere 20 veces se da por hecho que no puede con esa caza.
