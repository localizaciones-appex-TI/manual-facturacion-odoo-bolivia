# Manual de facturación en Odoo — Bolivia (SIAT)

Manual de usuario para configurar Odoo y emitir, anular y regularizar documentos fiscales ante el SIN.

**Sitio publicado:** <https://localizaciones-appex-ti.github.io/manual-facturacion-odoo-bolivia/>

El sitio se genera con [MkDocs](https://www.mkdocs.org/) y el tema [Material](https://squidfunk.github.io/mkdocs-material/). Este repositorio contiene solo el manual; los módulos de Odoo están en otro repositorio.

## Estructura

| Ruta | Contenido |
|---|---|
| `docs/index.md` | Portada con accesos directos |
| `docs/parte-1/` | Parte I. Configuración inicial (empresa, sucursales, puntos de venta, catálogos) |
| `docs/parte-2/` | Parte II. Tipos de documento fiscal: una página por documento, nombrada por el documento |
| `docs/parte-3/` | Parte III. Operaciones comunes (anulación, fuera de línea y contingencia) |
| `docs/glosario.md` | Glosario |
| `docs/img/` | Capturas de pantalla (WebP), una carpeta por parte |
| `docs/assets/` | Logo e ícono del sitio |
| `docs/stylesheets/extra.css` | Colores de Odoo, portada, pasos numerados |
| `mkdocs.yml` | Configuración del sitio y menú (`nav:`) |

## Ver el sitio en la computadora

Requiere Python 3.10 o superior.

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Luego abrir <http://127.0.0.1:8000/>. Cada cambio guardado en `docs/` se ve al instante.

## Editar el manual

- Cada página es un archivo Markdown dentro de `docs/`. Una página nueva se agrega también al menú, en la sección `nav:` de `mkdocs.yml`.
- **Parte II:** las secciones no llevan número, para no confundirlas con el código del tipo de documento del SIN. Las referencias entre páginas se escriben como enlaces con el nombre de la sección, por ejemplo `[Factura de compra-venta › Errores frecuentes y cómo resolverlos](factura-de-compra-venta.md#errores-frecuentes-y-como-resolverlos)`.
- **Partes I y III:** se numeran (1, 1.1, 1.2…) y se citan como «sección 3.5 de la Parte I».
- Las listas numeradas se muestran como pasos con círculos; las viñetas y capturas de un paso van sangradas con cuatro espacios debajo de él.
- Los recuadros se escriben como `!!! warning "Importante"` o `!!! note "Nota"`, con el texto sangrado debajo.
- Antes de subir cambios, `mkdocs build --strict` debe terminar sin advertencias: detecta enlaces rotos o a títulos que no existen.

## Capturas de pantalla

- Van en `docs/img/<parte>/` en formato WebP y se insertan con `![Captura](../img/parte-1/nombre.webp){ width="624" loading="lazy" }`.
- Lo importante de cada captura se marca con un recuadro rojo.
- **El sitio es público.** Antes de agregar una captura, tape (desenfoque) los datos sensibles: NIT y teléfonos de la empresa, correos, código de sistema, token delegado y el código QR de las facturas impresas.

## Publicación

Cada cambio en `main` ejecuta el flujo `.github/workflows/manual.yml`: construye el sitio y lo publica en GitHub Pages en uno o dos minutos. El estado de cada publicación se ve en la pestaña **Actions**.

La publicación depende de que GitHub Pages esté activado con origen «GitHub Actions» (Settings → Pages) y de la variable de repositorio `PUBLICAR_PAGES` con valor `true` (Settings → Secrets and variables → Actions). Sin esa variable, el flujo solo construye el sitio y lo deja como artefacto descargable.
