"""Render all v*.html thumbnails to PNG at 1280x720 via Playwright, then build a 3x5 contact sheet."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = Path(__file__).resolve().parent
HTMLS = sorted(HERE.glob("v[0-9][0-9]-*.html"))
print(f"found {len(HTMLS)} thumbnail HTML files")

# Render each HTML to its matching PNG
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
    page = context.new_page()
    for html in HTMLS:
        out = html.with_suffix(".png")
        page.goto(html.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(900)  # let webfonts settle
        page.screenshot(
            path=str(out),
            full_page=False,
            clip={"x": 0, "y": 0, "width": 1280, "height": 720},
            omit_background=False,
            type="png",
        )
        print(f"  OK  {out.name}  ({out.stat().st_size//1024} KB)")
    browser.close()

# Build contact sheet: 3 columns x 5 rows, each cell scaled to 426x240 (1280/3 ~= 426)
print("\nbuilding contact sheet...")
COLS, ROWS = 3, 5
CELL_W, CELL_H = 426, 240  # 426*3=1278 + 6 padding margin
PAD = 12
LABEL_H = 32
sheet_w = COLS * CELL_W + (COLS + 1) * PAD
sheet_h = ROWS * (CELL_H + LABEL_H) + (ROWS + 1) * PAD
sheet = Image.new("RGB", (sheet_w, sheet_h), (13, 17, 23))

from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("arial.ttf", 14)
except Exception:
    font = ImageFont.load_default()

pngs = sorted(HERE.glob("v[0-9][0-9]-*.png"))
for i, png in enumerate(pngs[:15]):
    col = i % COLS
    row = i // COLS
    x = PAD + col * (CELL_W + PAD)
    y = PAD + row * (CELL_H + LABEL_H + PAD)
    img = Image.open(png).convert("RGB").resize((CELL_W, CELL_H), Image.LANCZOS)
    sheet.paste(img, (x, y))
    label = f"{png.stem}"
    draw.text((x + 4, y + CELL_H + 6), label, fill=(220, 220, 170), font=font)

contact = HERE / "_contact-sheet.png"
sheet.save(contact, "PNG", optimize=True)
print(f"OK  contact sheet -> {contact.name}  ({contact.stat().st_size//1024} KB)")
print(f"\nall done. {len(pngs)} PNGs + 1 contact sheet in {HERE}")
