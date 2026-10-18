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

**Estadísticas base de las clases de la Temporada 1** — tabla corregida (filas 54–60 de la pestaña principal; la tabla de las filas 45–51 y la de "Habilidades 2.0" son versiones anteriores y **no se usan**). Es el **reparto base** que recibe el personaje por ser de esa clase (decidido); la clase se elige en el nivel 20 (ver 1.7). Cada clase suma 10 puntos:

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

### 1.6 Del nivel 1 al 19: solo arquetipo (decidido)

- Del 1 al 19 el personaje es solo **atacante físico** o **atacante mágico**: **sin clase ni especialización**.
- Al crear el personaje hay **tres opciones**, con el reparto base de una de las clases finales:

| Perfil de inicio | Reparto (STR/INT/AGI) | Tomado de | Armas |
|---|---|---|---|
| Físico cuerpo a cuerpo | 5 / 1 / 4 | Combatiente | Espada larga (lenta, fuerte) o espada corta (rápida, floja) |
| Físico a distancia | 2 / 2 / 6 | Atacante a distancia | Arco |
| Mágico | 1 / 7 / 2 | Mago | Bastón de dos manos (nunca pega con él) |

- Al elegir clase en el nivel 20 se pasa al reparto propio de la clase (tabla de 1.2).
- Es una etapa de **aprendizaje**: atacar, moverse, hacer misiones, leer el mapa, recolectar y entender las profesiones. Debería durar unas **3–4 semanas** de juego (orientativo).
- **Un solo tipo de arma** para todo el tramo, que solo mejora en daño (espada larga de bronce → de cobre → de plata…). Solo el físico cuerpo a cuerpo puede elegir entre dos (espada larga o corta), y **ambas deben rendir lo mismo** por segundo, tanto contra un jefe como cazando.
- La velocidad del arma se expresa en **segundos entre golpe y golpe**: espada larga 2,60 s, espada corta 1,40 s.
- Al subir de nivel crecen las estadísticas y el daño del arma, y los mobs también: matar un mob de tu nivel cuesta lo mismo en el nivel 1 que en el 10 o el 19.
- Formas de combatir en esta etapa:

| Arquetipo | Cómo hace daño |
|---|---|
| **Físico cuerpo a cuerpo** | 80–90 % del daño en **golpes blancos**; de vez en cuando un **golpe potenciado** que pega algo más de lo normal |
| **Físico a distancia** | Golpes blancos continuos y de vez en cuando una habilidad que **dispara tres flechas** a la vez |
| **Mágico** | **No hace daño con el arma**: todo sale de **dos hechizos básicos**. Uno débil que se puede lanzar siempre (1 s de enfriamiento, 2 s de lanzamiento) y otro fuerte con enfriamiento. Rotación: **fuerte, 3 débiles, fuerte, 3 débiles…** |

- Lo único que se calibra en esta etapa es la **paridad entre arquetipos** (1.4) con las estadísticas base, y las habilidades básicas son el punto de equilibrio.

### 1.7 Nivel 20: elección de clase (decidido)

- Al llegar al 20 se desbloquea una **misión del entrenador de clase**: "ya sabes pelear con armas, pero no te has especializado". Ofrece las clases del arquetipo. Por ejemplo, un físico cuerpo a cuerpo puede ser **Luchador** (espadas), **Asesino** (dagas) o **Combatiente** (espadas).
- Con la clase llegan:
  - las **armas propias de la clase**;
  - el **reparto base de la clase** (tabla de 1.2: 7/1/2, 5/1/4…);
  - **muchas más estadísticas visibles**;
  - **4–5 habilidades nuevas**, con activas y pasivas;
  - equipo especializado (raro) y el contenido de profesiones y desarrollo del personaje.
- **Cada clase cambia lo que da cada punto de estadística** (valores de ejemplo):
  - **Luchador**: cada punto de STR da más vida (120 en lugar de 100); INT solo da 20 de maná plano.
  - **Mago** (bastones): más regeneración de maná y más daño de hechizos.
  - **Invocador** (varitas): menos daño base, más regeneración de maná y más potencia de escudos y curaciones.
- Lo que la hoja muestra del 1 al 20 sobre clases y armas es informativo: **todo se desbloquea en el 20**.

## 2. Simulador

`herramientas/simulador/` (ver su README) ejecuta la prueba del muñeco con los datos en CSV.

**Orden de trabajo (decidido):** primero se calibran los tres perfiles de inicio (1.6) solo con golpes blancos para los físicos y con los dos hechizos para el mágico; las habilidades de los físicos (golpe potenciado, disparo triple) se añaden después.

**Pruebas:**
- **Jefe**: 20 minutos contra un objetivo de 50 millones de vida.
- **Caza**: 1.000 mobs de 1.000 de vida. El daño que sobra al rematar se pierde (penaliza los golpes grandes); cada golpe tira su crítico.

**Supuestos** (todo ajustable en los CSV):
- **Fórmula del golpe**: (daño del arma o del hechizo + daño base de AGI) × (1 + % daño base de STR) × (1 + % daño de habilidad de INT, solo en hechizos) × crítico.
- **Por punto** (propuesta inicial): STR → +20 vida, +0,2 vida/s, +0,5 % defensa física y mágica, +1,5 % daño; INT → +15 maná, +0,2 maná/s, +2,5 % daño de habilidad; AGI → +2 daño plano por golpe, +0,5 % crítico, +1 % daño crítico. Crítico base: 5 % y ×1,5.
- **Referencia**: espada larga con 52 de daño por golpe (equivale a 20 de daño por segundo antes de estadísticas). Arco a 2,0 s entre golpes (propuesta). Hechizo fuerte = 3 veces el débil, 8 s de enfriamiento para que entren tres débiles entre uno y otro.

**Resultado calibrado** (nivel 1):

| Perfil | Arma | s/golpe | Daño por golpe | DPS contra jefe | Caza (min) | Daño perdido al rematar |
|---|---|---|---|---|---|---|
| Cuerpo a cuerpo | Espada larga | 2,6 | 52 | 25,77 | 660,4 | 2,2 % |
| Cuerpo a cuerpo | Espada corta | 1,4 | 24,3 | 25,77 | 659,4 | 1,9 % |
| Distancia | Arco | 2,0 | 35,9 | 25,77 | 665,8 | 3,0 % |
| Mágico | — | — | Fuerte 75,8 · débil 25,3 | 25,78 | 662,6 | 2,5 % |

- Contra el jefe, los cuatro quedan **iguales** (diferencia del 0,1 %).
- Cazando, la diferencia máxima es del **1 %** (repetido con varias semillas: 0,9–1,0 %).
- La espada corta pega un 53 % menos por golpe que la larga (no un 40 %): las estadísticas planas de AGI se suman a cada golpe y favorecen a las armas rápidas, así que hay que bajarle más el daño.

**Prueba con mobs de 100 de vida** (mismos 1.000 mobs, mismas armas calibradas):

| Perfil | Golpe normal / crítico | Golpes por mob | Caza (min) | Frente a la media | Daño perdido |
|---|---|---|---|---|---|
| Espada larga | 64,5 / 99,3 | siempre 2 (el crítico se queda a 0,7 de matar de un golpe) | 86,7 | +2,2 % | 25,4 % |
| Espada corta | 34,7 / 53,5 | 3, a veces 2 | 69,8 | −17,6 % | 7,5 % |
| Arco | 49,3 / 77,0 | 3 (dos golpes normales suman 98,6), 2 si hay crítico | 94,8 | +11,9 % | 32,0 % |
| Mágico | fuerte 95,2 / 144,7 · débil 34,9 / 53,1 | depende de la rotación | 87,7 | +3,5 % | 26,6 % |

Diferencia máxima: **35,8 %**. Cuando un mob muere en 2–3 golpes, lo que manda es **cuántos golpes hacen falta para matarlo** (umbrales), no el daño por segundo. Un arma que se queda a 1 punto de un umbral (el arco con 98,6 contra 100 de vida) pierde un golpe entero por mob.

**Diferencia máxima según la vida del mob** (mismas armas):

| Vida del mob | 100 | 150 | 200 | 250 | 300 | 400 | 500 | 750 | 1.000 | 2.000 |
|---|---|---|---|---|---|---|---|---|---|---|
| Golpes de espada larga por mob (aprox.) | 2 | 2–3 | 3 | 4 | 5 | 6 | 8 | 11 | 15 | 30 |
| Diferencia entre perfiles | 35,8 % | 20,6 % | 22,9 % | 8,3 % | 5,3 % | 8,2 % | 3,9 % | 3,3 % | 1,0 % | 0,8 % |

**Conclusión:** la igualdad de daño por segundo solo se traslada a la caza si los mobs aguantan **bastantes golpes del arma más lenta**: con unos 8 golpes la diferencia baja a ~4 %, y con 15 o más, a ~1 %.

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
