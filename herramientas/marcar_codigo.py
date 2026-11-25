"""Marca como código (letra monoespaciada) lo que el usuario ve tal cual en Odoo o en el SIN.

1. Valores de catálogo con su código:  1 - FACTURA COMPRA-VENTA,  1 - EFECTIVO,  908 - VALIDADA
2. Estados y códigos del SIN:         VALIDADA, ANULACION CONFIRMADA, (código 908)
3. Mensajes de error textuales:       «EL NIT NO TIENE HABILITADO…», «Sin conexión con los servicios del SIN»

No toca títulos, nombres de botones o campos (siguen en negrita) ni rutas de menú.
Las «comillas» que no son mensajes (p. ej. «sección 3.5 de la Parte I») quedan como están.

Uso: python herramientas/marcar_codigo.py docs/parte-2/factura-de-compra-venta.md [más archivos...]
     python herramientas/marcar_codigo.py --todo
"""
import glob
import re
import sys

MAY = 'A-ZÁÉÍÓÚÑÜ'
# 1. "N - TEXTO EN MAYÚSCULAS" (al menos dos letras seguidas en mayúscula). No incluye el punto final.
VALOR = re.compile(rf'(?<![\w`])(\d{{1,3}} - [{MAY}][{MAY}0-9 /().,\-]*[{MAY}0-9)])(?![\w`])')
# 2. Estados del SIN en mayúsculas
ESTADO = re.compile(r'(?<![\w`-])(REVERSION DE ANULACION CONFIRMADA|ANULACION CONFIRMADA|ANULACIÓN CONFIRMADA|VALIDADA|OBSERVADA|RECHAZADA|PENDIENTE|ANULADA)(?![\w`])')
CODIGO = re.compile(r'(código |\()(9\d\d)(?=\)|\b)')


def pegar_numero(valor):
    """1 - FACTURA -> 1 + nbsp + - + nbsp + FACTURA: el número no se separa de la primera palabra al cortar la línea."""
    return re.sub(r'^(\d+) - ', lambda m: m.group(1) + '\u00a0-\u00a0', valor)
# 3. Mensajes entre comillas: los que están mayormente en mayúsculas, o los que el texto presenta como mensaje
COMILLAS = re.compile(r'«([^»\n]{6,}?)»')
PRESENTA = re.compile(r'(aparece|apareció|muestra|responde|respondió|dice|mensaje|error|advierte|avisa|rechaz\w*|observ\w*|devuelve|recomendación|leyenda)[^«»\n]{0,15}$', re.I)


def es_mensaje(texto, antes):
    letras = [c for c in texto if c.isalpha()]
    if letras and sum(c.isupper() for c in letras) / len(letras) > 0.6:
        return True
    return bool(PRESENTA.search(antes)) and not texto.lower().startswith(('sección', 'secciones'))


def marcar_linea(linea):
    if linea.lstrip().startswith('#') or '![' in linea:   # títulos y capturas: no tocar
        return linea
    # Proteger lo que ya es código y las URL de los enlaces
    guardado = []
    def guardar(m):
        guardado.append(m.group(0)); return f'\x00{len(guardado) - 1}\x00'
    s = re.sub(r'`[^`]*`|\]\([^)]*\)', guardar, linea)

    def mensaje(m):
        if es_mensaje(m.group(1), s[:m.start()]):
            return guardar(type('M', (), {'group': lambda self, i=0: f'`{m.group(1)}`'})())
        return m.group(0)
    s = COMILLAS.sub(mensaje, s)
    # el número queda pegado a la primera palabra (espacios no separables): «1 - FACTURA» no se corta tras el 1
    def valor(m):
        v, resto = m.group(1), ''
        if v.endswith(')') and v.count(')') > v.count('('):   # «(1 - EN LÍNEA)»: el paréntesis queda afuera
            v, resto = v[:-1], ')'
        return guardar(type('M', (), {'group': lambda self, i=0: '`' + pegar_numero(v) + '`'})()) + resto
    s = VALOR.sub(valor, s)
    s = ESTADO.sub(lambda m: guardar(type('M', (), {'group': lambda self, i=0: f'`{m.group(1)}`'})()), s)
    s = CODIGO.sub(lambda m: m.group(1) + guardar(type('M', (), {'group': lambda self, i=0: f'`{m.group(2)}`'})()), s)

    for i, g in enumerate(guardado):           # restaurar (pueden estar anidados)
        s = s.replace(f'\x00{i}\x00', g)
    for i, g in enumerate(guardado):
        s = s.replace(f'\x00{i}\x00', g)
    # **`x`** -> `x`  (el código ya se distingue; la negrita sobra)
    s = re.sub(r'\*\*(`[^`]+`)\*\*', r'\1', s)
    # Dentro del código las barras de escape de Markdown se verían tal cual: FAC\_SEG -> FAC_SEG
    s = re.sub(r'`[^`]+`', lambda m: re.sub(r'\\([_*#<>\[\]])', r'\1', m.group(0)), s)
    return s


def marcar(ruta):
    lineas = open(ruta, encoding='utf-8').read().split('\n')
    nuevas = [marcar_linea(l) for l in lineas]
    if nuevas != lineas:
        open(ruta, 'w', encoding='utf-8', newline='\n').write('\n'.join(nuevas))
    return sum(a != b for a, b in zip(lineas, nuevas))


if __name__ == '__main__':
    rutas = glob.glob('docs/**/*.md', recursive=True) if sys.argv[1:] == ['--todo'] else sys.argv[1:]
    for r in rutas:
        n = marcar(r)
        if n:
            print(f'{r}: {n} líneas')
