# Resumen ejecutivo

Vista rápida del proyecto. El detalle de cada decisión está en `docs/DISENO_BASE.md`; las fases, en `docs/HOJA_DE_RUTA.md`.

## Estado actual

- **Fase**: diseño general terminado y **capítulo de estadísticas de la Temporada 1 cerrado** (con simuladores de balance en `herramientas/simulador/`). Todavía no hay proyecto de Unreal.
- **En curso**: capítulo de **profesiones** (`docs/PROFESIONES.md`).
- **Forma de trabajo**: la primera conversación fijó los parámetros generales; a partir de ahora se trabaja **un capítulo de detalle por sesión**.

## Lo que está definido

**Base**
- MMORPG 3D, solo PC, Unreal Engine 5.5.4. Lógica en C++ con GAS; el servidor decide todo lo importante. Cámara elevada ajustable (estilo WoW).
- **Pilares**: el personaje evoluciona · hay más que subir de nivel · temporadas · todo cuesta moneda · juego limpio · funciones que se desbloquean por nivel.

**Progresión**
- Temporadas: T1 (1–20: clase de inicio hasta el 19 —Mágica - Rango, Física - Melee, Física - Rango—, especialización 1 en el 20) · T2 (20–40, especialización 2) · T3 (40–60, especialización 3). Futuras: 80, 90, 100.
- Subclases desde el nivel 60: comparten nivel; cada clase con su conjunto de equipo vinculado.

**Estadísticas (Temporada 1, cerrado)**
- Niveles 1–19 con tres clases de inicio; en el 20, **6 especializaciones** que recalculan los mismos 370 puntos con su conversión propia, 8 habilidades cada una (área para todas; solo el Mago encadena la suya) y un recurso secundario (Ira, Energía, Foco, Trance, Esencia).
- Balance **por rol**: las de daño mandan contra un objetivo, el Combatiente aguanta conglomerados (hasta 12 mobs) y provoca con el Embate dejando huecos de agro, el Mago es el que más daño hace en área y el Invocador es el único curandero. Sin amenaza extra para el tanque en la Temporada 1.
- **La STR solo da defensa física**; la mágica la dará la joyería.
- **Neutrales de la Temporada 1** (lineales hasta la Temporada 3): precisión y evasión (solo contra golpes físicos, escalones de 5 puntos; los mobs tienen tanta como su nivel), defensa física y mágica (10.000 puntos = 50 %), daño a monstruos (15 % normal, 20 % máximo), CDR (10 % normal, 15 % máximo, no afecta al Embate), velocidad de recolección y de fabricación.
- **Potenciación de caza** (el "vigor" de MIR4): +100 % de experiencia por tiempo en combate, hasta 8 horas; se recarga desconectado, recolectando o fabricando; sin píldoras.
- **Poder**: se calibrará en el capítulo de objetos, con el equipo perfecto de cada especialización y pesos distintos por clase.
- Detalle: `docs/RESUMEN_ESTADISTICAS.md`.

**Grupo y botín**
- Sin mobs "marcados": todo se reparte por **daño efectivo** (grupo = una unidad).
- Grupos de 5 con bonus de experiencia +10 % a +25 %.
- Reparto por prioridad y rotación; armadura individual (tirada por miembro) y de grupo (cualquier clase); objetos de misión fuera de la rotación.

**Mundo**
- Familias de mobs por temporada (T1: bestias, humanoides, elementales; T2: + no-muertos; T3: + insectos).
- Zonas de caza divididas por estilo de juego; recolección en zonas propias; vetas enriquecidas por todo el mapa.
- Teletransporte estilo Lineage 2: puntos fijos, con coste, que hay que descubrir. Guardianes estáticos en los pasos a zonas altas.
- Mapa: zona de inicio protegida → pueblo neutral → **capital** (controlada por un clan) rodeada de **4 villas** con facción propia.

**Objetos**
- 9 fuentes · 7 calidades (gris → cian) · armaduras de tela, cuero y placas.
- 16 ranuras (8 equipo + 8 joyería; la mitad desde el nivel 41), todas con apariencia y transfiguración. Sin casco ni hombreras.
- **Desarrollo +1 a +10**: piedras general, potenciada, pacificada y santificada con tablas cerradas; zona segura hasta +5; los objetos destruidos dejan cristales.
- **Encantamiento**: estadísticas aleatorias con papiros que fabrica la profesión de encantamiento.
- **Fabricación**: los mobs de nivel máximo de cada temporada sueltan componentes de la calidad máxima; objetivo: 1 pieza por semana con 6 h/día.

**Códice**
- Pestañas: Personaje (equipo de la clase activa), Caza (objetos hechos con trofeos de cada familia de mob; compartido) y Servidor (equipo de otras clases; compartido). Sin tiempo limitado.
- Objetos que se consumen al registrar; entradas que piden más piezas y más desarrollo; crece cada temporada.

**Profesiones**
- 6 principales (2 activas; se cambian con coste progresivo sin perder progreso): sastre, peletero, herrero, joyero, encantamiento, inventor (abierto a todos; el Recolector tendrá bonificaciones extra). Las seis fabrican piedras potenciadas y pacificadas con un objeto intermedio de cualquier profesión; solo el inventor, santificadas. El herrero fabrica todas las armas; encantamiento, papiros en blanco que luego se inscriben. Sin tala ni alquimia.
- 5 secundarias (todas): cocinero, desollador, minero, herborista, pesca.
- **Recolección**: 10 s por recogida de base; la velocidad de recolección es general y cada 100 % reduce el tiempo a la mitad. Minería y herboristería suben por puntos como en WoW y a 100 puntos dan +25 % cada una. Las vetas enriquecidas piden 50 puntos, dan el material del grado más alto de la temporada y se recogen 1–3 veces. La energía no tiene profesión.
- **Fabricación**: a 100 puntos de una profesión, el tiempo de sus recetas se reduce a la mitad (el máximo).

**Inventario y economía**
- Bolsas general, de componentes y de consumibles; bolsa invisible para misiones; nada se pierde; venta rápida; organizar; banco con pestañas (banco de tropa en nivel 60).
- Oro como moneda principal (cobre/plata/oro/lingote); ficha de oro estilo WoW; honor, valor, monedas de clan, moneda premium.
- **Quema** en cada transacción entre jugadores; comisión menor en P2P que en el mercado.
- Mercado **regional** (compartido por todos los servidores de una región), tiendas privadas estilo Lineage 2 y encargos de fabricación.
- Publicar en el mercado: el objeto queda "pendiente" entre 15 y 20 minutos (se puede cancelar), después está a la venta 14 días; ventas y devoluciones llegan por **correo**.
- **Correo**: entre jugadores, solo texto; los objetos solo llegan del mercado o del equipo del juego.

**Otros sistemas**
- **Muerte**: −5 % de experiencia (también en PvP); 3 recuperaciones gratis al día.
- **Juego automático**: con el juego abierto; hasta 8 h/día encadenables; botín restringido en automático.
- **Clanes**: se crean en el nivel 10 con cobre; 30 → 100 miembros; árbol de técnicas por cooperación (sin moneda premium); contribución semanal visible.
- **Misiones**: principal (desbloquea y enseña; incluye clase y profesiones), secundarias, diarias (cuenta y clan), semanales, únicas. Reputación de facción con misiones no principales.
- **Mazmorras** de 5 desde T2 (también asistidas con IA); **bandas** flexibles de 10 a 40 más adelante.
- **Clasificación**: poder, códice y clanes (nivel y poder). Sin clasificación por nivel del personaje; filtrable por clase; común a toda la región; el sitio web publica cada día el top 100 de cada región.
- **Seguridad** (`docs/SEGURIDAD.md`): alertas silenciosas con tres informes encadenados (instantáneo, 5 minutos, 1 hora), ban de un año con apelación, origen verificado de todo objeto que entra al mercado y alerta de objeto perfecto.
- **Menú principal** único con submenús desplegables (estilo MIR4).

**PvP**
- Zonas con reglas distintas en **días normales** y **eventos** (fines de semana): inicio sin PvP; ciudades sin ataque; zonas de combate con honor; campo abierto con karma; durante eventos, PvP libre en la zona de guerra (capital + villas) y paz en el resto.
- Todos contra todos (grupo, clan y alianzas protegen). Duelos aislados sin penalización; arenas más adelante.
- Karma: nombre en rojo y sin viaje rápido; se quita matando mobs o muriendo. Honor solo por víctimas de hasta 5 niveles menos.
- Conquista de capital y villas: se habilita en la Temporada 3.

## Pendiente

**Capítulos de detalle** (uno por sesión):
1. ~~**Estadísticas**~~ — **cerrado para la Temporada 1** (`docs/ESTADISTICAS.md`, `docs/ESTADISTICAS_NIVEL_20.md`, `docs/ESTADISTICAS_NEUTRALES.md`; resumen en `docs/RESUMEN_ESTADISTICAS.md`). Para la Temporada 2: neutrales de PvP, botín y jefes, primer balance PvP y crecimiento por nivel desde el 20.
2. **Profesiones** — en curso (`docs/PROFESIONES.md`).
3. Personajes → habilidades (incluye las cantidades de curas, escudos y recursos secundarios).
4. Mapas (incluye guerra de territorios, asedios, cementerios, élites y conglomerados).
5. Recursos (tiempos base de recolección).
6. Objetos (incluye cantidades del códice, trofeos, armadura por especialización, daño de las armas por tramos, pociones y la calibración del poder).
7. Contenido por temporada (distribución de todo lo anterior y curva de experiencia).

**Para más adelante**: espíritus, entrenamiento con temporizador, karma completo, reglas de bandas, todos los números (precios, comisiones, cristales, tiempos).

**Para el final**: ambientación y estilo artístico.

## Recomendaciones

1. **Recortar la primera versión jugable** a una porción vertical (una zona, 6 clases 1–20, caza en grupo, un jefe de mundo, recolección, 2–3 profesiones, desarrollo y códice básico).
2. **Resolver pronto la arquitectura de servidor**: el servidor dedicado de Unreal soporta del orden de cien jugadores por instancia; un MMO necesita repartir el mundo entre varios servidores. Decidido: los servidores se agrupan por **región**, y cada región comparte un mismo mercado y una misma clasificación; las clasificaciones de otras regiones se ven en el sitio web (top 100 diario).
3. **Modelar la economía en una hoja de cálculo** (entradas vs. salidas de moneda) antes de fijar precios.
4. **Cuidar la monetización** para que no se perciba como "pagar para ganar". Steam no admite juegos con NFT.
5. **Detección de bots en el servidor**, además de los límites del automático. Decidido: alertas automáticas al staff cuando una estadística llega a valores irregulares (por ejemplo, más de 200 % de velocidad de recolección en la Temporada 1, o fabricar más rápido que la mitad del tiempo de una receta), con el informe completo del personaje (incluido con quién comerció y habló), en tres informes (instantáneo, 5 minutos y 1 hora) y ban de un año si se confirma; detalle en `docs/SEGURIDAD.md`.
6. **Dividir `DISENO_BASE.md`** en un archivo por sistema cuando empiecen los capítulos de detalle.
7. **Empezar la parte técnica en paralelo**: proyecto de Unreal con C++ y Git LFS, y prototipo de personajes y estadísticas.
