# Manual de facturación en Odoo — Bolivia (SIAT)

Manual de usuario para configurar Odoo y emitir, anular y regularizar documentos fiscales ante el SIN. Se publica como sitio web con [MkDocs](https://www.mkdocs.org/) y el tema [Material](https://squidfunk.github.io/mkdocs-material/).

## Estructura

| Ruta | Contenido |
|---|---|
| `docs/index.md` | Portada |
| `docs/parte-1/` | Parte I. Configuración inicial |
| `docs/parte-2/` | Parte II. Tipos de documento fiscal (una página por documento) |
| `docs/parte-3/` | Parte III. Operaciones comunes |
| `docs/glosario.md` | Glosario |
| `docs/img/` | Capturas de pantalla (WebP) |
| `docs/stylesheets/extra.css` | Colores y estilos propios |
| `mkdocs.yml` | Configuración del sitio y menú |

## Ver el sitio en la computadora

Requiere Python 3.10 o superior.

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Luego abrir <http://127.0.0.1:8000/>. Cada cambio guardado en `docs/` se ve al instante.

## Editar el manual

- Cada página es un archivo Markdown dentro de `docs/`.
- Una página nueva se agrega también al menú, en la sección `nav:` de `mkdocs.yml`.
- Las capturas van en `docs/img/` y se insertan con `![Captura](../img/nombre.webp){ width="624" loading="lazy" }`.
- Los recuadros se escriben como `!!! warning "Importante"` o `!!! note "Nota"`, con el texto sangrado debajo.
- Antes de subir cambios, `mkdocs build --strict` debe terminar sin advertencias: detecta enlaces rotos o a títulos que no existen.

## Publicación

Cada cambio en `main` ejecuta el flujo `.github/workflows/manual.yml`, que construye el sitio y lo deja como artefacto descargable en la pestaña Actions. Si GitHub Pages está activado (Settings → Pages → Source: GitHub Actions) y existe la variable de repositorio `PUBLICAR_PAGES` con valor `true`, además lo publica en Pages.
