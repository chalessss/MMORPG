# CLAUDE.md

Contexto del proyecto para Claude. Léelo al iniciar cada sesión.

## Idioma y comunicación

- Responder siempre en **español**.
- El usuario suele enviar **notas de voz transcritas**: pueden traer muletillas o errores de transcripción (p. ej. "Cloud" = "Claude"). Interpretar la intención y preguntar si algo importante es ambiguo.
- **Niveles y números concretos** que el usuario menciona al describir sistemas ("en el nivel 3", "10 cargas", "300 de oro") son **ejemplos**, salvo que diga explícitamente que es un valor decidido. No señalar contradicciones entre ejemplos; los valores reales se fijan al diseñar cada sistema en detalle. Cuando el usuario dé valores muy exactos y estructurales (como los rangos de nivel de las temporadas: 1–20, 21–40, 41–60) y no esté claro si son definitivos, **preguntar si es un valor cerrado o un ejemplo**.
- **Mensajes que empiezan con `*`**: son preguntas técnicas o puntuales fuera del flujo del proyecto. Responderlas **sin realizar acciones** sobre el proyecto (no editar archivos, no hacer commits), salvo que se pida explícitamente.

## El proyecto

- Videojuego tipo **MMORPG / RPG online**, empezando prácticamente desde cero.
- **Motor:** Unreal Engine 5.5.4. Lógica de juego en **C++** (sistemas, estadísticas, fórmulas, red); Blueprints solo para lo visual y prototipos rápidos. Estadísticas y habilidades con el **Gameplay Ability System (GAS)**. Los `.uasset`/`.umap` son binarios: usar **Git LFS** y no editarlos desde Claude.
- Ideas previas: sistema de personajes con estadísticas (vida, daño, armadura) y sus escalados.
- **3D**, solo **PC** (teclado y ratón). Cámara elevada por defecto, ajustable estilo WoW (zoom, rotación, inclinación).
- **Subclases:** un personaje puede tener varias clases y cambiar entre ellas sin crear otro personaje ni volver a subir desde cero. Se desbloquean en el nivel 60, pero el modelo de datos del personaje debe soportarlo desde el inicio.
- Pendiente de definir: ambientación y estilo artístico.
- Datos de diseño en Google Sheets "Organizando la Base de Datos del Juego" (ID `1uhGfmeDtatEYMx7jZ2251bmSZtDjxfwNCl5PHncEjNM`): árbol de clases, estadísticas, habilidades y armas. Leerla vía conector de Google Drive (exportar a .xlsx conserva las fórmulas).

## Progresión por temporadas (decidido)

Estilo Lineage 2: el personaje evoluciona eligiendo especializaciones. Cada temporada es un **lanzamiento de contenido** separado en el tiempo, para evitar la carrera al nivel máximo. La duración **no es fija**: se decidirá tras el lanzamiento según el ritmo de los jugadores y el contenido disponible. Además de subir de nivel habrá profesiones, subclases y contenido PvE/PvP (estilo WoW).

La hoja de ruta completa está en `docs/HOJA_DE_RUTA.md`: mantenerla actualizada al cerrar tareas o tomar decisiones.

| Temporada | Niveles | Elección | Clases |
|---|---|---|---|
| 1 | 1–20 | Arquetipo (Físico/Mágico) + clase base | Luchador, Combatiente, Asesino, Atacante a distancia, Mago, Invocador |
| 2 | 20–40 | Especialización 1 | Dos manos, Espadas duales, Tanque, Daguero, Arquero, Hechicero, Encantador… |
| 3 | 40–60 | Especialización final | ~19 clases (Paladín, Berserker, Nigromante, Sacerdote, Monje…) |

Implicaciones técnicas:
- El nivel máximo y las especializaciones disponibles se controlan por **configuración de temporada** (datos), no por código: el sistema debe soportar 60 niveles desde el inicio.
- Cada temporada necesita contenido de **endgame** propio en su nivel máximo (mazmorras, jefes, PvP, equipo, crafteo), con parches intermedios.
- Prever mecánicas de "catch-up" para jugadores que lleguen en temporadas posteriores.
- **Primera versión del juego = Temporada 1** únicamente.
- Temporadas futuras (4, 5…) podrían subir el nivel a 80, 90, 100 y añadir nuevas formas de potenciar al personaje sin tocar la base.

## Documentación

- `docs/RESUMEN_EJECUTIVO.md`: **leer primero** — vista rápida de todo lo decidido, lo pendiente y las recomendaciones.
- `docs/HOJA_DE_RUTA.md`: fases del proyecto y decisiones pendientes.
- Forma de trabajo: la primera conversación fijó los parámetros generales de todos los sistemas; ahora se trabaja **un capítulo de detalle por sesión** (estadísticas, personajes/habilidades, mapas, recursos, objetos, profesiones, contenido por temporada).
- `docs/DISENO_BASE.md`: qué existe en el juego (personajes, mobs, jefes, NPCs, recursos, objetos) y sistemas principales.

Mantener cada fase pequeña y funcional antes de pasar a la siguiente. Datos de balance (estadísticas, escalados) preferiblemente fuera del código (DataTables de Unreal importadas desde CSV/JSON) para poder ajustarlos sin programar.

## Git

- Rama de desarrollo: `claude/videojuego-project-structure-5ofiej`.
