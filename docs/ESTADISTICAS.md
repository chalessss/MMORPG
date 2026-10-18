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

Hay además una columna con las anotaciones `AGI>INT`, `INT>STR`, `STR>AGI` (ver 1.3).

**Estadísticas base de las clases de la Temporada 1** — tabla corregida (filas 54–60 de la pestaña principal; la tabla de las filas 45–51 y la de "Habilidades 2.0" son versiones anteriores y **no se usan**). Cada clase suma 10 puntos:

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

En las filas 62–70 hay otro borrador de reparto, con columnas Físico / Mágico:

| Estadística | Da | Y además | Físico | Mágico |
|---|---|---|---|---|
| STR | Daño base | Defensa física | 6 | 3 |
| AGI | Crítico | Evasión | 6 | 5 |
| INT | Daño de habilidad | Defensa mágica | 3 | 7 |
| HP | Vida máxima | Regeneración de vida | 7 | 6 |
| MP | Maná máximo | Regeneración de maná | 3 | 4 |
| WD (arma) | Daño de arma | Velocidad de ataque | 7 | 3 |
| ARM (armadura) | Absorción de daño | Reducción de daño de mobs | 6 | 2 |

**Velocidad de ataque por arma** (pestaña "Armas"): lanza 0,9 · espada 1,0 · espada corta 1,3 · daga 1,6 · ballesta 0,8 · arco 1,1 · bastón 0,6 · libro 0,9 · varita 1,2.

**Habilidades de ejemplo** con daño base, enfriamiento, tiempo de lanzamiento y alcance (Golpe al suelo, Golpe de mango, Inmolar…): se tratarán en el capítulo de personajes y habilidades, pero las fórmulas de este capítulo deben encajar con ellas.

### 1.3 Triángulo de ventajas (decidido)

Las estadísticas principales forman un sistema de **piedra, papel o tijera**: **STR > AGI > INT > STR**.

- Cada personaje tiene un tipo que le gana a otro y otro tipo que le gana a él. Nadie le gana a todos.
- Con condiciones parecidas, un personaje **no debe poder ganarle matemáticamente a su counter** y **debe ganarle con facilidad al tipo débil**.
- El tipo depende de la clase y de sus estadísticas base. En la Temporada 1: STR = Luchador y Combatiente; AGI = Asesino y Atacante a distancia; INT = Mago e Invocador.
- **Todas las clases y especializaciones** (hasta las ~19 finales) se encasillarán en el triángulo para saber contra quién son buenas y contra quién son malas.

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
