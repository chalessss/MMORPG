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
- **Tres informes consecutivos**, nunca uno por acción (para no saturar los sistemas si alguien fabrica, por ejemplo, cada 0,1 s):
  1. **Instantáneo**, al cruzar el límite.
  2. **De 5 minutos**: registro completo de todas las recolecciones o fabricaciones de los 5 minutos siguientes.
  3. **De 1 hora**: el mismo registro durante la hora siguiente.
- **Contenido de los informes**: estadísticas base, todo el equipo, de dónde sale cada % de la estadística, recetas y materiales, hora exacta y tiempo de cada acción; **con quién interactuó** en el **chat** y en el **comercio** (a quién le compró en el mercado, a quién le vendió y con quién hizo intercambios manuales); más adelante, información del dispositivo.
- El registro de chat y comercio sirve para detectar **cuentas mula** (cuentas usadas para mover recursos a otras) y **seguir el movimiento del oro y los recursos** dentro del juego.

## 3. Sanciones (decidido)

- Exploit confirmado en recolección o fabricación (tres informes consecutivos): **ban de 1 año**.
- **Apelación**: el jugador ve un aviso de "su cuenta ha sido suspendida hasta [fecha]" con un **formulario** para explicar por qué cree que el ban o el informe fue injusto; se gestiona como un ticket.

## 4. Pagos y términos y condiciones

- Los **términos y condiciones** dirán que, al alcanzar ciertos límites irregulares, se envía la configuración del personaje y del juego para revisarla, y que puede haber suspensiones.
- **Bloquear devoluciones y contracargos** (*chargebacks*) de una cuenta detectada como fraudulenta, para evitar que alguien use el exploit, mueva los recursos y además recupere su dinero. **Pendiente de validar** con asesoría legal y con las plataformas de pago.

## 5. Mercado: publicación con retraso (decidido)

- Al publicar un objeto en el mercado, **no aparece al momento**: queda como **"pendiente por confirmarse"**.
- El servidor le asigna una hora de publicación **aleatoria entre 15 y 20 minutos** después (por ejemplo, a los 18 min 30 s), y **no se le dice al jugador**: solo ve "pendiente por confirmarse".

## 6. Preguntas abiertas

- Tras el informe de 1 hora, si la irregularidad sigue, ¿empieza un ciclo nuevo de tres informes?
- Mercado: ¿qué se busca exactamente con el retraso (frenar bots que compran y revenden al instante, mover recursos entre cuentas mula…)? ¿Se puede cancelar una publicación pendiente? ¿El objeto queda bloqueado mientras tanto?
