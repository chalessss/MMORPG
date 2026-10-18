# Capítulo de detalle — Estadísticas (parte 2): nivel 20 y clases

Estado: **en curso**. Segunda sesión del capítulo de estadísticas. La primera sesión cerró las estadísticas **previas** a la elección de clase (niveles 1–19, tres perfiles sin clase): ver `docs/RESUMEN_ESTADISTICAS.md` y el detalle en `docs/ESTADISTICAS.md`. Esta sesión cubre las **estadísticas finales de los personajes ya afectados por el cambio de clase en el nivel 20** (primera especialización).

## 1. Punto de partida

### 1.0 Clases de inicio: nombres oficiales (decidido)

- En el nivel 1 el jugador elige **daño mágico** o **daño físico**. Según lo que elija, el personaje sale con una de estas clases de inicio:

| Elección | Clase de inicio (nombre oficial) | Perfil de la parte 1 |
|---|---|---|
| Daño mágico | **Mágica - Rango** | Mágico |
| Daño físico | **Física - Melee** | Físico cuerpo a cuerpo |
| Daño físico | **Física - Rango** | Físico a distancia |

- Los nombres de clase que se usaron al describir los perfiles de inicio (Combatiente, Atacante a distancia, Mago…) eran **ejemplos de la especialización que elegirían después**, no el nombre oficial de la clase de inicio.
- Las estadísticas de estas clases son las de los perfiles cerrados en la parte 1 (reparto, armas, crecimiento y habilidades).
- **Física son dos clases distintas** (decidido): Física - Melee y Física - Rango, cada una con sus propias especializaciones.

### 1.0b Especializaciones del nivel 20 (decidido)

Lista cerrada: son **todas** las especializaciones que habrá en el nivel 20.

| Clase de inicio | Especializaciones del nivel 20 |
|---|---|
| Física - Melee | **Luchador**, **Combatiente**, **Asesino** |
| Física - Rango | **Atacante a distancia** (única opción) |
| Mágica - Rango | **Mago**, **Invocador** |


### 1.0c Transición en el nivel 20: se recalcula todo (decidido)

- Al elegir especialización **se recalculan todas las estadísticas** con el reparto de la especialización, como si el personaje siempre lo hubiera tenido.
- **Cada especialización tiene su propia conversión** de STR, INT y AGI: un mismo punto no da lo mismo a todas. Por ejemplo, la STR da **menos daño físico al Asesino** que al Luchador, pero el Asesino saca **más probabilidad de crítico** de su AGI.
- Se hace un **balance nuevo de las 6 especializaciones** a partir de su reparto base y de esa conversión propia.

### 1.0d Balance desde el nivel 20: por rol, no por paridad (decidido)

- **Del 1 al 19 se buscaba paridad**: que todos llegaran al nivel 20 a la vez, sin una clase muy adelantada. **Desde el 20 ya no**: las especializaciones no tienen que quedar en el mismo ritmo de caza.
- El **simulador solo sirve de aproximación**, como referencia de que cada rol cumple su papel:
  - las de **daño** hacen mucho daño;
  - las que **curan** no se quedan en cero de daño;
  - las que **tanquean** hacen un daño medio.
- **Cada rol caza a su manera.** Los tanques irán a **zonas de conglomerados**, con muchos mobs juntos, donde aguantan el daño gracias a la armadura y matan en área. Allí deben sacar **la misma experiencia** que otra especialización matando mobs de uno en uno.
- Ejemplo: si un Invocador intenta pegar a seis mobs a la vez, lo matan en 2–3 segundos; un Combatiente los aguanta y además hace mucho más daño en área.
- Implicación para el capítulo de mapas: cada zona de caza debe prever **mobs agrupados** para las especializaciones que aguantan y pegan en área, además de mobs sueltos.

### 1.1 Cómo llega el personaje al nivel 20

Valores del nivel 19 (ficha vigente: `python3 herramientas/simulador/simular.py --ficha`):

| Clase de inicio | Vida | Maná | Armadura | Defensa | Golpe blanco |
|---|---|---|---|---|---|
| Física - Melee (espada larga / corta) | 4.975 | 920 | 950 | 19,5 % | 1.072 / 922 |
| Física - Rango (arco) | 2.075 | 1.220 | 950 | 7,9 % | 929 |
| Mágica - Rango | 1.575 | 2.990 | 950 | 5,9 % | — |

- Qué da cada punto (común a todos hasta el 19): **STR** +25 vida, +0,2 vida/s, +0,1 % de defensa física y mágica, +1,5 % de daño; **INT** +15 maná, +0,2 maná/s, +2,5 % de daño de habilidades; **AGI** +2 de daño plano por golpe.
- Cuatro habilidades por perfil, en nivel de habilidad 4 desde el nivel 15.
- Caza de 1.000 mobs en el nivel 19: espada larga 823 min, espada corta 765, arco 1.060, mágico 928 (38,5 % de diferencia, intencionada).

### 1.2 Lo que ya está decidido sobre el nivel 20 (de la parte 1)

- Una **misión del entrenador de clase** ofrece las clases del arquetipo (`ESTADISTICAS.md`, 1.7).
- Con la clase llegan: **armas propias**, el **reparto base de la clase**, **muchas más estadísticas visibles**, **4–5 habilidades nuevas** (activas y pasivas), equipo especializado y el contenido de profesiones y desarrollo.
- **Cada clase recibe una pasiva que cambia lo que da cada punto** (valores de ejemplo):
  - **Mágicos**: cada punto de INT vale mucho más (por ejemplo, ×3), sobre todo en daño.
  - **Agilidad**: cada pocos puntos de AGI (por ejemplo, cada 3) suben el crítico, el robo de vida o lo que haga falta para equilibrar.
  - **Luchador / Combatiente**: la STR da más vida y más armadura (por ejemplo, 120 de vida en lugar de 100); la INT solo da maná plano.
  - **Mago** (bastones): más regeneración de maná y más daño de hechizos.
  - **Invocador** (varitas): menos daño base, más regeneración de maná y más potencia de escudos y curaciones.
- **6–8 habilidades activables** por clase, y con ellas se ajusta el coste de maná. Objetivo: **300–1.000 pociones de maná cada 1.000 mobs**, con **menos de 150 de diferencia** entre perfiles.
- **El PvP se balancea desde el nivel 20**, con el triángulo **STR > AGI > INT > STR** (`ESTADISTICAS.md`, 1.3).
- Objetivos de daño por rol (de ejemplo): daño puro un 3–5 % por encima de la media, tanque un 5 % por debajo y curandero un 8 % por debajo (`ESTADISTICAS.md`, 1.5).

### 1.3 Reparto base de las clases (tabla vigente de la hoja, filas 54–60)

| ID | Clase | STR | INT | AGI | Arma (hoja) | Velocidad | Recurso secundario |
|---|---|---|---|---|---|---|---|
| CL_LUC | Luchador | 7 | 1 | 2 | Espada | 1,0 | Ira |
| CL_COM | Combatiente | 5 | 1 | 4 | Espada | 1,0 | Ira |
| CL_ASE | Asesino | 3 | 1 | 6 | Daga | 1,6 | Energía |
| CL_ATA | Atacante a distancia | 2 | 2 | 6 | Arco | 1,1 | Foco |
| CL_MAG | Mago | 1 | 7 | 2 | Bastón | 0,6 | Iluminación |
| CL_INV | Invocador | 2 | 5 | 3 | Varita | 1,2 | Iluminación |

La velocidad de la hoja está en golpes relativos; en el simulador se expresa en segundos entre golpe y golpe.

## 2. Trabajo de esta sesión

1. ~~**Especializaciones por clase de inicio**~~: decidido (1.0b).
2. ~~**Transición en el nivel 20**~~: se recalcula todo (1.0c). Falta fijar el crecimiento por nivel de cada especialización.
3. **Pasiva de clase**: qué da cada punto de STR, INT y AGI en cada una de las 6 clases.
4. **Habilidades de clase** (6–8 activables) en lo que afecta a las estadísticas: daño, enfriamiento y coste de maná.
5. **Armas de clase**: daño y velocidad de daga, varita y espadas de clase.
6. **Recursos secundarios** (Ira, Energía, Foco, Iluminación): cómo se generan y gastan.
7. **Estadísticas visibles nuevas** desde el nivel 20 (las neutrales de la hoja que se muestran y empiezan a contar).
8. **Simulación de las 6 clases en el nivel 20**: caza de 1.000 mobs y jefe de 20 minutos, con el objetivo de pociones de maná.
9. **Primer balance PvP** con el triángulo STR > AGI > INT > STR.
10. **Ficha cerrada del nivel 20** por clase.

## 3. Preguntas abiertas

- **Nombres de las etapas**: con la clase base en el nivel 20, la "especialización 1" (Dos manos, Tanque, Arquero…) parece pasar al nivel 40 y la especialización final al 60, como en la hoja. En los documentos generales aún figura la especialización 1 en el 20. Hay que confirmarlo y unificarlo.
- **Flecos de la parte 1** que conviene cerrar aquí: validar los valores por punto de INT y AGI, daño de las armas por tramos y pociones que curen según el nivel.
