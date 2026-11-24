# 3. Descuento global

El descuento global es una rebaja sobre el **total de la factura**, no sobre un producto en particular; por ejemplo, un 10 % por pago al contado. Ante el SIN se informa como **descuento adicional** de la factura, y Odoo lo reparte en proporción entre las líneas para que cada una informe su parte.

## 3.1 Descuento por línea o descuento global

- **Descuento por línea:** se carga en la columna de descuento de cada línea y solo afecta a ese producto (paso «Cargar las líneas» de [Factura de compra-venta › Paso a paso](../parte-2/factura-de-compra-venta.md#paso-a-paso-crear-y-emitir-la-factura)).
- **Descuento global:** se aplica una sola vez sobre el total con el botón de descuento de la factura, como se explica abajo.

Los dos se pueden usar en la misma factura.

## 3.2 Configurar el producto de descuento (una sola vez)

Odoo registra el descuento global como una línea con un producto especial. Hay que crearlo antes del primer uso:

1. **Crear el producto.** Facturación → Clientes → Productos → **Nuevo**, con un nombre claro, por ejemplo «Descuento adicional», y tipo **Servicio**.

1. **Marcarlo como descuento global.** En la pestaña **Facturación (BO)**, activar **Producto/Servicio**; al hacerlo aparece la casilla **Es descuento Global**, que también hay que activar.

1. **Guardar.**

!!! note "Nota"

    Debe existir un solo producto marcado como descuento global: Odoo usa el primero que encuentra. Si no hay ninguno, al aplicar el descuento aparece «Si desea aplicar un descuento global, configure el item activando la casilla "Descuento global" en el producto».

## 3.3 Aplicar el descuento en una factura

1. **Cargar la factura en borrador** con todas sus líneas, como cualquier factura del tipo de documento que corresponda.

1. **Pulsar el botón de descuento (%)**, debajo de las líneas de la factura, junto a «Términos y condiciones». Solo aparece mientras la factura está en borrador.

1. **Elegir cómo se expresa el descuento** en la ventana **Descuento global**:

    - **Monto:** se escribe el importe a descontar, en la moneda de la factura.
    - **Porcentaje:** se escribe el porcentaje y Odoo calcula el monto sobre el total de la factura.

1. **Pulsar Aplicar.** Odoo agrega una línea con el producto de descuento y precio negativo, y en los totales aparece **Monto de Descuento**.

1. **Confirmar la factura** como siempre. En la factura impresa el descuento sale en la fila **DESCUENTO Bs** de los totales, y el monto a pagar ya lo descuenta.

Para cambiar el descuento antes de confirmar, se vuelve a pulsar el botón y se aplica el nuevo valor: Odoo reemplaza el monto de la línea de descuento. Para quitarlo, se borra esa línea.

## 3.4 Devoluciones de una factura con descuento global

Al emitir una nota de crédito-débito sobre una factura que tenía descuento global, Odoo quita la línea de descuento de la nota y traslada a cada línea devuelta la parte del descuento que le correspondía en la factura original. Así el importe de la nota coincide con lo que el cliente realmente pagó por esos productos.

Para las devoluciones de facturas con descuento adicional, el SIN tiene un documento propio: la [nota de crédito-débito con descuento (tipo 47)](../parte-2/nota-de-credito-debito-con-descuento.md).
