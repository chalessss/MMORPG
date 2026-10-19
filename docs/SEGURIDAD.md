# Seguridad, antitrampas y antibots

Estado: **en curso**. Reúne las decisiones de seguridad que van saliendo en los capítulos. Detalle de origen: `docs/ESTADISTICAS_NEUTRALES.md` (7.1, 7.3 y 7.4). La parte técnica (información del dispositivo, herramientas de terceros…) se diseñará más adelante.

## 1. Principio general (decidido)

- El servidor decide todo lo importante (pilar "juego limpio").
- Cualquier estadística o ventaja que llegue a **valores irregulares** debe poder detectarse y generar un informe. Los umbrales se ajustan **temporada a temporada**.

## 2. Alertas automáticas (decidido)

| Alerta | Umbral (Temporada 1) |
|---|---|
| Velocidad de recolección | Más de **200 %** |
| Velocidad de fabricación | Fabricar más rápido que la **mitad del tiempo** de una receta (por ejemplo, **4,9 s o menos** en una receta de 10 s) |

**Protocolo** (para todas las alertas):
- **Silenciosas**: al jugador no se le avisa ni se le bloquea; solo le llega la notificación al equipo de seguridad (ticket tipo Jira, correo al staff…).
- **Informes encadenados**, nunca uno por acción (para no saturar los sistemas si alguien fabrica, por ejemplo, cada 0,1 s):
  1. **Informe 1, instantáneo**, al cruzar el límite. Dispara el informe 2.
  2. **Informe 2, de 5 minutos**: registro completo de todas las recolecciones o fabricaciones de los 5 minutos siguientes. Después se lanza el informe 3.
  3. **Informe 3, de 1 hora**: el mismo registro durante la hora siguiente.
- **Qué se hace con cada resultado:**

| Informe 1 | Informe 2 (5 min) | Informe 3 (1 h) | Acción |
|---|---|---|---|
| Irregular | Irregular | Irregular | **Ban automático** |
| Irregular | Limpio | Limpio | Nada: falso positivo o pico puntual; no se suspende ni se corta el servicio |
| Irregular | Limpio | Irregular | Se **desconecta** la cuenta del servidor (al jugador le parece una caída de internet o del servidor). Al volver a conectarse se hace un **segundo seguimiento de 1 hora**; si también es irregular, ban. Así hay **dos informes de 1 hora** de respaldo y no se banea por uno solo que pudo fallar |

- Al jugador baneado **solo se le dice "actividad irregular"**: nunca qué se detectó ni en qué horario. Los informes de 1 hora quedan como respaldo por si apela.
- **Contenido de los informes**: estadísticas base, todo el equipo, de dónde sale cada % de la estadística, recetas y materiales, hora exacta y tiempo de cada acción; **con quién interactuó** en el **chat** y en el **comercio** (a quién le compró en el mercado, a quién le vendió y con quién hizo intercambios manuales); más adelante, información del dispositivo.
- El registro de chat y comercio sirve para detectar **cuentas mula** (cuentas usadas para mover recursos a otras) y **seguir el movimiento del oro y los recursos** dentro del juego.

## 3. Sanciones (decidido)

- Exploit confirmado en recolección o fabricación (según la tabla de 2): **ban de 1 año**.
- **Apelación**: el jugador ve un aviso de "su cuenta ha sido suspendida hasta [fecha]" con un **formulario** para explicar por qué cree que el ban o el informe fue injusto; se gestiona como un ticket.

## 4. Pagos y términos y condiciones

- Los **términos y condiciones** dirán que, al alcanzar ciertos límites irregulares, se envía la configuración del personaje y del juego para revisarla, y que puede haber suspensiones.
- **Bloquear devoluciones y contracargos** (*chargebacks*) de una cuenta detectada como fraudulenta, para evitar que alguien use el exploit, mueva los recursos y además recupere su dinero. **Pendiente de validar** con asesoría legal y con las plataformas de pago.

## 5. Mercado: publicación con retraso (decidido)

- Al publicar un objeto en el mercado, **sale de la bolsa del jugador** y queda guardado en una bolsa invisible del servidor, en estado **"pendiente por confirmarse"**. Nadie más lo ve; solo el vendedor, como pendiente.
- El servidor le asigna una hora de publicación **aleatoria entre 15 y 20 minutos** después (por ejemplo, a los 18 min 30 s), y **no se le dice al jugador**.
- Mientras está pendiente hay un botón de **cancelar**: el objeto vuelve a la bolsa. Sirve, por ejemplo, si alguien se equivoca de precio (1.000 de oro en vez de 10.000) y así evita que se lo compren al instante.
- Pasado ese tiempo ya **no se puede cancelar**: el objeto pasa a la bóveda del mercado y queda a la venta **hasta 14 días**. Si no se vende, vuelve al vendedor **por correo**.
- Al venderse, el vendedor recibe un **correo** (como en WoW): qué se vendió, por cuánto, la comisión del mercado y lo que recibe.

## 6. Preguntas abiertas

- Ninguna por ahora.
