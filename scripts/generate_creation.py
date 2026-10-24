#!/usr/bin/env python3
"""Generate glyph-only header SVGs and a text-only Markdown alternative.

Python 3.9+, standard library only. Edit art/creation.txt, then run this file.
--check exits nonzero when generated assets are stale. No runtime dependencies.
"""
import argparse
from html import escape
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CELL, LINE, PAD, SIZE = 9, 20, 22, 15
ALT = 'AKHTAR. Two stippled hands reach toward one another, their index fingers separated by a small gap.'


def read_art():
    rows = (ROOT / 'art/creation.txt').read_text(encoding='utf-8').splitlines()
    assert len(rows) == 22, 'Keep the established 22-row composition'
    assert all(len(r) == 93 for r in rows), 'Every row must contain 93 single-width cells'
    assert all(unicodedata.east_asian_width(c) not in 'WF' and not unicodedata.combining(c)
               and (c == ' ' or not c.isspace()) for r in rows for c in r), 'Unsupported cell width'
    assert rows[0] == '╭' + '─'*91 + '╮' and rows[-1] == '╰' + '─'*91 + '╯'
    assert all(r[0] == r[-1] == '│' for r in rows[1:-1])
    return rows


def zone(row, col):
    # Give all four sides of the frame the same quiet contrast.
    if col in (0, 92):
        return 'frame'
    # Only the distal index contours move; palms, knuckles and other digits stay fixed.
    if row in (13, 14) and 38 <= col <= 45:
        return 'left'
    if row in (13, 14) and 47 <= col <= 53:
        return 'right'
    return 'still'


def svg(rows, animated=True):
    width, height = 2*PAD + len(rows[0])*CELL, 2*PAD + len(rows)*LINE
    motion = '''
.left { animation: approach-left 10s ease-in-out infinite; }
.right { animation: approach-right 10s ease-in-out infinite; }
.spark { opacity:0; fill:#b4befe; animation: creation 10s ease-in-out infinite; }
@keyframes approach-left { 0%,60%,88%,100% {transform:translateX(0)} 72%,78% {transform:translateX(4px)} }
@keyframes approach-right { 0%,60%,88%,100% {transform:translateX(0)} 72%,78% {transform:translateX(-4px)} }
@keyframes creation { 0%,72%,80%,100% {opacity:0} 76% {opacity:.8} }
@media (prefers-reduced-motion:reduce) {
  .left,.right,.spark {animation:none} .spark {opacity:0}
}
''' if animated else '.spark {opacity:0}'
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           '<title id="title">AKHTAR — the moment before creation</title>',
           '<desc id="desc">'+ALT+(' A ten-second loop: stillness, a slight reach, one lavender pulse, and return.' if animated else '')+'</desc>',
           '<style>text {font-family:ui-monospace,"SFMono-Regular",Consolas,"Liberation Mono",monospace;font-size:15px;font-variant-ligatures:none;fill:#cdd6f4} .frame {fill:#9399b2}' + motion + '</style>',
           f'<rect width="{width}" height="{height}" fill="#181825"/>']
    for row, line in enumerate(rows):
        # Explicit x coordinates for every glyph avoid font fallback and space-width drift.
        start = 0
        while start < len(line):
            group = zone(row, start)
            end = start + 1
            while end < len(line) and zone(row, end) == group:
                end += 1
            chars = [(i,c) for i,c in enumerate(line[start:end],start) if c!=' ']
            if chars:
                xs = ' '.join(str(PAD+i*CELL) for i,c in chars)
                cls = 'frame' if row in (0,len(rows)-1) else group
                out.append(f'<text class="{cls}" x="{xs}" y="{PAD+row*LINE+SIZE}">{escape("".join(c for i,c in chars))}</text>')
            start = end
    # The gap lies between the two index fingertips on row 14.
    out += [f'<text class="spark" x="{PAD+46.5*CELL}" y="{PAD+14*LINE+SIZE}">•</text>', '</svg>']
    return '\n'.join(out)+'\n'


def outputs():
    rows=read_art()
    return {'assets/creation.svg':svg(rows), 'assets/creation-static.svg':svg(rows,False),
            'art/README-static.md':'<!-- Generated from art/creation.txt; entirely text, no images. -->\n<pre>\n'+escape('\n'.join(rows))+'\n</pre>\n'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for name, content in outputs().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8')
            print('Wrote',name)
    if stale:
        parser.exit(1,'Stale assets: '+', '.join(stale)+'\n')
    if args.check:
        print('Generated assets match canonical artwork.')

if __name__=='__main__':
    main()
