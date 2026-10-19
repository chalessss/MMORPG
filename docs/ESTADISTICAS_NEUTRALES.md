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

### 6.2 Encaje en el juego (propuesta por validar)

- El vigor sería la versión concreta de la **experiencia de descanso** que ya se apuntaba en el diseño base (3.26: "posiblemente un híbrido que también se cargue con la recolección"), pero cargada **solo con la recolección** y con píldoras.
- **Experiencia de caza** (la neutral) sería una de las fuentes del % extra, junto con otras que ya existen en el diseño: códice, técnicas de clan, consumibles y, más adelante, espíritus. La bonificación de grupo (+10 % a +25 %) iría aparte.
- Mostrar siempre la experiencia base y la extra por separado, como en MIR4, y un panel con el detalle de las fuentes.
