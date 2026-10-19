# Resumen ejecutivo — Estadísticas

Vista rápida de cómo quedaron las estadísticas tras la primera sesión del capítulo. El detalle, las pruebas y el porqué de cada decisión están en `docs/ESTADISTICAS.md`; los números se pueden reproducir con el simulador de `herramientas/simulador/`.

## Estado

- **Niveles 1–19 (sin clase): cerrados**, salvo los flecos de la última sección.
- **Nivel 20** (especialización 1 y estadísticas finales con ella): **cerrado** en `docs/ESTADISTICAS_NIVEL_20.md` (ficha en la sección 2). Resumen al final de este archivo.

## Principios decididos

- **Del 1 al 19 solo importa el PvE.** El PvP y el triángulo **STR > AGI > INT > STR** se balancean desde el nivel 20.
- **Paridad de caza al inicio, diferencias después**: en el nivel 1 los tres perfiles cazan al mismo ritmo; luego se van diferenciando a propósito (el mágico hace más daño pero es frágil; el guerrero aguanta). En grupo se nota más el trabajo en equipo.
- **Valores siempre enteros** (daño, vida, maná, estadísticas). La regeneración se muestra cada 5 s. Tiempos y porcentajes pueden llevar decimales.
- **Las estadísticas neutrales** (evasión, precisión, daño a jefes…) vendrán de joyería y encantamientos, no de STR, INT o AGI.

## Perfiles de inicio (niveles 1–19)

Del 1 al 19 solo hay tres **clases de inicio**: en el nivel 1 se elige daño mágico (**Mágica - Rango**) o daño físico (**Física - Melee** o **Física - Rango**). La especialización se elige en el nivel 20 con una misión del entrenador.

| Perfil | Reparto base (STR / AGI / INT) | Arma | Segundos entre golpes | Daño del arma | Crecimiento por nivel (= bono del arma de nivel 1) |
|---|---|---|---|---|---|
| Física - Melee | 5 / 4 / 1 | Espada larga o espada corta | 2,6 / 1,4 | 75 / 37 | +10 STR, +5 AGI, +3 INT |
| Física - Rango | 3 / 5 / 2 | Arco | 2,0 | 35 | +4 STR, +10 AGI, +4 INT |
| Mágica - Rango | 2 / 2 / 6 | Bastón (nunca pega con él) | — | — | +3 STR, +5 AGI, +10 INT |

- El arma de nivel 1 da exactamente lo que se gana en cada nivel (easter egg).
- Las espadas pegan más fuerte para compensar que el cuerpo a cuerpo camina entre mobs.

## Qué da cada punto

| Estadística | Por punto | Estado |
|---|---|---|
| **STR** | +25 vida · +0,2 vida/s · +0,1 % defensa **física** (la mágica la da la joyería) · +1,5 % de daño en todos los golpes | Validado |
| **INT** | +15 maná · +0,2 maná/s · +2,5 % de daño de habilidades | Validado |
| **AGI** | +2 de daño plano en cada golpe | Validado |
| **Base** | 100 vida · 0,5 vida/s · 50 maná · 0,5 maná/s | — |

**Fórmula del golpe**: (daño del arma o de la habilidad + daño plano de AGI) × (1 + % de STR) × (1 + % de INT, solo habilidades) × crítico, redondeado a entero.

## Combate

- **Crítico** (no depende de AGI en este tramo): probabilidad 1 % + 0,2 % por nivel (tope 5 %); un crítico suma +2 % + 0,4 % por nivel (tope +10 %).
- **Armadura**: 50 por nivel (50 en el 1, 500 en el 10, 1.000 en el 20). Cada 100 restan 1 de daño a cada golpe recibido, de cualquier fuente.
- **Pociones**: +100 de vida o de maná, 20 s de enfriamiento. Los mágicos reciben pociones extra en las misiones del tutorial.
- **Descansos**: se para a recuperarse si no queda vida para otro mob. Que el mágico descanse es intencionado.

## Habilidades (4 por perfil)

| Perfil | Nivel 1 | Nivel 1 | Nivel 10 | Nivel 10 |
|---|---|---|---|---|
| Cuerpo a cuerpo | **Golpe doble**: 150 % + 75 % del arma, 20 s | **Golpe al suelo**: 300 % del arma, 3 s de animación, 40 s | **Golpe sangriento**: 300 % del arma, cuesta 1/6 de la vida máxima, 10 s | **Pasiva**: robo de vida 5 % y +0,1 vida/s por punto de STR |
| Distancia | **Disparo cargado**: 200 % del arma, 2 s de carga, 12 s | **Ráfaga triple**: 3 × 120 % del arma, 40 s | **Disparo potente**: 350 % del arma, 3 s de lanzamiento, 15 s | **Pasiva**: robo de vida 0,3 % y +3 % de crítico |
| Mágico | **Hechizo fuerte**: 97 de daño, 2 s, 8 s | **Hechizo débil**: 32 de daño, 2 s, se lanza siempre | **Escudo de maná**: absorbe el 20 % de la vida máxima durante 8 s, 20 s | **Celeridad**: hechizos un 2 % más rápidos |

- **Coste de maná** en % del maná máximo (crece con el personaje).
- **Niveles de habilidad** con libros: nivel 2 en el nivel de personaje 5, nivel 3 en el 10 y nivel 4 en el 15. Cada uno suma **+25 % de coste y +2 % de daño sobre el anterior** (nivel 4: +95 % de coste, +6,1 % de daño).

## Mobs

- Dos tipos de daño (físico o mágico) y dos distancias. Ciclo: **básico, básico, potenciado (×2)**.
- Vida: 420 en el nivel 1 y **+30 % por nivel** (47.231 en el 19). Daño básico: 6 en el nivel 1 y 53 en el 19.
- En las simulaciones salen en rotación: cuerpo a cuerpo físico → a distancia mágico → cuerpo a cuerpo mágico → a distancia físico.

## Valores clave por nivel

| Nivel | Perfil | Vida | Maná | Armadura | Defensa física | Golpe blanco |
|---|---|---|---|---|---|---|
| 1 | Espada larga / corta | 475 | 110 | 50 | 1,5 % | 114 / 67 |
| 1 | Arco | 275 | 140 | 50 | 0,7 % | 72 |
| 1 | Mágico | 225 | 290 | 50 | 0,5 % | — |
| 10 | Espada larga / corta | 2.725 | 515 | 500 | 10,5 % | 471 / 373 |
| 10 | Arco | 1.175 | 680 | 500 | 4,3 % | 403 |
| 10 | Mágico | 900 | 1.640 | 500 | 3,2 % | — |
| 19 | Espada larga / corta | 4.975 | 920 | 950 | 19,5 % | 1.072 / 922 |
| 19 | Arco | 2.075 | 1.220 | 950 | 7,9 % | 929 |
| 19 | Mágico | 1.575 | 2.990 | 950 | 5,9 % | — |

Ficha completa nivel a nivel: `python3 herramientas/simulador/simular.py --ficha`.

## Resultado de la simulación (1.000 mobs por nivel, caza real)

| Nivel | Espada larga | Espada corta | Arco | Mágico | Diferencia |
|---|---|---|---|---|---|
| 1 | 165 min | 166 min | 170 min · 129 poc. | 170 min · 181 poc. | 2,9 % |
| 5 | 200 | 175 | 171 · 393 poc. | 174 · 297 poc. | 16,8 % |
| 10 | 248 · 284 poc. | 240 · 296 poc. | 297 · 295 poc. | 263 | 23,8 % |
| 15 | 450 | 419 | 571 · 539 poc. | 524 · 18 poc. | 36,3 % |
| 19 | 823 | 765 | 1.060 · 1.182 poc. | 928 | 38,5 % |

(Pociones de vida y maná sumadas. Nadie muere.) El mágico es el más rápido hasta el nivel 10 y luego para más a recuperar maná; el guerrero aguanta sin pociones salvo en los niveles 10–14; el arco es el que más pociones gasta.

## Pendiente

**Para cerrar del todo el 1–19:**
1. Validar los valores por punto de **INT** y **AGI**.
2. **Daño de las armas por tramos** (bronce → cobre → plata).
3. **Pociones por nivel** (ahora curan siempre 100).

**Nivel 20 (próxima sesión):**
- Pasivas de clase que cambian lo que da cada punto: INT ×3 para los mágicos; cada pocos puntos de AGI, crítico o robo de vida; STR con más vida y armadura para los que aguantan.
- **6–8 habilidades activables** por clase y ajuste del coste de maná (objetivo: 300–1.000 pociones de maná cada 1.000 mobs en el nivel máximo, con menos de 150 de diferencia entre perfiles).

**Más adelante en el capítulo:** neutrales, topes y rendimientos decrecientes, puntuación de poder e implementación en GAS.

## Parte 2 — Nivel 20: especialización 1 (cerrada)

Detalle: `docs/ESTADISTICAS_NIVEL_20.md` · simulador: `herramientas/simulador/simular20.py`.

- **Clases de inicio** (1–19): Mágica - Rango, Física - Melee y Física - Rango. En el nivel 20, la **especialización 1**: Luchador, Combatiente y Asesino (melee), Atacante a distancia (rango), Mago e Invocador (mágica).
- **Se recalcula todo** con el reparto de la especialización y **sin puntos extra** (370 puntos en el nivel 20). Cada especialización tiene su **conversión propia** (pasiva de especialización) y una **pasiva de arma**.
- **8 habilidades** por especialización: 2 de daño, una pasiva y una activa de la clase de inicio, más pasiva de especialización, pasiva de arma, **área** e **individual**. Todas las áreas tienen enfriamiento salvo la Lluvia de fuego del Mago.
- **Recurso secundario** que potencia las habilidades: Ira (Luchador, Combatiente), Energía (Asesino), Foco (Atacante), Trance y Esencia de Iluminación (Mago, Invocador).
- **Balance por rol**, no por paridad: las de daño mandan contra un objetivo, el Combatiente aguanta conglomerados (hasta 12 mobs) y el Mago es el que más daño hace en área en grupo; el Invocador es el único curandero.
- **Maná**: Mago e Invocador pagan sus hechizos con un valor exacto que sube con el nivel de la habilidad (hasta el 10); los físicos, un % del maná máximo.
- **Agro**: el Combatiente provoca con el Embate (7 s cada 10 s) y lo alterna con Fisura; sin amenaza extra en la Temporada 1: los jugadores tienen que aprender a controlar el agro.

| Especialización | Vida | Maná | Defensa física | Crítico | Jefe (daño/s) | Mobs/hora de uno en uno |
|---|---|---|---|---|---|---|
| Luchador | 6.575 | 605 | 25,9 % | 4,8 % | 1.517 | 90 |
| Combatiente | 7.500 | 605 | 42,0 % | 4,8 % | 637 | 49 (239 con 12 mobs) |
| Asesino | 3.985 | 605 | 11,1 % | 23,1 % | 1.900 | 105 |
| Atacante | 2.320 | 1.160 | 7,4 % | 18,9 % | 2.243 | 122 |
| Mago | 1.580 | 5.230 | 3,7 % | 4,8 % | 2.367 | 126 |
| Invocador | 2.320 | 2.825 | 7,4 % | 4,8 % | 746 | 61 |

**Pendiente**: estadísticas visibles nuevas del nivel 20, primer balance PvP, cantidades de curas, escudos, pociones mejoradas y recursos secundarios; después, neutrales, topes, poder e implementación en GAS.

## Parte 3 — Neutrales (en curso)

Detalle: `docs/ESTADISTICAS_NEUTRALES.md`.

- **Temporada 1**: evasión, precisión, defensa física, defensa mágica, daño a monstruos, experiencia de caza, velocidad de recolección y CDR. **Temporada 2**: debilitación y su resistencia, daño y resistencia PvP, efecto de pociones, % de caída, % de caída con suerte y daño a jefes.
- **Lineales hasta la Temporada 3**; allí llegará un punto óptimo (rendimientos decrecientes).
- **Precisión y evasión**: la evasión solo vale contra golpes físicos (los hechizos aciertan siempre); acierto por escalones de 5 puntos (5 o más por encima: 100 %; −10 % por cada 5 por debajo, hasta 0 %); los mobs tienen precisión y evasión igual a su nivel.
- **Defensa física y mágica**: puntos del equipo, 10.000 = 50 % de reducción (lineal), que se suman a la de la STR. **La STR solo da defensa física**; la mágica la dan collares, brazaletes y demás joyería.
- **Daño a monstruos**: % extra contra monstruos (no jefes); en la Temporada 1 se llega a un 15 % con equipo normal y como máximo a un 20 % con objetos o encantamientos concretos. Más adelante se compensa con la vida de los mobs.
- **Potenciación de caza** (el "vigor" de MIR4): +100 % de experiencia por tiempo en combate, hasta 8 horas acumuladas; se recarga desconectado (1 a 1), recolectando o fabricando (el tiempo base de cada acción). Sin píldoras. Las demás fuentes de experiencia (joyería, códice…) suman siempre.
- **Velocidad de recolección**: 10 s por recogida en el nivel 1; general para todos los recursos; minería +25 %, herboristería +25 % y encantamientos raros; cada 100 % reduce el tiempo a la mitad (5 s, 2,5 s, 1,25 s…), nunca llega a 0. Alerta automática al staff si alguien supera el 200 % (Temporada 1), con el informe completo del personaje.
- **Velocidad de fabricación**: a 100 puntos de una profesión de fabricación, el tiempo de sus recetas se reduce a la mitad (10 s → 5 s). Es el máximo; si alguien fabrica en 4,9 s o menos, alerta automática al equipo de seguridad.
- **CDR**: resta un % a los enfriamientos (no al Embate, para mantener el hueco de agro); en la Temporada 1, 10 % con equipo normal y 15 % como máximo; tope absoluto 40 %.
