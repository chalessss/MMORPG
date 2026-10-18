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
- **6–8 habilidades activables** por clase (sustituido por la estructura de 8 habilidades de 1.6), y con ellas se ajusta el coste de maná. Objetivo: **300–1.000 pociones de maná cada 1.000 mobs**, con **menos de 150 de diferencia** entre perfiles.
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

### 1.6 Estructura de habilidades (decidido)

Todas las especializaciones tienen **8 habilidades** con la misma distribución:

| # | Tipo | Cuándo | Qué es |
|---|---|---|---|
| 1 | General de daño | Clase de inicio (1–19) | Ya configurada en la parte 1 |
| 2 | General de daño | Clase de inicio (1–19) | Ya configurada en la parte 1 |
| 3 | Pasiva | Clase de inicio (1–19) | Ya configurada en la parte 1 |
| 4 | Activa | Clase de inicio (1–19) | Ya configurada en la parte 1 |
| 5 | **Pasiva de especialización** | Especialización (nivel 20) | Indica la **tasa de conversión** de STR, AGI e INT: cuánto suma cada punto a las demás estadísticas secundarias (borrador en 1.4) |
| 6 | **Pasiva de arma** | Especialización (nivel 20) | Da daño o estadísticas **extra por usar el tipo de arma correcto** de la especialización |
| 7 | **Área** | Especialización (nivel 20) | Un hechizo o golpe **fuerte de daño en área** |
| 8 | **Individual** | Especialización (nivel 20) | Un hechizo o golpe **fuerte de daño a un solo objetivo** |

**Lista de habilidades por especialización (decidido, nombres del usuario):**

| # | Tipo | Luchador | Combatiente | Asesino | Atacante | Mago | Invocador |
|---|---|---|---|---|---|---|---|
| 1 | General de daño | Golpe doble | Golpe doble | Golpe doble | Disparo cargado | Lanza de hielo | Lanza de hielo |
| 2 | General de daño | Golpe al suelo | Golpe al suelo | Golpe bajo | Ráfaga triple | Bola de fuego | Bola de fuego |
| 3 | Pasiva | Sed de sangre | Sed de sangre | Sed de sangre | Ojo de Halcón | Celeridad | Celeridad |
| 4 | Activa | Golpe sangriento | Golpe sangriento | Golpe sangriento | Disparo potente | Escudo de maná | Escudo de maná |
| 5 | Pasiva de especialización | Afinidad con la fuerza | Afinidad con la fuerza | Afinidad con la agilidad | Afinidad con la agilidad | Afinidad con el intelecto | Afinidad con el intelecto |
| 6 | Pasiva de arma | Golpes más rápidos con espadas cortas | Más armadura y defensa con espadas largas | Más probabilidad de crítico | Más daño a distancia y más alcance | Más daño de hechizos y regeneración de maná | Más potencia de escudos, curas y apoyos al grupo; más regeneración de maná por punto de INT; +50 % de daño contra monstruos (no jefes) |
| 7 | Área | Torbellino | Fisura | Lluvia de cuchillas | Lluvia de flechas | Lluvia de fuego | Lluvia de estrellas |
| 8 | Individual | Ejecutar | Embate | Desgarro | Disparo certero | Fuego de alma | Restauración |

- Las habilidades 1–4 son las de la clase de inicio (parte 1) con **nombres nuevos**: la pasiva "Robo de vida" de Física - Melee pasa a llamarse **Sed de sangre** y la de Física - Rango **Ojo de Halcón**; el hechizo fuerte y el débil de Mágica - Rango pasan a ser **Bola de fuego** (el fuerte: más tiempo de preparación y lanzamiento) y **Lanza de hielo** (el débil: ligera, se lanza siempre). El Asesino cambia el Golpe al suelo por el **Golpe bajo**.
- La pasiva de arma de cada especialización es la propuesta aceptada.

Con esta estructura cada especialización tiene **5 habilidades que se activan** (1, 2, 4, 7 y 8) y 3 pasivas; con ellas se ajusta el coste de maná del nivel 20.

**Habilidad de área (decidido):**
- **Todas** las especializaciones tienen una habilidad de daño en área.
- **Todas llevan enfriamiento** (10–15 s o algo más) y no se pueden encadenar, **salvo la Lluvia de fuego del Mago**: es la única clase que puede dedicarse a lanzar su área sin parar para hacer muchísimo daño (limitada solo por el maná).
- **Robo de vida en área**: cuenta en cada mob golpeado. Si un Combatiente (con curanderos y magos) junta 15–20 mobs y eso le da aguante, está bien. Las habilidades que no deben escalar así lo llevan reducido: la **Lluvia de cuchillas roba vida al 50 %** (lo indica en su descripción).
- El **Combatiente escala mejor en área** que el resto de físicos (menos enfriamiento o más daño), y su ventaja es que **aguanta** rodeado de mobs.
- Los **magos escalan tanto en daño** que, contra un grupo de 10–15 mobs, harán **más daño en área que el Combatiente**; el Combatiente no debe llegar a superarlos en daño.

**Habilidades concretas ya definidas:**

| Especialización | Habilidad | Detalle |
|---|---|---|
| Combatiente | 7 · Área: **Fisura** | **Solo se puede usar con Ira**; consume poca Ira, pero la necesita |
| Luchador | 8 · Individual: **Ejecutar** | Golpe de remate (encaja con su futuro de daño neto a doble espada en la especialización 3). Cuando al objetivo le queda **poca vida (%)**: **la mitad de enfriamiento**, **más daño** y **no pide Ira**. Pensada para usarla sin parar en el tramo final: contra un jefe dispara el daño en su última parte; a un mob pequeño lo mata de un golpe |
| Combatiente | 8 · Individual: **Embate** | Carga con el arma a dos manos que **empuja al enemigo hacia delante**. Golpe muy fuerte con **enfriamiento largo**; **consume toda la Ira** que tenga en ese momento para hacer daño extra (encaja con su futuro de tanque: Tanque, Paladín…) |
| Invocador | 8 · Individual: **Restauración** | **Cura**, no daño: el Invocador es **el único curandero** del equipo. Lanzada sobre un aliado le cura la cantidad completa y **el Invocador se cura además una parte** (por ejemplo, 500 al aliado y 100–200 a sí mismo). Si el Invocador tiene la vida llena, esa parte va al **siguiente aliado más débil** |
| Invocador | 4 · Activa: **Escudo de maná** | Se lo puede poner **a un aliado**: el aliado recibe el escudo al 100 % y el Invocador **un 20–30 %** de ese escudo |
| Asesino | 1 · Daño | Mantiene el **Golpe doble** |
| Asesino | 2 · Daño | **Golpe bajo** en lugar del Golpe al suelo (un daguero no salta a golpear el suelo) |
| Asesino | 7 · Área: **Lluvia de cuchillas** (antes "Danza de cuchillos") | Lanza cuchillos **en círculo a su alrededor** (no en cono ni delante). Daño **no muy alto**; se puede lanzar **varias veces seguidas gastando Energía**, y **solo con Energía**: sin ella pega golpes normales |

Siguiente paso: **parametrizar el daño**, el enfriamiento y el coste de cada habilidad. Las cantidades de cura y escudo del Invocador se fijarán más adelante, al hablar de cómo se mejoran las habilidades.

### 1.7 Daño de las habilidades 7 y 8 (decidido, con los ajustes del usuario)

Parámetros de daño cerrados para la simulación (individual, en grupo y contra jefe). Mismo criterio que en la parte 1: las físicas en **% del daño del arma**, las mágicas en **puntos** (antes de multiplicar por las estadísticas). Referencias de la parte 1: Golpe doble 225 % cada 20 s, Golpe al suelo 300 % cada 40 s, Disparo potente 350 % cada 15 s, Bola de fuego 97 cada 8 s, Lanza de hielo 32. El coste de maná se calibrará en el simulador.

| Especialización | Habilidad | Daño | Enfriamiento | Lanzamiento | Recurso |
|---|---|---|---|---|---|
| Luchador | Torbellino (área, a su alrededor) | 150 % del arma a cada mob | 15 s | — | Potenciada por la Ira |
| Luchador | Ejecutar | 250 %; con el objetivo **por debajo del 20 % de vida**: **500 %** | 12 s; **6 s** en el remate | — | En el remate no pide Ira |
| Combatiente | Fisura (área) | 200 % del arma a cada mob | **10 s** | — | Cuesta **15 de Ira** |
| Combatiente | Embate (carga y empuje) | 400 % + **2 % por punto de Ira** gastado (Ira llena: 600 %) | 30 s | — | Gasta **toda la Ira** |
| Asesino | Lluvia de cuchillas (círculo a su alrededor) | 80 % del arma a cada mob; **roba vida solo al 50 %** | **10 s** | — | **25 de Energía** por uso |
| Asesino | Desgarro (remate) | 350 % + sangrado en 6 s según la Energía gastada: **≥ 70 % → 100 %**, **40–70 % → 70 %**, **< 40 % → 50 %** | 12 s | — | Gasta **el 100 % de la Energía** que tenga |
| Atacante | Lluvia de flechas (zona) | 120 % del arma por segundo durante 4 s a cada mob | 25 s | **No le interrumpe**: la lanza y sigue disparando a su objetivo mientras caen las flechas | — |
| Atacante | Disparo certero | 400 % | 15 s | 2 s | Gasta el **Foco**: +10 % por punto y **daño verdadero** |
| Mago | Lluvia de fuego (zona) | **Canalizada**: se queda quieto invocándola; cae **un impacto por segundo** de 60 a cada mob, durante 5 s (300) | **Sin enfriamiento**: el Mago es el único que puede encadenar su área | 5 s canalizando | — |
| Mago | Fuego de alma | 250 | 15 s | 3 s | Más fuerte durante el Trance |
| Invocador | Lluvia de estrellas (zona) | **Se lanza como la Lluvia de flechas**: 1 s de lanzamiento y **no interrumpe**; las estrellas caen durante **7 s** (14 estrellas, 2 por segundo) mientras el Invocador cura, escuda o sigue atacando: un **daño constante (dot)**, no una ráfaga. Caen **más seguidas** que la lluvia del mago y golpean a **todos** los mobs de la zona, sean 10 o 20, con **daño bajo** para no hacer demasiado daño en área (20 por estrella). Contra un solo objetivo, **todas las estrellas le caen a él**; con 6, 8 o 10 mobs, **a todos a la vez**, así que rinde sobre todo en grupos grandes. A **todos los aliados** de la zona les pone un **escudo** igual al daño de una estrella | 20 s | 1 s | — |
| Invocador | Restauración (cura) | Cura el **30 % de la vida máxima**. Lanzada sobre un aliado: el aliado recupera el 30 % y el Invocador **el 15 %** si le falta vida; si no, ese 15 % va a otro aliado al que le falte | — | — | Potenciada por la Esencia |

### 1.8 Simulación del nivel 20 (aproximación)

Simulador: `python3 herramientas/simulador/simular20.py` (ficha: `--ficha`), con los datos en `herramientas/simulador/datos/nivel20/`. Mob del nivel 20: 61.400 de vida y 59 de daño por golpe básico. Cada prueba son 300 mobs; en los conglomerados **todos los mobs del grupo pegan a la vez** y todos entran en las habilidades de área. En las pruebas 1 y 2 cada especialización caza **sola**; la 3 imita el grupo con mobs que no le pegan (el tanque los aguanta).

**Pociones mejoradas (decidido):** al llegar al nivel 20 se desbloquean pociones mejoradas que recuperan más (por ejemplo, 400 de maná en vez de 100); los valores se fijarán más adelante. En la simulación: 400 de vida o de maná, 20 s de enfriamiento; se bebe maná al bajar de la mitad.

**Supuestos de la simulación** (por validar):
- Las habilidades de área físicas aplican su % al golpe entero (arma + daño plano de la AGI); los impactos de las lluvias mágicas (Lluvia de fuego, Lluvia de estrellas) no suman el daño plano de la AGI en cada impacto.
- Ajustes: el Invocador saca 1 de daño plano por punto de AGI (en vez de 2); Lluvia de fuego cuesta el 6 % del maná y Fuego de alma el 4 %; el Golpe sangriento solo se usa si deja más de la mitad de la vida.
- Pasivas de arma: Luchador −10 % de tiempo entre golpes; Combatiente +5 % de defensa y +500 de armadura; Asesino +5 % de crítico; Atacante +10 % de daño; Mago +10 % de daño de hechizos y +20 % de regeneración de maná; Invocador +20 % de curas y escudos, **+0,2 de maná por segundo por punto de INT** (decidido, ver 1.9) y **+50 % de daño contra monstruos, no contra jefes** (decidido, ver 1.9).
- Los topes de crítico suben al 50 % de probabilidad y +150 % de daño desde el nivel 20 (provisional).

**Ficha del nivel 20:**

| Especialización | STR | AGI | INT | Vida | Maná | Defensa | Armadura | Crítico | Daño crítico |
|---|---|---|---|---|---|---|---|---|---|
| Luchador | 259 | 74 | 37 | 6.575 | 605 | 25,9 % | 1.000 | 4,8 % | +9,6 % |
| Combatiente | 185 | 148 | 37 | 7.500 | 605 | 42,0 % | 1.500 | 4,8 % | +9,6 % |
| Asesino | 111 | 222 | 37 | 3.985 | 605 | 11,1 % | 1.000 | 23,1 % | +65,1 % |
| Atacante a distancia | 74 | 222 | 74 | 2.320 | 1.160 | 7,4 % | 1.000 | 18,9 % | +76,2 % |
| Mago | 37 | 74 | 259 | 1.580 | 5.230 | 3,7 % | 1.000 | 4,8 % | +9,6 % |
| Invocador | 74 | 111 | 185 | 2.320 | 2.825 | 7,4 % | 1.000 | 4,8 % | +9,6 % |

**Resultados (simulación 5: Lluvia de estrellas de 7 s sin interrumpir; maná de Mago e Invocador en valor exacto y pasiva de arma del Invocador, ver 1.9):**

| Especialización | Jefe (daño/s) | Jefe en remate (< 20 %) | Mobs/hora de uno en uno | Grupos de 6 | Grupos de 12 | En grupo, 12 mobs que no le pegan |
|---|---|---|---|---|---|---|
| Luchador | 1.517 | **1.787** (+18 %) | 90 | 127 | 179 | 181 |
| Combatiente | 637 (sin Ira: el jefe no le pega en la prueba) | 637 | 49 | **131** | **235** | — (es quien recibe) |
| Asesino | 1.900 | 1.900 | 105 | 124 | muere | 144 |
| Atacante a distancia | 2.243 | 2.243 | **122** | muere | muere | 417 |
| Mago | **2.367** | 2.367 | **126** | muere | muere | **800** |
| Invocador | 746 | 746 | 61 | muere | muere | 130 |

Lectura:
- **Contra un objetivo** mandan las de daño (Mago y Atacante, las que más contra el jefe). El Combatiente hace un daño medio y el Invocador, el más bajo, sin quedarse en cero.
- **Solos en conglomerados**: el Combatiente es el que mejor caza con 12 mobs encima; el Luchador también aguanta gracias al robo de vida en área del Torbellino; el Asesino aguanta 6 pero no 12 (su Lluvia de cuchillas roba al 50 %); los de distancia mueren en cuanto les pegan 6.
- **En grupo**, con alguien que aguante los golpes, el **Mago es con diferencia el que más daño hace en área** (800 mobs/hora, 3,4 veces el Combatiente), como se buscaba.
- **El Mago casi no bebía pociones** porque solo bebía cuando le faltaba maná para una habilidad, y su Lanza de hielo es barata; además una poción de 100 era el 2 % de su maná. Ahora bebe al bajar de la mitad (279 pociones de 400 cada 300 mobs), pero aún descansa el 28 % del tiempo: **el maná sigue sin calibrar** (objetivo: 300–1.000 pociones cada 1.000 mobs).
- **Lluvia de estrellas sin interrumpir** (antes canalizada 2,5 s): el Invocador gana un **6 %** de daño contra el jefe (675 → 715) y apenas cambia cazando (37 → 39 mobs/hora solo; 70 → 72 en grupo). Las estrellas son una parte pequeña de su daño (unos 80 de daño por segundo a cada mob de los 715), porque su daño se dejó bajo a propósito; lo que gana es tiempo libre para curar y escudar. A cambio, al lanzar más hechizos, gasta más maná (565 → 847 pociones cada 300 mobs).
- **Lluvia de estrellas de 7 s** (14 estrellas en vez de 10, al mismo ritmo): contra el jefe +4 % (715 → 746) y solo +5 % cazando de uno en uno (39 → 41), pero **en grupo con 12 mobs +22 %** (72 → 88 mobs/hora). Con el tanque delante: 61 mobs/hora con 6 mobs, 69 con 8, 78 con 10 y 88 con 12.
- En la simulación 3 se corrigió además un fallo que a veces le quitaba el último impacto a la Lluvia de flechas (el Atacante sube un poco).
- **Pendiente de simular**: el grupo completo (tanque + curandero + daño) con las curas y escudos del Invocador a aliados.

### 1.9 Coste de maná de Mago e Invocador (decidido)

- **Mago e Invocador** usan el maná de forma constante (las demás especializaciones deberían usarlo bastante menos). Para ellos dos, el coste de los hechizos pasa a ser un **valor exacto de maná**, no un % del maná máximo. Con el %, cada punto de INT subía el maná máximo y encarecía los hechizos más de lo que subía la regeneración, así que más INT nunca cerraba el déficit.
- El coste **sube con el nivel de la habilidad**: +25 % sobre el nivel anterior en cada nivel, del 1 al **10** (nivel 4: ×1,95; nivel 10: ×7,45).
- En el nivel de personaje 20 las habilidades llegan **como mucho al nivel 4**. Las habilidades 1–4 llegan al 20 en nivel 4 (lo ganaron en los niveles 5, 10 y 15) y las 5–8 se desbloquean en nivel 1.
- Más adelante, con habilidades de nivel 10, el equipo legendario dará **miles de puntos de INT** (por ejemplo, 5.000–6.000): sobrará maná, se regenerará mucho más y podrán permitirse hechizos mucho más caros.
- Las demás especializaciones siguen con el coste en % del maná máximo.

Valores de partida (nivel 1 de la habilidad → coste en el nivel en que se tiene en el nivel 20):

| Hechizo | Quién | Nivel 1 | En el nivel 20 |
|---|---|---|---|
| Lanza de hielo | Mago e Invocador | 75 | 146 (nivel 4) |
| Bola de fuego | Mago e Invocador | 150 | 293 (nivel 4) |
| Escudo de maná | Mago e Invocador | 200 | 391 (nivel 4) |
| Lluvia de fuego | Mago | 300 | 300 (nivel 1) |
| Fuego de alma | Mago | 200 | 200 (nivel 1) |
| Lluvia de estrellas | Invocador | 250 | 250 (nivel 1) |
| Restauración | Invocador | 300 | 300 (nivel 1) |

Efecto (caza de uno en uno; pociones de maná de 400 cada 1.000 mobs):

| | Antes (% del maná) | Ahora (valor exacto) |
|---|---|---|
| **Mago** | 90 mobs/hora · ~930 pociones · **28 % descansando** | **126 mobs/hora** · ~620 pociones · **sin descansar** |
| **Invocador** | 41 mobs/hora · ~2.700 pociones · sin descansar | 35 mobs/hora · ~3.700 pociones · **15 % descansando** |

- El Mago queda dentro del objetivo (300–1.000 pociones) y ya no se sienta.
- El Invocador no cuadraba: con 185 de INT regeneraba 74 de maná por segundo, menos que el Mago (94), y además de atacar cura y escuda (~3.700 pociones cada 1.000 mobs y 15 % del tiempo descansando).
- **Corrección (decidido):** su **pasiva de arma** (más potencia de escudos y curas) le da además **+0,2 de maná por segundo por cada punto de INT** (0,4 de su pasiva de especialización + 0,2 = 0,6). Regenera **112 por segundo** (558 cada 5 s) y queda en **41 mobs/hora, ~430 pociones cada 1.000 mobs y sin descansar**; contra el jefe, 746 de daño por segundo.
- **Más caza para el Invocador (decidido):** su pasiva de arma le da además **+50 % de daño contra monstruos** (no contra jefes). Resultado: de uno en uno **41 → 61 mobs/hora** (~440 pociones de maná cada 1.000 mobs, sin descansar); en grupo con 12 mobs **88 → 130 mobs/hora**; contra el jefe sigue en 746.

### 1.10 Simulación del grupo completo

- **Maná de los físicos (decidido):** se queda como está (entre ~350 y ~1.000 pociones de maná cada 1.000 mobs).
- El simulador ya admite **varios personajes a la vez** (prueba 4 de `simular20.py`). Supuestos:
  - Todos los mobs pegan al **tanque** (Combatiente); si cae, pasan al siguiente (cuerpo a cuerpo y después los de distancia).
  - Quien muere vuelve a los 30 s con todo lleno; si cae el grupo entero, los mobs se recuperan.
  - El Invocador cura con Restauración al aliado más herido cuando baja del 60 % (30 % de su vida; si cura a otro, se cura él la mitad o se la da al siguiente más herido); pone el Escudo de maná al tanque cuando le van a pegar (el tanque recibe el escudo entero y el Invocador un 25 %); cada estrella de la Lluvia de estrellas escuda a los aliados (no a él) con el daño que hace, durante 8 s.
  - Se descansa si a cualquiera le queda poca vida o poco maná, y se espera a que todos se recuperen.

**Resultados** (300 mobs por prueba; "por miembro" = mobs/hora del grupo entre sus miembros, porque la experiencia se reparte):

Trío: Combatiente, Mago, Invocador.

| Mobs a la vez | Mobs/hora del grupo | Por miembro | Caídas | Pociones de vida del tanque | Curado / escudo por segundo | Reparto del daño |
|---|---|---|---|---|---|---|
| 1 | 226 | 75 | 0 | 0 | 9 / 283 | Combatiente 20 %, Mago 55 %, Invocador 24 % |
| 6 | 571 | 190 | 0 | 0 | 0 / 315 | Combatiente 23 %, Mago 62 %, Invocador 15 % |
| 12 | 1.102 | 367 | 0 | 0 | 0 / 302 | Combatiente 22 %, Mago 68 %, Invocador 11 % |
| 20 | 1.849 | 616 | 0 | 0 | 11 / 342 | Combatiente 21 %, Mago 69 %, Invocador 11 % |

Grupo de 5: Combatiente, Invocador, Mago, Atacante a distancia, Asesino.

| Mobs a la vez | Mobs/hora del grupo | Por miembro | Caídas | Pociones de vida del tanque | Curado / escudo por segundo | Reparto del daño |
|---|---|---|---|---|---|---|
| 1 | 379 | 76 | 0 | 0 | 16 / 396 | Combatiente 11 %, Invocador 13 %, Mago 29 %, Atacante 27 %, Asesino 20 % |
| 6 | 846 | 169 | 0 | 0 | 0 / 593 | Combatiente 14 %, Invocador 9 %, Mago 40 %, Atacante 25 %, Asesino 12 % |
| 12 | 1.620 | 324 | 0 | 0 | 0 / 604 | Combatiente 13 %, Invocador 7 %, Mago 45 %, Atacante 26 %, Asesino 8 % |
| 20 | 2.602 | 520 | 0 | 0 | 12 / 589 | Combatiente 14 %, Invocador 6 %, Mago 45 %, Atacante 28 %, Asesino 7 % |

Lectura:
- **Los roles funcionan en grupo**: el Combatiente aguanta hasta 20 mobs sin que nadie muera, el **Mago hace la mayor parte del daño en área** (45–69 %) y el Invocador aporta algo de daño y, sobre todo, escudos.
- **De uno en uno, el grupo no compensa por sí solo**: por miembro sale como cazar solo (trío 75 frente a una media de 79 de sus miembros solos; grupo de 5, 76 frente a 93). Lo compensará la **bonificación de experiencia de grupo** (+10 % a +25 %, ya decidida).
- **En conglomerados el grupo caza muchísimo más**: con 12–20 mobs, cada miembro saca **4–7 veces** lo que sacaría solo. Si se quiere evitar, se puede ajustar con la experiencia por mob de las zonas de conglomerados o el tamaño de los grupos de mobs (capítulo de mapas).
- **El curandero casi no tiene que curar**: los escudos (los de las estrellas y el Escudo de maná) y el robo de vida en área del Combatiente cubren casi todo el daño, y el tanque no bebe pociones. Con el mob del nivel 20 (59 de daño por golpe), el daño que entra en grupo es bajo; los mobs de las zonas de conglomerados, los élites y los jefes deberían pegar más para que la cura importe.

## 2. Trabajo de esta sesión

1. ~~**Especializaciones por clase de inicio**~~: decidido (1.0b).
2. ~~**Transición en el nivel 20**~~: se recalcula todo (1.0c). Falta fijar el crecimiento por nivel de cada especialización.
3. **Pasiva de especialización** (habilidad 5, ver 1.6): qué da cada punto de STR, INT y AGI en cada una de las 6 especializaciones (borrador en 1.4).
4. **Habilidades 6–8 de cada especialización** (pasiva de arma, área e individual; ver 1.6) en lo que afecta a las estadísticas: daño, enfriamiento y coste de maná.
5. **Armas de clase**: daño y velocidad de daga, varita y espadas de clase.
6. ~~**Recursos secundarios**~~: mecánica decidida (1.5). Faltan los valores.
7. **Estadísticas visibles nuevas** desde el nivel 20 (las neutrales de la hoja que se muestran y empiezan a contar).
8. **Simulación de las 6 clases en el nivel 20**: hecha, solos (1.8) y en grupo (1.10); maná calibrado para Mago e Invocador (1.9).
9. **Primer balance PvP** con el triángulo STR > AGI > INT > STR.
10. **Ficha cerrada del nivel 20** por clase.

## 3. Preguntas abiertas

- **Flecos de la parte 1** que conviene cerrar aquí: validar los valores por punto de INT y AGI, daño de las armas por tramos y pociones que curen según el nivel.
