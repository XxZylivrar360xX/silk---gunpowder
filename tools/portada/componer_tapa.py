"""Compone la tapa completa (contraportada + lomo + portada) para tapa blanda de KDP.

Uso (desde la raiz del vault):
    python -B tools/portada/componer_tapa.py --libro mascaras --paginas 740 \
        --extension 99_Reference/book_covers/Mascaras_De_Cristal_Colombina_extension.webp \
        --base 99_Reference/book_covers/Mascaras_De_Cristal_Colombina_base.webp \
        --sinopsis 11_Books/Book_01_Mascaras_De_Cristal/00_Sinopsis_Contraportada.md \
        --salida 99_Reference/book_covers/Mascaras_De_Cristal_Tapa_6x9_v1.png

Formato 6 x 9 in, sangrado de 0.125 in, 300 ppp, papel crema (0.0025 in por pagina).
La extension es la imagen base continuada hacia la izquierda; la base se pega
intacta a la derecha para que la portada no cambie. La tipografia de portada es
la de componer_portada.py. El hueco del codigo de barras (abajo a la derecha de
la contraportada) se deja libre: lo pone KDP.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import componer_portada as cp  # noqa: E402

DPI = 300
SANGRADO = 0.125
CORTE_W, CORTE_H = 6.0, 9.0
CREMA = 0.0025                    # pulgadas por pagina
F_TEXTO = cp.FONTS / "GARA.TTF"   # Garamond para la sinopsis
TEXTO = (222, 218, 210)


def px(pulgadas: float) -> int:
    return round(pulgadas * DPI)


def medidas(paginas: int) -> dict:
    lomo = paginas * CREMA
    return {
        "W": px(2 * SANGRADO + 2 * CORTE_W + lomo), "H": px(CORTE_H + 2 * SANGRADO),
        "contra": px(SANGRADO + CORTE_W), "lomo": px(lomo), "lomo_in": lomo,
    }


def fondo(extension: Path, base: Path, W: int, H: int) -> Image.Image:
    ext = Image.open(extension).convert("RGB")
    b = Image.open(base).convert("RGB")
    k = max(W / ext.width, H / ext.height)
    E = ext.resize((round(ext.width * k), round(ext.height * k)), Image.LANCZOS)
    B = b.resize((round(b.width * E.height / b.height), E.height), Image.LANCZOS)
    x0 = E.width - B.width
    m = Image.new("L", B.size, 255)
    d = ImageDraw.Draw(m)
    F = 150                                   # costura difuminada
    for x in range(F):
        d.line([(x, 0), (x, B.height)], fill=int(255 * x / F))
    E.paste(B, (x0, 0), m)
    y0 = (E.height - H) // 2                  # se alinea a la derecha: la portada no se mueve
    return E.crop((E.width - W, y0, E.width, y0 + H))


def con_lienzo(Wv: int, Hv: int):
    """Cambia temporalmente el lienzo de componer_portada."""
    class _L:
        def __enter__(self):
            self.prev = (cp.W, cp.H)
            cp.W, cp.H = Wv, Hv
        def __exit__(self, *a):
            cp.W, cp.H = self.prev
    return _L()


def portada(im: Image.Image, x0: int, libro: tuple) -> None:
    linea1, enlace, linea2, num, con_mancha = libro
    panel = im.crop((x0, 0, im.width, im.height))
    Hv = 4096
    Wv = round(panel.width * Hv / panel.height)
    grande = panel.resize((Wv, Hv), Image.LANCZOS)
    with con_lienzo(Wv, Hv):
        cp.aplicar_tipografia(grande, linea1, enlace, linea2, num, con_mancha)
    im.paste(grande.resize(panel.size, Image.LANCZOS), (x0, 0))


def oscurecer_franja(im: Image.Image, x0: int, x1: int, alfa: float, borde: int) -> None:
    capa = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(capa)
    for x in range(x0 - borde, x1 + borde):
        if x < 0 or x >= im.width:
            continue
        t = 1.0
        if x < x0:
            t = (x - (x0 - borde)) / borde
        elif x >= x1:
            t = ((x1 + borde) - x) / borde
        d.line([(x, 0), (x, im.height)], fill=int(255 * alfa * max(0.0, min(1.0, t))))
    im.paste(Image.new("RGB", im.size, (0, 0, 0)), (0, 0), capa)


def lomo(im: Image.Image, x0: int, ancho: int, libro: tuple) -> None:
    linea1, enlace, linea2, num, _ = libro
    oscurecer_franja(im, x0, x0 + ancho, 0.62, 40)
    L, A = im.height, ancho                   # tira horizontal que luego se gira
    tira = Image.new("RGB", (L, A), (0, 0, 0))
    tira.paste(im.crop((x0, 0, x0 + ancho, L)).rotate(90, expand=True), (0, 0))
    with con_lienzo(L, A):
        def largo(texto, tam, track):
            return sum(f.getlength(c) for c, f in cp.piezas(texto, tam)) + track * (len(texto) - 1)
        nombre = f"{linea1} {enlace} {linea2}"
        tam = min(118, round(A * 0.26))
        while largo(nombre, tam, 12) > L * 0.50 or largo("VICTOR PAZ", round(tam * 0.6), 14) > L * 0.17:
            tam -= 2
        ta = round(tam * 0.6)
        def poner(texto, t_, track, inicio=None, fin=None):
            ln = largo(texto, t_, track)
            cx = inicio + ln / 2 if inicio is not None else fin - ln / 2
            return cp.mascara(cp.piezas(texto, t_), track, cx, A / 2 + round(t_ * 0.72) / 2), ln
        m, _ = poner(nombre, tam, 12, inicio=L * 0.19)
        caja = m.getbbox()
        tira.paste(Image.new("RGB", tira.size, (0, 0, 0)), (0, 5), m.point(lambda v: int(v * 0.8)))
        tira.paste(cp.cincelado(m, cp.degradado_metal(caja[1], caja[3], cp.PLATA), prof=2), (0, 0), m)
        autor, _ = poner("VICTOR PAZ", ta, 14, fin=L * 0.93)
        tira.paste(Image.new("RGB", tira.size, cp.GRIS), (0, 0), autor.point(lambda v: int(v * 0.95)))
        numero, ln_n = poner(num, ta, 10, inicio=L * 0.075)
        tira.paste(Image.new("RGB", tira.size, cp.GRIS), (0, 0), numero)
        capa = Image.new("RGBA", tira.size, (0, 0, 0, 0))
        cp.rombo(ImageDraw.Draw(capa), (L * 0.075 + ln_n + L * 0.19) / 2, A / 2, 12)
        tira.paste(capa, (0, 0), capa)
    im.paste(tira.rotate(-90, expand=True), (x0, 0))


def sinopsis_de(ruta: Path) -> str:
    t = ruta.read_text(encoding="utf-8")
    cuerpo = t.split("---")[1]
    return " ".join(cuerpo.split())


def partir(texto: str, f: ImageFont.FreeTypeFont, ancho: int) -> list[str]:
    lineas, actual = [], ""
    for p in texto.split():
        prueba = f"{actual} {p}".strip()
        if f.getlength(prueba) <= ancho:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def contraportada(im: Image.Image, ancho_contra: int, texto: str, num: str) -> None:
    x0 = px(SANGRADO + 0.55)
    col = px(3.85)
    oscurecer_franja(im, 0, x0 + col + px(0.2), 0.45, px(0.6))
    f = ImageFont.truetype(str(F_TEXTO), 50)          # ~12 pt
    lineas = partir(texto, f, col)
    interlinea = round(50 * 1.5)
    y = px(SANGRADO + 2.0)
    d = ImageDraw.Draw(im)
    for i, ln in enumerate(lineas):
        palabras = ln.split()
        ultima = i == len(lineas) - 1
        if ultima or len(palabras) == 1:
            d.text((x0, y), ln, font=f, fill=TEXTO, anchor="ls")
        else:                                          # justificado
            libre = col - sum(f.getlength(p) for p in palabras)
            hueco = libre / (len(palabras) - 1)
            x = x0
            for p in palabras:
                d.text((x, y), p, font=f, fill=TEXTO, anchor="ls")
                x += f.getlength(p) + hueco
        y += interlinea
    # firma de la saga abajo a la izquierda (el codigo de barras va abajo a la derecha)
    fs = ImageFont.truetype(str(cp.F_CAPITAL), 40)
    marca = f"SEDA Y PÓLVORA · LIBRO {num}"
    yb = im.height - px(SANGRADO + 0.62)
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    cp.rombo(ImageDraw.Draw(capa), x0 + 9, yb - 14, 9)
    im.paste(capa, (0, 0), capa)
    x = x0 + 40
    for c in marca:
        fc = ImageFont.truetype(str(cp.F_RESPALDO), 40) if c in cp.SIN_GLIFO else fs
        d.text((x, yb), c, font=fc, fill=cp.GRIS, anchor="ls")
        x += fc.getlength(c) + 6
    return len(lineas)


def guias(im: Image.Image, m: dict) -> Image.Image:
    g = im.copy()
    d = ImageDraw.Draw(g)
    s = px(SANGRADO)
    rojo, cian = (255, 60, 60), (60, 220, 255)
    d.rectangle([s, s, m["W"] - s, m["H"] - s], outline=rojo, width=4)        # corte
    d.line([(m["contra"], 0), (m["contra"], m["H"])], fill=cian, width=4)    # lomo
    d.line([(m["contra"] + m["lomo"], 0), (m["contra"] + m["lomo"], m["H"])], fill=cian, width=4)
    bx1 = m["contra"] - px(0.25)                                             # codigo de barras
    by1 = m["H"] - s - px(0.25)
    d.rectangle([bx1 - px(2.0), by1 - px(1.2), bx1, by1], outline=(255, 220, 0), width=4)
    return g


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--libro", choices=sorted(cp.LIBROS), required=True)
    ap.add_argument("--paginas", type=int, required=True)
    ap.add_argument("--extension", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--sinopsis", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--guias", help="PNG de revision con corte, lomo y codigo de barras marcados")
    a = ap.parse_args()
    libro = cp.LIBROS[a.libro]
    m = medidas(a.paginas)
    im = fondo(Path(a.extension), Path(a.base), m["W"], m["H"])
    portada(im, m["contra"] + m["lomo"], libro)
    lomo(im, m["contra"], m["lomo"], libro)
    n = contraportada(im, m["contra"], sinopsis_de(Path(a.sinopsis)), libro[3])
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    im.save(a.salida, dpi=(DPI, DPI), optimize=True)
    if a.guias:
        guias(im, m).save(a.guias)
    print(f"ok: {a.salida} {im.size} · lomo {m['lomo_in']:.3f} in ({a.paginas} pp) · sinopsis {n} lineas")


if __name__ == "__main__":
    main()
