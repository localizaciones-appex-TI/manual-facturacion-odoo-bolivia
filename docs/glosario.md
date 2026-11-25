# Anexo. Glosario

| Término | Qué es |
|---|---|
| SIN | Servicio de Impuestos Nacionales, la entidad que recibe y valida las facturas. |
| SIAT | Sistema del SIN con el que Odoo se comunica para emitir, consultar y anular facturas. |
| NIT | Número de Identificación Tributaria de la empresa o del cliente. |
| Sucursal | Establecimiento registrado ante el SIN. La casa matriz tiene código 0. |
| Punto de venta | Caja o canal desde donde se emite, dentro de una sucursal. Cada uno tiene su código, CUIS, CUFD y secuencias. |
| CUIS | Código Único de Inicio de Sistemas. Habilita al punto de venta para facturar; tiene una vigencia de 365 días (sección 3.1 de la Parte I). |
| CUFD | Código Único de Facturación Diaria. Lo exige cada factura y vence a las 24 horas; pedir uno nuevo invalida el anterior. |
| CUF | Código Único de Factura. Identifica a cada factura ante el SIN y se genera al emitirla. |
| Documento sector | Tipo de documento ante el SIN. Compra-venta es el 1; alquiler de bienes inmuebles el 2; exportación el 3; exportación en libre consignación el 4; servicios turísticos y hospedaje el 6; tasa cero el 8; compra y venta de moneda extranjera el 9; duty free el 10; comercialización de hidrocarburos el 12; servicios básicos el 13; ICE el 14; entidades financieras el 15; hoteles el 16; hospitales y clínicas el 17; exportación de minerales el 20; prevalorada el 23; nota de crédito-débito el 24; exportación de servicios el 28; nota de conciliación el 29; suministro de energía el 31; seguros el 34; compra-venta con bonificaciones el 35; prevalorada sin derecho a crédito fiscal el 36; comercialización de GNV el 37; comercialización de GN y GLP el 39; compra-venta tasas el 41; importación y comercialización de lubricantes el 44; comercial de exportación precio venta el 45; nota de crédito-débito con descuento el 47; nota de crédito-débito ICE el 48; comercialización de combustible el 55. |
| Tipo de emisión | Modalidad de envío: 1 En línea (la habitual), 2 Fuera de línea, 3 Masivo, 4 Contingencia. |
| Leyenda | Frase de la Ley 453 que debe llevar cada factura, según la actividad económica. |
| Código SIAT | Código del producto o servicio en el catálogo del SIN, siempre ligado a una actividad económica. |
| Código Nandina | Clasificación arancelaria que se informa para los bienes. |
| Estado EDI | Respuesta del SIN sobre la factura (`VALIDADA`, `OBSERVADA`, `ANULACIÓN CONFIRMADA`, etc.). |
| Tipo Entorno | Ambiente del SIN al que se conecta el punto de venta: 1 producción, 2 pruebas (piloto). |
