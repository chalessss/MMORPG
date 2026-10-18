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
