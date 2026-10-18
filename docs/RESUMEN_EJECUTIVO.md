# Resumen ejecutivo

Vista rápida del proyecto. El detalle de cada decisión está en `docs/DISENO_BASE.md`; las fases, en `docs/HOJA_DE_RUTA.md`.

## Estado actual

- **Fase**: diseño general terminado (todos los sistemas definidos a nivel de parámetros base). Todavía no hay código ni proyecto de Unreal.
- **Forma de trabajo**: la primera conversación fijó los parámetros generales; a partir de ahora se trabaja **un capítulo de detalle por sesión**.

## Lo que está definido

**Base**
- MMORPG 3D, solo PC, Unreal Engine 5.5.4. Lógica en C++ con GAS; el servidor decide todo lo importante. Cámara elevada ajustable (estilo WoW).
- **Pilares**: el personaje evoluciona · hay más que subir de nivel · temporadas · todo cuesta moneda · juego limpio · funciones que se desbloquean por nivel.

**Progresión**
- Temporadas: T1 (1–20: arquetipo hasta el 19, clase base en el 20) · T2 (20–40, especialización) · T3 (40–60, especialización final). Futuras: 80, 90, 100.
- Subclases desde el nivel 60: comparten nivel; cada clase con su conjunto de equipo vinculado.

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
- **Encantamiento**: estadísticas aleatorias con papiros que fabrican los encantadores.
- **Fabricación**: los mobs de nivel máximo de cada temporada sueltan componentes de la calidad máxima; objetivo: 1 pieza por semana con 6 h/día.

**Códice**
- Pestañas: Personaje (equipo de la clase activa), Caza (objetos hechos con trofeos de cada familia de mob; compartido) y Servidor (equipo de otras clases; compartido). Sin tiempo limitado.
- Objetos que se consumen al registrar; entradas que piden más piezas y más desarrollo; crece cada temporada.

**Profesiones**
- 6 principales (2 activas; se cambian con coste progresivo sin perder progreso): sastre, peletero, herrero, joyero, encantador, inventor (exclusivo de la rama Recolector).
- 5 secundarias (todas): cocinero, desollador, minero, herborista, pesca.

**Inventario y economía**
- Bolsas general, de componentes y de consumibles; bolsa invisible para misiones; nada se pierde; venta rápida; organizar; banco con pestañas (banco de tropa en nivel 60).
- Oro como moneda principal (cobre/plata/oro/lingote); ficha de oro estilo WoW; honor, valor, monedas de clan, moneda premium.
- **Quema** en cada transacción entre jugadores; comisión menor en P2P que en el mercado.
- Mercado del servidor, tiendas privadas estilo Lineage 2 y encargos de fabricación.

**Otros sistemas**
- **Muerte**: −5 % de experiencia (también en PvP); 3 recuperaciones gratis al día.
- **Juego automático**: con el juego abierto; hasta 8 h/día encadenables; botín restringido en automático.
- **Clanes**: se crean en el nivel 10 con cobre; 30 → 100 miembros; árbol de técnicas por cooperación (sin moneda premium); contribución semanal visible.
- **Misiones**: principal (desbloquea y enseña; incluye clase y profesiones), secundarias, diarias (cuenta y clan), semanales, únicas. Reputación de facción con misiones no principales.
- **Mazmorras** de 5 desde T2 (también asistidas con IA); **bandas** flexibles de 10 a 40 más adelante.
- **Clasificación**: nivel, poder, códice y clanes (nivel y poder).
- **Menú principal** único con submenús desplegables (estilo MIR4).

**PvP**
- Zonas con reglas distintas en **días normales** y **eventos** (fines de semana): inicio sin PvP; ciudades sin ataque; zonas de combate con honor; campo abierto con karma; durante eventos, PvP libre en la zona de guerra (capital + villas) y paz en el resto.
- Todos contra todos (grupo, clan y alianzas protegen). Duelos aislados sin penalización; arenas más adelante.
- Karma: nombre en rojo y sin viaje rápido; se quita matando mobs o muriendo. Honor solo por víctimas de hasta 5 niveles menos.
- Conquista de capital y villas: se habilita en la Temporada 3.

## Pendiente

**Capítulos de detalle** (uno por sesión):
1. **Estadísticas** (en curso, `docs/ESTADISTICAS.md`) — incluye revisar la hoja de Google Sheets.
2. Personajes → habilidades.
3. Mapas (incluye guerra de territorios, asedios, cementerios).
4. Recursos.
5. Objetos (incluye cantidades del códice, trofeos, armadura por especialización).
6. Profesiones.
7. Contenido por temporada (distribución de todo lo anterior).

**Para más adelante**: espíritus, entrenamiento con temporizador, karma completo, reglas de bandas, todos los números (precios, comisiones, cristales, tiempos).

**Para el final**: ambientación y estilo artístico.

## Recomendaciones

1. **Recortar la primera versión jugable** a una porción vertical (una zona, 6 clases 1–20, caza en grupo, un jefe de mundo, recolección, 2–3 profesiones, desarrollo y códice básico).
2. **Resolver pronto la arquitectura de servidor**: el servidor dedicado de Unreal soporta del orden de cien jugadores por instancia; un MMO necesita repartir el mundo entre varios servidores.
3. **Modelar la economía en una hoja de cálculo** (entradas vs. salidas de moneda) antes de fijar precios.
4. **Cuidar la monetización** para que no se perciba como "pagar para ganar". Steam no admite juegos con NFT.
5. **Detección de bots en el servidor**, además de los límites del automático.
6. **Dividir `DISENO_BASE.md`** en un archivo por sistema cuando empiecen los capítulos de detalle.
7. **Empezar la parte técnica en paralelo**: proyecto de Unreal con C++ y Git LFS, y prototipo de personajes y estadísticas.
