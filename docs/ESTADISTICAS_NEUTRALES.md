# Capítulo de detalle — Estadísticas (parte 3): neutrales

Estado: **cerrado para la Temporada 1** (las neutrales de la Temporada 2 se diseñarán más adelante). Tercera parte del capítulo de estadísticas (parte 1: `docs/ESTADISTICAS.md`, niveles 1–19; parte 2: `docs/ESTADISTICAS_NIVEL_20.md`, nivel 20). Las neutrales no dependen de STR, INT ni AGI: vienen de la **joyería y los encantamientos** (decidido en la parte 1).

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
- No hacen falta más pruebas por ahora (decidido): solo una o, como mucho, dos piezas darán precisión, y los escalados se harán con el equipo.

## 3. Escalado de las neutrales (decidido)

- **Lineal hasta la Temporada 3.** Las estadísticas suben en línea recta. En la Temporada 3, cuando los escalados empiecen a ser muy altos, se pondrá un **punto óptimo** (curva logarítmica): a partir de ahí cada punto rinde cada vez menos (por ejemplo, 100 puntos ya no dan 10 de evasión sino 3–4) y compensa más repartirlos en otras estadísticas (regeneración, precisión…). Ese punto **no debe llegar antes de la Temporada 3**.
- Las cantidades exactas de cada pieza de equipo se fijarán más adelante: solo una o, como mucho, dos piezas darán precisión, y el escalado dependerá del equipo.

## 4. Defensa física y defensa mágica

### 4.1 Reglas (decidido)

- Son **puntos exactos** que da el equipo. Cada punto da un **porcentaje de reducción** del daño de su tipo: la defensa física reduce el daño físico recibido y la mágica, el mágico.
- **Lineal** (ver 3): **10.000 puntos = 50 % de reducción**, es decir, **0,005 % por punto** (1 % cada 200 puntos). Hacen falta miles de puntos para llegar a un 30–50 %.
- **Se suma** a la defensa que dan las estadísticas principales: la del Combatiente es la de su STR **más** la de su equipo. Los tanques tendrán que seguir subiendo la reducción de daño físico porque recibirán cada vez más daño.
- Los personajes de **fuerza** reciben sobre todo **menos daño físico**; buscarán **reducción mágica** en el equipo para equilibrarse, y así quedarán mejor equilibrados que otras clases.

| Puntos de defensa | Reducción |
|---|---|
| 10 | 0,05 % |
| 200 | 1 % |
| 1.000 | 5 % |
| 2.000 | 10 % |
| 6.000 | 30 % |
| 10.000 | 50 % |

- Con **10 puntos de defensa física y 10 de mágica**, en el nivel 20 la reducción sube un **0,05 %** de cada tipo: en la Temporada 1 la defensa del equipo apenas se notará.
- En el simulador: `defensa_pct_por_punto`, `defensa_fisica_jugador` y `defensa_magica_jugador`; los mobs ya pegan con daño físico o mágico (la mitad de cada tipo) y cada uno se reduce con su defensa.

### 4.2 La STR solo da defensa física (decidido)

- Cada punto de STR da **solo reducción de daño físico** (0,1 %; 0,2 % en el Combatiente). Deja de dar defensa mágica, en todos los niveles.
- La defensa mágica que se pierde la darán **collares, brazaletes y demás joyería**; con el equipo de **grado raro** se debería recuperar.
- Efecto en la simulación:
  - **Niveles 1–19** (`simular.py --niveles`): casi nada. Nadie muere; los cuerpo a cuerpo tardan un 1–3 % más entre los niveles 10 y 14 y beben más pociones de vida entre el 10 y el 17 (por ejemplo, en el nivel 14 la espada larga pasa de 307 a 648 pociones cada 1.000 mobs).
  - **Nivel 20**: el Luchador ya no aguanta 12 mobs a la vez, el Asesino muere 8 veces con 6, el grupo de 5 no puede con 12 élites y la mazmorra con adds de élite ya no se supera. Con mobs normales en grupo casi no cambia.
- **Es intencionado**: los grupos grandes de mobs solo llegan en el nivel 20, y los élites fuertes piden antes fabricar equipo y empezar por bandas con **élites de solo ×2**. Los personajes llegan débiles al 20 y tienen que optimizar recursos, hacer pausas y aprender a juntar mobs. El **Combatiente** debe ser el primero en llegar a tener resistencias suficientes para pelear solo con el equipo básico.

## 5. Daño a monstruos (decidido)

- **Porcentaje** que se suma al daño de cada golpe blanco y de cada habilidad contra **monstruos** (no contra jefes: para ellos llegará "daño a jefes" en la Temporada 2). Ejemplo: con un 1 %, un golpe de 300 contra un mob hace 303.
- **Temporada 1 (niveles 1–20)**: con el equipo normal se llega a **un 15 %**; como **máximo un 20 %** sumando todo el equipo, y solo con objetos concretos o encantamientos concretos.
- Se controla con **porcentajes planos** en el equipo y, en temporadas siguientes, con **multiplicadores de vida de los mobs**: si alguien llega, por ejemplo, a un 200 %, la vida de los mobs debe subir lo suficiente para que no mueran de un golpe, sin olvidar que habrá jugadores con muy poco daño a monstruos que también tienen que poder matarlos.
- **Invocador**: el daño a monstruos del equipo **se suma** al +50 % de su pasiva de arma: **65 %** con equipo normal y **70 %** como máximo con encantamientos y objetos concretos.
- Efecto aproximado: un 15 % de daño a monstruos acelera la caza en algo menos de un 15 % (el daño que sobra al rematar cada mob se pierde).

## 6. Experiencia de caza y vigor (en estudio)

### 6.1 Referencia: el vigor de MIR4 (lo que le gusta al usuario)

- El **vigor** es un tiempo acumulado durante el cual el personaje recibe **experiencia extra al matar mobs** ("Hunting EXP Boost"). Se ve en un panel con el % total y el tiempo que queda (por ejemplo, +353,65 % durante 2 h 36 min).
- **Solo se consigue recolectando** (o con **píldoras de vigor**); descansar no da vigor. Así obliga a recolectar o a usar píldoras.
- El % extra viene de **varias fuentes**, cada una con su aporte, y el panel las detalla (en MIR4: espíritus, tesoro, conquista, códice, entrenamiento…; cada una aparece multiplicada por ×1,5 mientras el vigor está activo).
- En el registro de combate se ve la experiencia **base** del mob y, entre paréntesis, la **extra** de todas las fuentes: "Exp +9.472 (+7.384)".

### 6.2 Potenciación de caza (decidido)

- **Nombre:** el vigor del juego se llamará **potenciación de caza** ("porcentaje de potenciación de caza").
- Cada mob da una **experiencia base**. Mientras la potenciación de caza está activa, el personaje recibe **+100 % de experiencia** sobre esa base (el doble), como el vigor de MIR4 o la experiencia de descanso de WoW.
- **Todas las demás fuentes de experiencia extra se suman a ese 100 %**: códice, piedras, espíritus, encantamientos, joyería (la neutral **experiencia de caza**) o cualquier otra que haya en el juego. Es una suma simple de porcentajes (sin el ×1,5 de MIR4). Ejemplo: 100 % + 10 % de joyería + 5 % de códice = +115 %.
- **Funciona por tiempo**, como en MIR4 (no como la barra de WoW), y **solo se gasta el tiempo en combate**: estar quieto no lo consume.
- Hay un **máximo de tiempo acumulado** (por ejemplo, 8 horas). Al gastarlo, lo que más conviene es recargarlo haciendo otras cosas: **recolectar**, **fabricar con una profesión** u otras acciones; quizá también **estando desconectado**, como en WoW.
- En combate se muestra la experiencia base y, entre paréntesis, la extra; un panel detalla cada fuente.

### 6.3 Reglas completas (decidido)

- **Sin potenciación activa**, las demás fuentes (joyería, códice, espíritus…) **siguen sumando su %**; solo se pierde el +100 % de la potenciación.
- **Máximo acumulado: 8 horas.** Coincide con el máximo de juego automático: son las horas en las que conviene dejar al personaje cazando solo. Cuando se acaban, se sigue ganando experiencia pero perdiendo una parte importante; para recuperarla hay que recargar.
- **Recarga:**
  - **Desconectado**: **1 segundo de potenciación por cada segundo** de desconexión.
  - **Recolectando y fabricando**: cada acción suma una **cantidad exacta** de potenciación, igual al **tiempo base** de esa acción. Si minar una veta tarda 10 s de base, suma 10 s aunque la **velocidad de recolección** la haya bajado a 6–7 s. Así, recolectar más rápido carga la potenciación más deprisa.
  - **Objetivo** (hacia el final de la Temporada 1): recolectando o fabricando durante **la mitad del tiempo** (unas 4 horas) se recuperan las 8 horas. Los tiempos base de recolección y el ritmo esperado se calibrarán en el capítulo de recursos/profesiones.
  - Si alguien se pone todo el equipo de velocidad de recolección (por ejemplo, un inventor) y baja una veta a 3–4 s, no es un problema: recogerá más rápido y cargará más potenciación, que normalmente no usará porque quien vive de recolectar apenas caza.
- **Sin píldoras de potenciación** (decidido): en MIR4 se pueden acumular hasta tres días de vigor con píldoras y dejar el personaje cazando solo esos tres días, lo que parece injusto. Aquí la única forma de recargar es desconectarse, recolectar o fabricar.
- **Objetivo de diseño:** que mientras se sube de nivel la gente **pare a recolectar**. Al llegar al nivel 20 deben tener materiales para fabricar **dos o tres objetos**, y al subir del 20 al 40 tendrán que recolectar los materiales de las zonas nuevas para poder fabricar al llegar al 40. En el nivel máximo la potenciación ya no importa.

## 7. Velocidad de recolección (decidido)

- **Cómo se recolecta** (como en MIR4): zonas de recolección con 20, 30 o 40 plantas, vetas o puntos de energía. El personaje se acerca y recoge con una animación: **picar** (minerales), **escarbar** matas (hierbas) o una especie de **baile** (energía).
- **Tiempo base: 10 s** por cada recogida en el nivel 1, sin ninguna bonificación. Cada recogida suma a la potenciación de caza esos 10 s de base, se tarde lo que se tarde (6.3).
- La **velocidad de recolección** reduce ese tiempo. Es **general**: vale para todos los recursos, no solo para el de la profesión que la da.
- **Máximo: 100 %** sumando todas las fuentes.
- **Fuentes:**

| Fuente | Velocidad |
|---|---|
| Profesión secundaria de **minería** | +25 % |
| Profesión secundaria de **herboristería** | +25 % |
| **Encantamientos** en el equipo: muy raros, +1–3 % por pieza; hay que reforjar o ajustar todo el equipo para llegar | hasta +25 % |

- **No habrá profesión de energía** (decidido): la energía no tiene profesión propia; su recolección solo se acelera con la velocidad general.
- **Sin tope en la estadística** (decidido): se controla con el valor que dé cada objeto o encantamiento (por ejemplo, un objeto con +5 % o un encantamiento con +3 %), que se fijará al diseñar cada objeto. Habrá quien monte un **equipo exclusivo de recolección** poniendo velocidad en todas las piezas (pecho, guantes…) y supere el 50 %: no es un problema.
- **Lo "gratuito" en el nivel 20**: el 25 % de minería y el 25 % de herboristería (50 % en total). Se consigue al llegar a **100 puntos** de cada profesión. Cada temporada tiene su propia rama de profesión, y el bonus solo se aplica a los recursos de su temporada; la velocidad de los objetos y encantamientos vale en todas partes (`docs/PROFESIONES.md`, 3.5).

- **Fórmula (decidido): cada 100 % de velocidad reduce el tiempo a la mitad.** **Tiempo = 10 s × 0,5^(velocidad ÷ 100)**: con 100 % se tarda **5 s**; con 200 %, **2,5 s**; con 300 %, **1,25 s**. Nunca llega a 0: por mucha velocidad que se consiga (aunque sea con un fallo o un exploit), siempre hay que tardar algo en recoger.

| Velocidad | 0 % | 25 % | 50 % | 75 % | 100 % | 200 % | 300 % |
|---|---|---|---|---|---|---|---|
| Tiempo por recogida | 10 s | 8,4 s | 7,1 s | 5,9 s | 5 s | 2,5 s | 1,25 s |
- Cómo se ven las vetas, cuántas recogidas tienen por calidad (común, poco común, raro…) y demás: en el capítulo de objetos.

### 7.1 Alerta contra bots y exploits (decidido)

- Cuando un personaje **supere un umbral de velocidad de recolección**, el servidor envía automáticamente una **alerta al equipo del juego** (como un ticket de Jira o un correo a un desarrollador o al staff): "este personaje llegó a X % con esta configuración".
- **Umbral de la Temporada 1: 200 %** (lo normal es 25 % de minería + 25 % de herboristería + lo poco que den los encantamientos). Se **ajusta temporada a temporada**. Cualquiera que lo supere genera la alerta.
- El informe llega **completo**: estadísticas base del personaje, **todo su equipo**, **de dónde sale cada % de recolección** (para detectar, por ejemplo, que la minería esté dando 100 % en vez de 25 % por un exploit) y, más adelante, la **información del dispositivo** (se diseñará en la parte de seguridad del juego).
- **Principio general**: cualquier estadística o ventaja que llegue a valores irregulares debe poder detectarse y generar su informe. Los **términos y condiciones** del juego indicarán que, al alcanzar ciertos límites irregulares, se envía la configuración del personaje y del juego para revisarla.

### 7.2 Puntos de profesión y vetas (decidido)

- Las profesiones de recolección suben **como en WoW**: según la veta o la planta que se recoja, se gana o no un punto de habilidad. Al llegar a **100 puntos** se obtiene su +25 % de velocidad de recolección.
- Con más puntos se pueden recoger vetas de más calidad. Por ejemplo, las **vetas enriquecidas** piden **50 puntos** de la profesión: 50 de minería para minerales, 50 de herboristería para hierbas.
- Una veta de minerales puede dar materiales distintos (acero, aleaciones, lingotes, piedras o fragmentos de algún material…).
- Las **vetas enriquecidas** dan el material del **grado más alto que exista en la temporada** y en **mayor cantidad**. Ejemplo: una veta de estaño normal da 1 lingote de estaño poco común; una enriquecida, 4 lingotes de estaño **raro** en la Temporada 2 (donde el raro es el grado más alto), y **épicos** en la Temporada 3, cuando llega el equipo épico.
- Las enriquecidas solo se pueden recoger **1, 2 o 3 veces** (no cientos de veces como las vetas de MIR4).
- **La energía es distinta**: se acumula como el cobre, no tiene materiales distintos ni vetas enriquecidas, y la puede recoger cualquiera. Cada punto de energía da una **cantidad que depende de su calidad**.

### 7.3 Velocidad de fabricación (decidido)

- Al llegar a **100 puntos** en una profesión de fabricación (encantamiento, joyería, peletería, herrería…), se recibe un **bonus de especialización**: **el tiempo de fabricación se reduce a la mitad** en las recetas de esa profesión. Una receta de 10 s pasa a **5 s exactos**.
- Se expresa así, "se reduce a la mitad", y no como un %, para que no se confunda con la velocidad de recolección.
- **Es lo más rápido que se puede fabricar**: no hay ningún otro bonus ni mejora de velocidad de fabricación.
- **Alerta de seguridad**: si alguien fabrica algo en **4,9 s o menos** (más rápido que la mitad del tiempo de la receta), el servidor avisa al equipo de seguridad con todo el detalle: quién, con qué velocidad, qué receta, qué materiales, su equipo y su configuración completa, para saber si es un fallo de programación o cómo lo consiguió (como la alerta de 7.1).

### 7.4 Protocolo de las alertas de seguridad (decidido)

Vale para todas las alertas (recolección, fabricación y las que se añadan):

- **Silenciosas**: al jugador **no se le avisa de ninguna forma** y **no se le bloquea**. Puede seguir recolectando o fabricando a esa velocidad; solo le llega la notificación al equipo.
- **Tres informes, no uno por acción**. Si alguien consigue fabricar en 0,1 s, enviar un aviso por objeto serían más de 600 correos por minuto y podría saturar o tumbar los sistemas. En su lugar:
  1. **Primer informe**, en el momento en que se cruza el límite: la notificación con la configuración completa del personaje.
  2. **Informe de 5 minutos**: el registro completo de **todas** las recolecciones o fabricaciones de los 5 minutos siguientes (hora exacta, recurso o receta, tiempo de cada una, todo).
  3. **Informe de 1 hora**: el mismo registro durante la hora siguiente.
- Así se distingue un **pico puntual** (algo raro en un segundo que no se repite en los 5 minutos ni en la hora) de una **velocidad anormal sostenida**.
- **Suspensión de la cuenta**: solo con **tres informes consecutivos** (instantáneo, 5 minutos y 1 hora) que confirmen la irregularidad, nunca por un único aviso. Sanción, apelación, contenido completo de los informes y demás: `docs/SEGURIDAD.md`.

## 8. CDR — reducción de enfriamiento (configuración estándar)

El usuario pidió configurarla "según el estándar"; estos son los valores propuestos:

- **Qué hace**: resta un % al **enfriamiento** de las habilidades activas. **Enfriamiento final = enfriamiento × (1 − CDR)**. Con un 10 %, una habilidad de 20 s pasa a 18 s. Lineal, como el resto de neutrales hasta la Temporada 3.
- **A qué no afecta**: tiempos de lanzamiento y canalización (eso es la Celeridad), pociones, recursos secundarios (Ira, Energía, Foco, Trance, Esencia) ni habilidades sin enfriamiento (Lluvia de fuego).
- **Excepción: el Embate**. Su provocación dura 7 s y su enfriamiento es de 10 s; si la CDR lo acortara, el hueco de 2–3 s sin agro desaparecería (con un 30 % el Combatiente tendría el agro siempre). Por eso **la CDR no afecta al Embate**.
- **Valores por temporada** (como el daño a monstruos): en la Temporada 1, **10 % con equipo normal** y **15 % como máximo** con objetos o encantamientos concretos. **Tope absoluto del 40 %** en cualquier temporada, para que ninguna habilidad se pueda encadenar.
- En el simulador: `cdr_jugador_pct`, `cdr_tope_pct` y `cdr_excluidas` en `parametros.csv`.

Efecto en el nivel 20 (daño por segundo contra el jefe · mobs/hora de uno en uno):

| Especialización | Sin CDR | 10 % | 15 % |
|---|---|---|---|
| Luchador | 1.517 · 90 | 1.564 · 94 | 1.602 · 96 |
| Combatiente | 637 · 48 | 664 · 50 | 665 · 50 |
| Asesino | 1.900 · 105 | 1.989 · 110 | 2.001 · 112 |
| Atacante | 2.243 · 122 | 2.417 · 130 | 2.518 · 135 |
| Mago | 2.367 · 126 | 2.378 · 127 | 2.408 · 129 |
| Invocador | 746 · 61 | 757 · 62 | 767 · 62 |

- Con el 15 % máximo, la CDR da entre un **1 y un 12 %** más de daño. Quien más gana es el **Atacante** (sus disparos fuertes tienen enfriamiento); el **Mago** casi nada, porque su daño sale de la Lanza de hielo y de la Lluvia de fuego, que no tienen enfriamiento.

Con esto quedan vistas todas las neutrales de la Temporada 1.

## 9. Puntuación de poder (se calibra en el capítulo de objetos)

- **Sin clasificación por nivel** (decidido): el nivel tiene tope y todos llegarán al máximo. Queda la clasificación por **poder** (además de la de códice y las de clanes).
- **Clasificación de poder por clase** (decidido): se podrá filtrar por especialización. Si alguna estadística queda algo desbalanceada y da más poder sin dar más daño, no importa, porque cada clase se compara con las de su misma clase.
- **La calibración del poder se hace en el capítulo de objetos** (decidido), cuando existan los equipos ideales:
  - Para cada especialización se monta su **equipo perfecto**: todas las piezas posibles, con todas las mejoras perfectas, eligiendo lo que más rinda para su clase. Ese personaje marca el **poder máximo**.
  - **Cada estadística da un poder distinto según la especialización**, en función de lo que le sirve. Por ejemplo, al Combatiente la STR le daría unos 10 puntos de poder, la AGI 3 y la INT 1.
  - Hay que evitar que una estadística dé tanto poder que convenga acumularla aunque no sirva: por ejemplo, un Mago con 150 % de crítico y sin INT, sin regeneración de maná y sin daño de habilidades.
  - Se calibrará con **pruebas en el simulador**: por ejemplo, quitarle a un personaje 20 de precisión, poner ese hueco en crítico y ver si su daño sube o baja. El poder de cada estadística debe reflejar lo que aporta de verdad.
- Pruebas hechas en esta sesión (sirven de punto de partida):
  - Sumar las estadísticas finales con una tabla igual para todos hace depender el poder de la clase: en el nivel 20 sin equipo, el Luchador saldría con unos 3.200 y el Invocador o el Atacante con unos 2.000.
  - Idea propuesta: poder = nivel (100 por nivel) + niveles de habilidad (20 por nivel) + equipo y otras fuentes con una tabla de equivalencias. Queda como referencia; los pesos serán por especialización.
