# 2. Facturación fuera de línea y eventos significativos

La facturación en línea depende de la conexión con el SIAT: cada factura se autoriza en el momento de emitirla. Cuando esa conexión se interrumpe, la normativa permite seguir facturando sin conexión y regularizar las facturas después. Para eso existe el botón Fuera de línea del punto de venta y el menú Eventos significativos.

## 2.1 Si el SIN no responde: qué hacer paso a paso

Esta guía es para el caso más común: el SIN está en mantenimiento o no responde, o se cortó el internet del local. No hace falta dejar de vender: el punto de venta se pone **fuera de línea**, se sigue facturando en Odoo y, cuando el servicio vuelve, las facturas se envían solas al SIN. Las secciones siguientes explican la norma con más detalle.

!!! warning "Importante"

    Odoo no pasa solo a fuera de línea. Si el SIN no responde, al confirmar una factura aparece «Sin conexión con los servicios del SIN» y la factura queda en borrador. Hay que poner el punto de venta fuera de línea a mano, como se explica abajo.

### Cómo darse cuenta

- Al confirmar una factura aparece **«Sin conexión con los servicios del SIN»**, o la confirmación tarda y termina en error.
- En el punto de venta, el botón **Verificar conexión con SIAT** (sección 3.4 de la Parte I) no confirma la conexión.
- El SIN publica con anticipación los **mantenimientos programados**: conviene estar atento a sus avisos.

### Qué evento corresponde

| Qué está pasando | Evento | Qué se hace |
|---|---|---|
| Internet funciona, pero el SIN no responde o está en mantenimiento | **2 - Inaccesibilidad al servicio web de la Administración Tributaria** | Fuera de línea en Odoo (pasos de abajo) |
| Se cortó el internet del local | **1 - Corte del servicio de internet** | Fuera de línea en Odoo (pasos de abajo) |
| Falla el propio sistema (Odoo, la computadora o la luz) y no se puede usar | **5, 6 o 7** | Talonario de contingencia con CAFC (sección 2.5) |

### Paso a paso (eventos 1 y 2)

1. **Abrir el punto de venta** que no puede facturar: Ajustes → Facturación (BO) → Compañia → Puntos de Venta → el punto de venta (sección 3.2 de la Parte I). Si la empresa factura desde varios puntos de venta, se hace en cada uno.

1. **Pulsar Fuera de línea.** Odoo abre un evento significativo, guarda la hora de inicio y el CUFD que estaba vigente, y muestra los campos **Evento** y **Facturas por Paquete**.

1. **Revisar el tipo de evento** antes de emitir la primera factura. El evento se crea con el **2** (inaccesibilidad al servicio del SIN), que es el que corresponde a un mantenimiento. Si lo que se cortó es el internet del local, abra el evento desde el campo **Evento** y cámbielo a **1**. Deje **Facturas por Paquete** como está.

1. **Facturar con normalidad.** Las facturas se crean y se confirman igual que siempre; Odoo completa solo la fecha y hora de emisión. Cada factura queda **Registrada**, con su número y su CUF, pero todavía no está validada por el SIN: se valida cuando se envía, al volver en línea.

1. **Entregar la factura al cliente** como siempre: impresa o en PDF. Es válida desde que se emite y lleva una leyenda que indica que fue emitida fuera de línea. El cliente puede verificarla en el SIAT cuando termine la contingencia.

1. **Cuando el SIN vuelva, pulsar En línea** en el mismo punto de venta. Odoo comprueba la conexión, pide un CUFD nuevo, cierra el evento con la hora actual, lo registra en el SIN y envía todas las facturas del evento en paquetes. Si el SIN todavía no responde, aparece «Sin CONEXIÓN con el SIAT» y el punto de venta sigue fuera de línea: espere y vuelva a intentar.

1. **Comprobar que todo quedó validado:**

    - Ajustes → Facturación (BO) → Compañia → **Eventos Significativos**: el evento figura con estado **Enviado**.
    - Ajustes → Facturación (BO) → Compañia → **Paquetes**: el paquete del evento tiene sus líneas en **908 - VALIDADA**.
    - En cada factura, el campo **Estado EDI** dice **VALIDADA**.

!!! note "Nota"

    El evento debe registrarse en el SIN dentro de las **48 horas** posteriores al fin de la contingencia (sección 2.3). No deje el punto de venta fuera de línea más tiempo del necesario: apenas el SIN responda, pulse En línea.

### Qué no se puede hacer mientras el punto de venta está fuera de línea

- **Notas de crédito-débito y otros documentos de ajuste:** Odoo responde «SERVICIO NO DISPONIBLE». Se emiten cuando el punto de venta vuelve a estar en línea.
- **Anular o revertir facturas:** la anulación se hace contra el SIN, así que hay que esperar a que responda (sección 1).

### Si algo falla al volver en línea

- **El evento no se registró** (en la lista de Eventos significativos sigue en **Borrador**): se puede reenviar con el botón de envío de esa fila, siempre dentro del plazo de 48 horas.
- **Un paquete no quedó validado:** abra el paquete en Ajustes → Facturación (BO) → Compañia → **Paquetes**. Cada línea muestra el código y el mensaje del SIN. Los botones **Enviar Facturas** y **Validar Facturas** del paquete, o los botones **R** (recepción) y **V** (validación) de cada línea, permiten reintentar.
- **Error 981 (rango de fechas inválido):** alguna factura quedó con fecha fuera del inicio y el fin del evento. No cambie a mano las fechas de las facturas emitidas durante el evento.

### Si el mantenimiento está anunciado

1. **Antes de que empiece**, pulse **Solicitar CUFD** en cada punto de venta, para que el evento arranque con un CUFD recién pedido. En los eventos 1 y 2 ese CUFD sigue sirviendo hasta 72 horas mientras dure la contingencia.
1. **Al empezar el mantenimiento**, ponga los puntos de venta **fuera de línea** con el evento **2** y siga facturando.
1. **Al terminar**, pulse **En línea** en cada punto de venta y compruebe que los eventos y los paquetes quedaron validados.

## 2.2 Qué es un evento significativo

Un evento significativo es un hecho propio del sistema de facturación que impide seguir emitiendo documentos fiscales en línea. La RND 102100000011 reconoce siete, que son los mismos que ofrece Odoo al registrar el evento: corte del servicio de internet (1), inaccesibilidad al servicio web de la Administración Tributaria (2), ingreso a zonas sin internet por despliegue de punto de venta (3), venta en lugares sin internet (4), virus informático o falla de software (5), cambio de infraestructura de sistema o falla de hardware (6) y corte de suministro de energía eléctrica (7).

La norma no trata a los siete de la misma manera. En los eventos 1 a 4 se siguen emitiendo facturas digitales, pero fuera de línea: son facturas normales que se generan sin conexión y se envían al SIAT cuando esta vuelve. En los eventos 5 a 7, en cambio, el sistema mismo está caído, así que corresponde emitir facturas por contingencia, que son talonarios impresos con un CAFC (Código de Autorización de Factura de Contingencia) solicitado con anticipación al SIN. El botón Fuera de línea de Odoo cubre el primer caso: la emisión sin conexión desde el propio sistema.

Los eventos 3 y 4, que son ventas en zonas sin internet, requieren además una autorización previa del SIN, en la que se describe la operativa, su frecuencia, el periodo y el alcance geográfico.

## 2.3 Vigencia del CUFD y plazos para regularizar

El CUFD dura 24 horas, pero durante una contingencia esa vigencia se extiende: hasta 72 horas en los eventos 1 y 2, y hasta 15 días en los eventos 3 y 4, siempre que el evento esté registrado y la firma digital no esté revocada.

Los plazos que debe tener presentes son tres. El inicio y el fin del evento se registran hasta 48 horas después de concluida la contingencia. Las facturas emitidas fuera de línea se registran dentro de las 48 horas siguientes al restablecimiento de la comunicación con el SIN. Las facturas por contingencia, las del talonario impreso, tienen un plazo mayor: 72 horas desde el restablecimiento. En los eventos 3 y 4 hay un límite adicional: las transacciones de un periodo fiscal no deben registrarse después del día 10 del mes siguiente.

Una factura emitida fuera de línea tiene validez jurídica y probatoria desde que se emite. Al comprador se le entrega el XML y la representación gráfica, que lleva una leyenda indicando que es la representación gráfica de un documento fiscal digital emitido fuera de línea. Si el evento no permite enviarla por correo, se imprime y se entrega sin que el comprador la pida. Una vez terminada la contingencia, el comprador puede verificar la factura en las opciones de consulta del SIAT.

La normativa también exige tener al menos una medida de seguridad prevista para estos casos: generación eléctrica alternativa, equipos o software de respaldo, o un stock de facturas por contingencia. Ese stock no puede superar el 10% de las facturas emitidas en el último periodo reportado; si no existe ese dato, se asigna un talonario por casa matriz o sucursal.

## 2.4 Cómo se maneja en Odoo

El botón Fuera de línea está entre los botones del punto de venta y hace exactamente lo que indica: pone ese punto de venta fuera de línea. Al activarlo se elige cuál de los siete eventos corresponde.

El registro de los eventos se consulta en Facturación (BO), opción Eventos significativos. La lista muestra el nombre del evento, el punto de venta, el tipo de evento elegido, la fecha de inicio, la fecha de finalización, el CUFD con el que se abrió y el estado.

![Captura](../img/parte-3/02-facturacion-fuera-de-linea-y-eventos-significativo-01.webp){ width="624" loading="lazy" }

Las fechas de inicio y finalización se registran automáticamente: no hay que escribirlas. La fecha de inicio queda al poner el punto de venta fuera de línea y la de finalización al volver a ponerlo en línea.

Mientras el punto de venta está fuera de línea, las facturas se emiten con normalidad pero no se envían al SIAT. Quedan guardadas y se envían después, en paquetes. Cuando el punto de venta vuelve a estar en línea, esas facturas se regularizan solas: no hay que enviarlas una por una.

En la lista de eventos, el estado indica en qué situación está cada uno. Un evento en Borrador es un evento todavía no comunicado al SIAT; uno en Enviado ya fue comunicado. Tenga en cuenta los plazos de la sección anterior: el evento debe quedar registrado dentro de las 48 horas posteriores al fin de la contingencia.

## 2.5 Facturas por contingencia con CAFC (eventos 5 a 7)

En los eventos 5, 6 y 7 el que falla es el propio sistema de facturación, así que no se puede emitir ni siquiera fuera de línea. En ese caso se usan **facturas por contingencia**: un talonario impreso, preimpreso con un **CAFC** (Código de Autorización de Facturas de Contingencia) que entrega el SIN, y con un rango de números propio. Durante la contingencia las facturas se llenan a mano; cuando el sistema vuelve, se cargan en Odoo y se envían al SIAT.

**Antes de la contingencia: registrar el CAFC.** Cada talonario autorizado por el SIN se carga una sola vez en Ajustes → Facturación (BO) → Compañia → Códigos CAFC → Nuevo:

- **Código**: el CAFC tal como figura en la autorización del SIN.

- **Sucursal**, **Documento Sector** y **Actividad Económica**: a qué sucursal, tipo de documento y actividad corresponde el talonario. Debe haber un solo CAFC por documento sector y actividad.

- **Rangos** (Desde – Hasta): la numeración impresa del talonario, por ejemplo 1 – 50. La **Secuencia Actual** empieza en el valor Desde y avanza sola con cada factura cargada.

**Durante la contingencia: emitir en papel.** Se llenan las facturas del talonario en orden correlativo y se entrega el original al comprador. No hace falta Odoo para esto.

**Al volver el sistema: cargar las facturas en Odoo.** Con el punto de venta todavía fuera de línea y el evento 5, 6 o 7 elegido (sección 2.4):

1. **Crear una factura por cada factura del talonario**, en el mismo orden en que se emitieron, con el mismo cliente, las mismas líneas y el mismo importe.

1. **Poner la fecha y hora de emisión real** en el campo Fecha y Hora EDI. No puede ser anterior al inicio del evento.

1. **Confirmar.** Odoo marca la factura como **Factura Manual - CAFC**, le asigna el número siguiente del rango del CAFC (no el de la secuencia del punto de venta) y muestra el código en el campo CAFC de la pestaña Factura (BO).

1. **Volver a poner el punto de venta en línea.** Las facturas se envían al SIAT en paquetes, con su CAFC, igual que las de los eventos 1 a 4.

!!! warning "Importante"

    El número que Odoo asigna sale de la Secuencia Actual del CAFC, no del papel. Si las facturas se cargan en otro orden, o se salta una, los números de Odoo dejan de coincidir con los del talonario. Antes de confirmar, compare la Secuencia Actual con el número de la factura en papel. El plazo para regularizar las facturas por contingencia es de 72 horas desde que se restablece el sistema (sección 2.3).

Si al confirmar aparece «No se encontró CAFC's vinculados al documento» o «No se encontró un código CAFC para la Actividad Económica asociada», falta cargar el CAFC de ese tipo de documento y actividad. Si aparece «Ha llegado al final de la secuencia para el CAFC», el talonario se agotó y hay que registrar el siguiente. Las facturas prevaloradas (tipos 23 y 36) no admiten emisión con CAFC.
