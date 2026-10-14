# Diseño base del juego

Qué existe dentro del juego y cómo se relaciona, antes de entrar en valores concretos (estadísticas, daño, tiempos). Documento vivo: se completa a medida que se toman decisiones.

## 1. El juego en una frase

MMORPG 3D para PC donde cada jugador hace evolucionar a su personaje a lo largo de temporadas (estilo Lineage 2), en un mundo con combate, profesiones, recolección y contenido PvE y PvP (estilo World of Warcraft).

## 2. Pilares de diseño

1. **El personaje evoluciona**: empieza sencillo y crece con especializaciones, subclases y equipo.
2. **Hay más que subir de nivel**: profesiones, recolección, mazmorras, jefes, PvP, economía.
3. **Temporadas**: el contenido se publica por etapas; cada una tiene su propio endgame.
4. **Juego limpio**: el servidor decide todo lo importante (combate, botín, recolección) para combatir trampas y bots.

## 3. Entidades del mundo

Todo lo que existe en el mundo pertenece a una de estas familias.

```
Entidades del mundo
├── Personajes jugadores
├── NPCs de combate
│   ├── Mobs (monstruos)
│   └── Jefes
├── NPCs de interacción (no combaten)
├── Recursos recolectables
└── Objetos interactivos del mundo
```

### 3.1 Personajes jugadores

Los controla una persona.

- Arquetipo (Físico / Mágico) → clase base → especialización 1 → especialización final.
- Varias **subclases** por personaje, cada una con su propio progreso. Se desbloquean en el **nivel 60** (del 1 al 40 se aprende a jugar bien la clase; del 40 al 60 se sube rápido). Reglas detalladas: más adelante.
- Estadísticas principales (STR / INT / AGI), derivadas y neutrales.
- Recursos: vida, MP y un recurso secundario según la clase (Ira, Energía, Foco, Iluminación).
- Habilidades, equipo, inventario, profesiones, misiones y reputación.

### 3.2 NPCs de combate — Mobs

Enemigos que pueblan el mundo y las mazmorras.

- Tienen nivel, estadísticas, habilidades y comportamiento (IA).
- **Categorías propuestas:**
  - **Normal**: enemigo común.
  - **Élite**: más fuerte, pensado para grupos o jugadores preparados.
  - **Raro**: aparece con poca frecuencia y da mejor botín.
- **Comportamiento:**
  - **Agresivo**: ataca al ver al jugador.
  - **Neutral**: solo ataca si lo atacan.
  - **Pasivo**: nunca ataca (animales, criaturas ambientales).
- Al morir dan experiencia y botín. Reaparecen tras un tiempo.
- Pueden ser fuente de recursos (pieles, carne, materiales) mediante profesiones.

### 3.3 NPCs de combate — Jefes

Enemigos especiales con mecánicas propias (fases, habilidades únicas, ataques que hay que esquivar).

- **Jefe de mazmorra**: al final o a lo largo de una mazmorra, para grupos.
- **Jefe de mundo**: aparece en el mundo abierto cada cierto tiempo y reúne a muchos jugadores; puede generar PvP alrededor.
- **Jefe de banda (raid)**: contenido de endgame para grupos grandes.
- Botín especial y, en algunos casos, ligado a la temporada.

### 3.4 NPCs de interacción

No combaten (o solo se defienden). El jugador habla o comercia con ellos.

| Tipo | Función |
|---|---|
| Dador de misiones | Da y recibe misiones |
| Comerciante | Compra y vende objetos |
| Entrenador de clase | Enseña habilidades, gestiona especializaciones y subclases |
| Entrenador de profesión | Enseña y sube de rango las profesiones |
| Banquero / almacén | Guarda objetos del jugador |
| Transporte | Viaje rápido entre zonas (teletransporte, monturas) |
| Herrero / mejora | Repara y mejora equipo |
| Guardia | Protege ciudades; puede combatir |
| Ambiental | Da vida al mundo (diálogos sueltos, sin función) |

Un mismo NPC puede tener varias funciones (por ejemplo, comerciante y dador de misiones).

### 3.5 Recursos recolectables

Puntos del mundo donde se obtienen materiales.

| Recurso | Profesión asociada | Ejemplos |
|---|---|---|
| Minerales | Minería | Cobre, hierro, plata, gemas |
| Plantas | Herboristería | Hierbas para pociones |
| Madera | Tala | Troncos para armas y construcción |
| Pesca | Pesca | Peces para cocina |
| Pieles / partes de mobs | Desuello | Cuero, colmillos, escamas |

Los materiales alimentan las profesiones de fabricación (herrería, alquimia, cocina, etc.). Los materiales útiles para el equipo de nivel alto solo los dan mobs y recursos de nivel alto.

Hay **dos sistemas de recolección** (decidido):

#### A. Zonas de recolección (estilo MIR4)

- Zonas concretas del mapa con muchos puntos de recolección (por ejemplo, 20 menas en una zona).
- Cada punto tiene un **grado** que define qué materiales da, en qué cantidad y con qué calidad (común, poco común, raro…).
- Cada punto tiene una **cantidad de cargas** (pueden ser cientos). Cada "golpe" de recolección gasta carga y da uno o varios materiales.
- **Uso exclusivo**: solo una persona puede recolectar un punto al mismo tiempo.
- Al agotarse las cargas, el punto desaparece y **reaparece** tras un tiempo.

#### B. Vetas enriquecidas (estilo WoW)

- Versión especial y escasa de un recurso (por ejemplo, "veta de cobre enriquecida"): **materiales mejores y en mayor cantidad**, pero **pocas cargas** (por ejemplo, 10).
- **Compartidas y por jugador**: cualquier jugador cercano puede recolectarla a la vez, y **cada jugador** puede sacar todas las cargas de la veta (si llegan 30 personas, las 30 recolectan).
- La **cuenta atrás** (por ejemplo, **1 minuto**) empieza en el **primer golpe** de cualquier jugador. Durante ese minuto todos pueden recolectar; al terminar, la veta desaparece para todos. **Agotar las cargas no la hace desaparecer**: solo el tiempo.
- **Cargas individuales**: cada jugador ve y gasta **sus propias** cargas; para todo el que llega la veta siempre muestra las cargas completas (si yo saco 9, el siguiente sigue viendo 10, no 1).
- **Velocidad de recolección**: cada golpe tarda un tiempo que mejora con el progreso del personaje (por ejemplo, 2 s por carga al principio → la veta de 10 cargas se vacía en 20 s; más adelante 1 s → 10 s). Un recolector rápido vacía su parte y se va a buscar otra veta, mientras la veta sigue disponible para los demás hasta que termine el minuto.
- **Aparición aleatoria** entre muchos puntos posibles de la zona (por ejemplo, 70 puntos posibles, máximo 10 vetas activas a la vez, reaparición cada ~5 min).
- Objetivo: que los jugadores aprendan los puntos, creen rutas de recolección y avisen a sus amigos para recolectar juntos.

Todos los valores (cargas, tiempos, cantidades, probabilidades) son datos ajustables.

### 3.6 Objetos interactivos del mundo

Elementos con los que se puede interactuar y que no son NPCs ni recursos.

- Cofres (botín), puertas y palancas, portales, puntos de resurrección, objetos de misión, carteles o tablones de misiones.

### 3.7 Botín de un mob (decidido)

Cada mob tiene una **tabla de botín** con dos partes. Ejemplo, un lobo:

| Tipo | Recompensa | Cantidad / probabilidad | A quién le llega | Apilable | Tamaño de pila |
|---|---|---|---|---|---|
| **Fijo** | Experiencia | Cantidad exacta | Repartida según contribución | — | — |
| **Fijo** | Moneda | Cantidad exacta | Repartida según contribución | — | — |
| **Variable** | Armaduras del grupo | % (baja) | Para el grupo: armadura de **cualquier clase**, a un miembro al azar | No | — |
| **Variable** | Armaduras individuales | % (p. ej. 30 %) | **Individual**: solo de la clase del personaje | No | — |
| **Variable** | Objetos de misión | % | **Individual**: solo a quien tenga la misión activa | Sí | Por definir |
| **Variable** | Objetos de profesión | % | Para todos por igual (rotación) | Sí | Por definir |
| **Variable** | Objetos de códice | % | Para todos por igual (rotación) | Sí | Por definir |
| **Variable** | "Basura" (objetos para vender) | % | Para todos por igual (rotación) | Sí | Por definir |

**Apilables**: el equipo (armas, armaduras, joyería) no se apila; cada pieza ocupa su propio espacio. El resto de objetos se apila; el tamaño máximo de cada pila se definirá con el inventario.

Los valores concretos de cada mob se definirán más adelante en las tablas de datos.

### 3.8 Reparto de recompensas (decidido)

**No existe "el primero que golpea se lo queda"** (sin mobs "grises" estilo WoW). La **contribución** es el **daño efectivo** hecho al mob: si el mob tiene 500 de vida y el golpe final es de 5.000, cuentan 500.

**Entre jugadores o grupos distintos** que atacan al mismo mob, **todo** se reparte según la contribución, incluidas las armaduras individuales. Ejemplo: el grupo 1 hace el 80 % del daño y el grupo 2 el 20 %:

| | Grupo 1 (80 % del daño) | Grupo 2 (20 % del daño) |
|---|---|---|
| Fijos (experiencia, moneda) | 80 % | 20 % |
| Armaduras del grupo | 80 % de probabilidad | 20 % de probabilidad |
| Armaduras individuales | Cada miembro: su % × 0,8 | Cada miembro: su % × 0,2 |
| Objetos de misión | 80 % de probabilidad | 20 % de probabilidad |
| Objetos de profesión | 80 % de probabilidad | 20 % de probabilidad |
| Objetos de códice | 80 % de probabilidad | 20 % de probabilidad |
| "Basura" | 80 % de probabilidad | 20 % de probabilidad |

- **Fijos**: reparto exacto. Mob de 300 XP: 240 para el grupo 1 y 60 para el grupo 2. La moneda se reparte en la unidad mínima (cobre); lo que no llegue a 1 cobre se pierde.
- **Variables**: cada objeto tira su probabilidad de caer; si cae, un marcador interno decide a qué unidad (jugador o grupo) va, con la contribución como probabilidad.
- **Excepción — armaduras individuales**: cada jugador tira su propia probabilidad multiplicada por la contribución de su unidad. Con un 30 % base: en el grupo 1 (80 %) cada miembro tiene 24 %; en el grupo 2 (20 %), 6 %.
- Un **grupo cuenta como una sola unidad**; un jugador sin grupo es una unidad propia. Funciona igual en mobs normales y en jefes de mundo o de banda.
- Solo cuenta el **daño efectivo**: si el mob tiene 500 de vida y el golpe final es de 5.000, cuentan 500.
- **Sin contribución mínima** y **sin penalización por diferencia de nivel**: los materiales valiosos solo los dan mobs de nivel alto.

**Moneda**: cobre, plata y oro; 100 cobre = 1 plata (100 plata = 1 oro, por confirmar).

**Aggro**: estadística aparte, independiente del reparto. Los tanques generan más aggro con sus habilidades y estadísticas.

### 3.9 Grupos y bandas (decidido)

El juego está pensado para **jugarse en grupo**: jugar acompañado siempre debe rendir más que jugar solo.

**Grupo**: máximo **5 personas**. Es la única agrupación que recibe bonus de experiencia y moneda.

| Miembros | Bonus de experiencia |
|---|---|
| 1 (solo) | — |
| 2 | +10 % |
| 3 | +15 % |
| 4 | +20 % |
| 5 | +25 % |

- **Bonus de moneda**: existe y crece con el tamaño del grupo; valores por definir (orientativo: +5 %, +10 %, +15 %, +20 %).
- **Banda (raid)**: agrupación grande para actividades concretas (10, 20, 50 o 100 personas según la actividad). Los tamaños se desbloquean con las temporadas. Sin bonus de experiencia. Reglas propias por definir.

#### Reparto dentro del grupo (decidido)

- **Experiencia y moneda**: a partes iguales entre los miembros, más el bonus de grupo.
- **Objetos**: se reparten **por rotación con prioridad**.

**Orden de prioridad** (de mayor a menor):

1. Armaduras del grupo
2. Armaduras individuales
3. Objetos de misión
4. Objetos de profesión
5. Objetos de códice
6. "Basura"

**Algoritmo**

1. Se tira la probabilidad de cada categoría para saber qué cae.
2. Se recorren los objetos caídos en orden de prioridad. Cada uno se entrega **al azar** a un miembro **no excluido**.
   - **Excepción — armaduras individuales**: no se sortean. **Cada miembro no excluido** tira su propia probabilidad, y todos los que acierten reciben una (del tipo de su clase). Pueden caer varias en una muerte.
   - **Nadie recibe dos armaduras en la misma muerte**: quien recibió la armadura del grupo no tira por la individual.
   - **Excepción — objetos de misión**: quedan **fuera del sorteo de rotación**. Solo pueden ir a miembros que tienen la misión activa y aún necesitan el objeto (al azar entre ellos), **sin importar la exclusión**, y recibirlo no excluye de lo que sigue. Un objeto de misión nunca se pierde por la rotación.
3. Quien recibe un objeto queda **excluido** de los siguientes.
4. Cuando los 5 miembros han recibido algo, la exclusión se reinicia y todos vuelven a estar habilitados.
5. Termina cuando no quedan objetos.

*(En los ejemplos 1 y 2, solo un miembro acierta su tirada de armadura individual.)*

**Ejemplo 1 — caen 4 objetos** (armadura del grupo, armadura individual, códice, basura):
armadura del grupo → jugador 3 · armadura individual → jugador 5 (excluido 3) · códice → jugador 2 (excluidos 3, 5) · basura → jugador 4 (excluidos 3, 5, 2). Fin.

**Ejemplo 2 — caen 6 objetos** (todas las categorías):
armadura del grupo → jugador 2 · armadura individual → jugador 4 · misión → jugador 1 · profesión → jugador 5 · códice → jugador 3 · todos recibieron: se reinicia la exclusión · basura → jugador 4. Fin.

**Ejemplo 3 — varias armaduras individuales** (armadura del grupo, armaduras individuales, códice, basura):
armadura del grupo → jugador 3 · los jugadores 1, 2, 4 y 5 tiran su armadura individual; aciertan 5, 4 y 2 → una armadura para cada uno · códice → jugador 1 (único no excluido) · todos recibieron: se reinicia la exclusión · basura → jugador 4. Fin.

**Notas por tipo de objeto**

- **Armaduras del grupo**: probabilidad baja; armadura de **cualquier clase**. Permite conseguir armaduras de clases que no hay en el grupo (por ejemplo, de mago en un grupo sin magos) para los códices de otras clases. Se pueden comerciar o vender en el mercado.
- **Armaduras individuales**: siempre del tipo propio de la clase de quien la recibe. Su probabilidad se ajusta por la contribución del grupo (3.8). Es la fuente principal para el códice de la propia clase.
- **Objetos de misión**: en cada muerte cae como máximo uno para el grupo, así que una misión tarda **lo mismo sola que en grupo** (en grupo se necesitan más objetos, pero se matan más mobs). Si nadie del grupo necesita el objeto, no cae.

### 3.10 Roles (decidido)

- **Todas las clases y especializaciones pueden hacer daño** y jugar solas, incluidas las de tanque y sanador.
- En grupo, cada especialización es más eficiente en su rol: el tanque aguanta y atrae a los mobs, el sanador cura, el DPS hace daño.
- Habrá zonas pensadas para grupos (por ejemplo, muchos mobs agresivos) donde un tanque y un sanador hacen que subir de nivel sea mucho más rápido.

### 3.11 Códice (estilo MIR4 — detalle en un capítulo propio más adelante)

Sistema de colección que da **estadísticas permanentes a la cuenta**. Por ahora solo se fija lo básico:

- **Los mobs sueltan insignias**, el material del códice (objetos de códice en la tabla de botín). Cada zona tiene las suyas.
- Con las insignias se **fabrican** objetos de códice, que se **mejoran** y se **registran**. Fabricación, mejora y niveles de las entradas: por definir.
- **Registro**: el objeto **se consume** y desaparece del inventario; queda registrado en la cuenta. Cada línea del códice necesita sus objetos concretos: un objeto no cubre varias líneas.
- **Códice de armaduras**: las armaduras sobrantes o sustituidas también se registran, en vez de venderse por poco. Cuando el códice está completo, las armaduras de más se mejoran y se venden en el mercado.
- **Bonificaciones de cuenta**: se mantienen al cambiar de subclase (el códice de ataque mágico sigue sirviendo si un guerrero pasa a mago).
- **Todas las estadísticas suman para todas las clases**, a diferencia de MIR4: el ataque mágico también ayuda a un guerrero, pero mucho menos que a un mago. Se definirá en el capítulo de estadísticas.

Inspiración (MIR4): material por zona con grados, combinable y ligado → objeto de códice (material + moneda) → mejora (p. ej. +2) → entrada que pide un conjunto de objetos → bonificación fija → efectos totales sumados.

### 3.12 Objetos: clasificación (en curso)

#### Fuente (de dónde sale un objeto)

Es la primera clasificación de todo objeto.

| Fuente | Ejemplos |
|---|---|
| Caza | Botín de mobs y jefes |
| Misión | Recompensas de misiones |
| Fabricación | Profesiones, combinación de insignias |
| Compra a NPC | Comerciantes |
| Logros | Recompensas por cumplir objetivos |
| Recolección | Minerales, plantas, madera, pesca |
| Eventos | Recompensas de eventos temporales o de temporada |
| PvP | Recompensas de arenas y zonas PvP |
| Cofres del mundo | Cofres y objetos interactivos |

El comercio entre jugadores y el mercado no crean objetos, solo los mueven, así que no son una fuente.

#### Calidad

| Calidad | Color |
|---|---|
| Común | Gris |
| Poco común | Verde |
| Raro | Azul |
| Épico | Rojo |
| Legendario | Amarillo |
| Mítico | Morado |
| Cósmico | Cian |

La calidad máxima disponible sube con cada temporada:

| Temporada | Niveles | Calidad máxima |
|---|---|---|
| 1 | 1–20 | Poco común |
| 2 | 20–40 | Raro |
| 3 | 40–60 | Épico |
| Siguientes expansiones | — | Legendario, Mítico, Cósmico |

#### Tipos de armadura (decidido)

Solo tres tipos: **tela**, **cuero** y **placas** (sin malla). Regla para asignar el tipo a cualquier clase, actual o futura:

| Tipo | Quién lo usa | Concepto |
|---|---|---|
| **Tela** | Clases de **daño mágico** | Magos, invocadores, sanadores mágicos |
| **Placas** | Clases físicas **de primera línea** | Tanques y luchadores que aguantan al frente pegando (bruisers, gladiadores) |
| **Cuero** | Clases físicas **que evitan el combate directo** | Arqueros, pícaros, asesinos: golpear rápido y desaparecer |

- **Niveles 1–20**: clases mágicas en tela y clases físicas en cuero (las placas llegan con las especializaciones).
- **Cualquier personaje puede llevar cualquier tipo**, pero el tipo propio de su clase le da una **bonificación de especialización en armadura** (por ejemplo, +1 % de agilidad con cuero). Con otro tipo la pierde.
- La armadura individual del botín (3.7) cae siempre del tipo propio de la clase del personaje.
- Bonificaciones por conjunto o por pieza: se definirán junto con los objetos y las estadísticas.

**Propuesta de asignación según el árbol de clases** (borrador; se revisará al diseñar el contenido de cada temporada):

| Base (1–20) | Especialización 1 (20–40) | Especialización final (40–60) |
|---|---|---|
| Luchador — cuero | Dos manos — placas | Lancero — placas · Guerrero — placas |
| | Espadas duales — **?** | Gladiador — placas · Danzador — cuero |
| | Tanque — placas | Paladín — placas · Guardián — placas |
| Asesino — cuero | Daguero — cuero | Sutileza — cuero · Sanguinario — cuero |
| | Cazarrecompensas — cuero | Asesino — cuero · Mutilador — cuero |
| Combatiente — cuero | Frenético — placas | Berserker — placas |
| | Recolector — **?** | Carroñero — **?** · Explorador — cuero |
| Atacante a distancia — cuero | Arquero — cuero | Ballestero, Cazador, Francotirador — cuero |
| Mago — tela | Hechicero, Chamán — tela | Piromántico, Arcanista, Elementalista, Brujo, Alquimista — tela |
| Invocador — tela | Encantador — tela | Sacerdote, Conjurador, Nigromante, Bardo, Monje — tela |

#### Ranuras de equipo (decidido)

Dos grupos: **equipo** (ropa y armas) y **joyería**, con **8 ranuras cada uno**: **4 disponibles del nivel 1 al 40 y 4 que se desbloquean del 41 al 60**. La distribución es simétrica a propósito, para que la interfaz quede equilibrada (4 a cada lado) y no haya que rehacerla al añadir ranuras, como le pasó a MIR4.

| Grupo | Ranura | Tipo (tela/cuero/placas) | Apariencia | Disponible |
|---|---|---|---|---|
| Equipo | Arma | No | Sí | Nivel 1 |
| Equipo | Pecho | **Sí** | Sí | Nivel 1 |
| Equipo | Arma secundaria | No (depende de la clase) | Sí | Nivel 1 (objetos desde el nivel 21) |
| Equipo | Pantalón | **Sí** | Sí | Nivel 1 |
| Equipo | Guantes | **Sí** | Sí | Nivel 41 |
| Equipo | Botas | **Sí** | Sí | Nivel 41 |
| Equipo | Cintura | No | Sí | Nivel 41 |
| Equipo | Espalda | No | Sí | Nivel 41 |
| Joyería | Collar | No | Sí | Nivel 1 |
| Joyería | Anillo | No | Sí | Nivel 1 |
| Joyería | Arete | No | Sí | Nivel 1 |
| Joyería | Brazalete | No | Sí | Nivel 1 |
| Joyería | Tiara | No | Sí | Nivel 41 |
| Joyería | Anillo 2 | No | Sí | Nivel 41 |
| Joyería | Arete 2 | No | Sí | Nivel 41 |
| Joyería | Brazalete 2 | No | Sí | Nivel 41 |

- 16 ranuras en total: 8 hasta el nivel 40 y 8 más desde el 41.
- **Joyería duplicada**: no se pueden llevar dos piezas idénticas (dos anillos, aretes o brazaletes iguales). Cada pieza de joyería tiene **estadísticas aleatorias** dentro de unos rangos (mínimo y máximo por estadística), así que cada pieza es única. Más adelante habrá **conjuntos** (por ejemplo, el del "Furioso") con bonificaciones por llevar varias piezas.
- **Arma secundaria**: la ranura está abierta desde el nivel 1 por simetría, pero las armas secundarias (escudo, carcaj, frasco, libro…) solo caen desde el nivel 21, con la primera especialización.
- Piezas con tipo de armadura: pecho y pantalón (nivel 1–40); guantes y botas (desde el 41).
- Solo **pecho, guantes, pantalón y botas** tienen tipo de armadura: son las piezas que cuentan para la bonificación de especialización en armadura.
- **Sin casco ni hombreras**, a propósito: muchos jugadores ocultan el casco para lucir la cara que personalizaron. La cabeza queda despejada; la **tiara** es la pieza de cabeza (pequeña, no tapa el rostro).
- **Todas las ranuras tienen apariencia**, joyería incluida: los jugadores detallistas pueden coordinar colores (por ejemplo, joyería de amatista azul a juego con un conjunto azul).
- **Desbloqueo de apariencias**: al obtener un objeto por cualquier vía (botín, mercado, intercambio, recompensa…) se desbloquea su apariencia para el personaje. Prestarse objetos para conseguir la apariencia y devolverlos está permitido. También habrá apariencias de eventos.
- **Transfiguración**: la apariencia de una pieza se puede cambiar por otra. Sirve también para cosméticos de eventos (por ejemplo, transformar la tiara en un sombrero de vaquero).

**Referencia de interfaz (MIR4)**: pantalla de personaje con pestañas separadas para equipo y joyería; las ranuras rodean al modelo 3D y cada una muestra su calidad (color), grado (I, II, III…) y nivel de mejora (+5, +6…).

### 3.13 Comercio entre jugadores (decidido)

- Los intercambios directos entre jugadores **siempre cobran una comisión en oro**: no se pueden pasar objetos gratis.
- El mercado y el comercio no crean objetos, solo los mueven (ver Fuentes en 3.12).

### 3.14 PvP (decidido)

- **PvP abierto solo en ciertas zonas**: hay **zonas seguras** (sin combate entre jugadores) y **zonas peligrosas** (PvP libre). Un único tipo de servidor; sin servidores separados PvE y PvP.
- Cada jugador decide si entra a las zonas peligrosas a pelear por recursos.
- Las zonas PvP dan **botín especializado en PvP** (objetos que mejoran estadísticas PvP); las zonas PvE dan botín enfocado al PvE.

### 3.15 Profesiones (decidido, estilo WoW)

- **Todas las profesiones disponibles desde el nivel 1** (Temporada 1 incluida).
- **2 profesiones principales** por personaje y **todas las secundarias** que se quieran.
- Lista y detalle de profesiones: capítulo propio más adelante (base WoW, con ajustes de Lineage 2 u otros juegos).

### 3.16 Monturas (decidido)

- **Solo terrestres** (sin monturas voladoras).
- Todas funcionan igual: el personaje se sube y gana velocidad de movimiento. Lo que cambia es la **apariencia** (caballos, bicicletas, motos…).

### 3.17 Inventario (en curso)

Objetivo: que el inventario **nunca sea una fuente de frustración** (llenarse de objetos inútiles, tener que volver a la base a vender).

**Venta directa desde el inventario** (estilo MIR4): se selecciona el objeto y se vende, sin NPC. Ir a un NPC solo tiene sentido para **intercambiar** objetos por otra cosa, no para venderlos por moneda.

**Bolsas**: un inventario **general** y **dos bolsas especiales**, cada una en su propia casilla.

**Casillas de bolsa**

| Casilla | Básicas | De pago (oro, precio alto) | Máximo |
|---|---|---|---|
| **Bolsa principal** | 1 — no se puede vender, quitar ni cambiar; se **amplía con oro** | — | 1 |
| **Bolsas normales** | 3 — se desbloquean con **misiones** | 4.ª y 5.ª | 5 |
| **Bolsa de componentes** | 1 | 1 más | 2 |
| **Bolsa de consumibles** | 1 | — (siempre una sola) | 1 |

Máximo total: 9 bolsas.

| Bolsa | Qué guarda | Cómo se llena |
|---|---|---|
| **General** | Equipo, basura y todo lo que no cabe en las especiales | Automático |
| **Componentes** | Todo lo que sirve para fabricar (componentes de profesiones principales y secundarias, insignias del códice…) | Automático |
| **Consumibles** | Pociones de vida y de maná, elixires, comidas | **El jugador decide** qué pone en cada espacio (por ejemplo, de 10 espacios: 6 de pociones, 2 de comida, 1 de elixir y 1 libre) |

- **Desbordamiento**: si una bolsa especial está llena, lo que llega va a la **bolsa general**. **Nunca se pierde un objeto** por falta de espacio en una bolsa especial.
- Ventaja: inventario ordenado, y es imposible vender por accidente los componentes.

**Terminología**: **componentes** = cualquier objeto que se usa para fabricar algo, sea de profesión principal o secundaria.

**Objetos de misión — "bolsa invisible"**: no ocupan espacio ni se muestran en el inventario. Solo se ven como progreso en el **registro de misiones** (por ejemplo, "Pieles de lobo 3/5"). Se eliminan al completar o abandonar la misión. Así nadie se bloquea por tener el inventario lleno, y quien acepte muchas misiones sin terminarlas no acumula miles de objetos visibles.

**Tamaño de las pilas**: lo define **cada objeto** al crearlo, según su calidad y lo frecuente que sea. Los objetos muy abundantes (por ejemplo, insignias del códice, de las que se acumulan 10.000–20.000) tienen pilas muy grandes para no ocupar espacio.

**De dónde salen las bolsas**:
- La fuente principal son las **profesiones**: cada profesión puede fabricar una bolsa mayor usando **solo sus propios materiales** (el desollador con componentes de desuello, el encantador con componentes de encantamiento…). Así cualquier jugador que suba una profesión puede hacerse una bolsa.
- Los jugadores **especializados en profesiones** pueden fabricar bolsas un poco más grandes (por ejemplo, de 34 a 36 o 38 espacios): una ventaja pequeña, no abismal.

**Desbloqueo progresivo, ligado a la introducción del juego**:
- Niveles 1–3: los mobs solo dan **experiencia y cobre**; el jugador aprende lo básico sin llenar el inventario.
- Al llegar al nivel 3, un NPC de misión presenta las **profesiones** y desbloquea la **casilla de la bolsa de componentes**.
- Al avanzar en el juego se desbloquean **más casillas** y se consiguen **mejores bolsas**.

**Organizar bolsas** (referencia: botón "Limpiar bolsas" de WoW): botón con icono de brocha en la bolsa general que ordena todo automáticamente:
- Lo **útil** se coloca empezando por la **esquina inferior derecha**, de abajo hacia arriba y de derecha a izquierda.
- La **basura** se coloca empezando por la **esquina superior izquierda**, de arriba hacia abajo y de izquierda a derecha.
- Así la basura queda agrupada en un extremo y lo útil en el otro.
- Orden dentro de lo útil: **por categoría** (equipo, consumibles, componentes…) y dentro de cada una **por calidad**, de mayor a menor.

**Asignar bolsas** (referencia: WoW): una bolsa del inventario general puede convertirse en bolsa **solo para un tipo** de objeto. Es una **recompensa de profesiones**:
- Al llevar la **primera profesión principal al máximo** → se pueden asignar bolsas a **componentes**.
- Al llevar **una profesión secundaria al máximo** → se pueden asignar bolsas a **consumibles**.
- Ejemplo: quien pasa una tarde minando o fabricando en masa tiene sus componentes siempre ordenados en las mismas bolsas.
- *Propuesta por confirmar*: opciones por bolsa para excluirla del botón de organizar y de la venta rápida (como "Ignorar esta bolsa" en WoW).

**Venta rápida** (referencia: MIR4):
- Panel de **lista de venta** junto al inventario: muestra cuántos objetos van seleccionados y permite elegir la cantidad a vender de cada pila.
- **Filtros de selección automática**: por calidad (común, poco común, raro…) y si se incluyen o no objetos comerciables.
- Botones: **selección automática** (aplica los filtros), **reiniciar** y **vender**.
- **Bloqueo de objetos**: el jugador puede bloquear cualquier objeto (candado) para que nunca entre en la venta rápida.
- *Propuestas por confirmar*: filtro por categoría (basura, equipo, componentes…); que la selección automática **excluya el equipo que aún falta registrar en el códice**; mostrar el total de moneda antes de confirmar.

**Banco** (referencia: WoW):
- **Banco personal**: uno por personaje, organizado en **pestañas**.
  - **Pestaña 1 — general**: guarda cualquier tipo de objeto.
  - **Pestaña 2 — componentes**: solo componentes.
  - **Pestañas adicionales**: se compran (como las casillas de bolsa) y, al desbloquearlas, el jugador decide si quedan abiertas a todo o asignadas a un tipo de objeto.
- Comodidades: buscador, botón de organizar y botón **"Depositar todos los componentes"**.
- **Banco de tropa** (compartido entre los personajes de la cuenta): la pestaña existe pero se desbloquea en el **nivel 60**, cuando llega el contenido para varios personajes en la cuenta (por ejemplo, clases especiales que se añadan más adelante).

### 3.18 Mejora de equipo (en curso)

Mezcla de MIR4 y Lineage 2.

- Niveles de mejora de **+1 a +10**. El máximo es **+10** y **nunca cambia** (ni con nuevas temporadas).
- Intentar mejorar un objeto a +10 está **bloqueado**: el sistema avisa "No es posible realizar más mejoras en este equipo".

**Referencia (MIR4)**:
- Coste por intento: piedra de mejora (de la calidad del objeto) + otro material (Darksteel) + moneda.
- Muestra la **probabilidad de éxito**, el nivel actual → siguiente y el cambio de poder.
- **Zona segura** (niveles bajos): si falla, el objeto no baja de nivel.
- **Zona de peligro** (niveles altos): si falla, **el objeto se destruye**.
- Estadística de **bonificación de probabilidad de mejora**; la probabilidad nunca supera el 100 %.
- Botón de **mejora automática**.

*Cambios respecto a MIR4: por definir con el usuario.*

## 4. Sistemas principales

Lo que hace funcionar a las entidades anteriores. Se desarrollan por fases según la hoja de ruta.

| Sistema | Qué cubre |
|---|---|
| Combate | Daño, defensa, crítico, evasión, aggro, muerte y resurrección |
| Progresión | Niveles, experiencia, especializaciones, subclases, temporadas |
| Habilidades | Activas y pasivas, enfriamientos, costes, efectos (buffs/debuffs) |
| Objetos y equipo | Armas, armaduras, rarezas, mejoras |
| Inventario y banco | Guardar y gestionar objetos |
| Profesiones | Recolección y fabricación |
| Misiones | Misiones de historia, secundarias, diarias |
| IA de NPCs | Patrullas, agresividad, persecución, mecánicas de jefes |
| Interacción | Hablar, comerciar, recolectar, abrir, usar |
| Social | Grupos, clanes, chat, amigos |
| PvP | Duelos, arenas, zonas PvP |
| Economía | Moneda, comercio entre jugadores, subastas |

## 5. Base técnica común (Unreal Engine)

- **Personajes jugadores, mobs y jefes** comparten una misma base de "criatura combatiente" con el Gameplay Ability System: todos tienen estadísticas, habilidades y efectos, y el mismo código de combate sirve para todos.
- **NPCs de interacción, recursos y objetos del mundo** comparten un sistema de **interacción** común: el jugador se acerca, pulsa una tecla y la entidad responde según su tipo.
- Los datos de cada entidad (estadísticas de mobs, botín, tiempos de reaparición, recursos) viven en tablas importadas desde la hoja de cálculo.

## 6. Alcance de la Temporada 1 (propuesta)

Entra:
- Personajes: 6 clases base, niveles 1–20.
- Mobs normales, élites y raros para las zonas de nivel 1–20.
- Jefes de mazmorra; al menos un jefe de mundo.
- NPCs: misiones, comerciantes, entrenadores, banco, transporte.
- Recolección y algunas profesiones de fabricación.
- PvP básico (duelos y alguna zona PvP).

Queda para más adelante:
- Especializaciones de las temporadas 2 y 3.
- Bandas (raids) grandes.
- Subasta y economía avanzada.

## 7. Preguntas abiertas

**Pendientes para más adelante**
- **Bonus de moneda** por tamaño de grupo: valores.
- **Bandas** (se desbloquean en el nivel 40 o 60): reglas de reparto de experiencia, moneda y botín.
- **Subclases** (desde el nivel 60): nivel de cada subclase, qué se comparte, límite de subclases.
- **Comercio**: valor de la comisión; si el mercado también cobra comisión.
- **Profesiones**: lista de principales y secundarias.

**Temas base por definir**
- Inventario: espacio inicial de cada bolsa y ampliaciones de la principal; banco: número total de pestañas y espacios por pestaña; precios de pestañas y casillas de pago (se calcularán a partir del oro que genera un personaje por día); ¿límite de misiones activas a la vez?
- Mejora de equipo (+N).
- Consumibles y otros objetos.
- Monedas: ¿100 plata = 1 oro?, monedas especiales.
- Ambientación y estilo artístico.

**Capítulos propios**
- **Estadísticas**: peso de cada estadística por clase, PvE vs. PvP; revisar la hoja (valores base que no coinciden, fórmula que suma el nivel dos veces, nombres de habilidades desplazados, modelo de estadísticas).
- **Códice**: fabricación, mejora, niveles de entradas.
- **Contenido por temporada**: tipo de armadura de cada especialización y casos dudosos (Espadas duales, Recolector, Carroñero, Mutilador); si el tipo puede cambiar entre la especialización 1 y la final.
