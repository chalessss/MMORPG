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
| Encantador | Pesca |
| Inventor (solo la rama Recolector) | |

- Todas disponibles desde el nivel 1. La misión de la línea principal que las presenta (hacia el nivel 3) desbloquea la casilla de la bolsa de componentes; se puede elegir una profesión ya o más tarde.
- **2 principales activas**; las demás quedan inhabilitadas **sin perder progreso**. Cada cambio cuesta oro con una curva suave (logarítmica) que sube con cada cambio.
- **Inventor**: lo ofrece una misión al convertirse en Recolector; para aprenderlo hay que inhabilitar una de las dos principales. Es el único que fabrica **piedras santificadas**.
- **Encantador**: el único que fabrica **papiros de encantamiento**; no fabrica piedras de desarrollo.
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
| Sastre, peletero, herrero, joyero | Piedras **potenciadas** y **pacificadas** (piedras generales + un objeto de su profesión + cristales + oro) |
| Inventor | Piedras potenciadas, pacificadas y **santificadas** (generales + potenciadas + pacificadas + oro) |
| Encantador | Papiros de encantamiento (el número de estadísticas depende de la calidad del objeto y del nivel de encantamiento) |
| Cocinero | Elixir defensivo, elixir ofensivo y comida; mejoran con el nivel de la profesión; la estadística depende del ingrediente (pescado, carne, planta…) |
| Todas | Una **bolsa** mayor con sus propios materiales; los especializados la hacen un poco más grande (34 → 36–38 espacios) |

### 1.5 Otras recompensas ya decididas

- Primera principal al máximo → se pueden asignar bolsas a componentes. Una secundaria al máximo → bolsas a consumibles.
- Fabricar para otros (encargos, tiendas privadas estilo Lineage 2) debe dar al fabricante experiencia, moneda y otras recompensas.
- Clanes: bonificaciones de fabricación y recolección (técnicas del clan).

## 2. Incoherencias detectadas

1. **Tala** aparece en la tabla de recursos (`DISENO_BASE.md` 3.5: "Madera — Tala") pero no en la lista de profesiones. ¿Se quita la madera, se añade la tala como secundaria o la recoge cualquiera sin profesión (como la energía)?
2. **Alquimia** aparece en 3.5 ("herrería, alquimia, cocina") pero no existe como profesión; las pociones de vida y maná son de NPC (3.21). Propuesta: borrar la mención.
3. **Encantador** es a la vez una profesión y una especialización 2 (Invocador → Encantador). Puede confundir en la interfaz y en las misiones. ¿Se renombra una de las dos?
4. **La hoja de cálculo** (pestaña "asd") marca que el encantador fabrica piedras potenciadas y pacificadas; los documentos dicen que no. Propuesta: vale lo de los documentos y se corrige la hoja.
5. **Inventor en la Temporada 1**: el Recolector es especialización 2, así que en la T1 no habría inventores ni **piedras santificadas**. ¿Es lo buscado (la santificada llega en la T2) o la T1 necesita otra vía?
6. **Placas en la T1**: los niveles 1–20 solo usan tela y cuero, así que el herrero no tendría armaduras que fabricar en la T1. ¿Fabrica las **armas** de todas las clases?

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
| Herrero (armas, placas) | Lingotes, minerales | Minero |
| Joyero (joyería) | Gemas, metales preciosos | Minero (gemas en vetas) |
| Encantador (papiros) | Esencias, residuo elemental | Botín de elementales; ¿desencantar objetos? |
| Inventor (piedras santificadas, ¿artefactos?) | Piedras de desarrollo, componentes de todas | Comercio y otras profesiones |
| Cocinero (comida y elixires) | Carne, pescado, hierbas | Desollador, pesca, herborista |

## 4. Preguntas abiertas

Ver el orden propuesto en la sección 3. Se responden en la sesión y pasan a "decidido" en este documento.
