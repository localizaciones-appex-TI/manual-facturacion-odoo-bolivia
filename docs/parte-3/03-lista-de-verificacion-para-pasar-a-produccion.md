# 3. Lista de verificación para pasar a producción

Mientras se configura y se prueba, la empresa trabaja en el entorno Pruebas y Piloto, donde las facturas no tienen valor legal. Pasar a producción es cambiar ese entorno y volver a pedir al SIAT los códigos que dependen de él. Esta lista sirve para hacerlo en orden y no olvidar nada; cada punto remite a la sección donde se explica.

!!! warning "Importante"

    Los códigos obtenidos en Pruebas y Piloto (CUIS, CUFD y token) no sirven en producción. Haga el cambio en un momento sin ventas, por ejemplo fuera del horario de atención, y no emita facturas hasta terminar la lista.

## 3.1 Antes del cambio

1. **Sistema autorizado.** Impuestos Nacionales aprobó el sistema para producción y entregó el Código de sistema de producción.

1. **Token delegado de producción** generado en la Oficina Virtual del SIN (sección 1.3 de la Parte I).

1. **Certificado digital vigente**, cargado en Odoo, si la modalidad es Electrónica en línea (sección 1.3 de la Parte I).

1. **Sucursales y puntos de venta** registrados en el SIN con los mismos códigos que en Odoo (secciones 2 y 3 de la Parte I).

1. **Documentos sector habilitados** para el NIT en el SIAT: cada tipo de documento que se vaya a emitir tiene que estar habilitado, además de activo en Odoo, en Códigos de Tipo Documento (la sección de cada documento en la Parte II lo explica).

1. **Talonario de contingencia** y su CAFC, si la empresa lo usará (sección 2.4 de esta parte).

## 3.2 El cambio en Odoo

1. **Tipo de entorno en «Producción»** en la pestaña Facturación (BO) de la empresa (sección 1.3 de la Parte I).

1. **Código de sistema y Token delegado** reemplazados por los de producción.

1. **Simular envío al SIAT desactivado**, si se usó durante las pruebas: con esa casilla activa, las facturas no llegan al SIN.

1. **CUIS nuevo** en cada punto de venta y, después, **CUFD nuevo** (sección 3 de la Parte I). Siempre primero el CUIS.

1. **Catálogos SIAT sincronizados** en producción: actividades, productos y servicios, leyendas, tipos de documento y demás (sección 4 de la Parte I); y la homologación de unidades, países y formas de pago revisada (sección 5 de la Parte I).

1. **Secuencias de los puntos de venta** revisadas: la numeración de producción empieza de nuevo y no debe arrastrar los números usados en las pruebas.

## 3.3 Después del cambio

1. **Una primera factura real** de compra-venta, con un importe bajo, que quede en **VALIDADA**.

1. **Verificación en el SIAT** con el enlace de la pestaña Factura (BO): la factura aparece y ya no lleva la leyenda «sin valor legal» (sección 1.3 de esta parte).

1. **Un documento de cada tipo** que se vaya a usar, antes de facturar en volumen.

1. **Renovación diaria del CUFD** asignada a un responsable: dura 24 horas y no se renueva solo.

1. **Vencimiento del CUIS y del certificado** anotado en la agenda: el CUIS dura 365 días y el certificado tiene su propia fecha de vencimiento.
