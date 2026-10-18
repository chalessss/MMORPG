# Capítulo de detalle — Estadísticas

Estado: **en curso**. Primer capítulo de detalle. Este archivo recoge el punto de partida (lo ya decidido y lo que hay en la hoja de cálculo), la propuesta de estructura y las preguntas abiertas. Se irá completando en la sesión.

## 1. Punto de partida

### 1.1 Ya decidido en el diseño base

- Tres estadísticas **principales**: Fuerza (STR), Inteligencia (INT) y Agilidad (AGI), más estadísticas **derivadas** y **neutrales**.
- Recursos: vida, maná (MP) y un recurso secundario según la clase (Ira, Energía, Foco, Iluminación).
- **Todas las estadísticas suman para todas las clases**, pero no por igual: el ataque mágico ayuda a un guerrero mucho menos que a un mago.
- Fuentes de estadísticas: nivel, equipo, desarrollo (+1 a +10), encantamiento (estadísticas aleatorias), códice (bonificaciones planas y porcentuales de cuenta), joyería con rangos aleatorios, consumibles de cocina, técnicas de clan, conjuntos.
- La **puntuación de poder** (clasificación) se calcula a partir de las estadísticas: fórmula pendiente de este capítulo.
- Los valores de balance van en datos (hoja → DataTables), no en código.

### 1.2 Lo que hay en la hoja "Organizando la Base de Datos del Juego"

**Qué da cada punto de estadística principal** (pestaña principal, columnas W–Z) — **decidido**: cada punto de STR, INT o AGI sube todas las secundarias de su columna. Las **neutrales** no dependen de ninguna principal.

| Fuerza | Inteligencia | Agilidad | Neutrales |
|---|---|---|---|
| Vida base | Maná base | Daño base | Evasión |
| Regeneración de vida | Regeneración de maná | Crítico | Precisión |
| % defensa física | % daño de habilidad | Crítico aumentado | Defensa física |
| % defensa mágica | | | Defensa mágica |
| % daño base | | | Daño a monstruos |
| | | | Daño a jefes |
| | | | Reducción de enfriamiento (CDR) |
| | | | Debilitación |
| | | | Resistencia a la debilitación |
| | | | Daño PvP |
| | | | Resistencia PvP |
| | | | Experiencia de caza |

Hay además una columna con las anotaciones `AGI>INT`, `INT>STR`, `STR>AGI` (ver 1.3).

**Estadísticas base de las clases de la Temporada 1** — tabla corregida (filas 54–60 de la pestaña principal; la tabla de las filas 45–51 y la de "Habilidades 2.0" son versiones anteriores y **no se usan**). Es el **reparto de nivel 1** que recibe el personaje por ser de esa clase (decidido). Cada clase suma 10 puntos:

| ID | Clase | STR | INT | AGI | Recurso secundario |
|---|---|---|---|---|---|
| CL_LUC | Luchador | 7 | 1 | 2 | Ira (Medidor de Ira) |
| CL_COM | Combatiente | 5 | 1 | 4 | Ira (Medidor de Ira) |
| CL_ASE | Asesino | 3 | 1 | 6 | Energía (Medidor de Energía) |
| CL_ATA | Atacante a distancia | 2 | 2 | 6 | Foco (Puntos de Foco) |
| CL_MAG | Mago | 1 | 7 | 2 | Iluminación (Trance de Iluminación) |
| CL_INV | Invocador | 2 | 5 | 3 | Iluminación (Esencia de Iluminación) |

Todas usan MP como recurso primario.

La fila 45 añade tres neutrales a la lista: **efecto de pociones**, **% de caída** y **% de caída con suerte**.

Las filas 62–70 tienen otro borrador de reparto (STR → daño base y defensa física, AGI → crítico y evasión…): **descartado**; se usa el de las columnas W–Z.

**Origen de las neutrales (decidido):** vienen del **equipo secundario** (collar, aretes y demás joyería) y de **encantamientos** concretos. Se suman aparte, sin depender de STR, INT ni AGI.

**Velocidad de ataque por arma** (pestaña "Armas"): lanza 0,9 · espada 1,0 · espada corta 1,3 · daga 1,6 · ballesta 0,8 · arco 1,1 · bastón 0,6 · libro 0,9 · varita 1,2.

**Habilidades de ejemplo** con daño base, enfriamiento, tiempo de lanzamiento y alcance (Golpe al suelo, Golpe de mango, Inmolar…): se tratarán en el capítulo de personajes y habilidades, pero las fórmulas de este capítulo deben encajar con ellas.

### 1.3 Triángulo de ventajas (decidido)

Las estadísticas principales forman un sistema de **piedra, papel o tijera**: **STR > AGI > INT > STR**.

- Cada personaje tiene un tipo que le gana a otro y otro tipo que le gana a él. Nadie le gana a todos.
- Con condiciones parecidas, un personaje **no debe poder ganarle matemáticamente a su counter** y **debe ganarle con facilidad al tipo débil**.
- El tipo depende de la clase y de sus estadísticas base. En la Temporada 1: STR = Luchador y Combatiente; AGI = Asesino y Atacante a distancia; INT = Mago e Invocador.
- **Todas las clases y especializaciones** (hasta las ~19 finales) se encasillarán en el triángulo para saber contra quién son buenas y contra quién son malas.

### 1.4 Prioridad de balance en la Temporada 1 (decidido)

- **Del nivel 1 al 20 solo importa el PvE.** El PvP no se balancea hasta el nivel 20, cuando llega la primera especialización.
- **Paridad de caza**: las 6 clases base (mágicas, físicas cuerpo a cuerpo y físicas a distancia) deben tener un **ritmo de caza contra mobs casi igual**. Subir de nivel un mago o un atacante físico debe costar el mismo tiempo para conseguir los mismos derribos, y por tanto la misma experiencia y el mismo oro del 1 al 20.
- Se comprobará con una **simulación** que use las estadísticas base: 100, 200 o 500 mobs por clase, comparando el tiempo total. La diferencia entre clases debe ser muy pequeña.

### 1.5 Armas y prueba del muñeco (decidido)

- Cada **tipo de arma** tiene su **daño por golpe** y su **velocidad de ataque** propios. Una espada de dos manos no pega como una daga, un libro o una varita.
- Armas de la Temporada 1 según la hoja: Luchador y Combatiente → espada (1,0); Asesino → daga (1,6); Atacante a distancia → arco (1,1); Mago → bastón (0,6); Invocador → varita (1,2).
- **Prueba del muñeco**: un objetivo con vida prácticamente infinita (por ejemplo, 50 millones) al que cada clase golpea durante **20 minutos** a nivel 1. El daño total de todas las clases debe salir casi igual.
- Cuando haya roles, el objetivo será distinto por rol (valores de ejemplo, se fijarán más adelante): **daño puro** un 3–5 % por encima de la media; **tanque** alrededor de un 5 % por debajo; **curandero** alrededor de un 8 % por debajo, porque dedican la pelea a otras cosas. En la Temporada 1 las 6 clases base son de daño y deben quedar iguales.

## 2. Simulador

`herramientas/simulador/` (ver su README) ejecuta la prueba del muñeco con los datos en CSV.

**Propuesta usada en la primera versión** (todo ajustable en los CSV):
- **Daño de arma normalizado**: daño por golpe = 40 / velocidad, para que todas las armas tengan el mismo daño por segundo en ataque básico (espada 40, daga 25, bastón 66,7…). Las armas lentas pegan más fuerte por golpe.
- **Fórmula del golpe**: (daño del arma o de la habilidad + daño base de AGI) × (1 + % daño base de STR) × (1 + % daño de habilidad de INT, solo en habilidades) × crítico.
- **Por punto**: STR → +20 vida, +0,2 vida/s, +0,5 % defensa física y mágica, +1,5 % daño; INT → +15 maná, +0,2 maná/s, +2,5 % daño de habilidad; AGI → +2 daño plano por golpe, +0,5 % crítico, +1 % daño crítico. Crítico base: 5 % de probabilidad y ×1,5.
- Habilidades de la hoja: las de daño de cada clase (el Luchador tiene dos: Golpe al suelo y Golpe de mango) y Maestría (+10 a la estadística principal durante 600 s) para todas.

**Primer resultado** (20 minutos, nivel 1): diferencia del **28 %** entre la clase más fuerte (Luchador, +15 % sobre la media) y la más débil (Combatiente, −10 %). El simulador calcula cuánto habría que mover el daño de las habilidades de cada clase para igualarlas.

## 3. Estructura propuesta del capítulo

1. **Lista cerrada de estadísticas** y a qué categoría pertenece cada una (principal, derivada, neutral, PvP, utilidad).
2. **Crecimiento por nivel**: cuántos puntos de principales da cada nivel y si el reparto es fijo por clase o en parte libre.
3. **Conversión principales → derivadas**: cuánto da cada punto de STR/INT/AGI.
4. **Eficiencia por clase**: tabla que dice cuánto aprovecha cada clase cada estadística ("todo suma, pero no igual").
5. **Fórmulas de combate**: golpe/fallo (precisión vs. evasión), crítico, daño contra defensa, multiplicadores (monstruos, jefes, PvP), debilitación.
6. **Topes y rendimientos decrecientes** para las estadísticas porcentuales (crítico, CDR, evasión…).
7. **Tabla de valores por fuente**: qué estadísticas y cuánto da cada fuente (equipo por calidad, desarrollo, encantamiento, códice, cocina…).
8. **Puntuación de poder**.
9. **Implementación**: AttributeSets de GAS y DataTables.

## 4. Preguntas abiertas

Ver la conversación de la sesión; se trasladarán aquí las respuestas como decisiones.
