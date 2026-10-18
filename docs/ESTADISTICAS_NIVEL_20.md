# Capítulo de detalle — Estadísticas (parte 2): nivel 20 y clases

Estado: **en curso**. Segunda sesión del capítulo de estadísticas. La primera sesión cerró las estadísticas **previas** a la elección de clase (niveles 1–19, tres perfiles sin clase): ver `docs/RESUMEN_ESTADISTICAS.md` y el detalle en `docs/ESTADISTICAS.md`. Esta sesión cubre las **estadísticas finales de los personajes ya afectados por el cambio de clase en el nivel 20** (primera especialización).

## 1. Punto de partida

### 1.0 Clases de inicio: nombres oficiales (decidido)

- En el nivel 1 el jugador elige **daño mágico** o **daño físico**. Según lo que elija, el personaje sale con una de estas clases de inicio:

| Elección | Clase de inicio (nombre oficial) | Perfil de la parte 1 |
|---|---|---|
| Daño mágico | **Mágica - Rango** | Mágico |
| Daño físico | **Física - Melee** | Físico cuerpo a cuerpo |
| Daño físico | **Física - Rango** | Físico a distancia |

- Los nombres de clase que se usaron al describir los perfiles de inicio (Combatiente, Atacante a distancia, Mago…) eran **ejemplos de la especialización que elegirían después**, no el nombre oficial de la clase de inicio.
- Las estadísticas de estas clases son las de los perfiles cerrados en la parte 1 (reparto, armas, crecimiento y habilidades).
- **Física son dos clases distintas** (decidido): Física - Melee y Física - Rango, cada una con sus propias especializaciones.

### 1.0b Especializaciones del nivel 20 (decidido)

Lista cerrada: son **todas** las especializaciones que habrá en el nivel 20.

| Clase de inicio | Especializaciones del nivel 20 |
|---|---|
| Física - Melee | **Luchador**, **Combatiente**, **Asesino** |
| Física - Rango | **Atacante a distancia** (única opción) |
| Mágica - Rango | **Mago**, **Invocador** |

**Rol, arma y forma de cazar (decidido):**

| Especialización | Rol | Arma | Cómo caza |
|---|---|---|---|
| Luchador | Daño físico cuerpo a cuerpo | Espadas cortas | Mobs de uno en uno |
| Asesino | Daño físico cuerpo a cuerpo | Dagas (**se crean por profesión**) | Mobs de uno en uno |
| Combatiente | Daño físico cuerpo a cuerpo, aguanta | Espadas largas | **En área** (zonas de conglomerados) |
| Atacante a distancia | Daño físico a distancia | Arcos | Mobs de uno en uno |
| Mago | Daño mágico a distancia | Bastón | Mobs de uno en uno |
| Invocador | Daño mágico a distancia, **potencia al grupo** | Varita (**se crea por profesión**) | Mobs de uno en uno |

- Las dos armas de Física - Melee se reparten entre sus especializaciones: la **espada corta** pasa al Luchador y la **espada larga** al Combatiente.
- Dagas y varitas no se consiguen como las demás armas: **se fabrican con una profesión**.
- **Arma inicial (decidido)**: la recompensa de la misión "elige tu especialización" es un objeto propio de la especialización elegida, que solo ella puede usar. Para el Asesino es su **primera daga** y para el Invocador su **primera varita**; las siguientes se fabrican.

### 1.0e Nombres de las etapas (decidido)

| Etapa | Cuándo | Clases |
|---|---|---|
| Clase de inicio | Niveles 1–19 | Mágica - Rango, Física - Melee, Física - Rango |
| **Especialización 1** | Nivel 20 | Luchador, Combatiente, Asesino, Atacante a distancia, Mago, Invocador |
| **Especialización 2** | Temporada 2 (nivel 40 según la hoja) | Dos manos, Espadas duales, Tanque, Daguero, Arquero, Hechicero, Encantador… |
| **Especialización 3** | Temporada 3 (nivel 60 según la hoja) | Lancero, Berserker, Carroñero, Explorador… (~19) |

### 1.0c Transición en el nivel 20: se recalcula todo (decidido)

- Al elegir especialización **se recalculan todas las estadísticas** con el reparto de la especialización, como si el personaje siempre lo hubiera tenido.
- **Cada especialización tiene su propia conversión** de STR, INT y AGI: un mismo punto no da lo mismo a todas. Por ejemplo, la STR da **menos daño físico al Asesino** que al Luchador, pero el Asesino saca **más probabilidad de crítico** de su AGI.
- Se hace un **balance nuevo de las 6 especializaciones** a partir de su reparto base y de esa conversión propia.
- **Mismos puntos, otro reparto (decidido)**: la especialización **no da puntos extra**. En el nivel 20 todas las clases de inicio llevan **370 puntos** de STR + AGI + INT (10 de base y 18 por nivel, contando el arma); al especializarse se **redistribuyen** según el reparto de la especialización (por ejemplo, el Luchador 7/2/1 → 259 STR, 74 AGI, 37 INT).
- La fuerza nueva sale de la **conversión propia** de cada especialización, de sus habilidades y de su arma. Los valores se **reajustan** para ir perfilando a cada una hacia lo que hará en la especialización 2:
  - **Luchador**: un poco más de daño y un poco más de aguante que la clase de inicio.
  - **Combatiente**: el que entra a pegarse a muerte y recibe todo el daño: su STR da **más vida máxima y más resistencias**, a cambio de menos daño por golpe (lo compensa el daño en área).

### 1.0d Balance desde el nivel 20: por rol, no por paridad (decidido)

- **Del 1 al 19 se buscaba paridad**: que todos llegaran al nivel 20 a la vez, sin una clase muy adelantada. **Desde el 20 ya no**: las especializaciones no tienen que quedar en el mismo ritmo de caza.
- El **simulador solo sirve de aproximación**, como referencia de que cada rol cumple su papel:
  - las de **daño** hacen mucho daño;
  - las que **curan** no se quedan en cero de daño;
  - las que **tanquean** hacen un daño medio.
- **Cada rol caza a su manera.** Los tanques irán a **zonas de conglomerados**, con muchos mobs juntos, donde aguantan el daño gracias a la armadura y matan en área. Allí deben sacar **la misma experiencia** que otra especialización matando mobs de uno en uno.
- Ejemplo: si un Invocador intenta pegar a seis mobs a la vez, lo matan en 2–3 segundos; un Combatiente los aguanta y además hace mucho más daño en área.
- Implicación para el capítulo de mapas: cada zona de caza debe prever **mobs agrupados** para las especializaciones que aguantan y pegan en área, además de mobs sueltos.

### 1.1 Cómo llega el personaje al nivel 20

Valores del nivel 19 (ficha vigente: `python3 herramientas/simulador/simular.py --ficha`):

| Clase de inicio | Vida | Maná | Armadura | Defensa | Golpe blanco |
|---|---|---|---|---|---|
| Física - Melee (espada larga / corta) | 4.975 | 920 | 950 | 19,5 % | 1.072 / 922 |
| Física - Rango (arco) | 2.075 | 1.220 | 950 | 7,9 % | 929 |
| Mágica - Rango | 1.575 | 2.990 | 950 | 5,9 % | — |

- Qué da cada punto (común a todos hasta el 19): **STR** +25 vida, +0,2 vida/s, +0,1 % de defensa física y mágica, +1,5 % de daño; **INT** +15 maná, +0,2 maná/s, +2,5 % de daño de habilidades; **AGI** +2 de daño plano por golpe.
- Cuatro habilidades por perfil, en nivel de habilidad 4 desde el nivel 15.
- Caza de 1.000 mobs en el nivel 19: espada larga 823 min, espada corta 765, arco 1.060, mágico 928 (38,5 % de diferencia, intencionada).

### 1.2 Lo que ya está decidido sobre el nivel 20 (de la parte 1)

- Una **misión del entrenador de clase** ofrece las clases del arquetipo (`ESTADISTICAS.md`, 1.7).
- Con la clase llegan: **armas propias**, el **reparto base de la clase**, **muchas más estadísticas visibles**, **4–5 habilidades nuevas** (activas y pasivas), equipo especializado y el contenido de profesiones y desarrollo.
- **Cada clase recibe una pasiva que cambia lo que da cada punto** (valores de ejemplo):
  - **Mágicos**: cada punto de INT vale mucho más (por ejemplo, ×3), sobre todo en daño.
  - **Agilidad**: cada pocos puntos de AGI (por ejemplo, cada 3) suben el crítico, el robo de vida o lo que haga falta para equilibrar.
  - **Luchador / Combatiente**: la STR da más vida y más armadura (por ejemplo, 120 de vida en lugar de 100); la INT solo da maná plano.
  - **Mago** (bastones): más regeneración de maná y más daño de hechizos.
  - **Invocador** (varitas): menos daño base, más regeneración de maná y más potencia de escudos y curaciones.
- **6–8 habilidades activables** por clase, y con ellas se ajusta el coste de maná. Objetivo: **300–1.000 pociones de maná cada 1.000 mobs**, con **menos de 150 de diferencia** entre perfiles.
- **El PvP se balancea desde el nivel 20**, con el triángulo **STR > AGI > INT > STR** (`ESTADISTICAS.md`, 1.3).
- Objetivos de daño por rol (de ejemplo): daño puro un 3–5 % por encima de la media, tanque un 5 % por debajo y curandero un 8 % por debajo (`ESTADISTICAS.md`, 1.5).

### 1.3 Reparto base de las especializaciones (decidido)

Confirmado por el usuario (coincide con la tabla vigente de la hoja, filas 54–60). Todas usan **MP** (maná) como recurso primario y tienen un **recurso secundario** propio (ver 1.5).

| ID | Clase | STR | INT | AGI | Arma (hoja) | Velocidad | Recurso secundario |
|---|---|---|---|---|---|---|---|
| CL_LUC | Luchador | 7 | 1 | 2 | Espada (decidido: espada corta) | 1,0 | Ira (Medidor de Ira) |
| CL_COM | Combatiente | 5 | 1 | 4 | Espada (decidido: espada larga) | 1,0 | Ira (Medidor de Ira) |
| CL_ASE | Asesino | 3 | 1 | 6 | Daga | 1,6 | Energía (Medidor de Energía) |
| CL_ATA | Atacante a distancia | 2 | 2 | 6 | Arco | 1,1 | Foco (Puntos de Foco) |
| CL_MAG | Mago | 1 | 7 | 2 | Bastón | 0,6 | Iluminación (Trance de Iluminación) |
| CL_INV | Invocador | 2 | 5 | 3 | Varita | 1,2 | Iluminación (Esencia de Iluminación) |

La velocidad de la hoja está en golpes relativos; en el simulador se expresa en segundos entre golpe y golpe.

### 1.4 Borrador 1 de la conversión por especialización (por validar)

Primer reparto de los 370 puntos y de lo que da cada punto. Lo que no aparece en la tabla de conversión es igual que en la clase de inicio (STR: 25 vida, 0,2 vida/s, 0,1 % de defensa, 1,5 % de daño; AGI: 2 de daño plano; INT: 15 maná, 0,2 maná/s, 2,5 % de daño de habilidad).

| Especialización | Cambios en la conversión |
|---|---|
| Luchador | STR: **2 % de daño** por punto (en vez de 1,5 %) |
| Combatiente | STR: **40 de vida**, **0,2 % de defensa**, 1 % de daño · AGI: 1,75 de daño plano |
| Asesino | STR: 35 de vida, 1 % de daño · AGI: 1,5 de daño plano, **+0,06 % de crítico** y **+0,25 % de daño crítico** |
| Atacante a distancia | STR: 30 de vida · AGI: **+0,05 % de crítico** y **+0,3 % de daño crítico** |
| Mago | STR: 40 de vida · INT: 20 de maná, 0,3 maná/s, **4,25 % de daño de habilidad** |
| Invocador | STR: 30 de vida · INT: 0,4 maná/s, **1,5 % de daño de habilidad** (su fuerte será potenciar al grupo) |

Resultado en el nivel 20. El daño por segundo es solo de golpes blancos o de la rotación básica del mágico, sin habilidades: sirve para comparar cada especialización con su clase de inicio, no entre melee, rango y mágico.

| | STR | AGI | INT | Vida | Maná | Defensa | Crítico | Daño crítico | Daño/s | vs. clase de inicio |
|---|---|---|---|---|---|---|---|---|---|---|
| Física - Melee, espada corta (ref.) | 205 | 104 | 61 | 5.225 | 965 | 20,5 % | 5 % | +10 % | 717 | — |
| Física - Melee, espada larga (ref.) | 205 | 104 | 61 | 5.225 | 965 | 20,5 % | 5 % | +10 % | 446 | — |
| **Luchador** (espada corta) | 259 | 74 | 37 | 6.575 | 605 | 25,9 % | 5 % | +10 % | 821 | +15 % |
| **Combatiente** (espada larga) | 185 | 148 | 37 | 7.500 | 605 | 37,0 % | 5 % | +10 % | 368 | −17 % (en un solo mob) |
| **Asesino** (daga 20 de daño, 1,0 s) | 111 | 222 | 37 | 3.985 | 605 | 11,1 % | 18,3 % | +65,5 % | 834 | +16 % |
| Física - Rango (ref.) | 83 | 205 | 82 | 2.175 | 1.280 | 8,3 % | 5 % | +10 % | 502 | — |
| **Atacante a distancia** | 74 | 222 | 74 | 2.320 | 1.160 | 7,4 % | 16,1 % | +76,6 % | 568 | +13 % |
| Mágica - Rango (ref.) | 62 | 102 | 206 | 1.650 | 3.140 | 6,2 % | 5 % | +10 % | 1.505 | — |
| **Mago** | 37 | 74 | 259 | 1.580 | 5.230 | 3,7 % | 5 % | +10 % | 1.841 | +22 % |
| **Invocador** | 74 | 111 | 185 | 2.320 | 2.825 | 7,4 % | 5 % | +10 % | 1.082 | −28 % |

- La daga (20 de daño, 1,0 s entre golpes) es provisional.
- Desde el nivel 20 el crítico deja de estar limitado al 5 % y +10 % para las especializaciones de AGI (topes nuevos por definir).
- Los melee bajan de maná (965 → 605) porque su INT baja; dependerán más de su recurso secundario (Ira, Energía).

### 1.5 Recurso secundario (decidido)

- Desde el nivel 20 cada especialización tiene, además del maná, un **recurso secundario** (tabla de 1.3). Del 1 al 19 las clases de inicio solo tienen maná.
- **Función:** el recurso secundario **potencia las habilidades**: aumenta su **efectividad** o su **daño neto**. El maná sigue siendo lo que cuesta lanzar la habilidad.

| Recurso | Especialización | Cómo se consigue | Qué hace |
|---|---|---|---|
| Ira | **Luchador** | Se llena al golpear | Potencia **cualquier habilidad activa** que use |
| Ira | **Combatiente** | Se llena sobre todo **al recibir daño**: cuantos más mobs le pegan, más rápido | Habilita **habilidades exclusivas** que solo se pueden usar si tiene Ira |
| Energía | **Asesino** | **Empieza llena** y se consume al usar habilidades; se regenera, **más rápido cuanta más AGI** | Potencia las habilidades que la gastan |
| Foco | **Atacante a distancia** | **Puntos** que se van habilitando (con los disparos, y más si no se mueve) | Al gastarlos, potencian el disparo y le dan **daño verdadero**: esa habilidad **ignora la reducción de daño de la armadura** |
| Iluminación (Trance) | **Mago** | Se carga con los hechizos | Entra en **trance** cada **50–60 s** en combates largos, durante **10 s como máximo**: hechizos más fuertes |
| Iluminación (Esencia) | **Invocador** | Se carga con cada hechizo y cada apoyo | Escudos, curas y potenciaciones al grupo más fuertes |

**Por definir:** cuánto potencia cada recurso (porcentajes), el tamaño de cada medidor y el número máximo de puntos de Foco. Se calibrará en el simulador junto con las habilidades de cada especialización.

## 2. Trabajo de esta sesión

1. ~~**Especializaciones por clase de inicio**~~: decidido (1.0b).
2. ~~**Transición en el nivel 20**~~: se recalcula todo (1.0c). Falta fijar el crecimiento por nivel de cada especialización.
3. **Pasiva de clase**: qué da cada punto de STR, INT y AGI en cada una de las 6 clases.
4. **Habilidades de clase** (6–8 activables) en lo que afecta a las estadísticas: daño, enfriamiento y coste de maná.
5. **Armas de clase**: daño y velocidad de daga, varita y espadas de clase.
6. ~~**Recursos secundarios**~~: mecánica decidida (1.5). Faltan los valores.
7. **Estadísticas visibles nuevas** desde el nivel 20 (las neutrales de la hoja que se muestran y empiezan a contar).
8. **Simulación de las 6 clases en el nivel 20**: caza de 1.000 mobs y jefe de 20 minutos, con el objetivo de pociones de maná.
9. **Primer balance PvP** con el triángulo STR > AGI > INT > STR.
10. **Ficha cerrada del nivel 20** por clase.

## 3. Preguntas abiertas

- **Flecos de la parte 1** que conviene cerrar aquí: validar los valores por punto de INT y AGI, daño de las armas por tramos y pociones que curen según el nivel.
