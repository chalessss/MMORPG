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

## 2. Precisión y evasión (en estudio)

### 2.1 Propuesta de fórmula

Cada golpe (del jugador o del mob) puede **fallar**:

**Acierto = 95 % + 1 % × (precisión del atacante − evasión del defensor)**, entre un **mínimo del 50 %** y un **máximo del 100 %**.

- Con la misma precisión que la evasión del objetivo se acierta el 95 %; cada punto de diferencia mueve un 1 %.
- Fallan los golpes blancos, las habilidades y cada impacto de las áreas (por separado en cada mob). **Los sangrados no fallan.**
- Para la prueba, los mobs del nivel 20 tienen **20 de precisión y 20 de evasión**; el jugador, sin joyería, 0 de cada una.
- En el simulador está desactivada por defecto (`acierto_base_pct` = 100) hasta decidirla; la prueba se ejecuta con `python3 herramientas/simulador/simular20.py --precision`.

### 2.2 Precisión: cuánto daño se pierde

Caza de uno en uno contra un mob con 20 de evasión (mobs/hora):

| Especialización | Precisión 0 (acierta 75 %) | 10 (85 %) | 20 (95 %) | 30 o más (100 %) | Sin fallos |
|---|---|---|---|---|---|
| Luchador | 68 | 77 | 86 | 90 | 90 |
| Combatiente | 36 | 41 | 46 | 48 | 49 |
| Asesino | 90 | 96 | 101 | 105 | 105 |
| Atacante | 92 | 103 | 116 | 123 | 122 |
| Mago | 95 | 107 | 119 | 126 | 126 |
| Invocador | 46 | 52 | 58 | 61 | 61 |

- La caza cae **en proporción a los fallos**: sin precisión (75 % de acierto) se caza un **20–25 % menos**.
- **Por encima del 100 % de acierto la precisión no sirve** (tope): en este ejemplo, a partir de 25–30 puntos.

### 2.3 Evasión: cuánto daño se evita

Mobs con 20 de precisión. Evasión 0 → recibe el 100 % de los golpes; 20 → 95 %; 30 → 85 %; 40 → 75 %; 60 → 55 %.

Caza de uno en uno (pociones de vida cada 300 mobs; nadie muere en ningún caso):

| Especialización | Evasión 0 | 20 | 30 | 40 | 60 |
|---|---|---|---|---|---|
| Atacante | 219 | 185 | 110 | 41 | 0 |
| Mago | 266 | 247 | 197 | 153 | 66 |
| Luchador, Asesino, Invocador | 0 | 0 | 0 | 0 | 0 |
| Combatiente (mobs/hora) | 46 | 46 | 45 | 44 | 42 |

Conglomerados (mobs/hora · pociones de vida cada 300 mobs):

| Caso | Evasión 0 | 20 | 40 | 60 |
|---|---|---|---|---|
| Luchador, 12 mobs | 170 · 172 | 170 · 142 | 173 · 37 | 172 · 0 |
| Asesino, 6 mobs | 117 · 208 | 118 · 155 | 121 · 16 | 121 · 0 |
| Combatiente, 12 mobs | 224 · 0 | 222 · 0 | 217 · 0 | 212 · 0 |
| Combatiente, 12 élites | muere | muere | muere | muere |

Grupo de 5 con 12 élites (sin control del agro): con evasión 0 el grupo cae 2 veces y el Mago muere 29 veces; con evasión 40 no cae nunca y el Mago muere 20 veces (el Atacante, de 23 a 10).

Lectura:
- La evasión **ahorra pociones y muertes**, sobre todo a los frágiles (Atacante, Mago) y a los cuerpo a cuerpo que cazan en grupo de mobs. Con 40 de evasión el Atacante gasta un 80 % menos de pociones.
- **La evasión perjudica al Combatiente**: si esquiva, no recibe el golpe y **no gana Ira**, así que caza algo más despacio (46 → 42 mobs/hora con 60 de evasión). Habría que decidir si esquivar también le da Ira, o asumir que la evasión no es su estadística.
- Contra élites la evasión ayuda, pero no sustituye al curandero ni al control del agro.

### 2.4 Preguntas abiertas

1. **¿Te sirve la fórmula** (95 % con la misma precisión que evasión, 1 % por punto, entre 50 % y 100 %)?
2. **¿Los hechizos pueden fallar** como los golpes, o los mágicos aciertan siempre (y la evasión solo vale contra físicos)?
3. **Precisión y evasión de los mobs**: ¿suben con su nivel (por ejemplo, 1 por nivel: 20 en el nivel 20) y son más altas en élites y jefes? Un mob de más nivel que el jugador sería más difícil de acertar, lo que frena cazar por encima del nivel (capítulo de mapas).
4. **Combatiente y evasión**: ¿esquivar le da Ira, o la evasión simplemente no es para él?
