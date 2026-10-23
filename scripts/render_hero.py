#!/usr/bin/env python3
"""Render the profile's original, self-hosted Catppuccin/terminal ASCII banner.
Requires Pillow: python -m pip install pillow
Usage: python scripts/render_hero.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1200, 436
C = {
    "crust":"#11111b", "mantle":"#181825", "base":"#1e1e2e",
    "surface":"#313244", "overlay":"#45475a", "text":"#cdd6f4",
    "subtext":"#a6adc8", "muted":"#6c7086", "lavender":"#b4befe",
    "blue":"#89b4fa", "green":"#a6e3a1", "peach":"#fab387",
    "mauve":"#cba6f7", "red":"#f38ba8", "yellow":"#f9e2af",
}
def first_font(candidates):
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    # Pillow can also resolve these installed family names on some systems.
    return "DejaVuSansMono.ttf"

MONO = first_font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/System/Library/Fonts/Menlo.ttc",  # macOS
    "/Library/Fonts/Menlo.ttc",
])
BOLD = first_font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/System/Library/Fonts/Menlo.ttc",
    "/Library/Fonts/Menlo.ttc",
])
fn = lambda p,n: ImageFont.truetype(p,n)
f11, f14, f16, f17, f19, f22 = (fn(MONO,n) for n in (11,14,16,17,19,22))
f13b, f17b = fn(BOLD,13),fn(BOLD,17)

# Seven-row ASCII block letterforms: letters are drawn from monospaced glyph cells.
GLYPHS = {
    "F":["11111","11000","11000","11110","11000","11000","11000"],
    "A":["01110","11011","11011","11111","11011","11011","11011"],
    "R":["11110","11011","11011","11110","11100","11010","11011"],
    "H":["11011","11011","11011","11111","11011","11011","11011"],
    "N":["11001","11101","11101","11011","11011","11011","11011"],
}

def art_rows():
    rows = []
    for r in range(7):
        pieces=[]
        for ch in "FARHAN":
            pieces.append("".join("██" if s=='1' else "  " for s in GLYPHS[ch][r]))
        rows.append("  ".join(pieces))
    return rows

ART=art_rows()
# Center columns: name is on left, succinct work interests on the right.

def base_frame():
    im = Image.new("RGB", (W,H), C["crust"])
    d = ImageDraw.Draw(im)
    # Matte, no gradients, no distracting effects.
    d.rounded_rectangle((25,24,W-25,H-24),radius=18,fill=C["base"],outline=C["overlay"],width=2)
    d.rounded_rectangle((26,25,W-26,84),radius=17,fill=C["mantle"])
    d.rectangle((26,64,W-26,84), fill=C["mantle"])
    d.line((27,84,W-27,84),fill=C["surface"],width=2)
    for x,color in [(57,C["red"]),(80,C["yellow"]),(103,C["green"])]:
        d.ellipse((x,49,x+11,60), fill=color)
    d.text((133,44), "farhan@localhost",font=f16,fill=C["subtext"])
    d.text((994,44),"~ / README.md",font=f14,fill=C["muted"])
    d.text((58,109),"$",font=f19,fill=C["green"])
    d.text((82,109),"figlet FARHAN",font=f19,fill=C["text"])
    d.text((1040,111),"[ SESSION 01 ]",font=f14,fill=C["muted"])
    # letter-art with restrained terminal glow color only, no actual blur
    for i,row in enumerate(ART):
        d.text((60,151 + i*27),row,font=f17,fill=C["lavender"])
    # Vertical separator from ASCII block to textual metadata.
    d.line((881,143,881,348),fill=C["surface"],width=2)
    d.text((914,153),"// FOCUS",font=f13b,fill=C["muted"])
    for j,(text,color) in enumerate([
        ("low-level",C["blue"]),("linux",C["mauve"]),("tooling",C["green"]),("experiments",C["peach"]),
    ]):
        y=189+j*36
        d.rectangle((916,y+7,923,y+14),fill=color)
        d.text((940,y-1),text,font=f16,fill=C["text"])
    d.line((58,359,W-58,359),fill=C["surface"],width=2)
    d.text((58,382),"$",font=f19,fill=C["green"])
    d.text((83,383),"printf",font=f17,fill=C["blue"])
    # Right-aligned nonanimated hint gives poster a restrained interface feel.
    d.text((1036,384),"[ RUNNING ]",font=f11,fill=C["muted"])
    return im

# Animate a typed phrase with a slow hold and a blinking block cursor.
PHRASES = [
    ' "building things close to the metal."',
    ' "small tools. difficult problems."',
    ' "curious about how it all works."',
]
frames=[]
def render(phrase, n, cursor=True):
    im=base_frame()
    d=ImageDraw.Draw(im)
    visible=phrase[:n]
    d.text((165,383),visible,font=f17,fill=C["text"])
    if cursor:
        x=165+int(d.textlength(visible,font=f17))+3
        d.rectangle((x,385,x+10,402),fill=C["lavender"])
    return im

# A full loop is roughly ten seconds, with restrained typing and cursor blinks.
for phrase in PHRASES:
    # reveal every two chars at a modest cadence
    for n in range(0,len(phrase)+1,2):
        frames.append(render(phrase,n,True))
    # hold & blink
    for k in range(15):
        frames.append(render(phrase,len(phrase),cursor=(k//4)%2==0))

# A static PNG is available for README users who prefer no motion.
render(PHRASES[0],len(PHRASES[0]),cursor=False).save(OUT/"terminal-hero-static.png",optimize=True)
# Convert to shared palette to reduce GIF size and avoid palette flicker.
from PIL import ImagePalette
pal_image=base_frame().quantize(colors=48,method=Image.Quantize.MEDIANCUT)
quantized=[]
for fr in frames:
    quantized.append(fr.quantize(palette=pal_image,dither=Image.Dither.NONE))
quantized[0].save(OUT/"terminal-hero.gif",save_all=True,append_images=quantized[1:],duration=102,loop=0,optimize=True,disposal=2)
print("Wrote",OUT/"terminal-hero.gif",len(frames),"frames")
