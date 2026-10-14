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

### 3.7 Reparto de recompensas al morir un mob o jefe (decidido)

**No existe "el primero que golpea se lo queda"** (sin mobs "grises" estilo WoW). Las recompensas se reparten según la **contribución**, que es el **daño efectivo** hecho al mob: si el mob tiene 500 de vida y el golpe final es de 5.000, cuentan 500.

| Recompensa | Cómo se reparte |
|---|---|
| **Experiencia** | Exactamente proporcional al daño. Mob de 300 XP: quien hizo el 20 % recibe 60, quien hizo el 80 % recibe 240. |
| **Moneda** | Proporcional al daño, en la unidad mínima (cobre). Lo que no llegue a 1 cobre se pierde. |
| **Objetos y materiales** | Cada objeto que puede soltar el mob tira su propia probabilidad de caer (p. ej. armadura 30 %). Si cae, se sortea a quién le toca con probabilidad igual a la contribución (85 % de daño → 85 % de opciones). Cada objeto se sortea por separado. |

- **Moneda**: cobre, plata y oro; 100 cobre = 1 plata (100 plata = 1 oro, por confirmar).
- **Sin contribución mínima**: cualquier daño cuenta, pero una contribución muy baja da muy poca experiencia, quizá ninguna moneda y pocas opciones de botín.
- **Sin penalización por diferencia de nivel**: los materiales valiosos solo los dan mobs de nivel alto, así que matar mobs bajos no compensa.
- **Grupos**: el grupo cuenta como una sola unidad. Si dos grupos atacan al mismo jefe, cada grupo recibe según su porcentaje de daño (clave en jefes de mundo y de banda).
- **Aggro**: estadística aparte, independiente del reparto. Los tanques generan más aggro con sus habilidades y estadísticas.

### 3.8 Grupos y bandas (decidido)

El juego está pensado para **jugarse en grupo**: jugar acompañado siempre debe rendir más que jugar solo.

**Grupo**: máximo **5 personas**. Es la única agrupación que recibe bonus de experiencia y moneda.

| Miembros | Bonus de experiencia |
|---|---|
| 1 (solo) | — |
| 2 | +10 % |
| 3 | +15 % |
| 4 | +20 % |
| 5 | +25 % |

*(Interpretación por confirmar: el bonus crece por cada miembro adicional; con el grupo completo de 5 es +25 %.)*

- **Bonus de moneda**: existe y crece con el tamaño del grupo; valores por definir (orientativo: +5 %, +10 %, +15 %, +20 %).
- **Banda (raid)**: agrupación grande para actividades concretas (10, 20, 50 o 100 personas según la actividad). Los tamaños se desbloquean con las temporadas. Sin bonus de experiencia. Reglas propias por definir.

#### Reparto de objetos dentro del grupo

Una vez el sorteo entre jugadores/grupos (3.7) asigna objetos al grupo, se reparten con dos sistemas:

**1. Botín por turnos con prioridad (objetos compartidos)**
- Los objetos se ordenan por prioridad: **equipo** (armas, armaduras) → **materiales de profesión** → **objetos comunes** (ingredientes de cocina, etc.) → **objetos de misión / otros**.
- En ese orden, cada objeto se asigna **al azar** entre los miembros que aún no han recibido nada.
- Quien recibe un objeto queda excluido de los siguientes, para que el botín rote. A la larga todos reciben más o menos lo mismo.

**2. Botín individual (objetos exclusivos)**
- Ciertos objetos especiales (por ejemplo, equipo exclusivo de personaje) se tiran **por separado para cada miembro** con su propia probabilidad (por ejemplo, 40 %).
- Un mismo mob puede dar varias copias: una para cada miembro al que le salga la tirada.

### 3.9 Roles (decidido)

- **Todas las clases y especializaciones pueden hacer daño** y jugar solas, incluidas las de tanque y sanador.
- En grupo, cada especialización es más eficiente en su rol: el tanque aguanta y atrae a los mobs, el sanador cura, el DPS hace daño.
- Habrá zonas pensadas para grupos (por ejemplo, muchos mobs agresivos) donde un tanque y un sanador hacen que subir de nivel sea mucho más rápido.

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

- **Bonus de experiencia**: confirmar la tabla (+10 % con 2 miembros … +25 % con 5).
- **Bonus de moneda** por tamaño de grupo: valores.
- **Moneda dentro del grupo**: ¿se reparte a partes iguales entre los miembros?
- **Botín por turnos**: cuando todos los miembros ya recibieron un objeto y quedan más, ¿se reinicia la rotación?
- **Objetos de misión**: ¿le llegan a cada miembro que tenga la misión (lo habitual), o entran en la rotación?
- **Bandas**: reglas de reparto de experiencia, moneda y botín.
- **Vetas enriquecidas**: ¿las 4–5 recolecciones son por jugador o el total compartido entre todos? ¿La cuenta atrás empieza siempre en el primer golpe?
- **Moneda**: ¿100 plata = 1 oro?
- ¿El **PvP** es libre en todo el mapa (con penalizaciones, estilo Lineage 2) o solo en zonas y modos concretos?
- ¿Qué **profesiones** entran en la Temporada 1 y cuántas puede tener cada personaje?
- ¿Habrá **monturas** desde la Temporada 1?
