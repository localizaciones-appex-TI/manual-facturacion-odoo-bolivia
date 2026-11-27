# Parte IV. Facturación desde otros módulos

Las Partes II y III explican cómo se emite cada documento desde **Facturación**. Algunas aplicaciones de Odoo también emiten facturas ante el SIN sin pasar por ese menú: cada una genera la factura a partir de su propia operación, con el punto de venta del SIAT y el tipo de documento que tenga configurados.

La factura que sale de estos módulos es la misma que se carga a mano: se ve en Facturación › Clientes › Facturas, tiene su **Estado EDI** y se anula, se revierte o se emite fuera de línea como explica la Parte III.

| **Módulo** | **Qué factura** | **Sección** |
|---|---|---|
| Punto de venta (BO) | Cada venta cobrada en la caja, como factura de compra-venta. | [1. Facturación desde el Punto de Venta (PdV)](01-facturacion-desde-el-punto-de-venta.md) |
