# Capítulo de detalle — Estadísticas

Estado: **en curso**. Primer capítulo de detalle. Los niveles 1–19 están cerrados: ver la ficha en la sección 3 (quedan tres flecos en la sección 6). La próxima sesión empieza por el nivel 20 (sección 4). Este archivo recoge el punto de partida (lo ya decidido y lo que hay en la hoja de cálculo), la propuesta de estructura y las preguntas abiertas. Se irá completando en la sesión.

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
| Físico a distancia | 3 / 2 / 5 (antes 2 / 2 / 6, ver 2.16) | Atacante a distancia | Arco |
| Mágico | 2 / 6 / 2 (antes 1 / 7 / 2, ver 2.16) | Mago | Bastón de dos manos (nunca pega con él) |

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
- **Caza**: 1.000 mobs. El daño que sobra al rematar se pierde (penaliza los golpes grandes); cada golpe tira su crítico.

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

### 2.1 Vida del mob (decidido)

- Se prefiere **matar muchos mobs rápido** a pasar minutos con uno solo (la probabilidad de botín lo exige).
- Al empezar, un **guerrero con espada larga mata un mob normal en 6–7 golpes**. Con las armas calibradas, eso es **420 de vida** a nivel 1.

**1.000 mobs de 420 de vida** (nivel 1):

| Perfil | Golpes por mob | Segundos por mob | Tiempo total | Frente al más rápido | Daño perdido al rematar |
|---|---|---|---|---|---|
| Arco | 8,50 | 16,99 | 283,2 min | — | 4,3 % |
| Espada larga | 6,64 | 17,26 | 287,6 min | +1,6 % | 5,6 % |
| Espada corta | 12,36 | 17,30 | 288,4 min | +1,8 % | 5,9 % |
| Mágico | 8,79 | 17,59 | 293,2 min | +3,5 % | 7,5 % |

- Diferencia máxima: **3,5 %**. El mágico es el que más pierde porque su hechizo fuerte (95 de daño) suele caer cuando al mob le queda poca vida.
- Con 6–7 golpes los umbrales todavía pesan: según la vida exacta (380–480) la diferencia oscila entre 2,8 % y 8,6 %. Con **vida variable de ±10 %** (378–462) la diferencia se queda en 3,5 % y deja de depender del número exacto.
- **Ritmo**: unos 17 s por mob, unos **3,5 mobs por minuto** a nivel 1 en un contra uno. Para llegar a decenas de mobs por minuto harían falta golpes más rápidos o más fuertes, mobs con menos vida o ataques en área.

### 2.2 Habilidades de los físicos (decidido) y recalibración

Diseño pedido para los físicos (los valores marcados como propuesta son ajustables):

| Perfil | Habilidad | Qué hace | Daño | Enfriamiento | Duración |
|---|---|---|---|---|---|
| Cuerpo a cuerpo | **Golpe doble** | Un golpe blanco que se convierte en golpe potenciado con remate del mango | 150 % + 75 % del arma (225 %) | 20 s (propuesta) | Lo que dura un golpe blanco |
| Cuerpo a cuerpo | **Golpe al suelo** | Salta y golpea el suelo; animación completa y lenta | 300 % del arma (propuesta) | 40 s (propuesta) | 3 s |
| Distancia | **Disparo cargado** | Carga la flecha y la suelta; el daño se aplica al soltar | 200 % del arma (propuesta) | 12 s | 2 s de carga |
| Distancia | **Ráfaga triple** | Tres disparos seguidos; la habilidad de más daño | 3 × 120 % del arma (propuesta) | 40 s | 1,5 s (propuesta) |

- Los enfriamientos del cuerpo a cuerpo se eligieron para que pase **el 80 % del tiempo dando golpes blancos**. Con 8 s y 15 s solo lo hacía el 57 % del tiempo y su daño salía en un 36 % de golpes blancos. El arquero queda también en un 80 % del tiempo.
- Las habilidades escalan con el daño del arma, así que mejoran con ella.
- **No se gasta una habilidad en un mob que muere con un golpe blanco** (o con el hechizo débil, en el mágico). Reduce mucho el daño perdido al rematar: el mágico pasa de 13,1 % a 6,9 % y la espada larga, de 11,0 % a 8,0 %.
- Se calibra con la **prueba de caza**: la espada larga es la referencia; la espada corta y el arco ajustan su daño por golpe y el mágico ajusta sus dos hechizos.

**Resultado** (nivel 1, 1.000 mobs de 420 de vida ±10 %):

| Perfil | Daño del arma | Golpe blanco | Habilidades (daño final sin crítico) | Acciones por mob | Segundos por mob | Caza | Daño perdido | Daño por segundo contra jefe |
|---|---|---|---|---|---|---|---|---|
| Espada larga | 52 | 64,5 | Golpe doble 94,8 + 51,8 · Golpe al suelo 180,7 | 5,39 | 14,14 | 235,7 min | 8,0 % | 32,58 |
| Espada corta | 27,7 | 38,4 | Golpe doble 54,6 + 31,7 · Golpe al suelo 100,4 | 9,69 | 14,12 | 235,3 min | 4,7 % | 31,29 |
| Arco | 34,5 | 47,9 | Disparo cargado 87,6 · Ráfaga triple 3 × 57,8 | 7,16 | 14,15 | 235,9 min | 6,3 % | 31,87 |
| Mágico | — | — | Fuerte 120,2 (base 96,8) · débil 43,3 (base 32,3) | 7,06 | 14,13 | 235,5 min | 6,9 % | 32,24 |

- Cazando, la diferencia máxima es del **0,3 %**; contra el jefe, del **4,1 %** (allí no se pierde nada al rematar, así que gana quien más pierde cazando).
- Reparto del daño contra el jefe: espada larga 64 % golpes blancos, 23 % golpe doble, 14 % golpe al suelo; arco 63 % golpes blancos, 23 % disparo cargado, 14 % ráfaga triple; mágico 48 % hechizo fuerte, 52 % débil.
- Los hechizos del mágico subieron un **28 %** (fuerte 75,8 → 96,8; débil 25,3 → 32,3) para compensar las habilidades nuevas de los físicos.
- Con las habilidades, el guerrero mata un mob de 420 de vida en **5,4 acciones** (antes, 6,6 golpes blancos) y el ritmo pasa de 17 a **14 s por mob**.

### 2.3 Caza real: desplazamiento, golpes del mob, vida y maná

**Decidido:**
- El **cuerpo a cuerpo** camina de un mob a otro (al menos **1–1,5 s**; más según cómo se repartan los mobs en el mapa) y siempre pelea cara a cara, así que recibe golpes todo el tiempo.
- Los de **distancia** (arquero y mágico) pegan **gratis mientras el mob se acerca**; a veces lo matan antes de que llegue. Reciben menos daño, por eso tienen **menos vida y regeneran más despacio** (sacan poca STR).
- Para eso existe la separación de STR (vida, regeneración de vida, defensas) e INT (maná, regeneración de maná).
- La desventaja del desplazamiento se compensará más adelante, al diseñar las zonas de caza, **subiendo algo el daño del cuerpo a cuerpo** para que mate en menos golpes.

**Cómo lo simula** (`supervivencia_en_caza = 1`; valores de propuesta en `parametros.csv` y `habilidades.csv`):
- Cuerpo a cuerpo: 1,5 s caminando antes de cada mob. Distancia: el mob tarda 2,5 s en llegar.
- El mob pega 6 cada 2 s (menos la defensa física de STR).
- Vida = 100 + 20 por STR; regeneración = 0,5 + 0,2 por STR. Maná = 50 + 15 por INT; regeneración = 0,5 + 0,2 por INT.
- Coste de maná: golpe doble 8, golpe al suelo 12, disparo cargado 6, ráfaga triple 12, hechizo fuerte 12, hechizo débil 5. Sin maná suficiente, la habilidad no se usa (el mágico espera).
- Tras cada mob se descansa (regeneración ×2) hasta llenar vida y maná si no queda para aguantar otro mob como el último (con un 25 % de margen) o si se baja del 35 %.
- La calibración de daño sigue haciéndose en combate puro.

**Primer resultado** (1.000 mobs, nivel 1):

| Perfil | Vida | Regen. vida/s | Maná | Regen. maná/s | Caza | Frente al más rápido | Pegando | Caminando | Descansando | Daño recibido por mob |
|---|---|---|---|---|---|---|---|---|---|---|
| Espada larga | 200 | 1,5 | 65 | 0,7 | 365,3 min | — | 62 % | 7 % | 31 % | 42,8 |
| Espada corta | 200 | 1,5 | 65 | 0,7 | 374,6 min | +2,5 % | 62 % | 7 % | 31 % | 44,0 |
| Arco | 140 | 0,9 | 80 | 0,9 | 436,3 min | +19,4 % | 51 % | 0 % | 49 % | 34,6 |
| Mágico | 120 | 0,7 | 155 | 1,9 | 536,5 min | +46,9 % | 43 % | 0 % | 57 % | 35,0 |

- Los golpes gratis reducen el daño recibido un **19 %**, pero no compensan tener **30–40 % menos vida y la mitad o menos de regeneración**: el arco y el mágico pasan mucho más tiempo descansando.
- El arco descansa por **vida** (su maná alcanza). El mágico descansa por **vida y maná** a la vez: gasta unos 47 de maná por mob y regenera unos 27 mientras pelea.
- El cuerpo a cuerpo, pese a caminar, queda **el más rápido**.
- Todos estos números (daño del mob, vida y regeneración por punto, costes de maná) son de partida: el siguiente paso es calibrarlos.

### 2.4 Prueba: armas con +10 STR, +10 INT y +5 AGI, sin descansos

Todas las armas dan el mismo bono (columnas `bono_str`, `bono_int`, `bono_agi` de `armas.csv`) y en la caza real **nunca se para a descansar** (`descansar = 0`): si se muere, se pierden 30 s.

| Perfil | Reparto con el arma | Daño por segundo contra jefe (antes → ahora) | Caza puro | Caza real | Frente al más rápido (real) | Caminando | Sin maná | Muertes |
|---|---|---|---|---|---|---|---|---|
| Espada larga | 15 / 11 / 9 | 32,6 → 47,1 | 171,3 min | 190,9 min | +32,9 % | 13 % | 0 % | 0 |
| Espada corta | 15 / 11 / 9 | 31,3 → 48,1 | 158,5 min | 179,2 min | +24,8 % | 14 % | 0 % | 0 |
| Arco | 12 / 12 / 11 | 31,9 → 48,0 | 166,1 min | 166,1 min | +15,6 % | 0 % | 0 % | 0 |
| Mágico | 11 / 17 / 7 | 32,2 → 54,3 | 143,6 min | 143,6 min | — | 0 % | 0 % | 0 |

- **Nadie necesita descansar**: con la vida (320–400), la regeneración (2,7–3,5/s) y el maná que dan los bonos, todos aguantan la caza entera sin morir ni quedarse sin maná.
- **El daño sube un 45–70 %** y la caza es un 30–40 % más rápida.
- **Se rompe la igualdad de daño** (19 % de diferencia en combate puro):
  - el **mágico** gana más porque +10 INT (+25 % de daño de hechizos) se aplica a todo su daño, mientras que a los físicos solo les sube las habilidades (~36 % de su daño);
  - +5 AGI (+10 de daño plano por golpe) favorece a las armas rápidas: la espada corta adelanta a la larga.
- En la caza real, el **cuerpo a cuerpo** queda último por el tiempo caminando (13–14 %), ahora que nadie descansa.
- Conclusión: el bono del arma debería ser **propio de cada tipo de arma** (por ejemplo, más STR en espadas, más AGI en arcos, más INT en bastones) y recalibrarse con el simulador.

### 2.5 Prueba: bono propio de cada tipo de arma, sin descansos

Sin tocar mobs, vida ni daño o velocidad de las armas. Bonos (STR / INT / AGI): **espadas 10 / 3 / 5**, **arco 4 / 4 / 10**, **bastón 3 / 10 / 5**.

| Perfil | Reparto con el arma | Daño por segundo contra jefe (sin bono → con bono) | Caza puro | Caza real | Frente al más rápido (real) | Caminando | Muerto | Muertes |
|---|---|---|---|---|---|---|---|---|
| Espada larga | 15 / 4 / 9 | 32,6 → 44,5 (+37 %) | 177,3 min | 201,5 min | +16,8 % | 12 % | 0 % | 0 |
| Espada corta | 15 / 4 / 9 | 31,3 → 46,5 (+49 %) | 162,8 min | 185,9 min | +7,7 % | 13 % | 0 % | 0 |
| Arco | 6 / 6 / 16 | 31,9 → 50,0 (+57 %) | 158,4 min | 172,5 min | — | 0 % | 8 % | 27 |
| Mágico | 4 / 17 / 7 | 32,2 → 49,4 (+53 %) | 160,7 min | 195,4 min | +13,3 % | 0 % | 15 % | 58 |

- En combate puro la diferencia baja a **11,9 %** (con el bono igual para todos era 19,2 %), pero la **espada larga queda la última**: los +10 de daño plano por golpe de AGI favorecen a la espada corta, que pega casi el doble de veces.
- El **arco** es quien más gana: +10 AGI le da daño plano y crítico en cada golpe.
- **Sin descansos, los de distancia mueren**: el arco y el mágico, con 180–220 de vida y 1,3–1,7 de regeneración, pierden más vida por mob de la que recuperan (el arco 27 muertes, el mágico 58). El cuerpo a cuerpo, con 400 de vida y 3,5/s, aguanta sin morir.
- El cuerpo a cuerpo pierde un 12–13 % del tiempo caminando.

### 2.6 Pociones (decidido)

- Del 1 al 19, cazando de uno en uno, **nadie debería morir** mientras tenga pociones: las muertes de 2.5 solo indican que faltaban las pociones en la simulación.
- Simulación (valores de propuesta): poción de vida +100, poción de maná +100, **20 s de enfriamiento** por tipo, la de vida se bebe al bajar del 40 %, la de maná cuando falta maná para lanzar.

**Resultado** (mismos bonos de arma que 2.5, sin descansos, con pociones; 1.000 mobs):

| Perfil | Caza real | Frente al más rápido | Caminando | Muertes | Pociones de vida | Pociones de maná |
|---|---|---|---|---|---|---|
| Arco | 158,4 min | — | 0 % | 0 | 59 | 0 |
| Mágico | 160,7 min | +1,5 % | 0 % | 0 | 99 | 0 |
| Espada corta | 185,9 min | +17,3 % | 13 % | 0 | 0 | 0 |
| Espada larga | 201,5 min | +27,2 % | 12 % | 0 | 0 | 0 |

- Con pociones **nadie muere**. El arco gasta unas 6 pociones de vida cada 100 mobs y el mágico unas 10; ninguno necesita pociones de maná.
- El cuerpo a cuerpo no gasta ninguna (le sobra vida y regeneración), pero queda último: pierde un 12–13 % caminando y la espada larga ya era la más lenta en combate puro.

### 2.7 Daño extra del cuerpo a cuerpo por la caminata (decidido)

El daño de las espadas se sube directamente para que el cuerpo a cuerpo, caminando entre mobs, cace al mismo ritmo que el arco y el mágico (que no se tocan). Se calcula con `simular.py --calibrar-real`.

**Valores siempre enteros (decidido):** el daño, la vida, el maná y las estadísticas que se ven en el juego son números enteros. Los datos se redondean (arco 34,5 → 35; hechizos 96,8 → 97 y 32,3 → 32) y el simulador redondea el daño de cada golpe, la vida de cada mob y el daño que hace.

| Arma | Daño por golpe antes | Daño por golpe ahora | Subida |
|---|---|---|---|
| Espada larga | 52 | **75** | +44 % |
| Espada corta | 28 | **37** | +32 % |

**Resultado** (bonos de arma de 2.5, sin descansos, con pociones; 1.000 mobs):

| Perfil | Caza real | Frente al más rápido | Caminando | Pociones de vida | Combate puro | Daño por segundo contra jefe |
|---|---|---|---|---|---|---|
| Arco (35) | 157,3 min | — | 0 % | 56 | 157,3 min | 50 |
| Espada corta (37) | 159,9 min | +1,7 % | 16 % | 0 | 137,3 min | 56 |
| Espada larga (75) | 160,3 min | +1,9 % | 16 % | 0 | 138,2 min | 60 |
| Mágico (97 / 32) | 160,8 min | +2,2 % | 0 % | 94 | 160,8 min | 49 |

- En la caza real los cuatro quedan a un **2,2 %** como máximo.
- A cambio, **sin caminar** (contra un jefe, o con mobs muy juntos) el cuerpo a cuerpo hace un **12–22 % más de daño** que los de distancia. Habrá que tenerlo en cuenta en mazmorras y jefes.
- **Regeneración (decidido)**: se expresa **cada 5 segundos**, redondeada al entero más cercano (por ejemplo, 3,5 de vida por segundo → 18 cada 5 s; 1,3 → 7 cada 5 s).
- La regla de enteros se aplica al daño, la vida, el maná y las estadísticas; **los tiempos y los porcentajes pueden llevar decimales** (2,6 s, 1,4 s, 150 %, 75 %, 120 %).

### 2.8 Prueba: +5 STR, +5 INT y +5 AGI para todos (como subir al nivel 2)

Mismas armas, mismos mobs (420 de vida) y mismas pociones que 2.7; solo se suman 5 puntos a cada estadística principal de todos los perfiles.

| Perfil | STR / AGI / INT | Daño por segundo contra jefe | Acciones por mob | Caza real | Frente al más rápido | Pociones de vida | Vida | Maná |
|---|---|---|---|---|---|---|---|---|
| Mágico | 4/7/17 → 9/12/22 | 49 → 68 (**+38 %**) | 4,8 → 3,6 | 160,8 → 118,6 min (−26 %) | — | 94 → 0 | 180 → 280 | 305 → 380 |
| Arco | 6/16/6 → 11/21/11 | 50 → 65 (+29 %) | 4,8 → 3,8 | 157,3 → 126,3 min (−20 %) | +6,5 % | 56 → 0 | 220 → 320 | 140 → 215 |
| Espada corta | 15/9/4 → 20/14/9 | 56 → 73 (+30 %) | 5,7 → 4,5 | 159,9 → 131,4 min (−18 %) | +10,8 % | 0 → 0 | 400 → 500 | 110 → 185 |
| Espada larga | 15/9/4 → 20/14/9 | 60 → 74 (+24 %) | 3,2 → 2,7 | 160,3 → 138,5 min (−14 %) | +16,7 % | 0 → 0 | 400 → 500 | 110 → 185 |

(Reparto con el bono del arma, en orden STR / AGI / INT.)

- Los mismos +5 **no suben a todos por igual**: la diferencia en la caza real pasa de 2,2 % a **16,7 %**.
  - **Mágico, el que más gana**: +5 INT (+12,5 % de daño de hechizos) multiplica **todo** su daño; a los físicos solo les sube las habilidades.
  - **Espada larga, la que menos**: +5 AGI suma +10 de daño plano por golpe, que rinde más en armas rápidas (espada corta, arco) que en un arma lenta.
  - STR (+7,5 % de daño) sube a todos por igual.
- Con +5 de STR nadie necesita pociones (todos ganan 100 de vida).
- Conclusión: el crecimiento por nivel no puede ser igual para todos; debe seguir el reparto de cada perfil (o ajustarse por perfil) y comprobarse con el simulador nivel a nivel.

### 2.9 Crecimiento por nivel = bono del arma de nivel 1 (decidido)

- Cada nivel, el personaje gana **las mismas estadísticas que da su arma de nivel 1**: cuerpo a cuerpo **+10 STR, +5 AGI, +3 INT**; distancia **+4 STR, +10 AGI, +4 INT**; mágico **+3 STR, +5 AGI, +10 INT** (valores actuales de prueba).
- **Easter egg**: el arma de nivel 1 "anuncia" el crecimiento nivel a nivel; quien se fije en sus estadísticas sabrá cuánto subirá cada nivel.

**Prueba a nivel 2** (mismas armas, mobs de 420 sin escalar, con pociones):

| Perfil | STR / AGI / INT (con arma) | Daño por segundo contra jefe | Caza real | Frente al más rápido |
|---|---|---|---|---|
| Mágico | 4/7/17 → 7/12/27 | 49 → 71 (+45 %) | 160,8 → 114,2 min (−29 %) | — |
| Arco | 6/16/6 → 10/26/10 | 50 → 73 (+45 %) | 157,3 → 114,8 min (−27 %) | +0,5 % |
| Espada corta | 15/9/4 → 25/14/7 | 56 → 77 (+36 %) | 159,9 → 127,0 min (−21 %) | +11,2 % |
| Espada larga | 15/9/4 → 25/14/7 | 60 → 77 (+29 %) | 160,3 → 134,4 min (−16 %) | +17,7 % |

**Daño por segundo contra jefe nivel a nivel** (no depende de los mobs; % frente al más bajo):

| Nivel | Espada larga | Espada corta | Arco | Mágico |
|---|---|---|---|---|
| 1 | 60 (+21 %) | 56 (+14 %) | 50 (+2 %) | 49 |
| 2 | 77 (+7 %) | 77 (+7 %) | 73 (+2 %) | 71 |
| 5 | 147 | 163 (+11 %) | 178 (+21 %) | 176 (+19 %) |
| 10 | 356 | 425 (+19 %) | 570 (+60 %) | 539 (+51 %) |
| 19 | 1.254 | 1.556 (+24 %) | 2.812 (+124 %) | 2.397 (+91 %) |

- Con las conversiones actuales (lineales y sin topes), **el arco y el mágico se disparan** al subir de nivel:
  - **AGI** se acumula por tres vías a la vez: daño plano por golpe, probabilidad de crítico (a nivel 19 el arco pasa del 100 %) y daño crítico (×3,5).
  - **INT** multiplica todo el daño del mágico (+25 % por nivel).
  - **STR** sube el daño solo un 1,5 % por punto.
- Estos números usaban un crítico provisional sin topes: ver 2.10 para los valores con los topes decididos.

### 2.10 Topes de crítico del 1 al 19 (decidido)

- Del nivel 1 al 19 la **probabilidad de crítico no pasa del 5 %** y un crítico **no suma más de un +10 % de daño**. (El ×1,5 y el +0,5 % de crítico por AGI usados hasta ahora eran valores provisionales.)
- En el simulador: crítico base 5 % con tope 5 %; un crítico sin estadísticas no suma daño y el "crítico aumentado" de AGI suma hasta +10 % (`tope_critico_pct`, `tope_critico_aumentado_pct`).

**Nivel 1 con los topes** (caza real, 1.000 mobs; sin recalibrar nada): espada larga 165,1 min · espada corta 166,1 (+0,6 %) · mágico 169,1 (+2,4 %) · arco 169,2 (+2,5 %). La igualdad se mantiene sin tocar las armas.

**Daño por segundo contra jefe nivel a nivel** (crecimiento = bono del arma de nivel 1; % frente al más bajo):

| Nivel | Espada larga | Espada corta | Arco | Mágico |
|---|---|---|---|---|
| 1 | 57 (+22 %) | 54 (+15 %) | 47 | 47 (+1 %) |
| 2 | 72 (+11 %) | 72 (+11 %) | 64 | 67 (+4 %) |
| 5 | 128 | 142 (+11 %) | 133 (+3 %) | 155 (+20 %) |
| 10 | 269 | 321 (+19 %) | 301 (+12 %) | 412 (+53 %) |
| 19 | 696 | 863 (+24 %) | 817 (+17 %) | 1.349 (+94 %) |

(En el nivel 1 el cuerpo a cuerpo va por delante contra el jefe a propósito: compensa la caminata en la caza, ver 2.7.)

- Sin el crítico, el que se dispara es el **mágico**: +10 INT por nivel son +25 % de daño de hechizos por nivel y multiplican todo su daño.
- La **espada corta** se separa de la larga por el daño plano de AGI por golpe (+5 AGI por nivel = +10 de daño en cada golpe, y la corta golpea casi el doble).
- El **arco** también crece algo más que la espada larga (+10 AGI por nivel = +20 de daño plano por golpe).
- Siguiente paso: ajustar cuánto da cada punto (sobre todo INT y el daño plano de AGI) para que los cuatro crezcan al mismo ritmo.

### 2.11 Caza nivel a nivel con mobs que escalan

`simular.py --niveles`: caza real del nivel 1 al 19 (300 mobs por nivel y perfil). Cada nivel suma el bono del arma de nivel 1 (2.9); las armas no cambian de daño todavía. **Los mobs escalan**: su vida sube como el daño por segundo medio de los perfiles en ese nivel y su daño, como la vida media.

| Nivel | Vida mob | Daño mob | Espada larga (s/mob · perdido) | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|---|---|
| 1 | 420 | 6 | 9,9 · 13,8 % | 9,9 · 7,9 % | 10,1 · 11,1 % | 10,1 · 9,6 % | 2,8 % |
| 5 | 1.147 | 17 | 11,5 · 12,1 % | 10,2 · 9,0 % | 10,1 · 14,1 % | 8,2 · 9,6 % | 40,2 % |
| 10 | 2.680 | 30 | 12,9 · 13,7 % | 10,4 · 8,7 % | 10,3 · 13,6 % | 7,4 · 12,3 % | 73,6 % |
| 15 | 5.054 | 44 | 13,9 · 15,9 % | 10,4 · 6,7 % | 10,4 · 11,3 % | 6,8 · 12,4 % | 103,8 % |
| 19 | 7.664 | 55 | 15,1 · 19,5 % | 10,5 · 5,5 % | 10,4 · 8,8 % | 6,4 · 10,4 % | 137,4 % |

- Con mobs que escalan, el ritmo medio se mantiene en unos **10 s por mob** en todos los niveles.
- Pero el reparto entre perfiles se abre nivel a nivel: el **mágico** cada vez más rápido (6,4 s por mob en el 19) y la **espada larga** cada vez más lenta (15,1 s); espada corta y arco se mantienen en la media. Es el crecimiento desigual de 2.10 (INT multiplica todo el daño del mágico; el daño plano de AGI favorece a las armas rápidas).
- **Daño perdido al rematar**: entre 5 y 20 %; el más alto, la espada larga en los niveles altos (pocos golpes muy grandes por mob).
- Pociones: el arco deja de necesitarlas desde el nivel 13; el mágico sigue bebiendo (16–58 cada 300 mobs).

**Variante: vida del mob +10 % por nivel** (compuesto; daño del mob igual que antes; `crecimiento_vida_mob_pct = 10`):

| Nivel | Vida mob | Espada larga (s/mob · perdido) | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|---|
| 1 | 420 | 9,9 · 13,8 % | 9,9 · 7,9 % | 10,1 · 11,1 % | 10,1 · 9,6 % | 2,8 % |
| 5 | 615 | 7,2 · 20,5 % | 6,3 · 13,0 % | 5,9 · 20,6 % | 5,0 · 18,0 % | 44,0 % |
| 10 | 990 | 6,6 · 33,3 % | 5,1 · 20,5 % | 4,7 · 29,4 % | 3,4 · 27,0 % | 97,8 % |
| 15 | 1.595 | 6,5 · 38,5 % | 5,1 · 30,8 % | 4,3 · 31,0 % | 2,6 · 28,0 % | 146,6 % |
| 19 | 2.335 | 7,0 · 43,9 % | 5,1 · 32,3 % | 4,3 · 31,6 % | 2,1 · 13,7 % | 236,1 % |

- Un +10 % por nivel se queda muy corto: el daño de los jugadores crece mucho más rápido (el daño medio contra jefe se multiplica por ~18 del nivel 1 al 19, unos **+17 % por nivel**), mientras que la vida del mob solo se multiplica por 5,6.
- A partir del nivel 5–6 los mobs mueren en **1–3 golpes**, y vuelve el problema de los umbrales: el **daño perdido al rematar sube al 30–44 %** y manda la velocidad de cada acción (la espada larga no baja de ~6,5 s porque cada golpe dura 2,6 s; el mágico mata casi con un hechizo de 2 s).
- Pociones: nadie las necesita desde el nivel 7 (los mobs mueren antes de hacer daño).
- Para que los mobs puedan crecer un 10 % por nivel, el daño de los jugadores también debería crecer ~10 % por nivel: eso implica un crecimiento de estadísticas por nivel menor (o conversiones por punto menores) que el bono del arma de nivel 1.

### 2.12 Tipos de mob (decidido)

- Los mobs son siempre de **dos tipos: físicos o mágicos**.
- Todos siguen el mismo ciclo: **dos ataques básicos y un ataque potenciado**, y vuelven a empezar.
- Un mob a distancia empieza a pegar en cuanto empieza la pelea: sin golpes gratis para los de distancia y daño también mientras el cuerpo a cuerpo camina hacia él. El daño físico se reduce con la defensa física y el mágico con la mágica.
- Supuesto pendiente de confirmar: el potenciado hace **el doble** que un básico.
- La primera prueba (tabla siguiente) usó solo dos tipos (físico cuerpo a cuerpo y mágico a distancia, 50 % / 50 %); la rotación decidida está debajo.

**Nivel 1** (caza real, 1.000 mobs, con pociones, sin descansos):

| Perfil | Caza real | Frente al más rápido | Daño recibido por mob | Pociones de vida (antes → ahora) |
|---|---|---|---|---|
| Espada larga | 164,3 min | — | 36,4 | 0 → 7 |
| Espada corta | 165,4 min | +0,6 % | 36,5 | 0 → 6 |
| Arco | 168,1 min | +2,3 % | 38,2 | 56 → 200 |
| Mágico | 168,6 min | +2,6 % | 39,8 | 94 → 256 |

- El ritmo de caza sigue igualado (**2,6 %**), porque las pociones evitan que nadie muera ni pare.
- Con mobs mágicos a distancia, los de distancia **pierden la ventaja de los golpes gratis en la mitad de los mobs**: ahora reciben tanto daño como el cuerpo a cuerpo (36–40 por mob) con la mitad de vida, y beben **3–4 veces más pociones** (unas 20–26 cada 100 mobs).
- El cuerpo a cuerpo apenas necesita pociones.

**Rotación de mobs para las simulaciones (decidido):** los mobs salen siempre en este orden y se repite: **cuerpo a cuerpo físico → a distancia mágico → cuerpo a cuerpo mágico → a distancia físico** (`rotacion_mobs = 1`). Así cada perfil recibe daño intercalado entre cuerpo a cuerpo y distancia, y entre físico y mágico. Con eso quedan cuatro tipos (el tipo de daño y la distancia son independientes).

Nivel 1 con la rotación (caza real, 1.000 mobs): espada larga 165,1 min · espada corta 166,1 (+0,6 %) · mágico 169,1 (+2,4 %) · arco 169,2 (+2,5 %). Pociones de vida: 6 · 4 · 252 · 196. Daño recibido por mob: 36–39 para todos. Prácticamente igual que con 50 % / 50 % al azar, porque la mitad de los mobs siguen pegando a distancia.

### 2.13 Del 1 al 19: vida del mob +30 % por nivel y crítico por nivel

- El potenciado del mob hace **el doble** que un básico (decidido).
- **Crítico por nivel** (prueba): probabilidad **1 %** a nivel 1, **+0,2 % por nivel**, tope 5 %; daño extra del crítico **+2 %** a nivel 1, **+0,4 % por nivel**, tope +10 %. De momento la AGI no da crítico (por un error, las simulaciones 2.13–2.20 aún sumaban el crítico de AGI; corregido en la ficha de la sección 3, con resultados prácticamente iguales).
- Vida del mob **+30 % por nivel** (compuesto); su daño sigue subiendo como la vida media de los jugadores. Rotación de los cuatro tipos de mob, 1.000 mobs por nivel, con pociones y sin descansos.

| Nivel | Vida mob | Espada larga (min · pociones) | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|---|
| 1 | 420 | 165 · 6 | 166 · 4 | 169 · 196 | 169 · 251 | 2,5 % |
| 2 | 546 | 168 · 0 | 162 · 0 | 160 · 282 | 153 · 332 | 10,0 % |
| 3 | 710 | 177 · 0 | 163 · 0 | 160 · 278 | 146 · 338 | 21,3 % |
| 4 | 923 | 180 · 0 | 168 · 0 | 165 · 377 | 148 · 404 | 21,9 % |
| 5 | 1.200 | 200 · 0 | 175 · 0 | 171 · 449 | 175 · 342 | 16,8 % |
| 6 | 1.559 | 219 · 0 | 186 · 0 | 182 · 486 | 193 · 335 | 20,1 % |
| 7 | 2.027 | 236 · 0 | 201 · 0 | 207 · 505 | 207 · 338 | 17,3 % |
| 8 | 2.635 | 259 · 0 | 220 · 0 | 244 · 509 | 222 · 370 | 17,6 % |
| 9 | 3.426 | 288 · 0 | 239 · 0 | 261 · 511 | 240 · 373 | 20,5 % |
| 10 | 4.454 | 327 · 0 | 268 · 0 | 296 · 592 | 257 · 394 | 27,1 % |
| 11 | 5.790 | 354 · 0 | 301 · 0 | 344 · 650 | 288 · 409 | 22,9 % |
| 12 | 7.527 | 410 · 0 | 342 · 0 | 374 · 729 | 333 · 452 | 23,2 % |
| 13 | 9.785 | 469 · 0 | 385 · 0 | 436 · 866 | 377 · 504 | 24,6 % |
| 14 | 12.721 | 542 · 0 | 442 · 0 | 499 · 990 | 416 · 540 | 30,2 % |
| 15 | 16.537 | 634 · 0 | 509 · 0 | 581 · 1.174 | 482 · 639 | 31,6 % |
| 16 | 21.498 | 730 · 0 | 591 · 0 | 685 · 1.442 | 583 · 747 | 25,2 % |
| 17 | 27.947 | 861 · 0 | 688 · 0 | 777 · 1.662 | 616 · 784 | 39,7 % |
| 18 | 36.332 | 1.010 · 0 | 809 · 0 | 918 · 1.992 | 793 · 999 | 27,4 % |
| 19 | 47.231 | 1.188 · 0 | 954 · 0 | 1.072 · 2.425 | 824 · 1.027 | 44,1 % |

- Con +30 % por nivel los mobs **crecen más que los jugadores** (cuyo daño sube ~17 % por nivel): matar 1.000 mobs pasa de ~165 min en el nivel 1 a **820–1.190 min** en el 19. Con +10 % (2.11) pasaba lo contrario. El punto de equilibrio está en torno a **+17 % por nivel** con el crecimiento de estadísticas actual.
- **Pociones**: el cuerpo a cuerpo no necesita ninguna desde el nivel 2; el **arco llega a 2,4 pociones por mob** y el mágico a 1 en el nivel 19. La poción cura siempre 100 mientras la vida de los jugadores sube (el arco tiene 1.660 de vida en el 19): las pociones también tendrán que escalar por nivel.
- La diferencia entre perfiles va del 2,5 % al **44 %**: la espada larga cada vez más lenta y el mágico el más rápido (el crecimiento desigual de 2.10).
- **Corrección**: esta tabla no mostraba las muertes. El arco y el mágico sí morían en niveles altos aun bebiendo pociones: en el nivel 10, 45 y 102 muertes; en el 19, **80 y 341** (cada una cuesta 30 s).

### 2.14 Primeras habilidades de supervivencia (una por perfil)

Valores de partida (ajustables en `habilidades.csv`):

| Perfil | Habilidad | Tipo | Qué hace |
|---|---|---|---|
| Arco | **Robo de vida** | Pasiva | Se cura el **10 %** del daño de cada golpe (para depender menos de las pociones) |
| Cuerpo a cuerpo | **Furia sangrienta** | Activa | Durante 12 s sus habilidades hacen **+40 %** de daño, pero cada una cuesta además un **5 % de su vida máxima**; enfriamiento 30 s; solo se activa con más de la mitad de la vida |
| Mágico | **Escudo de maná** | Activa | Absorbe daño hasta un **30 % de su vida máxima** durante 8 s; 15 de maná, 1 s de lanzamiento, enfriamiento 20 s; se lo pone cuando el mob ya le está pegando |

**Del 1 al 19** (vida del mob +30 % por nivel, rotación de mobs, 1.000 mobs por nivel; min · pociones · muertes):

| Nivel | Vida mob | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|---|
| 1 | 420 | 160 · 43 · 0 | 164 · 27 · 0 | 169 · 0 · 0 | 177 · 114 · 0 | 10,9 % |
| 2 | 546 | 163 · 12 · 0 | 159 · 17 · 0 | 160 · 0 · 0 | 161 · 149 · 0 | 2,8 % |
| 3 | 710 | 168 · 0 · 0 | 159 · 0 · 0 | 160 · 0 · 0 | 153 · 134 · 0 | 10,2 % |
| 4 | 923 | 174 · 0 · 0 | 164 · 0 · 0 | 165 · 0 · 0 | 150 · 179 · 0 | 16,1 % |
| 5 | 1.200 | 185 · 0 · 0 | 172 · 0 · 0 | 171 · 0 · 0 | 153 · 231 · 0 | 21,4 % |
| 6 | 1.559 | 205 · 0 · 0 | 178 · 0 · 0 | 179 · 0 · 0 | 159 · 273 · 0 | 29,0 % |
| 7 | 2.027 | 227 · 0 · 0 | 194 · 0 · 0 | 198 · 0 · 0 | 168 · 312 · 0 | 35,3 % |
| 8 | 2.635 | 250 · 0 · 0 | 212 · 0 · 0 | 226 · 0 · 0 | 177 · 387 · 0 | 41,6 % |
| 9 | 3.426 | 274 · 0 · 0 | 231 · 0 · 0 | 234 · 0 · 0 | 187 · 416 · 0 | 46,6 % |
| 10 | 4.454 | 305 · 0 · 0 | 259 · 0 · 0 | 271 · 0 · 0 | 206 · 444 · 0 | 47,9 % |
| 11 | 5.790 | 344 · 0 · 0 | 290 · 0 · 0 | 310 · 0 · 0 | 227 · 509 · 0 | 51,4 % |
| 12 | 7.527 | 382 · 0 · 0 | 331 · 0 · 0 | 346 · 0 · 0 | 252 · 619 · 0 | 51,6 % |
| 13 | 9.785 | 439 · 0 · 0 | 366 · 0 · 0 | 398 · 0 · 0 | 281 · 704 · 0 | 56,1 % |
| 14 | 12.721 | 505 · 0 · 0 | 423 · 0 · 0 | 458 · 0 · 0 | 316 · 831 · 0 | 59,9 % |
| 15 | 16.537 | 589 · 0 · 0 | 488 · 0 · 0 | 528 · 0 · 0 | 359 · 987 · 0 | 64,1 % |
| 16 | 21.498 | 678 · 0 · 0 | 563 · 0 · 0 | 638 · 0 · 0 | 411 · 1.103 · 0 | 65,0 % |
| 17 | 27.947 | 796 · 0 · 0 | 659 · 0 · 0 | 710 · 0 · 0 | 471 · 1.255 · 0 | 69,1 % |
| 18 | 36.332 | 937 · 0 · 0 | 769 · 0 · 0 | 847 · 0 · 0 | 544 · 1.456 · 0 | 72,1 % |
| 19 | 47.231 | 1.093 · 0 · 0 | 907 · 0 · 0 | 998 · 0 · 0 | 630 · 1.644 · 0 | 73,5 % |

- **Nadie muere** en ningún nivel (antes, el arco y el mágico morían a partir de nivel 5–10).
- **Arco**: con el robo de vida del 10 % **no necesita ninguna poción** (antes 196 en el nivel 1 y 2.425 en el 19). Probablemente es demasiado: se puede bajar el %.
- **Mágico**: el escudo baja las pociones a menos de la mitad en el nivel 1 (251 → 114), pero en niveles altos sigue bebiendo mucho (1.644 en el 19; la poción cura 100 fijo). Como ya no muere, es **el más rápido** desde el nivel 3, y la diferencia sube al 73,5 %. En el nivel 1 el escudo le cuesta tiempo (1 s de lanzamiento cada vez): queda un 10,9 % más lento.
- **Cuerpo a cuerpo**: la furia le da algo más de daño (espada larga 165 → 160 min en el nivel 1) a cambio de beber algunas pociones en los niveles 1–2 (43 y 27); desde el nivel 3 no necesita ninguna.

### 2.15 Habilidades 3 y 4 desde el nivel 10 (decidido) y ajustes

- Las habilidades de supervivencia **se desbloquean en el nivel 10** (columna `nivel_minimo` de `habilidades.csv`).
- **Arco**: robo de vida al **4 %**.
- **Cuerpo a cuerpo**: se descarta la furia. Su habilidad es **Golpe sangriento**: **300 % del arma** a cambio de **un sexto de su vida máxima** en cada uso, para que de verdad le haga daño y tenga que beber pociones. Enfriamiento de 10 s (propuesta); ocupa el hueco de un golpe blanco; solo se usa si después le queda más de un 25 % de vida.
- **Mágico**: escudo de maná sin cambios (desde el nivel 10).

**Del 1 al 19** (vida del mob +30 % por nivel, rotación de mobs, 1.000 mobs por nivel; min · pociones · muertes):

| Nivel | Vida mob | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|---|
| 1 | 420 | 165 · 6 · 0 | 166 · 4 · 0 | 169 · 196 · 0 | 169 · 251 · 0 | 2,5 % |
| 2 | 546 | 168 · 0 · 0 | 162 · 0 · 0 | 160 · 282 · 0 | 153 · 332 · 0 | 10,0 % |
| 3 | 710 | 177 · 0 · 0 | 163 · 0 · 0 | 160 · 278 · 0 | 146 · 338 · 0 | 21,3 % |
| 4 | 923 | 180 · 0 · 0 | 168 · 0 · 0 | 165 · 377 · 0 | 148 · 404 · 8 | 21,9 % |
| 5 | 1.200 | 200 · 0 · 0 | 175 · 0 · 0 | 171 · 449 · 0 | 175 · 342 · 51 | 16,8 % |
| 6 | 1.559 | 219 · 0 · 0 | 186 · 0 · 0 | 182 · 486 · 6 | 193 · 335 · 71 | 20,1 % |
| 7 | 2.027 | 236 · 0 · 0 | 201 · 0 · 0 | 207 · 505 · 16 | 207 · 338 · 82 | 17,3 % |
| 8 | 2.635 | 259 · 0 · 0 | 220 · 0 · 0 | 244 · 509 · 38 | 222 · 370 · 92 | 17,6 % |
| 9 | 3.426 | 288 · 0 · 0 | 239 · 0 · 0 | 261 · 511 · 45 | 240 · 373 · 102 | 20,5 % |
| 10 | 4.454 | 274 · 761 · 0 | 244 · 681 · 0 | 271 · 0 · 0 | 206 · 444 · 0 | 32,9 % |
| 11 | 5.790 | 308 · 871 · 0 | 273 · 771 · 0 | 310 · 0 · 0 | 227 · 509 · 0 | 36,6 % |
| 12 | 7.527 | 347 · 981 · 0 | 309 · 872 · 0 | 346 · 0 · 0 | 252 · 619 · 0 | 37,9 % |
| 13 | 9.785 | 390 · 1.095 · 0 | 348 · 973 · 0 | 398 · 0 · 0 | 281 · 704 · 0 | 41,3 % |
| 14 | 12.721 | 446 · 1.248 · 0 | 396 · 1.114 · 0 | 458 · 0 · 0 | 316 · 831 · 0 | 45,0 % |
| 15 | 16.537 | 511 · 1.437 · 0 | 454 · 1.286 · 0 | 528 · 0 · 0 | 359 · 987 · 0 | 47,3 % |
| 16 | 21.498 | 589 · 1.661 · 0 | 522 · 1.481 · 0 | 638 · 0 · 0 | 411 · 1.103 · 0 | 55,2 % |
| 17 | 27.947 | 680 · 1.922 · 0 | 606 · 1.731 · 0 | 710 · 0 · 0 | 471 · 1.255 · 0 | 50,9 % |
| 18 | 36.332 | 796 · 2.234 · 0 | 704 · 1.999 · 0 | 847 · 0 · 0 | 544 · 1.456 · 0 | 55,5 % |
| 19 | 47.231 | 926 · 2.631 · 0 | 825 · 2.377 · 0 | 998 · 0 · 0 | 630 · 1.644 · 0 | 58,5 % |

- **Niveles 4–9 (antes de las habilidades)**: el arco y el mágico **mueren** (el mágico desde el nivel 4, hasta 102 veces; el arco desde el 6, hasta 45) aun bebiendo 300–500 pociones: la poción de +100 se queda pequeña frente a mobs que pegan cada vez más.
- **Golpe sangriento**: el cuerpo a cuerpo pasa a beber **0,7–2,6 pociones por mob** (antes ninguna) y caza algo más rápido (espada larga 305 → 274 min en el nivel 10).
- **Arco con 4 %**: sigue sin necesitar ninguna poción desde el nivel 10. El robo de vida aún cubre todo el daño recibido.
- **Mágico**: sin cambios respecto a 2.14; es el más rápido desde el nivel 10 y la diferencia llega al 58,5 % en el 19.

### 2.16 Prueba: nuevo reparto base de mágico y arquero

Reparto base (STR / INT / AGI): **mágico 2 / 6 / 2** (antes 1 / 7 / 2) y **físico a distancia 3 / 2 / 5** (antes 2 / 2 / 6). El crecimiento por nivel sigue siendo el bono del arma de nivel 1, así que el cambio solo mueve un punto de cada estadística.

**Nivel 1** (caza real): espada larga 165,1 min · espada corta 166,1 (+0,6 %) · mágico 169,3 (+2,6 %) · arco 169,9 (+2,9 %). Vida: arco 220 → 240, mágico 180 → 200. Pociones: arco 196 → 177, mágico 251 → 231.

**Del 1 al 19** (mismas condiciones que 2.15; min · pociones · muertes de arco y mágico, que son los que cambian):

| Nivel | Arco (antes → ahora) | Mágico (antes → ahora) | Diferencia (antes → ahora) |
|---|---|---|---|
| 1 | 169 · 196 · 0 → 170 · 177 · 0 | 169 · 251 · 0 → 169 · 231 · 0 | 2,5 → 2,9 % |
| 4 | 165 · 377 · 0 → 165 · 355 · 0 | 148 · 404 · 8 → 143 · 412 · 0 | 21,9 → 26,0 % |
| 5 | 171 · 449 · 0 → 172 · 361 · 0 | 175 · 342 · 51 → 157 · 384 · 20 | 16,8 → 27,5 % |
| 7 | 207 · 505 · 16 → 203 · 526 · 9 | 207 · 338 · 82 → 198 · 356 · 65 | 17,3 → 19,0 % |
| 9 | 261 · 511 · 45 → 247 · 561 · 23 | 240 · 373 · 102 → 227 · 371 · 83 | 20,5 → 26,8 % |
| 10 | 271 · 0 · 0 → 271 · 0 · 0 | 206 · 444 · 0 → 205 · 408 · 0 | 32,9 → 33,6 % |
| 15 | 528 · 0 · 0 → 527 · 0 · 0 | 359 · 987 · 0 → 358 · 855 · 0 | 47,3 → 47,4 % |
| 19 | 998 · 0 · 0 → 998 · 0 · 0 | 630 · 1.644 · 0 → 628 · 1.271 · 0 | 58,5 → 59,0 % |

- El punto extra de STR da más vida: **menos muertes** del 4 al 9 (el mágico pasa de 102 a 83 en el nivel 9; el arco, de 45 a 23) y algo menos de pociones.
- El ritmo de caza apenas cambia; el desequilibrio entre perfiles sigue viniendo del crecimiento por nivel (el mágico sigue siendo el más rápido desde el nivel 2).

### 2.17 Niveles 5–9, descansos del mágico y pociones de misión (decidido)

- **Del nivel 5 al 9 no preocupa** que los de distancia aguanten pocos mobs seguidos: a esos niveles las misiones piden matar **20–50 mobs**, no 100 o 200.
- **Que el mágico descanse es sano**: mata más rápido, pero tiene que pararse unos segundos a recuperar vida antes de seguir; el guerrero, en cambio, caza sin parar. Esa pausa compensa parte de su ventaja de daño.
- **Coste en cobre**: los mágicos gastarán mucho más cobre en pociones que los guerreros. Se compensa **dándoles pociones en las misiones**: en el tutorial se les explica que son personajes a distancia pero muy frágiles, que deben cuidar su vida, y reciben **pociones extra**.
- El simulador pasa a usar **descansos** (`descansar = 1`): tras un mob, se para a recuperarse si no le queda vida para aguantar otro como el último.

**Del 1 al 19 con descansos** (mismas condiciones que 2.16; min · pociones · muertes):

| Nivel | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|
| 1 | 165 · 6 · 0 | 166 · 4 · 0 | 170 · 177 · 0 | 169 · 231 · 0 | 2,9 % |
| 3 | 177 · 0 · 0 | 163 · 0 · 0 | 160 · 261 · 0 | 146 · 321 · 0 | 21,3 % |
| 5 | 200 · 0 · 0 | 175 · 0 · 0 | 172 · 361 · 0 | 181 · 299 · 0 | 16,3 % |
| 7 | 236 · 0 · 0 | 201 · 0 · 0 | 220 · 396 · 0 | 229 · 259 · 0 | 17,3 % |
| 9 | 288 · 0 · 0 | 239 · 0 · 0 | 265 · 379 · 0 | 267 · 211 · 0 | 20,5 % |
| 10 | 336 · 182 · 0 | 322 · 206 · 0 | 271 · 0 · 0 | 205 · 408 · 0 | 63,7 % |
| 13 | 453 · 455 · 0 | 412 · 453 · 0 | 396 · 0 · 0 | 280 · 593 · 0 | 61,6 % |
| 16 | 649 · 1.000 · 0 | 615 · 676 · 0 | 634 · 0 · 0 | 409 · 965 · 0 | 58,5 % |
| 19 | 1.011 · 1.465 · 0 | 927 · 1.311 · 0 | 998 · 0 · 0 | 628 · 1.271 · 0 | 61,1 % |

- Con descansos **nadie muere** en ningún nivel: del 5 al 9 el arco y el mágico se paran a recuperarse en lugar de morir (el mágico pasa, por ejemplo, de 157 a 181 min en el nivel 5).
- Desde el nivel 10 el **cuerpo a cuerpo también descansa**: el golpe sangriento le quita tanta vida que, además de beber, tiene que pararse (espada larga 274 → 336 min en el nivel 10).
- El **mágico** casi no descansa desde el nivel 10 (el escudo lo protege) y sigue siendo el más rápido: la diferencia vuelve a estar en torno al 60 %.

### 2.18 Cuarta habilidad de cada perfil (desde el nivel 10)

| Perfil | Habilidad 3 | Habilidad 4 (nueva) |
|---|---|---|
| Cuerpo a cuerpo | Golpe sangriento (activa) | **Robo de vida** (pasiva): se cura el **4 %** del daño de cada golpe, para recuperar parte de la vida que gasta |
| Arco | Robo de vida 4 % (pasiva; luego 0,3 % + 3 % de crítico, ver 2.19) | **Disparo potente** (activa): **350 % del arma con 3 s de lanzamiento** (el daño de 3,5 golpes en el tiempo de 1,5); enfriamiento 15 s y 10 de maná (propuesta) |
| Mágico | Escudo de maná (activa), ahora absorbe el **20 %** de la vida máxima (antes 30 %) | **Celeridad** (pasiva): lanza los hechizos un **2 %** más rápido |

**Del 1 al 19** (con descansos y pociones; los niveles 1–9 no cambian respecto a 2.17; min · pociones · muertes):

| Nivel | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|
| 9 | 288 · 0 · 0 | 239 · 0 · 0 | 265 · 379 · 0 | 267 · 211 · 0 | 20,5 % |
| 10 | 256 · 305 · 0 | 249 · 299 · 0 | 248 · 0 · 0 | 205 · 314 · 0 | 24,8 % |
| 11 | 281 · 463 · 0 | 266 · 412 · 0 | 277 · 0 · 0 | 224 · 329 · 0 | 25,3 % |
| 12 | 316 · 321 · 0 | 289 · 357 · 0 | 328 · 0 · 0 | 250 · 404 · 0 | 31,1 % |
| 13 | 353 · 5 · 0 | 328 · 4 · 0 | 358 · 0 · 0 | 280 · 455 · 0 | 27,8 % |
| 14 | 404 · 0 · 0 | 371 · 0 · 0 | 417 · 0 · 0 | 315 · 584 · 0 | 32,4 % |
| 15 | 467 · 0 · 0 | 430 · 0 · 0 | 478 · 0 · 0 | 355 · 719 · 0 | 34,6 % |
| 16 | 539 · 0 · 0 | 496 · 0 · 0 | 560 · 0 · 0 | 407 · 814 · 0 | 37,5 % |
| 17 | 627 · 0 · 0 | 576 · 0 · 0 | 672 · 0 · 0 | 467 · 805 · 0 | 43,8 % |
| 18 | 732 · 0 · 0 | 673 · 0 · 0 | 759 · 0 · 0 | 538 · 788 · 0 | 41,0 % |
| 19 | 859 · 0 · 0 | 788 · 0 · 0 | 897 · 0 · 0 | 625 · 916 · 0 | 43,6 % |

- La diferencia desde el nivel 10 baja de ~60 % (2.17) a **25–44 %**.
- **Cuerpo a cuerpo**: con el robo de vida ya no necesita descansar y caza más rápido (espada larga 336 → 256 min en el nivel 10); bebe 300–460 pociones en los niveles 10–12 y **ninguna desde el 13**, cuando el robo de vida cubre lo que cuesta el golpe sangriento.
- **Arco**: el disparo potente le da algo más de ritmo (271 → 248 min en el nivel 10); sigue sin necesitar pociones.
- **Mágico**: con el escudo al 20 % bebe algo menos que antes en niveles altos (1.271 → 916 en el nivel 19), pero sigue siendo **el más rápido** desde el nivel 10.

### 2.19 Base de los niveles 1–19 cerrada (decidido)

- **Los perfiles quedan así** (reparto base, armas, crecimiento por nivel y las cuatro habilidades de 2.18): son las estadísticas básicas de los personajes.
- Único ajuste: el **robo de vida del arco baja del 4 % al 2 %**. Un personaje a distancia no debe curarse tanto; debe recibir daño y usar pociones.
- **El consumo de pociones no preocupa por ahora**: el equipo traerá **armadura**, una mitigación de daño no muy alta que lo reducirá.
- **No se busca que el juego esté perfectamente equilibrado de principio a fin**: tiene que empezar a verse la diferencia entre perfiles. Que el mágico y el arco hagan más daño está bien:
  - con las especializaciones, la mitad de los mágicos hará mucho daño y la otra mitad se encargará de curar, y necesitarán ese daño alto;
  - las clases de daño puro tendrán su propio daño; los tanques serán todavía más resistentes y harán mucho daño, pero en área.
- En grupo se notará más: guerreros que aguantan y mágicos que hacen mucho daño favorecen el trabajo en equipo.

**Efecto del 2 % en el arco**: solo necesita pociones en el nivel 10 (18 de cada 1.000 mobs); desde el 11 el robo de vida sigue cubriendo todo el daño que recibe. Para obligarle de verdad a beber haría falta bajarlo más (≈0,5–1 %) o esperar a que los mobs y las pociones se ajusten. El resto de la tabla queda igual que en 2.18.

**Corrección definitiva del arco (decidido):** su pasiva da dos cosas: **robo de vida del 0,3 %** y **+3 % de probabilidad de crítico** (sin pasar el tope del 5 %).

| Nivel | Arco antes (2 %) | Arco ahora (0,3 % + 3 % crítico) |
|---|---|---|
| 10 | 248 min · 18 pociones | 273 min · 447 pociones |
| 11 | 277 · 0 | 281 · 724 |
| 12 | 328 · 0 | 348 · 640 |
| 13 | 358 · 0 | 367 · 894 |
| 14–19 | 417–897 · 0 | igual tiempo · 1.099–1.438 pociones |

- Ahora **sí bebe pociones** de forma constante (unas 0,4–1,4 por mob), y en los niveles 10–13 además tiene que parar a descansar algo.
- El **crítico extra apenas suma daño**: con las reglas del 1 al 19 un crítico añade como mucho un +10 % (entre +5,6 y +9,2 % en los niveles 10–19) y la probabilidad ya roza el tope (2,8 % en el nivel 10 → 5 % con la pasiva; 4,6 % en el 19 → 5 %). En total, alrededor de un **+0,1 % de daño**. Si se quiere que el crítico se note, habrá que subir el daño extra del crítico o el tope.

### 2.20 Armadura (decidido)

- **Cada 100 puntos de armadura restan 1 punto de daño plano a cada golpe recibido**, venga de donde venga (mobs, JcJ o cualquier otra fuente). Ejemplo: con 500 de armadura, un golpe de 10 hace 5.
- Prueba: **50 de armadura en el nivel 1, 500 en el 10 y 1.000 en el 20** (50 por nivel), igual para todos los perfiles. En el simulador, cada golpe recibido hace como mínimo 1 (`armadura_por_nivel`, `armadura_por_punto_de_dano`).

**Pociones bebidas cada 1.000 mobs, sin armadura → con armadura** (los tiempos de caza apenas cambian):

| Nivel | Espada larga | Espada corta | Arco | Mágico |
|---|---|---|---|---|
| 1 | 6 → 0 | 4 → 0 | 177 → 126 | 231 → 180 |
| 3 | 0 → 0 | 0 → 0 | 261 → 213 | 321 → 265 |
| 5 | 0 → 0 | 0 → 0 | 361 → 259 | 299 → 348 |
| 7 | 0 → 0 | 0 → 0 | 396 → 372 | 259 → 307 |
| 9 | 0 → 0 | 0 → 0 | 379 → 433 | 211 → 287 |
| 10 | 332 → 149 | 300 → 316 | 447 → 402 | 314 → 110 |
| 11 | 463 → 63 | 412 → 165 | 724 → 331 | 329 → 102 |
| 12 | 321 → 0 | 357 → 0 | 640 → 405 | 404 → 125 |
| 13 | 5 → 0 | 4 → 0 | 894 → 271 | 455 → 128 |
| 15 | 0 → 0 | 0 → 0 | 1.186 → 141 | 719 → 175 |
| 17 | 0 → 0 | 0 → 0 | 1.438 → 0 | 805 → 95 |
| 19 | 0 → 0 | 0 → 0 | 1.101 → 0 | 916 → 0 |
| **Total 1–19** | **1.127 → 212 (−81 %)** | **1.077 → 481 (−55 %)** | **13.011 → 4.343 (−67 %)** | **8.673 → 3.765 (−57 %)** |

- La armadura resta un **~15–17 % del daño de cada golpe** del mob (por ejemplo, 0,5 de 6 en el nivel 1; 5 de 30 en el 10), y eso basta para que la regeneración y el robo de vida cubran mucho más: el consumo de pociones **baja a menos de la mitad** en todos los perfiles.
- En los niveles 5–9 el mágico bebe algo más que sin armadura porque descansa menos (gana tiempo y caza más rápido: la diferencia sube al 38–44 % en los niveles 5–6).
- Desde el nivel 16–18 nadie necesita pociones.

### 2.21 Valores por punto de STR revisados (decidido)

Los valores por punto usados hasta ahora eran una propuesta inicial de Claude que nunca se había validado. Para STR quedan así:

| STR por punto | Antes (propuesta) | Ahora |
|---|---|---|
| Vida | 20 | **25** |
| Regeneración de vida | 0,2/s | 0,2/s (sin cambios) |
| Defensa física y mágica | 0,5 % | **0,1 %** |
| % de daño en todos los golpes | 1,5 % | **1,5 %** (se mantiene: es daño que se hace, no reducción) |

INT y AGI siguen pendientes de validar.

**Del 1 al 19 con estos valores** (min · pociones; nadie muere):

| Nivel | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|
| 1 | 165 · 0 | 166 · 0 | 170 · 129 | 170 · 181 | 2,9 % |
| 2 | 169 · 0 | 163 · 0 | 163 · 228 | 154 · 284 | 9,6 % |
| 3 | 177 · 0 | 164 · 0 | 160 · 284 | 146 · 334 | 21,0 % |
| 4 | 181 · 0 | 169 · 0 | 165 · 316 | 144 · 383 | 25,7 % |
| 5 | 201 · 0 | 175 · 0 | 171 · 391 | 181 · 295 | 17,1 % |
| 6 | 218 · 0 | 187 · 0 | 181 · 478 | 218 · 232 | 20,5 % |
| 7 | 236 · 0 | 202 · 0 | 238 · 300 | 240 · 228 | 19,0 % |
| 8 | 260 · 0 | 220 · 0 | 275 · 249 | 256 · 249 | 24,7 % |
| 9 | 288 · 0 | 239 · 0 | 287 · 294 | 271 · 228 | 20,5 % |
| 10 | 331 · 316 | 321 · 266 | 305 · 295 | 206 · 345 | 60,8 % |
| 11 | 364 · 366 | 364 · 253 | 344 · 303 | 225 · 428 | 61,8 % |
| 12 | 404 · 496 | 385 · 408 | 395 · 367 | 251 · 569 | 61,1 % |
| 13 | 479 · 419 | 433 · 393 | 455 · 395 | 283 · 719 | 69,7 % |
| 14 | 534 · 582 | 509 · 420 | 516 · 408 | 317 · 829 | 68,2 % |
| 15 | 603 · 726 | 566 · 505 | 593 · 492 | 372 · 853 | 62,1 % |
| 16 | 664 · 1.021 | 601 · 808 | 689 · 577 | 468 · 656 | 47,2 % |
| 17 | 806 · 949 | 714 · 815 | 803 · 627 | 537 · 713 | 50,1 % |
| 18 | 880 · 1.509 | 800 · 987 | 933 · 854 | 596 · 974 | 56,5 % |
| 19 | 1.049 · 1.449 | 938 · 1.182 | 1.103 · 873 | 705 · 1.044 | 56,4 % |

- **Vida**: el cuerpo a cuerpo pasa de 400 a 475 en el nivel 1 y de 4.000 a 4.975 en el 19. La regeneración no cambia.
- **Defensa**: el cuerpo a cuerpo baja del 97,5 % al **19,5 %** en el nivel 19 (arco 7,9 %, mágico 5,9 %). El daño no cambia (golpe blanco de espada larga: 114 en el nivel 1, 1.072 en el 19).
- Con mucha menos defensa, **todos reciben más daño** en los niveles altos: desde el nivel 10 el cuerpo a cuerpo bebe 250–1.500 pociones cada 1.000 mobs y tiene que descansar (espada larga 859 → 1.049 min en el nivel 19); el arco y el mágico también beben más y tardan algo más que antes.
- Del 1 al 9 casi nada cambia: hasta el nivel 9 la defensa antigua aún era baja.

### 2.22 Robo de vida del cuerpo a cuerpo al 5 % (decidido)

Para bajar su consumo de pociones, el robo de vida del cuerpo a cuerpo pasa del **4 % al 5 %**. Del 1 al 9 no cambia nada (se desbloquea en el nivel 10).

| Nivel | Espada larga 4 % → 5 % (min · pociones) | Espada corta 4 % → 5 % |
|---|---|---|
| 10 | 331 · 316 → 314 · 340 | 321 · 266 → 298 · 304 |
| 11 | 364 · 366 → 333 · 521 | 364 · 253 → 321 · 382 |
| 12 | 404 · 496 → 389 · 457 | 385 · 408 → 368 · 372 |
| 13 | 479 · 419 → 451 · 376 | 433 · 393 → 409 · 348 |
| 14 | 534 · 582 → 505 · 531 | 509 · 420 → 475 · 407 |
| 15 | 603 · 726 → 563 · 781 | 566 · 505 → 516 · 562 |
| 16 | 664 · 1.021 → 648 · 712 | 601 · 808 → 585 · 589 |
| 17 | 806 · 949 → 733 · 1.029 | 714 · 815 → 665 · 695 |
| 18 | 880 · 1.509 → 857 · 1.097 | 800 · 987 → 748 · 781 |
| 19 | 1.049 · 1.449 → 965 · 1.501 | 938 · 1.182 → 855 · 1.065 |
| **Total 10–19** | **7.833 → 7.345 pociones (−6 %)** | **6.037 → 5.505 (−9 %)** |

- Las pociones bajan poco (6–9 %); lo que más mejora es el **tiempo**: descansa menos y caza un 5–10 % más rápido (espada larga 1.049 → 965 min en el nivel 19). La diferencia con el mágico baja de ~61 % a 52–63 % según el nivel.
- Lo que más vida le quita es el **golpe sangriento** (1/6 de la vida cada 10 s). Para bajar de verdad las pociones, la palanca más directa es su coste (1/7 o 1/8) o su enfriamiento.

**Regeneración extra para el cuerpo a cuerpo (decidido):** el golpe sangriento se mantiene tal cual (solo se usa con buena vida). Su pasiva, igual que la del arco, suma una segunda ventaja: además del robo de vida del 5 %, **cada punto de STR da +0,1 de vida por segundo** (la mitad de lo que ya da la STR, así que su regeneración sube un ~50 %: 108 → 161 cada 5 s en el nivel 10; 198 → 296 en el 19). Primero se probó a duplicarla (+0,2 por punto), pero dejaba al cuerpo a cuerpo sin consumir ninguna poción.

| Nivel | Espada larga (min · pociones) | Espada corta |
|---|---|---|
| 10 | 253 · 284 | 243 · 313 |
| 11 | 286 · 382 | 269 · 349 |
| 12 | 321 · 478 | 295 · 433 |
| 13 | 355 · 529 | 330 · 486 |
| 14 | 405 · 472 | 372 · 347 |
| 15 | 468 · 217 | 430 · 8 |
| 16–19 | 540–859 · 0 | 497–788 · 0 |

- Vuelve a beber pociones en los niveles 10–15 (unas 0,3–0,5 por mob), sin tener que descansar; desde el nivel 16 la regeneración y el robo de vida ya lo cubren todo.
- El arco y el mágico no cambian.

### 2.23 Coste de maná y libros de habilidad

**Objetivo (decidido):** todos los perfiles deben **gastar maná de verdad** y beber pociones de maná. En el nivel 19, entre **300 y 1.000 pociones de maná** cada 1.000 mobs, con **menos de 150 de diferencia** entre los tres. Los hechizos del mágico cuestan más (tiene mucho más maná); el arco, punto intermedio; el cuerpo a cuerpo, menos (también gasta vida).

- El coste de maná pasa a ser un **% del maná máximo** (crece con el personaje): golpe doble 7 %, golpe al suelo 11 %, disparo cargado 4 %, ráfaga triple 9 %, disparo potente 7 %, hechizo fuerte 4 %, hechizo débil 2 %, escudo 5 % (valores de partida, sin calibrar).
- Los físicos beben poción de maná cuando tienen una habilidad lista y les falta maná.

**Libros de habilidad (decidido):** las habilidades se mejoran con libros. Cada mejora: **+1 % de daño** y **+10 % de coste de maná**.
- Supuestos de la simulación (pendientes de confirmar): **una mejora por nivel** en cada habilidad (18 en el nivel 19) y mejoras **sumadas sobre el valor base** (nivel 19: +18 % de daño y +180 % de coste).

**Del 1 al 19 con costes en % y libros** (min · pociones de vida · pociones de maná; nadie muere):

| Nivel | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|
| 1 | 165 · 0 · 0 | 166 · 0 · 0 | 170 · 129 · 0 | 170 · 181 · 0 | 2,9 % |
| 5 | 198 · 0 · 0 | 175 · 0 · 0 | 171 · 390 · 0 | 173 · 274 · 0 | 15,9 % |
| 10 | 244 · 284 · 0 | 234 · 297 · 0 | 286 · 281 · 11 | 295 · 0 · 0 | 26,2 % |
| 13 | 335 · 256 · 0 | 313 · 290 · 0 | 416 · 358 · 263 | 441 · 0 · 0 | 41,2 % |
| 15 | 429 · 0 · 159 | 404 · 0 · 150 | 572 · 473 · 669 | 568 · 0 · 0 | 41,5 % |
| 17 | 568 · 0 · 594 | 535 · 0 · 565 | 787 · 604 · 1.074 | 838 · 0 · 0 | 56,5 % |
| 19 | 772 · 0 · **1.037** | 727 · 0 · **976** | 1.161 · 981 · **1.984** | 1.095 · 0 · **96** | 59,6 % |

- Con los libros, el coste de maná por fin se nota en niveles altos, pero aún **sin calibrar**: en el nivel 19 el cuerpo a cuerpo bebe ~1.000 de maná (en el límite), el **arco casi 2.000** (demasiado) y el **mágico solo 96**.
- El mágico, al depender del maná, **se para a descansar** para recuperarlo en vez de beber, y pasa de ser el más rápido a tardar más que el cuerpo a cuerpo desde el nivel 10 (705 → 1.095 min en el 19). Al descansar tampoco necesita pociones de vida.
- Siguiente paso: bajar el % del arco, decidir si el mágico debe beber en lugar de descansar por maná, y calibrar los % para quedar dentro de 300–1.000.

## 3. Ficha de los niveles 1–19 (en revisión: ver 2.21)

Resumen de todo lo decidido en la sección 2 para el tramo **sin clase** (niveles 1 al 19). La ficha completa, nivel a nivel, se genera con `python3 herramientas/simulador/simular.py --ficha` en `herramientas/simulador/resultados/` (`ficha_perfiles_1_19.csv` y `ficha_mobs_1_19.csv`), lista para pasar a DataTables.

### 3.1 Perfiles, armas y crecimiento

| Perfil | Reparto base (STR / AGI / INT) | Arma | Segundos entre golpes | Daño del arma | Bono del arma y crecimiento por nivel (STR / AGI / INT) |
|---|---|---|---|---|---|
| Físico cuerpo a cuerpo | 5 / 4 / 1 | Espada larga | 2,6 | 75 | +10 / +5 / +3 |
| Físico cuerpo a cuerpo | 5 / 4 / 1 | Espada corta | 1,4 | 37 | +10 / +5 / +3 |
| Físico a distancia | 3 / 5 / 2 | Arco | 2,0 | 35 | +4 / +10 / +4 |
| Mágico | 2 / 2 / 6 | Bastón (no pega) | — | — | +3 / +5 / +10 |

El arma de nivel 1 da el mismo bono que se gana en cada nivel (easter egg).

### 3.2 Qué da cada punto

| Estadística | Por punto |
|---|---|
| STR | +25 vida · +0,2 vida/s · +0,1 % defensa física y mágica · +1,5 % de daño en todos los golpes (antes +20 vida y +0,5 % de defensa: ver 2.21) |
| INT | +15 maná · +0,2 maná/s · +2,5 % de daño de habilidades |
| AGI | +2 de daño plano en cada golpe |
| Base | 100 de vida, 0,5 vida/s, 50 de maná, 0,5 maná/s |

- Daño de un golpe = (daño del arma o de la habilidad + daño plano de AGI) × (1 + % de STR) × (1 + % de INT, solo habilidades) × crítico. Se redondea a entero.
- **Crítico** (no depende de AGI en este tramo): probabilidad 1 % + 0,2 % por nivel, tope 5 %; daño extra 2 % + 0,4 % por nivel, tope +10 %.
- **Armadura**: 50 por nivel; cada 100 restan 1 de daño a cada golpe recibido (mínimo 1).
- **Regeneración** mostrada cada 5 s y redondeada. Daño, vida, maná y estadísticas siempre enteros.

### 3.3 Valores por nivel (extracto de la ficha)

| Nivel | Perfil | STR / AGI / INT | Vida | Regen. vida (5 s) | Maná | Regen. maná (5 s) | Armadura | Golpe blanco | % daño (STR) | % habilidad (INT) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Espada larga | 15 / 9 / 4 | 400 | 18 | 110 | 7 | 50 | 114 | 22,5 | 10 |
| 1 | Espada corta | 15 / 9 / 4 | 400 | 18 | 110 | 7 | 50 | 67 | 22,5 | 10 |
| 1 | Arco | 7 / 15 / 6 | 240 | 10 | 140 | 9 | 50 | 72 | 10,5 | 15 |
| 1 | Mágico | 5 / 7 / 16 | 200 | 8 | 290 | 19 | 50 | — | 7,5 | 40 |
| 10 | Espada larga | 105 / 54 / 31 | 2.200 | 108 | 515 | 34 | 500 | 471 | 157,5 | 77,5 |
| 10 | Espada corta | 105 / 54 / 31 | 2.200 | 108 | 515 | 34 | 500 | 373 | 157,5 | 77,5 |
| 10 | Arco | 43 / 105 / 42 | 960 | 46 | 680 | 45 | 500 | 403 | 64,5 | 105 |
| 10 | Mágico | 32 / 52 / 106 | 740 | 35 | 1.640 | 109 | 500 | — | 48 | 265 |
| 19 | Espada larga | 195 / 99 / 58 | 4.000 | 198 | 920 | 61 | 950 | 1.072 | 292,5 | 145 |
| 19 | Espada corta | 195 / 99 / 58 | 4.000 | 198 | 920 | 61 | 950 | 922 | 292,5 | 145 |
| 19 | Arco | 79 / 195 / 78 | 1.680 | 82 | 1.220 | 81 | 950 | 929 | 118,5 | 195 |
| 19 | Mágico | 59 / 97 / 196 | 1.280 | 62 | 2.990 | 199 | 950 | — | 88,5 | 490 |

(STR / AGI / INT incluyen el bono del arma.)

### 3.4 Habilidades

| Perfil | Habilidad | Nivel | Qué hace | Enfriamiento | Duración | Maná |
|---|---|---|---|---|---|---|
| Cuerpo a cuerpo | Golpe doble | 1 | 150 % + 75 % del arma | 20 s | un golpe blanco | 8 |
| Cuerpo a cuerpo | Golpe al suelo | 1 | 300 % del arma | 40 s | 3 s | 12 |
| Cuerpo a cuerpo | Golpe sangriento | 10 | 300 % del arma; cuesta 1/6 de la vida máxima | 10 s | un golpe blanco | — |
| Cuerpo a cuerpo | Robo de vida (pasiva) | 10 | se cura el 5 % del daño que hace y cada punto de STR da +0,1 de vida por segundo | — | — | — |
| Distancia | Disparo cargado | 1 | 200 % del arma | 12 s | 2 s | 6 |
| Distancia | Ráfaga triple | 1 | 3 × 120 % del arma | 40 s | 1,5 s | 12 |
| Distancia | Disparo potente | 10 | 350 % del arma | 15 s | 3 s | 10 |
| Distancia | Robo de vida (pasiva) | 10 | se cura el 0,3 % del daño y +3 % de crítico (sin pasar el tope) | — | — | — |
| Mágico | Hechizo fuerte | 1 | 97 de daño base | 8 s | 2 s | 12 |
| Mágico | Hechizo débil | 1 | 32 de daño base | 1 s | 2 s | 5 |
| Mágico | Escudo de maná | 10 | absorbe hasta el 20 % de la vida máxima | 20 s | 8 s (1 s de lanzamiento) | 15 |
| Mágico | Celeridad (pasiva) | 10 | hechizos un 2 % más rápidos | — | — | — |

### 3.5 Mobs y caza

- Dos tipos de daño (físico o mágico) y dos distancias; para simular, rotación fija: cuerpo a cuerpo físico → a distancia mágico → cuerpo a cuerpo mágico → a distancia físico. Ciclo de ataques: básico, básico, potenciado (×2).
- Vida: 420 en el nivel 1 (±10 % por mob) y **+30 % por nivel**. Daño: 6 por golpe básico en el nivel 1, creciendo como la vida media de los jugadores (53 en el nivel 19).
- El cuerpo a cuerpo camina 1,5 s hasta cada mob; a los de distancia el mob cuerpo a cuerpo tarda 2,5 s en llegar.
- Pociones: +100, 20 s de enfriamiento; se descansa tras un mob si no queda vida para otro. Los mágicos reciben pociones de misión extra.

**Caza real del 1 al 19** (1.000 mobs por nivel; min · pociones; nadie muere):

| Nivel | Vida mob | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|---|
| 1 | 420 | 165 · 0 | 166 · 0 | 170 · 129 | 170 · 181 | 2,9 % |
| 5 | 1.200 | 201 · 0 | 175 · 0 | 171 · 252 | 146 · 351 | 37,6 % |
| 10 | 4.454 | 249 · 152 | 231 · 357 | 249 · 406 | 206 · 112 | 20,9 % |
| 15 | 16.537 | 468 · 0 | 430 · 0 | 480 · 141 | 356 · 176 | 34,6 % |
| 19 | 47.231 | 859 · 0 | 788 · 0 | 896 · 0 | 625 · 0 | 43,4 % |

El mágico es el más rápido y el que más pociones necesita; el cuerpo a cuerpo, el que más aguanta. Esa diferencia es intencionada (2.19).

## 4. Nivel 20: elección de clase (próxima sesión)

Al llegar al nivel 20 se elige clase y **se reconfiguran las estadísticas**. Cada clase recibe una **pasiva** que cambia lo que da cada punto, para que empiecen a perfilarse:
- **Mágicos**: cada punto de INT vale mucho más (por ejemplo, ×3), sobre todo en daño.
- **Agilidad**: cada pocos puntos de AGI (por ejemplo, cada 3) suben el crítico, el robo de vida o lo que haga falta para equilibrar.
- **Guerreros y combatientes**: la STR da más vida y más armadura, para perfilarse como los que aguantan (tanques).
- Las demás clases se potencian según la especialización que elijan.

## 5. Estructura propuesta del capítulo

1. **Lista cerrada de estadísticas** y a qué categoría pertenece cada una (principal, derivada, neutral, PvP, utilidad).
2. **Crecimiento por nivel**: cuántos puntos de principales da cada nivel y si el reparto es fijo por clase o en parte libre.
3. **Conversión principales → derivadas**: cuánto da cada punto de STR/INT/AGI.
4. **Eficiencia por clase**: tabla que dice cuánto aprovecha cada clase cada estadística ("todo suma, pero no igual").
5. **Fórmulas de combate**: golpe/fallo (precisión vs. evasión), crítico, daño contra defensa, multiplicadores (monstruos, jefes, PvP), debilitación.
6. **Topes y rendimientos decrecientes** para las estadísticas porcentuales (crítico, CDR, evasión…).
7. **Tabla de valores por fuente**: qué estadísticas y cuánto da cada fuente (equipo por calidad, desarrollo, encantamiento, códice, cocina…).
8. **Puntuación de poder**.
9. **Implementación**: AttributeSets de GAS y DataTables.

## 6. Preguntas abiertas

**De los niveles 1–19 (para cerrar del todo):**
- **Validar los valores por punto de INT y AGI** (los de STR ya están: 2.21).
- **Actualizar la ficha de la sección 3** con los valores de STR de 2.21 (vida y defensa).
- **Daño de las armas por tramos** (bronce → cobre → plata): de momento el arma no cambia de daño en todo el tramo.
- **Pociones por nivel**: la poción cura siempre 100.
- **El crítico apenas se nota** (+10 % de daño como mucho): decidido así por ahora.

**Para la próxima sesión:** nivel 20 y clases (ver 4).
