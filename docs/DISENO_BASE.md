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

Puntos del mundo donde se obtienen materiales (estilo WoW / MIR4).

| Recurso | Profesión asociada | Ejemplos |
|---|---|---|
| Minerales | Minería | Hierro, plata, gemas |
| Plantas | Herboristería | Hierbas para pociones |
| Madera | Tala | Troncos para armas y construcción |
| Pesca | Pesca | Peces para cocina |
| Pieles / partes de mobs | Desuello | Cuero, colmillos, escamas |

- Cada punto tiene un nivel de profesión mínimo, un tiempo de recolección y un tiempo de reaparición.
- Los materiales alimentan las profesiones de fabricación (herrería, alquimia, cocina, etc.).

### 3.6 Objetos interactivos del mundo

Elementos con los que se puede interactuar y que no son NPCs ni recursos.

- Cofres (botín), puertas y palancas, portales, puntos de resurrección, objetos de misión, carteles o tablones de misiones.

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

- ¿Los recursos son **compartidos** (el primero que llega se los lleva) o **por jugador** (cada uno ve su propio recurso)?
- ¿El **botín** de mobs y jefes es compartido, por grupo o individual?
- ¿El **PvP** es libre en todo el mapa (con penalizaciones, estilo Lineage 2) o solo en zonas y modos concretos?
- ¿Qué **profesiones** entran en la Temporada 1 y cuántas puede tener cada personaje?
- ¿Habrá **monturas** desde la Temporada 1?
