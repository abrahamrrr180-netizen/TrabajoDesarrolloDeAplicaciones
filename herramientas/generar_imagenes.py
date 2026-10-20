"""Genera las ilustraciones SVG del blog en src/img."""
import math, os, sys
from math import comb

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
SANS = "font-family=\"'IBM Plex Sans','Segoe UI',Helvetica,Arial,sans-serif\""
MONO = "font-family=\"'IBM Plex Mono',Consolas,'Courier New',monospace\""
SERIF = "font-family=\"Fraunces,Georgia,'Times New Roman',serif\""


def save(name, body, w=1200, h=630, label=""):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'role="img" aria-label="{label}">\n{body}\n</svg>\n')
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)


# ---------------------------------------------------------------- favicon
save("favicon.svg", """
<rect width="64" height="64" rx="14" fill="#C2410C"/>
<path d="M20 12v40h14a12 12 0 0 0 0-24H20" fill="none" stroke="#F4EFE6" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
""", 64, 64, "Logotipo de Bitácora")

# ---------------------------------------------------------------- portada 1: gasolineras
rows = [("GASOLINA 95", "1,589"), ("GASÓLEO A", "1,479"), ("GASOLINA 98", "1,729")]
board = ""
for i, (k, v) in enumerate(rows):
    y = 200 + i * 92
    board += f'<rect x="640" y="{y}" width="420" height="72" rx="10" fill="#0B2A27"/>'
    board += f'<text x="664" y="{y+45}" {SANS} font-size="22" font-weight="600" fill="#9FD3C7" letter-spacing="2">{k}</text>'
    board += f'<text x="1036" y="{y+50}" {MONO} font-size="40" font-weight="500" fill="#FFB547" text-anchor="end">{v}</text>'
# mini gráfica de precios
pts = [1.62, 1.60, 1.61, 1.58, 1.57, 1.59, 1.55, 1.56, 1.53, 1.54]
xs = [660 + i * 42 for i in range(len(pts))]
ys = [520 + (1.62 - p) * 900 for p in pts]
path = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in zip(xs, ys))
save("portada-gasolineras.svg", f"""
<rect width="1200" height="630" fill="#134E48"/>
<circle cx="1110" cy="80" r="220" fill="#17605A"/>
<circle cx="120" cy="600" r="180" fill="#17605A"/>
<!-- surtidor -->
<g transform="translate(170 120)">
  <rect x="0" y="40" width="250" height="400" rx="26" fill="#F4EFE6"/>
  <rect x="0" y="40" width="250" height="70" rx="26" fill="#C2410C"/>
  <rect x="0" y="85" width="250" height="25" fill="#C2410C"/>
  <rect x="34" y="140" width="182" height="110" rx="10" fill="#0B2A27"/>
  <text x="125" y="208" {MONO} font-size="44" fill="#FFB547" text-anchor="middle">1,479</text>
  <rect x="44" y="280" width="70" height="34" rx="8" fill="#E8DFD0"/>
  <rect x="136" y="280" width="70" height="34" rx="8" fill="#E8DFD0"/>
  <rect x="44" y="330" width="162" height="70" rx="10" fill="#E8DFD0"/>
  <rect x="-20" y="430" width="290" height="34" rx="10" fill="#0B2A27"/>
  <path d="M250 150 h40 a24 24 0 0 1 24 24 v190 a20 20 0 0 0 40 0 v-170" fill="none" stroke="#F4EFE6" stroke-width="14" stroke-linecap="round"/>
  <rect x="338" y="150" width="34" height="56" rx="8" fill="#C2410C"/>
</g>
<!-- tablero -->
<text x="640" y="160" {SANS} font-size="24" font-weight="600" fill="#F4EFE6" letter-spacing="4">PRECIOS HOY · €/L</text>
{board}
<path d="{path}" fill="none" stroke="#FFB547" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="{xs[-1]}" cy="{ys[-1]:.0f}" r="8" fill="#FFB547"/>
""", label="Ilustración de un surtidor y un panel de precios de carburantes")

# ---------------------------------------------------------------- fig: arquitectura
boxes = [
    ("Ministerio", "API REST · JSON", "#E8DFD0", "#1D1B18"),
    ("Lector", "descarga y caché", "#F4EFE6", "#1D1B18"),
    ("Parser", "JSON → Estacion", "#F4EFE6", "#1D1B18"),
    ("Modelo", "List&lt;Estacion&gt;", "#F4EFE6", "#1D1B18"),
    ("Vista Swing", "JTable + controles", "#134E48", "#F4EFE6"),
]
g = ""
bw, gap, x0 = 196, 36, 22
for i, (t, s, fill, ink) in enumerate(boxes):
    x = x0 + i * (bw + gap)
    g += f'<rect x="{x}" y="70" width="{bw}" height="120" rx="14" fill="{fill}" stroke="#1D1B18" stroke-width="2"/>'
    g += f'<text x="{x+bw/2}" y="122" {SANS} font-size="24" font-weight="600" fill="{ink}" text-anchor="middle">{t}</text>'
    g += f'<text x="{x+bw/2}" y="156" {MONO} font-size="15" fill="{ink}" text-anchor="middle" opacity=".85">{s}</text>'
    if i < len(boxes) - 1:
        ax = x + bw + 4
        g += f'<path d="M{ax} 130 h{gap-12}" stroke="#C2410C" stroke-width="4"/><path d="M{ax+gap-14} 122 l10 8 l-10 8z" fill="#C2410C"/>'
g += f'<path d="M{x0+bw/2+ (bw+gap)} 190 v40 h{3*(bw+gap)} v-40" fill="none" stroke="#1D1B18" stroke-width="2" stroke-dasharray="6 6"/>'
g += f'<text x="{x0+bw/2+2.5*(bw+gap)}" y="262" {SANS} font-size="18" fill="#5B544A" text-anchor="middle">SwingWorker: todo esto corre fuera del hilo de la interfaz</text>'
save("gasolineras-arquitectura.svg", f'<rect width="1200" height="300" fill="#FBF8F2"/>{g}', 1200, 300,
     "Diagrama de capas: API del Ministerio, lector, parser, modelo y vista Swing")

# ---------------------------------------------------------------- fig: ventana
tabla = [("Repsol", "Av. de Madrid 12", "Logroño", "1,589", "1,479"),
         ("Petronor", "Ctra. N-232 km 3", "Logroño", "1,569", "1,459"),
         ("Ballenoil", "C/ Industria 4", "Lardero", "1,499", "1,399"),
         ("Cepsa", "Av. de Burgos 88", "Logroño", "1,605", "1,495"),
         ("Plenoil", "Pol. Cantabria s/n", "Logroño", "1,509", "1,409")]
cols = [(40, "Rótulo"), (210, "Dirección"), (500, "Municipio"), (700, "95 E5 €/L"), (870, "Gasóleo A €/L")]
rows_svg = ""
for j, (cx, h) in enumerate(cols):
    rows_svg += f'<text x="{cx+60}" y="214" {SANS} font-size="17" font-weight="600" fill="#1D1B18">{h}{" ▲" if j==4 else ""}</text>'
orden = sorted(tabla, key=lambda r: r[4])
for i, r in enumerate(orden):
    y = 232 + i * 52
    fill = "#FFF4E0" if i == 0 else ("#FFFFFF" if i % 2 == 0 else "#F6F3EE")
    rows_svg += f'<rect x="60" y="{y}" width="1080" height="52" fill="{fill}"/>'
    for (cx, _), val in zip(cols, r):
        f = MONO if "," in val else SANS
        rows_svg += f'<text x="{cx+60}" y="{y+33}" {f} font-size="18" fill="#1D1B18">{val}</text>'
save("gasolineras-ventana.svg", f"""
<rect width="1200" height="560" fill="#E8DFD0"/>
<rect x="40" y="30" width="1120" height="510" rx="12" fill="#FFFFFF" stroke="#1D1B18" stroke-width="2"/>
<rect x="40" y="30" width="1120" height="46" rx="12" fill="#134E48"/><rect x="40" y="60" width="1120" height="16" fill="#134E48"/>
<text x="70" y="61" {SANS} font-size="18" font-weight="600" fill="#F4EFE6">Precios de carburantes — España</text>
<circle cx="1080" cy="53" r="8" fill="#F4EFE6" opacity=".5"/><circle cx="1110" cy="53" r="8" fill="#F4EFE6" opacity=".5"/><circle cx="1140" cy="53" r="8" fill="#C2410C"/>
<text x="60" y="122" {SANS} font-size="17" fill="#5B544A">Provincia</text>
<rect x="150" y="98" width="200" height="36" rx="6" fill="#FBF8F2" stroke="#9A9184"/><text x="164" y="122" {SANS} font-size="17" fill="#1D1B18">La Rioja ▾</text>
<text x="380" y="122" {SANS} font-size="17" fill="#5B544A">Combustible</text>
<rect x="490" y="98" width="200" height="36" rx="6" fill="#FBF8F2" stroke="#9A9184"/><text x="504" y="122" {SANS} font-size="17" fill="#1D1B18">Gasóleo A ▾</text>
<rect x="720" y="98" width="260" height="36" rx="6" fill="#FBF8F2" stroke="#9A9184"/><text x="734" y="122" {SANS} font-size="17" fill="#9A9184">Buscar municipio…</text>
<rect x="1000" y="98" width="140" height="36" rx="6" fill="#C2410C"/><text x="1070" y="122" {SANS} font-size="17" font-weight="600" fill="#FFFFFF" text-anchor="middle">Actualizar</text>
<rect x="60" y="186" width="1080" height="46" fill="#E8DFD0"/>
{rows_svg}
<text x="60" y="518" {SANS} font-size="15" fill="#5B544A">Datos de ejemplo · 5 estaciones · ordenado por Gasóleo A (ascendente)</text>
""", 1200, 560, "Esquema de la ventana principal con filtros y una tabla de estaciones ordenada por precio")

# ---------------------------------------------------------------- portada 2: póker
def carta(x, y, rot, valor, palo, color):
    sym = {"c": "♥", "d": "♦", "p": "♠", "t": "♣"}[palo]
    return (f'<g transform="translate({x} {y}) rotate({rot})">'
            f'<rect x="-80" y="-112" width="160" height="224" rx="14" fill="#FBF8F2" stroke="#0E2A20" stroke-width="2"/>'
            f'<text x="-62" y="-70" {SERIF} font-size="40" font-weight="700" fill="{color}">{valor}</text>'
            f'<text x="-60" y="-34" font-size="30" fill="{color}">{sym}</text>'
            f'<text x="0" y="40" font-size="96" fill="{color}" text-anchor="middle">{sym}</text></g>')
R, N = "#C2410C", "#1D1B18"
cartas = (carta(260, 330, -10, "A", "c", R) + carta(400, 315, 6, "K", "c", R)
          + carta(650, 420, 0, "9", "c", R) + carta(830, 420, 0, "4", "c", R) + carta(1010, 420, 0, "Q", "p", N))
fichas = ""
for i, (cx, cy, c) in enumerate([(700, 170, "#C2410C"), (760, 160, "#F4EFE6"), (830, 175, "#E0A526")]):
    for k in range(4):
        fichas += f'<ellipse cx="{cx}" cy="{cy - k*14}" rx="46" ry="16" fill="{c}" stroke="#0E2A20" stroke-width="2"/>'
save("portada-poker.svg", f"""
<rect width="1200" height="630" fill="#1F4D3A"/>
<ellipse cx="640" cy="330" rx="640" ry="360" fill="#25593F"/>
<ellipse cx="640" cy="330" rx="560" ry="290" fill="none" stroke="#2F6B4C" stroke-width="3"/>
{fichas}
{cartas}
<text x="920" y="200" {SERIF} font-size="64" font-weight="700" fill="#F4EFE6">9 outs</text>
<text x="920" y="240" {MONO} font-size="24" fill="#BFE3CF">≈ 35 % al river</text>
""", label="Mesa de póker con un proyecto de color de corazones en el flop")

# ---------------------------------------------------------------- fig: gráfica outs
W, H = 1000, 520
L, Rm, T, B = 90, 30, 40, 80
pw, ph = W - L - Rm, H - T - B
def X(n): return L + (n - 1) / 14 * pw
def Y(p): return T + ph - p / 70 * ph
grid = ""
for p in range(0, 71, 10):
    grid += f'<line x1="{L}" x2="{W-Rm}" y1="{Y(p):.1f}" y2="{Y(p):.1f}" stroke="#E4DCCD"/>'
    grid += f'<text x="{L-12}" y="{Y(p)+6:.1f}" {MONO} font-size="15" fill="#5B544A" text-anchor="end">{p}%</text>'
for n in range(1, 16):
    grid += f'<text x="{X(n):.1f}" y="{T+ph+28}" {MONO} font-size="15" fill="#5B544A" text-anchor="middle">{n}</text>'
grid += f'<text x="{L+pw/2}" y="{H-18}" {SANS} font-size="17" fill="#1D1B18" text-anchor="middle">Número de outs (flop → river, dos cartas por ver)</text>'
exact = [(n, (1 - comb(47 - n, 2) / comb(47, 2)) * 100) for n in range(1, 16)]
r4 = [(n, 4 * n) for n in range(1, 16)]
corr = [(n, 4 * n - max(0, n - 8)) for n in range(1, 16)]
def line(pts, color, dash=""):
    d = "M" + " L".join(f"{X(n):.1f} {Y(p):.1f}" for n, p in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="4" {dash} stroke-linejoin="round"/>'
dots = "".join(f'<circle cx="{X(n):.1f}" cy="{Y(p):.1f}" r="4.5" fill="#1D1B18"/>' for n, p in exact)
ley = (f'<rect x="{L+20}" y="{T+6}" width="330" height="104" rx="8" fill="#FFFFFF" stroke="#E4DCCD"/>'
       f'<line x1="{L+36}" x2="{L+76}" y1="{T+34}" y2="{T+34}" stroke="#1D1B18" stroke-width="4"/>'
       f'<text x="{L+88}" y="{T+40}" {SANS} font-size="16" fill="#1D1B18">Probabilidad exacta</text>'
       f'<line x1="{L+36}" x2="{L+76}" y1="{T+62}" y2="{T+62}" stroke="#C2410C" stroke-width="4" stroke-dasharray="10 7"/>'
       f'<text x="{L+88}" y="{T+68}" {SANS} font-size="16" fill="#1D1B18">Regla del 4 (4·n)</text>'
       f'<line x1="{L+36}" x2="{L+76}" y1="{T+90}" y2="{T+90}" stroke="#0F766E" stroke-width="4"/>'
       f'<text x="{L+88}" y="{T+96}" {SANS} font-size="16" fill="#1D1B18">Con corrección: 4·n − (n − 8)</text>')
save("poker-grafica.svg", f"""
<rect width="{W}" height="{H}" fill="#FBF8F2"/>
{grid}
{line(r4, "#C2410C", 'stroke-dasharray="10 7"')}
{line(corr, "#0F766E")}
{line(exact, "#1D1B18")}
{dots}
{ley}
""", W, H, "Gráfica que compara la probabilidad exacta con la regla del 4 y su corrección para 1 a 15 outs")

# ---------------------------------------------------------------- portada 3: paella
import random
random.seed(7)
cx, cy = 600, 330
granos = ""
for _ in range(900):
    a = random.random() * 2 * math.pi
    r = math.sqrt(random.random()) * 228
    x, y = cx + r * math.cos(a), cy + r * math.sin(a)
    rot = random.random() * 180
    c = random.choice(["#E9B44C", "#E2A93B", "#F0C25E", "#D99A2B"])
    granos += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="7" ry="3" fill="{c}" transform="rotate({rot:.0f} {x:.0f} {y:.0f})"/>'
def gamba(x, y, rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})">'
            f'<path d="M-46 0 C-46 -34 10 -44 40 -18 C52 -6 44 10 30 8 C10 -12 -24 -14 -26 6 Z" fill="#E4572E" stroke="#9E2A0B" stroke-width="2"/>'
            f'<path d="M-46 0 l-18 -14 M-46 0 l-20 6" stroke="#9E2A0B" stroke-width="3"/>'
            f'<circle cx="30" cy="-6" r="3" fill="#1D1B18"/></g>')
def mejillon(x, y, rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})">'
            f'<path d="M0 -34 C26 -30 30 20 0 36 C-30 20 -26 -30 0 -34Z" fill="#23233A" stroke="#0E0E1C" stroke-width="2"/>'
            f'<path d="M0 -24 C14 -18 16 14 0 24 C-16 14 -14 -18 0 -24Z" fill="#F0A35E"/></g>')
def limon(x, y, rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})">'
            f'<path d="M-34 0 A34 34 0 0 1 34 0 Z" fill="#F2D53C" stroke="#C9A80F" stroke-width="3"/>'
            f'<path d="M0 0 L-22 -20 M0 0 L0 -28 M0 0 L22 -20" stroke="#E8C51E" stroke-width="2"/></g>')
mar = ""
for i in range(8):
    a = i / 8 * 2 * math.pi + 0.2
    mar += gamba(cx + 150 * math.cos(a), cy + 150 * math.sin(a), math.degrees(a) + 90)
for i in range(7):
    a = i / 7 * 2 * math.pi
    mar += mejillon(cx + 78 * math.cos(a), cy + 78 * math.sin(a), math.degrees(a))
mar += limon(cx, cy - 6, 0) + limon(cx + 196, cy + 60, 120) + limon(cx - 190, cy - 80, -60)
save("portada-paella.svg", f"""
<rect width="1200" height="630" fill="#C2410C"/>
<circle cx="600" cy="330" r="420" fill="#B23A0A"/>
<!-- quemador visto por debajo -->
<!-- asas -->
<rect x="268" y="306" width="70" height="40" rx="20" fill="#2B2B2B"/>
<rect x="862" y="306" width="70" height="40" rx="20" fill="#2B2B2B"/>
<circle cx="{cx}" cy="{cy}" r="282" fill="#3A3A3A"/>
<circle cx="{cx}" cy="{cy}" r="262" fill="#4A4A4A"/>
<circle cx="{cx}" cy="{cy}" r="244" fill="#C98A23"/>
{granos}
{mar}
<text x="60" y="590" {MONO} font-size="22" fill="#FFE2C7" letter-spacing="2">PAELLERA Ø 60 cm · 12–14 RACIONES</text>
""", label="Paella marinera vista desde arriba con gambas, mejillones y limón")

# ---------------------------------------------------------------- fig: fuego
fases = [  # (inicio min, fin min, nombre, nivel 0-3, color)
    (0, 4, "Marcar marisco", 2, "#E0A526"),
    (4, 10, "Sepia", 2, "#E0A526"),
    (10, 22, "Sofrito", 1, "#F0C25E"),
    (22, 26, "Caldo a hervir", 3, "#C2410C"),
    (26, 36, "Arroz · fuerte", 3, "#C2410C"),
    (36, 44, "Arroz · suave", 1, "#F0C25E"),
    (44, 46, "Socarrat", 3, "#9E2A0B"),
    (46, 51, "Reposo", 0, "#BDB3A3"),
]
W, H = 1100, 400
L, T = 70, 40
pw = W - L - 40
def XM(m): return L + m / 51 * pw
base = 290
fb = ""
for i in range(4):
    y = base - i * 60
    fb += f'<line x1="{L}" x2="{W-40}" y1="{y}" y2="{y}" stroke="#E4DCCD"/>'
fb += f'<text x="{L-10}" y="{base-180+6}" {SANS} font-size="15" fill="#5B544A" text-anchor="end">Alto</text>'
fb += f'<text x="{L-10}" y="{base-60+6}" {SANS} font-size="15" fill="#5B544A" text-anchor="end">Bajo</text>'
fb += f'<text x="{L-10}" y="{base-120+6}" {SANS} font-size="15" fill="#5B544A" text-anchor="end">Medio</text>'
fb += f'<text x="{L-10}" y="{base+6}" {SANS} font-size="15" fill="#5B544A" text-anchor="end">Off</text>'
for k, (a, b, n, lv, c) in enumerate(fases):
    x1, x2 = XM(a), XM(b)
    h = max(lv * 60, 8)
    fb += f'<rect x="{x1+2:.1f}" y="{base-h}" width="{x2-x1-4:.1f}" height="{h}" rx="6" fill="{c}"/>'
    ty = base + 34 + (k % 2) * 26
    fb += f'<text x="{(x1+x2)/2:.1f}" y="{ty}" {SANS} font-size="15" fill="#1D1B18" text-anchor="middle">{n}</text>'
for m in range(0, 52, 5):
    fb += f'<text x="{XM(m):.1f}" y="{T+4}" {MONO} font-size="14" fill="#5B544A" text-anchor="middle">{m}′</text>'
fb += f'<text x="{XM(31):.1f}" y="{base-196}" {SANS} font-size="14" fill="#9E2A0B" text-anchor="middle">dos aros</text>'
fb += f'<text x="{XM(40):.1f}" y="{base-76}" {SANS} font-size="14" fill="#5B544A" text-anchor="middle">solo aro interior</text>'
save("paella-fuego.svg", f'<rect width="{W}" height="{H}" fill="#FBF8F2"/>{fb}', W, H,
     "Cronograma de intensidad del fuego por fases durante unos 50 minutos")
print("ok")
