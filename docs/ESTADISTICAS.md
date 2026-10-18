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

**Qué da cada estadística principal** (pestaña principal, columnas W–Z):

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

Hay además una columna con anotaciones sin explicar: `AGI>INT`, `INT>STR`, `STR>AGI`.

**Estadísticas base de las clases de la Temporada 1** (pestaña "Habilidades 2.0"; suman 10 puntos de principales cada una):

| Clase | STR | INT | AGI | Evasión | Precisión |
|---|---|---|---|---|---|
| Luchador | 7 | 1 | 2 | 1 | 2 |
| Combatiente | 6 | 1 | 3 | 1 | 2 |
| Asesino | 3 | 1 | 6 | 1 | 2 |
| Atacante a distancia | 2 | 2 | 6 | — | — |
| Mago | 1 | 6 | 2 | — | — |
| Invocador | 2 | 5 | 3 | — | — |

**Velocidad de ataque por arma** (pestaña "Armas"): lanza 0,9 · espada 1,0 · espada corta 1,3 · daga 1,6 · ballesta 0,8 · arco 1,1 · bastón 0,6 · libro 0,9 · varita 1,2.

**Habilidades de ejemplo** con daño base, enfriamiento, tiempo de lanzamiento y alcance (Golpe al suelo, Golpe de mango, Inmolar…): se tratarán en el capítulo de personajes y habilidades, pero las fórmulas de este capítulo deben encajar con ellas.

## 2. Estructura propuesta del capítulo

1. **Lista cerrada de estadísticas** y a qué categoría pertenece cada una (principal, derivada, neutral, PvP, utilidad).
2. **Crecimiento por nivel**: cuántos puntos de principales da cada nivel y si el reparto es fijo por clase o en parte libre.
3. **Conversión principales → derivadas**: cuánto da cada punto de STR/INT/AGI.
4. **Eficiencia por clase**: tabla que dice cuánto aprovecha cada clase cada estadística ("todo suma, pero no igual").
5. **Fórmulas de combate**: golpe/fallo (precisión vs. evasión), crítico, daño contra defensa, multiplicadores (monstruos, jefes, PvP), debilitación.
6. **Topes y rendimientos decrecientes** para las estadísticas porcentuales (crítico, CDR, evasión…).
7. **Tabla de valores por fuente**: qué estadísticas y cuánto da cada fuente (equipo por calidad, desarrollo, encantamiento, códice, cocina…).
8. **Puntuación de poder**.
9. **Implementación**: AttributeSets de GAS y DataTables.

## 3. Preguntas abiertas

Ver la conversación de la sesión; se trasladarán aquí las respuestas como decisiones.
