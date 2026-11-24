---
hide:
  - navigation
---

# Preguntas frecuentes

Respuestas cortas a las dudas más comunes. Haga clic en una pregunta para ver la respuesta; cada una enlaza a la sección del manual que lo explica en detalle.

## Facturación del día a día

??? question "Al confirmar aparece «CUFD inválido». ¿Qué hago?"

    El CUFD del punto de venta venció (dura 24 horas) o **otro sistema pidió un CUFD nuevo** para el mismo punto de venta, y eso invalida el anterior. Abra el punto de venta, pulse **Solicitar CUFD** y vuelva a confirmar la factura, que quedó en borrador.

    Ver [Solicitar el CUIS y el CUFD](parte-1/03-configuracion-de-puntos-de-venta.md#33-solicitar-el-cuis-y-el-cufd).

??? question "¿Cada cuánto hay que pedir el CUFD y el CUIS?"

    El **CUFD** dura **24 horas** y el **CUIS**, **365 días**. Ninguno de los dos se renueva solo: hay que pedirlos con los botones **Solicitar CUFD** y **Solicitar CUIS** del punto de venta, o con **Actualizar CUFD(S)** y **Actualizar CUIS(S)** desde la sucursal para todos sus puntos de venta a la vez.

    Ver [Solicitar el CUIS y el CUFD](parte-1/03-configuracion-de-puntos-de-venta.md#33-solicitar-el-cuis-y-el-cufd).

??? question "La factura quedó «Registrada» pero no tiene número de factura ni CUF. ¿Se emitió?"

    No: el SIN no la recibió. Pasa cuando se confirma sin la casilla **Factura (BO)**, normalmente porque el diario de ventas no tiene activado el interruptor Factura (BO). Restablezca la factura a borrador, marque **Factura (BO)** en la pestaña del mismo nombre y vuelva a confirmar.

    Ver [Activar la facturación BO en el diario de ventas](parte-1/03-configuracion-de-puntos-de-venta.md#36-activar-la-facturacion-bo-en-el-diario-de-ventas).

??? question "La pantalla se quedó cargando al confirmar. ¿Vuelvo a confirmar?"

    Primero **recargue la factura**. El SIN pudo responder lento y la emisión haberse completado igual: si el **Estado EDI** dice **VALIDADA**, la factura ya está emitida y no hay que hacer nada más. Solo si sigue en borrador, vuelva a confirmar.

??? question "En «Tipo Documento» no aparece el documento que necesito."

    El punto de venta elegido no tiene la secuencia de ese tipo de documento. Agréguela en la pestaña **Secuencias Documentos** del punto de venta, o con el botón **Crear Secuencia**.

    Ver [Pestañas inferiores del punto de venta](parte-1/03-configuracion-de-puntos-de-venta.md#35-pestanas-inferiores).

??? question "El SIN no reconoce el NIT del cliente. ¿Puedo emitir igual?"

    Verifíquelo primero con el botón **Consultar NIT con SIAT** de la factura en borrador. Si el NIT está bien escrito y aun así debe emitir, marque **Forzar Envío** en la pestaña **Factura (BO)**: el SIN registra la factura con una observación.

??? question "¿Cómo hago un descuento sobre el total de la factura?"

    Con el **descuento global**: el botón **%** de la factura en borrador permite aplicar un monto o un porcentaje sobre el total, y Odoo lo reparte entre las líneas. Para descontar un solo producto, use la columna de descuento de esa línea.

    Ver [Descuento global](parte-3/03-descuento-global.md).

## Corregir una factura

??? question "Me equivoqué en una factura. ¿La anulo o hago una nota de crédito?"

    - **Anule** si la factura se emitió mal: datos del cliente, montos o documento equivocados.
    - **Emita una nota de crédito-débito** si la venta fue correcta pero después hubo una devolución, total o parcial.

    Ver [¿Anular o emitir una nota de crédito?](parte-3/01-anulacion-y-reversion.md#11-anular-o-emitir-una-nota-de-credito).

??? question "¿Hasta cuándo puedo anular una factura?"

    Según el SIN, una factura puede pasar de válida a anulada desde que se emite **hasta el día 9 del mes siguiente**. Después de esa fecha, la corrección se hace con una nota de crédito-débito.

??? question "Revertí una anulación. ¿Puedo volver a anular la factura?"

    No. Una factura se puede anular una sola vez y esa anulación se puede revertir una sola vez. Si después hay que corregir la venta, use una nota de crédito-débito.

    Ver [Límite: solo una anulación y una reversión](parte-3/01-anulacion-y-reversion.md#15-limite-solo-una-anulacion-y-una-reversion).

??? question "Al anular aparece «ERROR EN LA EJECUCIÓN DEL SERVICIO (RCV)»."

    Es un error del servicio del SIN; la factura sigue válida. Vuelva a intentarlo más tarde. Si el error persiste, repórtelo al SIN o al soporte del sistema.

## Si el SIN no responde

??? question "El SIN está en mantenimiento. ¿Dejo de vender?"

    No. Ponga el punto de venta **fuera de línea**, siga facturando con normalidad y, cuando el SIN vuelva, pulse **En línea**: Odoo registra el evento y envía las facturas solo.

    Ver [Si el SIN no responde: qué hacer paso a paso](parte-3/02-facturacion-fuera-de-linea-y-eventos-significativo.md#21-si-el-sin-no-responde-que-hacer-paso-a-paso).

??? question "¿Qué evento significativo elijo?"

    - **2**, si internet funciona pero el SIN no responde o está en mantenimiento. Es el que Odoo propone por defecto.
    - **1**, si se cortó el internet del local.
    - **5, 6 o 7**, si falla el propio sistema, la computadora o la luz: en ese caso se usa el talonario de contingencia con CAFC.

    Ver [Facturas por contingencia con CAFC](parte-3/02-facturacion-fuera-de-linea-y-eventos-significativo.md#25-facturas-por-contingencia-con-cafc-eventos-5-a-7).

??? question "¿La factura emitida fuera de línea es válida? ¿Qué le entrego al cliente?"

    Sí, es válida desde que se emite. Se le entrega al cliente como siempre, impresa o en PDF; lleva una leyenda que indica que se emitió fuera de línea. Cuando termine la contingencia, el cliente puede verificarla en el SIAT.

??? question "¿Puedo emitir notas de crédito o anular facturas mientras estoy fuera de línea?"

    No. Las notas de crédito-débito y las anulaciones necesitan respuesta del SIN: Odoo responde «SERVICIO NO DISPONIBLE». Hágalas cuando el punto de venta vuelva a estar en línea.

??? question "¿Cuánto tiempo tengo para regularizar las facturas del evento?"

    El evento y las facturas emitidas fuera de línea deben registrarse dentro de las **48 horas** siguientes al fin de la contingencia; las facturas por contingencia del talonario con CAFC, dentro de las **72 horas**. Por eso conviene pulsar **En línea** apenas el SIN responda.

    Ver [Vigencia del CUFD y plazos para regularizar](parte-3/02-facturacion-fuera-de-linea-y-eventos-significativo.md#23-vigencia-del-cufd-y-plazos-para-regularizar).

## Configuración

??? question "Abrimos una sucursal nueva. ¿Qué hay que hacer?"

    Primero registrarla ante Impuestos Nacionales; después crearla en Odoo con el **mismo número de sucursal**, pedir su CUIS y su CUFD y cargar sus puntos de venta.

    Ver [Agregar una sucursal nueva](parte-1/02-configuracion-de-sucursales.md#24-agregar-una-sucursal-nueva).

??? question "¿Qué significan CUF, CUFD, CUIS y CAFC?"

    - **CUIS:** código de inicio del sistema en cada punto de venta; dura 365 días.
    - **CUFD:** código diario que habilita la facturación; dura 24 horas.
    - **CUF:** código único de cada factura emitida.
    - **CAFC:** código de autorización de los talonarios de contingencia.

    Ver el [Glosario](glosario.md).
