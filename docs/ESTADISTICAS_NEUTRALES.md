# Capítulo de detalle — Estadísticas (parte 3): neutrales

Estado: **en curso**. Tercera parte del capítulo de estadísticas (parte 1: `docs/ESTADISTICAS.md`, niveles 1–19; parte 2: `docs/ESTADISTICAS_NIVEL_20.md`, nivel 20). Las neutrales no dependen de STR, INT ni AGI: vienen de la **joyería y los encantamientos** (decidido en la parte 1).

## 1. Neutrales por temporada (decidido)

| Temporada 1 (niveles 1–20) | Temporada 2 (niveles 21–40) |
|---|---|
| Evasión | Debilitación |
| Precisión | Resistencia a la debilitación |
| Defensa física | Daño PvP |
| Defensa mágica | Resistencia PvP |
| Daño a monstruos | Efecto de pociones |
| Experiencia de caza | % de caída |
| **Velocidad de recolección** (nueva) | % de caída con suerte |
| CDR (reducción de enfriamiento) | Daño a jefes |

- La **Temporada 1 es casi todo PvE**: sus neutrales se valoran por cómo afectan al **farmeo** (matar mobs, gastar pociones, recolectar). Las del PvP llegan en la Temporada 2.
- Orden de trabajo: primero **evasión y precisión**; después las demás de la Temporada 1.

## 2. Precisión y evasión

### 2.1 Reglas (decidido)

- **La evasión solo vale contra ataques físicos.** Los hechizos aciertan siempre: la evasión no restringe nada de los ataques mágicos.
- **Triángulo (PvP, Temporada 2):** los personajes de fuerza (Combatiente y los que buscarán estadísticas defensivas en el equipo) acumularán evasión para aguantar a los mobs; eso les dará **ventaja clara contra los de agilidad**, cuyos golpes (y críticos) dejarán de entrar y les bajará mucho el daño. Un mago les seguirá pegando siempre.
- **Cuidado con el mago:** hay que evitar que un mago se llene de evasión y el de agilidad ya no le pueda hacer nada. La joyería y las estadísticas que busque el mago tienen que ser **distintas de la evasión**. (La armadura ya separa mucho: los golpes del Asesino entran casi enteros a un mago, pero la armadura y la evasión de un Combatiente serán muy superiores.)
- **Mobs:** su precisión y su evasión **igualan su nivel** (un mob del nivel 20 tiene 20 de precisión y 20 de evasión). Los **élites** tendrán más evasión, vida y daño.
- **Equipo base:** con el equipo mínimo, un personaje debería llegar a **unos 15 puntos** de precisión; para acertar de verdad tendrá que buscar precisión extra en su equipo.
- **Fórmula por escalones** (golpes físicos; igual para el jugador contra el mob y para el mob contra el jugador):

| Precisión del atacante frente a la evasión del defensor | Acierto |
|---|---|
| 5 puntos o más por encima | **100 %** (acierta siempre) |
| Igual o hasta 4 por encima | 95 % (falla muy de vez en cuando) |
| De 1 a 5 por debajo | 90 % |
| De 6 a 10 por debajo | 80 % |
| De 11 a 15 por debajo | 70 % (por ejemplo, 30 de precisión contra 45 de evasión) |
| … | −10 % por cada 5 puntos (o fracción) más, hasta el **0 %** |

- Así se puede llegar a **acertar siempre** (100 %) y a **no acertar nunca** (0 %), y lo mismo con la evasión.
- En el simulador: `precision_activa` y los valores `acierto_*`, `precision_mob` y `evasion_mob` de `parametros.csv`. Está desactivada en las pruebas generales hasta cerrar los valores; la prueba se lanza con `python3 herramientas/simulador/simular20.py --precision`.

### 2.2 Primera simulación: el Combatiente (5, 10, 15 y 20 puntos de precisión y de evasión)

Contra mobs del nivel 20 (20 de precisión y 20 de evasión). La mitad de los mobs pega con daño físico (se puede esquivar) y la otra mitad con daño mágico (no). Pociones cada 300 mobs.

| Precisión y evasión | Acierta | Le aciertan (golpes físicos) | De uno en uno | Grupos de 6 | Grupos de 12 | Pociones de maná (uno en uno) |
|---|---|---|---|---|---|---|
| Sin fallos (referencia) | 100 % | 100 % | 49 mobs/h | 129 | 239 | 104 |
| 5 | 70 % | 100 % | 33 (−33 %) | 89 | 160 (17 pociones de vida) | 151 |
| 10 | 80 % | 100 % | 38 (−22 %) | 103 | 182 (8) | 134 |
| 15 | 90 % | 100 % | 43 (−12 %) | 114 | 211 (1) | 118 |
| 20 | 95 % | 95 % | 46 (−6 %) | 122 | 224 | 108 |

Lectura:
- Con el equipo base (~15 puntos) el Combatiente pierde un **12 %** de caza contra mobs de su nivel; con 5 puntos, un tercio. **Buscar precisión compensa**.
- Con poca precisión las peleas duran más: gasta **más maná** (104 → 151 pociones) y, con 12 mobs, empieza a necesitar pociones de vida.
- **Su evasión no hace nada hasta superar la precisión de los mobs**: con 5–15 puntos los mobs le aciertan siempre; con 20, un 95 % (esquiva 300–540 golpes cada 300 mobs). Para que los mobs fallen de verdad necesita **25 o más**.
- Pendiente: el resto de especializaciones y la evasión por encima de 20.
