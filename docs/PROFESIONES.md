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
| Las seis principales | Su **objeto intermedio** propio: llave de tuercas (herrero), madeja de lana (sastre), papiro en blanco (encantamiento)… Cualquiera sirve para la receta de piedras de cualquier profesión |
| Herrero | **Armas de todo tipo**, de todas las clases |
| Inventor | Además, piedras **santificadas**, en exclusiva (generales + potenciadas + pacificadas + oro) |
| Encantamiento | **Papiro en blanco** (primera receta; se vende) y su **inscripción** con una estadística (por ejemplo, velocidad de ataque); el papiro inscrito se aplica a la pieza. El número de estadísticas depende de la calidad del objeto y del nivel de encantamiento |
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
7. **Receta de las piedras (decidido):** cada principal fabrica su **objeto intermedio** (llave de tuercas, madeja de lana, papiro en blanco…) y **cualquiera vale** para cualquier receta de piedras, sin restricción. Motivo: que nadie tenga que cambiar de profesión solo para usar un objeto que fabricó antes.
8. **"Encantamiento"**: nombre compartido por la profesión y el sistema; se mantiene.

**Nuevas preguntas:**
9. **Papiro inscrito vs. azar**: el sistema de encantamiento (`DISENO_BASE.md` 3.19) decía que las estadísticas salen **al azar**. Con la inscripción ("póngale velocidad de ataque"), ¿quien inscribe **elige la estadística** y el azar queda solo en el **valor** (o en las estadísticas extra), o se inscribe a ciegas?
10. **Objeto intermedio del inventor**: ¿el inventor fabrica también su propio objeto intermedio, o compra el de otras profesiones?
11. **Placas**: cuando lleguen en la Temporada 2, ¿las fabrica el herrero o se reparten de otra forma?

## 3. Propuesta de estructura del capítulo

1. **Progresión de puntos**: 1–100 por temporada o tope que sube cada temporada (100 en T1, 200 en T2…); cómo se gana cada punto (colores de receta estilo WoW: naranja siempre, amarillo a veces, verde casi nunca, gris nunca); rangos del entrenador (aprendiz, oficial, experto…).
2. **Mapa de materiales**: qué secundaria alimenta a qué principal (propuesta en 3.1).
3. **Qué fabrica cada profesión** en la Temporada 1, por ranura y calidad.
4. **Recetas**: cómo se consiguen (entrenador, botín, reputación, misiones) y cuántas hay.
5. **Coste de cambiar de principal**: la curva de oro.
6. **Recompensas** de subir profesiones (experiencia, títulos, bolsas, códice).
7. **Encargos y tiendas privadas**: lo que gana el fabricante.
8. **Datos para Unreal**: tablas de profesiones, recetas y materiales (DataTables desde CSV).

### 3.1 Mapa de materiales (propuesta para discutir)

| Principal | Materiales principales | De dónde salen |
|---|---|---|
| Sastre (tela) | Telas | Botín de humanoides |
| Peletero (cuero) | Pieles, cuero | Desollador (bestias) |
| Herrero (armas de todo tipo) | Lingotes, minerales | Minero |
| Joyero (joyería) | Gemas, metales preciosos | Minero (gemas en vetas) |
| Encantamiento (papiros) | Esencias, residuo elemental | Botín de elementales; ¿desencantar objetos? |
| Inventor (piedras santificadas, ¿artefactos?) | Piedras de desarrollo, componentes de todas | Comercio y otras profesiones |
| Cocinero (comida y elixires) | Carne, pescado, hierbas | Desollador, pesca, herborista |

## 4. Preguntas abiertas

Ver el orden propuesto en la sección 3. Se responden en la sesión y pasan a "decidido" en este documento.
