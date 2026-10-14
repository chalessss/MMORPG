# CLAUDE.md

Contexto del proyecto para Claude. Léelo al iniciar cada sesión.

## Idioma y comunicación

- Responder siempre en **español**.
- El usuario suele enviar **notas de voz transcritas**: pueden traer muletillas o errores de transcripción (p. ej. "Cloud" = "Claude"). Interpretar la intención y preguntar si algo importante es ambiguo.
- **Mensajes que empiezan con `*`**: son preguntas técnicas o puntuales fuera del flujo del proyecto. Responderlas **sin realizar acciones** sobre el proyecto (no editar archivos, no hacer commits), salvo que se pida explícitamente.

## El proyecto

- Videojuego tipo **MMORPG / RPG online**, empezando prácticamente desde cero.
- **Motor:** Unity (C#).
- Ideas previas: sistema de personajes con estadísticas (vida, daño, armadura) y sus escalados.
- Pendiente de definir: 2D o 3D, plataforma (PC / móvil), ambientación.
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

## Plan de trabajo por fases

1. **Documento de diseño corto** (1–2 páginas): qué es el juego y qué entra en la primera versión.
2. **Estructura del proyecto**: tecnología y organización de carpetas (cliente, servidor, código compartido).
3. **Prototipo mínimo**: personaje moviéndose en un mapa y dos jugadores viéndose en tiempo real.
4. **Sistemas incrementales**, uno a la vez: combate, inventario, misiones, cuentas, base de datos…

Mantener cada fase pequeña y funcional antes de pasar a la siguiente. Datos de balance (estadísticas, escalados) preferiblemente fuera del código (tablas / ScriptableObjects) para poder ajustarlos sin programar.

## Git

- Rama de desarrollo: `claude/videojuego-project-structure-5ofiej`.
