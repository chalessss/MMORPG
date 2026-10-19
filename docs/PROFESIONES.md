# Capítulo de detalle — Profesiones

Estado: **en curso**. Este archivo recoge el punto de partida (lo ya decidido en otros documentos), las incoherencias detectadas, una propuesta de estructura y las preguntas abiertas. Se irá completando en la sesión.

## 1. Punto de partida (ya decidido)

### 1.1 Lista y reglas generales (`DISENO_BASE.md` 3.15)

| Principales (2 activas) | Secundarias (todas) |
|---|---|
| Sastre | Cocinero |
| Peletero | Desollador |
| Herrero | Minero |
| Joyero | Herborista |
| Encantamiento | Pesca |
| Inventor | |

- Todas disponibles desde el nivel 1. La misión de la línea principal que las presenta (hacia el nivel 3) desbloquea la casilla de la bolsa de componentes; se puede elegir una profesión ya o más tarde.
- **2 principales activas**; las demás quedan inhabilitadas **sin perder progreso**. Cada cambio cuesta oro con una curva suave (logarítmica) que sube con cada cambio.
- **Inventor**: lo puede aprender cualquiera (decidido); el único que fabrica **piedras santificadas**. La especialización Recolector tendrá bonificaciones extra exclusivas como inventor (se diseñan en la Temporada 2).
- **Encantamiento**: la única que fabrica **papiros de encantamiento**.
- Entrenador de profesión: enseña la profesión y la sube de rango.

### 1.2 Recolección (`ESTADISTICAS_NEUTRALES.md` 7 y 7.2)

- 10 s por recogida de base; la velocidad de recolección es general; cada 100 % reduce el tiempo a la mitad.
- Minería y herboristería suben por puntos como en WoW (según la veta o planta se gana o no un punto). A **100 puntos**, +25 % de velocidad cada una.
- Vetas enriquecidas: piden **50 puntos**, dan el material del grado más alto de la temporada en mayor cantidad y se recogen 1–3 veces.
- La energía no tiene profesión ni vetas enriquecidas.
- Recoger o fabricar recarga la potenciación de caza (10 s de base por recogida).

### 1.3 Fabricación

- A **100 puntos** de una profesión de fabricación, el tiempo de sus recetas se reduce a la mitad; es el máximo (`ESTADISTICAS_NEUTRALES.md` 7.3). Alerta silenciosa si alguien fabrica más rápido.
- Equipo: hacen falta componentes de la misma calidad; se pueden combinar 10 → 1 de la calidad siguiente; los mobs de nivel máximo de la temporada sueltan componentes de la calidad máxima; objetivo: 1 pieza de la calidad máxima por semana con 6 h/día (`DISENO_BASE.md` 3.17b).
- Interfaz de fabricación: pestañas por tipo (arma, armadura, accesorios), lista por calidad, receta con componentes y filtro "se puede fabricar".
- Calidad máxima por temporada: T1 poco común, T2 raro, T3 épico.

### 1.4 Lo que fabrica cada profesión (lo que ya se sabe)

| Profesión | Fabrica (decidido) |
|---|---|
| **Las seis principales** (sastre, peletero, herrero, joyero, encantamiento, inventor) | **Primera receta de todas:** piedras **potenciadas** y **pacificadas** (piedras generales + un **objeto intermedio** de cualquier principal + cristales + oro) |
| Las seis principales | Su **objeto intermedio** propio: llave de tuercas (herrero), madeja de lino (sastre), papiro en blanco (encantamiento), uno propio del inventor… Cualquiera sirve para la receta de piedras de cualquier profesión |
| Herrero | **Armas de todo tipo**, de todas las clases. Desde la Temporada 2, también **placas**, con especialización de herrería: **armas** o **armaduras** |
| Inventor | Además, piedras **santificadas**, en exclusiva (generales + potenciadas + pacificadas + oro) |
| Encantamiento | **Papiro en blanco** (primera receta; se vende) y su **inscripción**; el papiro inscrito se aplica a la pieza. Las estadísticas salen **al azar**; para cambiarlas se aplica otro encantamiento. El número de estadísticas depende de la calidad del objeto y del nivel de encantamiento |
| Cocinero | Elixir defensivo, elixir ofensivo y comida; mejoran con el nivel de la profesión; la estadística depende del ingrediente (pescado, carne, planta…) |
| Todas | Una **bolsa** mayor con sus propios materiales; los especializados la hacen un poco más grande (34 → 36–38 espacios) |

### 1.5 Otras recompensas ya decididas

- Primera principal al máximo → se pueden asignar bolsas a componentes. Una secundaria al máximo → bolsas a consumibles.
- Fabricar para otros (encargos, tiendas privadas estilo Lineage 2) debe dar al fabricante experiencia, moneda y otras recompensas.
- Clanes: bonificaciones de fabricación y recolección (técnicas del clan).

## 2. Incoherencias detectadas

**Resueltas:**
1. **Tala y madera — retiradas (decidido).** No hay madera como recurso ni profesión de tala. Más adelante podría volver como componente que **vende un NPC** (por ejemplo, un lote de madera para alguna receta de sastre o de peletero).
2. **Alquimia — retirada (decidido).** Era una mención antigua; no existe como profesión.
3. **Nombres (decidido):** la profesión se llama **encantamiento**; la especialización 2 del Invocador sigue llamándose **Encantador**.
4. **Piedras de desarrollo (decidido):** las generales caen **solo por caza**; las **potenciadas** (suben de +1 a +4 al azar) y las **pacificadas** las fabrican **las seis principales**, encantamiento incluida; las **santificadas**, solo el inventor. Se corrige el documento base; la hoja ya lo recogía así.

5. **Inventor (decidido):** abierto a **cualquier personaje**, así que ya hay piedras santificadas en la Temporada 1. El **Recolector** recibirá bonificaciones extra exclusivas por ser inventor, que se diseñarán al añadir esa especialización.
6. **Herrero (decidido):** fabrica **armas de todo tipo**.
7. **Receta de las piedras (decidido):** cada principal fabrica su **objeto intermedio** (llave de tuercas, madeja de lino, papiro en blanco…) y **cualquiera vale** para cualquier receta de piedras, sin restricción. Motivo: que nadie tenga que cambiar de profesión solo para usar un objeto que fabricó antes.
8. **"Encantamiento"**: nombre compartido por la profesión y el sistema; se mantiene.

9. **Estadísticas del encantamiento (decidido):** **aleatorias**; quien quiera otras aplica **otro encantamiento**. Más adelante, la **reforja**: el inventor (y las clases con bonificación de inventor, probablemente más de una) podrá cambiar **una** estadística concreta de un objeto encantado por otra (crítico → regeneración de vida). Se detalla en la temporada en que llegue.
10. **Objeto intermedio del inventor (decidido):** tiene el suyo, como las demás.
11. **Placas (decidido):** las fabrica el **herrero**. En la Temporada 2 el herrero elige una **especialización de herrería** (como en WoW): **armas** o **armaduras**. Pendiente: si la elección es definitiva o se puede cambiar, y qué conserva quien elige armaduras de las recetas de armas de la T1.

## 3. Progresión de puntos

### 3.1 Profesiones por temporada (decidido, estilo WoW actual)

- Cada profesión se divide **por temporadas**, y cada temporada tiene su propia rama de **1 a 100 puntos**, con nombre propio. Ejemplo (los nombres son provisionales): si la Temporada 1 es "del Vacío" y la 2 "de la Iluminación", existirán **Herrería del Vacío** y **Herrería de la Iluminación**, **Encantamiento del Vacío** y **Encantamiento de la Iluminación**…
- Para aprender la rama de una temporada **no hace falta** haber subido la anterior: quien empieza herrería en la Temporada 2 va directo a Herrería de la Iluminación, sin repetir los 100 puntos de la Temporada 1.
- Así el jugador sabe que solo avanza en la profesión **de la temporada en la que está jugando**, y nadie tiene que volver a empezar desde cero cada temporada.

### 3.2 Colores de receta (decidido)

| Color | Cuándo | Puntos al fabricar |
|---|---|---|
| **Naranja** | La receta **nunca se ha fabricado** y la profesión está **dentro de su tramo amarillo** (menos de 5 puntos por encima del punto en que se aprende) | **×2**: la primera fabricación da **2 puntos** con los mismos materiales |
| **Amarillo** | Desde la primera fabricación hasta **5 puntos** por encima del punto en que se aprende la receta | **1 punto seguro** |
| **Verde** | De +5 a +10 por encima del punto en que se aprende | **Probabilidad** de ganar 1 punto, escalonada (tabla de abajo). El objeto **siempre se fabrica**; lo que puede fallar es el punto |
| **Gris** | Desde +10 (cuando llega el rango siguiente) | 0 |

**Probabilidad en verde (decidido)**, contando desde el punto en que se aprende la receta:

| Punto | +5 → +6 | +6 → +7 | +7 → +8 | +8 → +9 | +9 → +10 |
|---|---|---|---|---|---|
| Probabilidad | 60 % | 55 % | 50 % | 45 % | 40 % |

Los últimos cinco puntos de cada tramo piden **más materiales**. *Supuesto por confirmar*: la receta pasa a gris al llegar a +10.

- El ×2 del naranja **incentiva fabricar una vez cada receta** en vez de repetir siempre la misma, y consume menos materiales para subir.
- Ejemplo: una receta que se aprende con 0 puntos → la primera fabricación pasa de 0 a **2**; tres fabricaciones en amarillo llevan a **5**; desde ahí, verde: 60 % para pasar a 6, 55 % a 7, 50 % a 8, 45 % a 9 y 40 % a 10.
- **El ×2 caduca (decidido)**: si la profesión llega al final del tramo amarillo de una receta (5 puntos por encima del punto en que se aprende) sin haberla fabricado nunca, la receta pasa **directamente de naranja a verde** y su primera fabricación ya no da 2 puntos: sigue la regla del verde. Así nadie puede **guardarse** primeras fabricaciones para gastarlas en la zona verde y subir los puntos con riesgo de forma segura.

### 3.3 Rangos del entrenador (decidido)

- Un **rango cada 10 puntos** (1–10, 11–20… 91–100).
- Cada rango enseña **como máximo 3 recetas**.
- Con 3 recetas por rango, sus tres primeras fabricaciones (naranja) ya dan 6 de los 10 puntos del rango.

### 3.4 Requisitos de nivel (decidido)

- **Ninguno**: un personaje de cualquier nivel puede subir una profesión hasta 100.
- El freno son los **materiales**: los de los últimos rangos salen de zonas con mobs de **nivel 20**. Quien no tenga nivel tiene que **comprarlos** (con oro, en el mercado) o ir subiendo nivel y profesión a la vez.

### 3.5 Bonus de los 100 puntos, por temporada (decidido)

- El bonus de llegar a 100 en una rama vale **solo para lo de su temporada**. Al recolectar, el servidor mira primero **de qué temporada es el recurso** (por ejemplo, un mineral de una zona de la Temporada 1 o de la 2) y solo aplica el +25 % de la rama de **esa** temporada.
- Lo mismo con la fabricación: el tiempo a la mitad vale para las recetas de la rama que llegó a 100.
- **Lo que no se pierde**: la velocidad de recolección de **objetos y encantamientos** es general y vale en todas las zonas. Quien llega a la Temporada 2 con, por ejemplo, un 15–20 % de su equipo lo conserva, y al subir las ramas nuevas a 100 vuelve a sumar el 50 % de minería y herboristería.
- Objetivo: que el bonus de profesión sea **exclusivo de las zonas de cada temporada**.

### 3.6 Todo cuesta oro (decidido)

Aprender una profesión, cada receta, cada rango del entrenador y cada especialización de profesión (por ejemplo, la de herrería) **cuesta oro**. Las cantidades se fijarán con el modelo de economía.

## 4. Propuesta de estructura del capítulo (resto)


1. ~~**Progresión de puntos**~~: decidida (sección 3).
2. ~~**Mapa de materiales**~~: decidido en lo general (4.1 y 4.2).
3. **Qué fabrica cada profesión** en la Temporada 1, por ranura y calidad.
4. **Recetas**: cómo se consiguen (entrenador, botín, reputación, misiones) y cuántas hay.
5. **Coste de cambiar de principal**: la curva de oro.
6. **Recompensas** de subir profesiones (experiencia, títulos, bolsas, códice).
7. **Encargos y tiendas privadas**: lo que gana el fabricante.
8. **Datos para Unreal**: tablas de profesiones, recetas y materiales (DataTables desde CSV).

### 4.1 Mapa de materiales (decidido en lo general)

**Dos familias de principales:**

| Familia | Profesiones |
|---|---|
| **Fibras y plantas** | Sastre, peletero, encantamiento |
| **Minerales** | Herrero, joyero, inventor |

**Cadena de la familia de fibras** (estilo WoW: el primer material se procesa primero en sastrería y las demás lo reutilizan):

| Paso | Quién | Receta |
|---|---|---|
| Material base | Botín de **humanoides** | **Bolas de lino** (la tela que sueltan) |
| 1 | **Sastre** (primera receta; es también su objeto intermedio) | 2 bolas de lino → 1 **madeja de lino** |
| 2 | **Encantamiento** | 2 madejas de lino → 1 **papiro** (en blanco) |
| 3 | **Peletero** | 1 **cuero** + 1 madeja de lino → material exclusivo de peletería |
| Cuero | **Cocinero** (primeras recetas) | Cualquier **carne** del juego → **cuero** |

**Familia de minerales**: el joyero se apoya sobre todo en el botín de **elementales** (para potenciar lo que fabrica con las menas); el herrero, en minería y en otra familia de mobs que se decidirá al detallar sus recetas, para repartir la demanda entre bestias, humanoides y elementales.

**Inventor**: tiene **materiales propios**; no depende de lo que fabriquen las demás profesiones.

**Regla para diseñar recetas**: cada paso de una cadena pide **o bien** un producto de una profesión secundaria, **o bien** dos unidades del objeto anterior (2 bolas → 1 madeja; 2 madejas → 1 papiro). El resto de cadenas se organizará con esta regla al detallar cada profesión.

**Riesgo anotado**: los sastres necesitarán cazar muchos humanoides. Se equilibra repartiendo los materiales del resto de profesiones entre las demás familias de mobs (elementales para los joyeros, etc.).

### 4.2 Sin desencantar (decidido)

- **No existe** destruir equipo para sacar materiales (el "desencantar" de WoW).
- La única forma de destruir objetos es la del **desarrollo**: si falla en la zona de peligro (por ejemplo, de +7 a +8), el objeto se destruye y deja **cristales**. Aparte, el **códice** consume los objetos que se registran.
- Objetivo: que haya **un único método de destrucción** y que solo se use cuando interesa conseguir cristales para fabricar piedras.

## 5. Preguntas abiertas

Ver el orden propuesto en la sección 4. Se responden en la sesión y pasan a "decidido" en este documento.
