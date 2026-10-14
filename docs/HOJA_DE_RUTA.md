# Hoja de ruta

Documento vivo: se actualiza a medida que se toman decisiones. Las fechas y duraciones son orientativas y se ajustarán con datos reales de los jugadores después del lanzamiento.

## Visión

MMORPG en Unreal Engine 5 donde el **personaje es el centro**: empieza sencillo y evoluciona a lo largo de temporadas mediante especializaciones (estilo Lineage 2). Además de subir de nivel, el jugador tiene otras cosas que hacer (estilo World of Warcraft): profesiones, subclases y contenido PvE y PvP.

## Modelo de temporadas

| Temporada | Niveles | Elección del jugador |
|---|---|---|
| 1 | 1–20 | Arquetipo (Físico / Mágico) + clase base (6 clases) |
| 2 | 20–40 | Especialización 1 |
| 3 | 40–60 | Especialización final (~19 clases) |

- Cada temporada es un lanzamiento de contenido. Su duración **no es fija**: se decidirá según cuánto tarden los jugadores en llegar al nivel máximo y cuánto contenido adicional haya.
- Cada temporada debe tener actividades en su nivel máximo (endgame), no solo subida de nivel.
- El sistema técnico soporta los 60 niveles desde el inicio; abrir una temporada es cambiar configuración/datos.

## Principio técnico clave

La lógica del juego (estadísticas, fórmulas, habilidades, progresión) se escribe en **C++**, separada de lo visual (Blueprints, animaciones, modelos). Así:
- se ejecuta en el servidor desde el principio (Unreal tiene red y servidor dedicado integrados): el servidor decide, el cliente muestra,
- se puede probar con pruebas automáticas,
- los valores de balance se cargan desde datos (la hoja de cálculo → DataTables de Unreal), no desde el código.

Estadísticas, habilidades, enfriamientos y efectos se construyen sobre el **Gameplay Ability System (GAS)** de Unreal, que ya resuelve buena parte de lo que necesita un RPG en red.

---

## Fase 0 — Fundamentos y decisiones

- [x] Motor: Unreal Engine 5.5.4
- [x] Modelo de progresión por temporadas
- [x] Hoja de datos de diseño (Google Sheets)
- [x] Juego en **3D**
- [x] Cámara: vista elevada por defecto, ajustable libremente estilo WoW (zoom, rotación, inclinación) para tener visión amplia en PvP
- [x] Plataforma: **solo PC** (ver justificación abajo)
- [x] Concepto de subclases (ver Fase 1)
- [x] Empezar el proyecto desde cero
- [ ] Diseño base: entidades y sistemas del juego (`docs/DISENO_BASE.md`) — borrador hecho, faltan preguntas abiertas
- [ ] Ambientación y estilo artístico
- [ ] Proyecto de Unreal **con C++** en el repositorio, con Git LFS para los archivos binarios

**Por qué solo PC:** controles e interfaz pensados para teclado y ratón sin compromisos; el rendimiento no queda limitado por los móviles; menos frente de bots (granjas de móviles / emuladores); alcance de desarrollo más manejable. Se mantiene la lógica separada del motor para no cerrar la puerta a otras plataformas en el futuro.

## Fase 1 — Sistema de personajes (foco actual)

Objetivo: tener personajes completos a nivel de datos y reglas, aunque visualmente sean básicos.

- [ ] Modelo de datos: arquetipo → clase base → especialización 1 → especialización final
- [ ] Subclases: un mismo personaje puede tener varias clases y cambiar entre ellas sin crear otro personaje ni empezar de cero (el modelo de datos debe soportarlo desde el inicio, aunque la función se active más adelante)
- [ ] Estadísticas principales (STR / INT / AGI) y derivadas (vida, maná, daño, crítico, defensas…)
- [ ] Estadísticas neutrales (evasión, precisión, CDR, PvP, caída de objetos…)
- [ ] Recursos: MP + recurso secundario por clase (Ira, Energía, Foco, Iluminación)
- [ ] Niveles, experiencia y crecimiento de estadísticas por nivel
- [ ] Sistema de habilidades (activas / pasivas, enfriamiento, lanzamiento, alcance, coste)
- [ ] Fórmulas de daño y defensa
- [ ] Armas y su influencia (velocidad de ataque, tipo de arma por clase)
- [ ] Importación de datos desde la hoja de cálculo a DataTables de Unreal
- [ ] Pruebas automáticas de las fórmulas
- [ ] Escena de prueba: crear un personaje, subirlo de nivel y atacar a un muñeco de entrenamiento

## Fase 2 — Mundo y combate PvE básico

- [ ] Movimiento, cámara y controles
- [ ] Enemigos con IA básica
- [ ] Combate en tiempo real usando el sistema de la Fase 1
- [ ] Experiencia por enemigos, botín básico
- [ ] Equipo e inventario

## Fase 3 — Multijugador

- [ ] Elegir solución de red (servidor autoritativo)
- [ ] Varios jugadores viéndose y moviéndose en el mismo mundo
- [ ] Combate sincronizado
- [ ] Cuentas de usuario y guardado de personajes en base de datos

## Fase 4 — Contenido de la Temporada 1

- [ ] Zonas para niveles 1–20
- [ ] NPCs y misiones
- [ ] Mazmorras y jefes
- [ ] Equipo y objetos de la temporada

## Fase 5 — Sistemas sociales y endgame

- [ ] Profesiones (recolección y crafteo)
- [ ] Subclases: activación y reglas para los jugadores
- [ ] Grupos, clanes y chat
- [ ] PvP (duelos, arenas, zonas PvP)
- [ ] Comercio y economía entre jugadores
- [ ] Códice (material por zona, fabricación, mejora, registro, bonificaciones de cuenta)

## Fase 6 — Pruebas y lanzamiento de la Temporada 1

- [ ] Alfa cerrada
- [ ] Balance con datos reales
- [ ] Beta
- [ ] Lanzamiento

## Después del lanzamiento

- Temporada 2 (niveles 20–40, especializaciones)
- Temporada 3 (niveles 40–60, especializaciones finales)
- Parches de contenido entre temporadas

---

## Decisiones pendientes

La lista viva de preguntas abiertas está en `docs/DISENO_BASE.md`, sección 7.
