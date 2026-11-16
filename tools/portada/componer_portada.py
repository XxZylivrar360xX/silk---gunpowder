"""Compone las portadas de la saga sobre una imagen base.

Uso (desde la raiz del vault):
    python -B tools/portada/componer_portada.py [--libro mascaras|sombras|voto|cuentas|juramento|hijos|camino] [--base RUTA] [--salida RUTA]

Reproduce el sistema tipografico de la saga (referencia: *Voto de Ceniza*):
titulo en capitales romanas tipo Trajan, plata cincelada, segunda linea con
inicial alta; "DE" pequeno; rombos rojos en el eje; autor abajo entre
filetes. Escala la base a 2560x4096 (KDP, 1:1.6).
Fichas: 99_Reference/book_covers/00_Portada_*.md
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

W, H = 2560, 4096
FONTS = Path("C:/Windows/Fonts")
F_CAPITAL = FONTS / "PERTILI.TTF"   # Perpetua Titling MT Light (capitales tipo Trajan)
F_RESPALDO = FONTS / "BKANT.TTF"    # Book Antiqua: glifos que Perpetua Titling no trae (·)
SIN_GLIFO = {"·"}
ROJO = (176, 18, 28)
GRIS = (214, 214, 214)
NEGRO = (0, 0, 0)


# ---------- fondo ----------

def base_escalada(ruta: Path) -> Image.Image:
    im = Image.open(ruta).convert("RGB")
    k = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    x0, y0 = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((x0, y0, x0 + W, y0 + H))
    return im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=60, threshold=2))


def degradado(im: Image.Image, y_ini: float, y_fin: float, a_ini: float, a_fin: float) -> None:
    """Oscurece en vertical entre dos alturas (fracciones de H), con curva suave."""
    capa = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(capa)
    y1, y2 = int(y_ini * H), int(y_fin * H)
    for y in range(min(y1, y2), max(y1, y2) + 1):
        t = (y - y1) / (y2 - y1) if y2 != y1 else 1
        t = t * t * (3 - 2 * t)
        d.line([(0, y), (W, y)], fill=int(255 * (a_ini + (a_fin - a_ini) * t)))
    im.paste(Image.new("RGB", (W, H), NEGRO), (0, 0), capa)


def mancha(im: Image.Image, cx: float, cy: float, r: float, a: float) -> None:
    """Oscurecimiento radial suave (para la esquina inferior izquierda)."""
    capa = Image.new("L", (W, H), 0)
    ImageDraw.Draw(capa).ellipse(
        [cx * W - r * W, cy * H - r * W, cx * W + r * W, cy * H + r * W], fill=int(255 * a))
    capa = capa.filter(ImageFilter.GaussianBlur(r * W * 0.45))
    im.paste(Image.new("RGB", (W, H), NEGRO), (0, 0), capa)


# ---------- texto ----------

def fuente(ruta: Path, tam: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(ruta), tam)


def piezas(texto: str, tam: int, tam_inicial: int | None = None):
    """Lista de (caracter, fuente). Con tam_inicial, la primera letra va alta (versalitas)."""
    out = []
    for i, c in enumerate(texto):
        t = tam_inicial if (tam_inicial and i == 0) else tam
        out.append((c, fuente(F_RESPALDO if c in SIN_GLIFO else F_CAPITAL, t)))
    return out


def mascara(pzs, track: float, cx: float, base_y: float, engrosar: int = 0) -> Image.Image:
    """Dibuja centrado sobre una linea base; engrosar dilata el trazo (pixeles impares)."""
    total = sum(f.getlength(c) for c, f in pzs) + track * (len(pzs) - 1)
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    x = cx - total / 2
    for c, f in pzs:
        d.text((x, base_y), c, font=f, fill=255, anchor="ls")
        x += f.getlength(c) + track
    if engrosar:
        m = m.filter(ImageFilter.MaxFilter(engrosar)).filter(ImageFilter.GaussianBlur(0.8))
    return m


def degradado_metal(y0: int, y1: int, paradas) -> Image.Image:
    g = Image.new("RGB", (W, H), NEGRO)
    d = ImageDraw.Draw(g)
    for y in range(y0, y1 + 1):
        t = (y - y0) / max(1, y1 - y0)
        for (t0, c0), (t1, c1) in zip(paradas, paradas[1:]):
            if t0 <= t <= t1:
                u = (t - t0) / (t1 - t0)
                d.line([(0, y), (W, y)], fill=tuple(int(a + (b - a) * u) for a, b in zip(c0, c1)))
                break
    return g


PLATA = [(0.0, (232, 229, 224)), (0.45, (196, 192, 186)), (0.55, (150, 146, 142)),
         (0.70, (208, 204, 198)), (1.0, (138, 134, 130))]


def cincelado(m: Image.Image, relleno: Image.Image, prof: int = 4, fuerza: float = 1.6) -> Image.Image:
    """Bisel: ilumina las caras que miran arriba-izquierda y oscurece las opuestas."""
    h = m.filter(ImageFilter.GaussianBlur(prof * 1.5))
    a = ImageChops.offset(h, prof, prof)
    b = ImageChops.offset(h, -prof, -prof)
    luz = ImageChops.subtract(b, a).point(lambda v: min(255, int(v * fuerza)))
    sombra = ImageChops.subtract(a, b).point(lambda v: min(255, int(v * fuerza)))
    relleno = ImageChops.add(relleno, Image.merge("RGB", (luz, luz, luz)))
    return ImageChops.subtract(relleno, Image.merge("RGB", (sombra, sombra, sombra)))


def titulo(im: Image.Image, pzs, track: float, base_y: float) -> tuple:
    m = mascara(pzs, track, W / 2, base_y, engrosar=5)
    caja = m.getbbox()
    im.paste(Image.new("RGB", (W, H), NEGRO), (0, 10), m.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.85)))
    im.paste(Image.new("RGB", (W, H), (30, 28, 28)), (0, 0), m.filter(ImageFilter.MaxFilter(5)))
    im.paste(cincelado(m, degradado_metal(caja[1], caja[3], PLATA)), (0, 0), m)
    return caja


def texto_fino(im: Image.Image, pzs, track: float, base_y: float, metal=False, color=GRIS, alfa=0.92) -> tuple:
    m = mascara(pzs, track, W / 2, base_y)
    caja = m.getbbox()
    im.paste(Image.new("RGB", (W, H), NEGRO), (0, 4), m.filter(ImageFilter.GaussianBlur(6)))
    if metal:
        im.paste(degradado_metal(caja[1], caja[3], PLATA), (0, 0), m)
    else:
        im.paste(Image.new("RGB", (W, H), color), (0, 0), m.point(lambda v: int(v * alfa)))
    return caja


def linea(d: ImageDraw.ImageDraw, p0, p1, color=GRIS, ancho_px=3, alfa=150) -> None:
    d.line([p0, p1], fill=color + (alfa,), width=ancho_px)


def rombo(d: ImageDraw.ImageDraw, cx: float, cy: float, r: float) -> None:
    d.polygon([(cx, cy - r * 1.35), (cx + r, cy), (cx, cy + r * 1.35), (cx - r, cy)], fill=ROJO + (255,))


# ---------- composicion ----------

LIBROS = {
    # clave: (linea 1, enlace, linea 2, numero romano, mancha en la esquina inferior izquierda)
    "mascaras": ("MÁSCARAS", "DE", "CRISTAL", "I", True),
    "sombras": ("SOMBRAS", "DE", "PODER", "II", False),
    "voto": ("VOTO", "DE", "CENIZA", "III", False),
    "cuentas": ("CUENTAS", "DE", "SANGRE", "IV", False),
    "juramento": ("JURAMENTO", "DE", "HIERRO", "V", False),
    "hijos": ("HIJOS", "DEL", "SILENCIO", "VI", False),
    "camino": ("CAMINO", "A", "CASA", "VII", False),
}


def componer(base: Path, salida: Path, linea1: str, enlace: str, linea2: str,
             libro: str, con_mancha: bool) -> None:
    im = base_escalada(base)
    aplicar_tipografia(im, linea1, enlace, linea2, libro, con_mancha)
    salida.parent.mkdir(parents=True, exist_ok=True)
    im.save(salida, optimize=True)
    print(f"ok: {salida} {im.size}")


def aplicar_tipografia(im: Image.Image, linea1: str, enlace: str, linea2: str,
                       libro: str, con_mancha: bool) -> None:
    """Degradados y tipografia de portada sobre una imagen de W x H (globales del modulo)."""
    degradado(im, 0.0, 0.36, 0.55, 0.0)      # aire para el titulo
    degradado(im, 0.76, 0.97, 0.0, 0.93)     # franja del autor
    if libro in ("III", "V", "VI", "VII"):
        degradado(im, 0.97, 1.0, 0.93, 0.93)  # lo claro asomaba bajo la franja (marmol del III, cobija del V, rio del VI, camino del VII)
    if con_mancha:
        mancha(im, 0.05, 1.0, 0.42, 0.75)    # esquina inferior izquierda

    cx = W / 2
    caja = texto_fino(im, piezas(f"SEDA Y PÓLVORA · LIBRO {libro}", 66), 26, 290)
    c1 = titulo(im, piezas(linea1, 268), 22, 880)
    # ajuste fino por libro, a pedido del autor: (sube el enlace, sube la linea 2), en px
    sube_de, sube_l2 = {"VI": (35, 70)}.get(libro, (0, 0))
    caja_de = texto_fino(im, piezas(enlace, 112), 20, c1[3] + 150 - sube_de, metal=True)
    c2 = titulo(im, piezas(linea2, 268, tam_inicial=336), 22, caja_de[3] + 300 - (sube_l2 - sube_de))

    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    linea(d, (cx, caja[3] + 60), (cx, c1[1] - 50), alfa=130)
    rombo(d, cx, (caja[3] + c1[1]) / 2 + 5, 20)
    yde = (caja_de[1] + caja_de[3]) / 2
    linea(d, (cx - 470, yde), (caja_de[0] - 60, yde), alfa=170)
    linea(d, (caja_de[2] + 60, yde), (cx + 470, yde), alfa=170)
    linea(d, (cx, c2[3] + 60), (cx, c2[3] + 340), alfa=130)
    rombo(d, cx, c2[3] + 200, 20)
    im.paste(capa, (0, 0), capa)

    caja_a = texto_fino(im, piezas("VICTOR PAZ", 104), 30, 3815, alfa=0.95)
    ya = (caja_a[1] + caja_a[3]) / 2
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    linea(d, (180, ya), (caja_a[0] - 80, ya), alfa=170)
    linea(d, (caja_a[2] + 80, ya), (W - 180, ya), alfa=170)
    im.paste(capa, (0, 0), capa)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--libro", choices=sorted(LIBROS), default="mascaras")
    ap.add_argument("--base", default="99_Reference/book_covers/Mascaras_De_Cristal_Colombina_base.webp")
    ap.add_argument("--salida", default="99_Reference/book_covers/Mascaras_De_Cristal_Colombina_v1.png")
    a = ap.parse_args()
    l1, enlace, l2, num, con_mancha = LIBROS[a.libro]
    componer(Path(a.base), Path(a.salida), l1, enlace, l2, num, con_mancha)
