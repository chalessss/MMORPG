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
- Pendiente de definir: 2D o 3D, plataforma (PC / móvil), ambientación y alcance de la primera versión.
- El usuario tiene un diagrama de la estructura base del juego (imagen) y hojas de Google Sheets con datos/fórmulas; preferir leer las hojas vía conector de Google Drive para conservar las fórmulas.

## Plan de trabajo por fases

1. **Documento de diseño corto** (1–2 páginas): qué es el juego y qué entra en la primera versión.
2. **Estructura del proyecto**: tecnología y organización de carpetas (cliente, servidor, código compartido).
3. **Prototipo mínimo**: personaje moviéndose en un mapa y dos jugadores viéndose en tiempo real.
4. **Sistemas incrementales**, uno a la vez: combate, inventario, misiones, cuentas, base de datos…

Mantener cada fase pequeña y funcional antes de pasar a la siguiente. Datos de balance (estadísticas, escalados) preferiblemente fuera del código (tablas / ScriptableObjects) para poder ajustarlos sin programar.

## Git

- Rama de desarrollo: `claude/videojuego-project-structure-5ofiej`.
