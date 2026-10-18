# Simulador de balance

Prueba del muñeco de entrenamiento: cuánto daño hace cada clase de la Temporada 1 golpeando durante 20 minutos a un objetivo sin defensa, a nivel 1. Por ahora solo con golpes blancos (`usar_habilidades = 0` en `parametros.csv`).

```
python3 herramientas/simulador/simular.py
```

Solo necesita Python 3, sin librerías extra. Todos los valores están en `datos/` (CSV): al cambiar un número y volver a ejecutar se ve al momento cómo queda cada clase. Son los mismos datos que más adelante se importarán a las DataTables de Unreal.

| Archivo | Contenido |
|---|---|
| `clases.csv` | Estadísticas base de nivel 1, estadística principal y arma de cada clase |
| `armas.csv` | Velocidad (golpes por segundo, de la hoja) y daño por golpe de cada arma |
| `habilidades.csv` | Daño, enfriamiento, tiempo de lanzamiento y efecto de cada habilidad (`*` = todas las clases) |
| `conversion.csv` | Cuánto da cada punto de STR, INT y AGI |
| `parametros.csv` | Duración de la prueba, crítico base y si se usan habilidades |

Supuestos de esta versión (ver `docs/ESTADISTICAS.md`): el crítico se cuenta por su valor esperado (sin azar), no se gasta maná, no hay defensa y el ataque básico se detiene mientras se lanza una habilidad.
