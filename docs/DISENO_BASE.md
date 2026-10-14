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
- Varias **subclases** por personaje, cada una con su propio progreso.
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

- Versión especial y escasa de un recurso (por ejemplo, "veta de cobre enriquecida"): **materiales mejores y en mayor cantidad**, pero **pocas recolecciones** (4–5).
- **Compartidas**: cualquier jugador cercano puede recolectarla a la vez.
- Al primer golpe empieza una **cuenta atrás** (por ejemplo, 15 s); al terminar, la veta desaparece y nadie más puede recolectarla.
- **Aparición aleatoria** entre muchos puntos posibles de la zona (por ejemplo, 70 puntos posibles, máximo 10 vetas activas a la vez, reaparición cada ~5 min).
- Objetivo: que los jugadores aprendan los puntos, creen rutas de recolección y avisen a sus amigos para recolectar juntos.

Todos los valores (cargas, tiempos, cantidades, probabilidades) son datos ajustables.

### 3.6 Objetos interactivos del mundo

Elementos con los que se puede interactuar y que no son NPCs ni recursos.

- Cofres (botín), puertas y palancas, portales, puntos de resurrección, objetos de misión, carteles o tablones de misiones.

### 3.7 Botín de un mob (decidido)

Cada mob tiene una **tabla de botín** con dos partes. Ejemplo, un lobo:

| Tipo | Recompensa | Cantidad / probabilidad | A quién le llega |
|---|---|---|---|
| **Fijo** | Experiencia | Cantidad exacta | Repartida según contribución |
| **Fijo** | Moneda | Cantidad exacta | Repartida según contribución |
| **Variable** | Armaduras del grupo | % (baja) | Para el grupo: armadura de **cualquier clase**, a un miembro al azar |
| **Variable** | Armaduras individuales | % (p. ej. 30 %) | **Individual**: solo de la clase del personaje |
| **Variable** | Objetos de misión | % | **Individual**: solo a quien tenga la misión activa |
| **Variable** | Objetos de profesión | % | Para todos por igual (rotación) |
| **Variable** | Objetos de códice | % | Para todos por igual (rotación) |
| **Variable** | "Basura" (objetos para vender) | % | Para todos por igual (rotación) |

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

#### Reparto dentro del grupo

- **Experiencia y moneda**: a partes iguales entre los miembros, más el bonus de grupo.
- **Objetos compartidos — rotación** (profesión, códice, basura): cada objeto que cae se asigna **al azar** entre los miembros que aún no han recibido nada; quien recibe uno queda excluido hasta que todos hayan recibido, y entonces la rotación se reinicia. A la larga todos reciben más o menos lo mismo.
- **Armaduras individuales — botín personal**: cada miembro tira **su propia probabilidad** (ajustada por la contribución de su grupo). Solo puede caerle equipo **de su propia clase**. Un mob puede dar varias piezas, una por cada miembro al que le salga la tirada. Es la fuente principal para el códice de la propia clase.
- **Armaduras del grupo — botín aleatorio**: probabilidad baja de que caiga una armadura de **cualquier clase**, asignada a **un miembro al azar**. Permite conseguir armaduras de clases que no hay en el grupo (por ejemplo, de mago en un grupo sin magos) para los códices de otras clases. También se pueden comerciar o vender en el mercado.
- **Objetos de misión — individuales**: solo los recibe quien tiene la misión activa, con su propia probabilidad. Una misión debe tardar **lo mismo solo que en grupo** (en grupo se matan más mobs, pero cada uno necesita sus propios objetos), para no castigar a quien juega solo.

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

Dos grupos: **equipo** (ropa y armas) y **joyería**. En cada grupo, 7 ranuras están disponibles desde el inicio y 1 se desbloquea en el nivel 41.

| Grupo | Ranura | Tipo (tela/cuero/placas) | Apariencia | Disponible |
|---|---|---|---|---|
| Equipo | Arma | No | Sí | Nivel 1 |
| Equipo | Arma secundaria | No (depende de la clase) | Sí | Nivel 1 |
| Equipo | Pecho | **Sí** | Sí | Nivel 1 |
| Equipo | Guantes | **Sí** | Sí | Nivel 1 |
| Equipo | Pantalón | **Sí** | Sí | Nivel 1 |
| Equipo | Botas | **Sí** | Sí | Nivel 1 |
| Equipo | Cintura | No | Sí | Nivel 1 |
| Equipo | Espalda | No | Sí | Nivel 41 |
| Joyería | Collar | No | Sí | Nivel 1 |
| Joyería | Anillo | No | Sí | Nivel 1 |
| Joyería | Arete | No | Sí | Nivel 1 |
| Joyería | Brazalete | No | Sí | Nivel 1 |
| Joyería | Tiara | No | Sí | Nivel 1 |
| Joyería | Anillo 2 | No | Sí | Nivel 1 |
| Joyería | Arete 2 | No | Sí | Nivel 1 |
| Joyería | Brazalete 2 | No | Sí | Nivel 41 |

- 16 ranuras en total.
- Solo **pecho, guantes, pantalón y botas** tienen tipo de armadura: son las piezas que cuentan para la bonificación de especialización en armadura.
- **Sin casco ni hombreras**, a propósito: muchos jugadores ocultan el casco para lucir la cara que personalizaron. La cabeza queda despejada; la **tiara** es la pieza de cabeza (pequeña, no tapa el rostro).
- **Todas las ranuras tienen apariencia**, joyería incluida: los jugadores detallistas pueden coordinar colores (por ejemplo, joyería de amatista azul a juego con un conjunto azul).
- **Transfiguración**: la apariencia de una pieza se puede cambiar por otra. Sirve también para cosméticos de eventos (por ejemplo, transformar la tiara en un sombrero de vaquero).

**Referencia de interfaz (MIR4)**: pantalla de personaje con pestañas separadas para equipo y joyería; las ranuras rodean al modelo 3D y cada una muestra su calidad (color), grado (I, II, III…) y nivel de mejora (+5, +6…).

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

- **Por temporada** (al diseñar su contenido): tipo de armadura de cada especialización y casos dudosos (Espadas duales, Recolector, Carroñero, Mutilador); si el tipo puede cambiar entre la especialización 1 y la final.
- **Ranuras**: ¿se pueden llevar dos piezas idénticas en anillo, arete y brazalete? ¿Cómo se obtienen las apariencias (colección de la cuenta al conseguir cada pieza, estilo WoW; cosméticos de eventos; tienda)?
- **Orden de prioridad** en la rotación de objetos compartidos (¿profesión → códice → basura?).
- **Códice**: capítulo propio más adelante (fabricación, mejora, niveles de entradas).
- **Estadísticas**: capítulo propio más adelante (peso de cada estadística por clase, PvE vs. PvP).
- **Bonus de moneda** por tamaño de grupo: valores.
- **Bandas**: reglas de reparto de experiencia, moneda y botín.
- **Vetas enriquecidas**: ¿las 4–5 recolecciones son por jugador o el total compartido entre todos? ¿La cuenta atrás empieza siempre en el primer golpe?
- **Moneda**: ¿100 plata = 1 oro?
- ¿El **PvP** es libre en todo el mapa (con penalizaciones, estilo Lineage 2) o solo en zonas y modos concretos?
- ¿Qué **profesiones** entran en la Temporada 1 y cuántas puede tener cada personaje?
- ¿Habrá **monturas** desde la Temporada 1?
