#!/usr/bin/env python3
"""Build the static glyph-only header. Python 3.9+, no packages.
Edit art/creation.txt (hands) or art/wordmark.txt, then run this file.
Use --check to verify generated files without writing.
"""
import argparse
from html import escape
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CELL, LINE, PAD = 9, 18, 24
ALT = 'AKHTAR. Two stippled hands: the left fingers curve gently downward, and the right index reaches toward them across open space.'


def sources():
    hands = (ROOT/'art/creation.txt').read_text(encoding='utf-8').splitlines()
    title = (ROOT/'art/wordmark.txt').read_text(encoding='utf-8').splitlines()
    if len(hands) != 24 or any(len(r) != 178 for r in hands):
        raise ValueError('Hands must occupy a 178-column, 24-row grid.')
    if len(title) != 6 or len({len(r) for r in title}) != 1:
        raise ValueError('Keep the original six-row wordmark on a rectangular grid.')
    for row in hands+title:
        if any(unicodedata.east_asian_width(c) in 'WF' or unicodedata.combining(c) or (c.isspace() and c!=' ') for c in row):
            raise ValueError('Only single-cell glyphs and ordinary spaces are supported.')
    return title, hands


def text(row, y, start=0, scale=1, muted=False):
    chars=[(i,c) for i,c in enumerate(row) if c!=' ']
    if not chars:
        return ''
    xs=' '.join(str(PAD+(start+i*scale)*CELL) for i,c in chars)
    return f'<text x="{xs}" y="{y}" font-size="{15*scale}" fill="#{("9399b2" if muted else "cdd6f4")}">{escape("".join(c for i,c in chars))}</text>'


def svg(title,hands):
    # Fine grid: 178 hand cells + 2 cells of breathing room on either side.
    # The original wordmark uses exactly two fine cells per glyph.
    cols, rows = 184, 43
    width,height=2*PAD+cols*CELL,2*PAD+rows*LINE
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
         '<title id="title">AKHTAR — the moment before creation</title>',
         f'<desc id="desc">{ALT} Entirely static character artwork.</desc>',
         '<style>text{font-family:ui-monospace,"SFMono-Regular",Consolas,"Liberation Mono",monospace;font-variant-ligatures:none}</style>',
         f'<rect width="{width}" height="{height}" fill="#181825"/>',
         text('╭'+'─'*(cols-2)+'╮',PAD+15,muted=True)]
    for r in range(1,rows-1):
        out.append(text('│'+' '*(cols-2)+'│',PAD+r*LINE+15,muted=True))
    out.append(text('╰'+'─'*(cols-2)+'╯',PAD+(rows-1)*LINE+15,muted=True))
    origin=(cols-len(title[0])*2)/2
    for r,line in enumerate(title):
        out.append(text(line,PAD+2*LINE+r*2*LINE+30,origin,2))
    for r,line in enumerate(hands):
        out.append(text(line,PAD+(17+r)*LINE+15,3))
    return '\n'.join(s for s in out if s)+'\n</svg>\n'


def outputs():
    title,hands=sources()
    # A text-only alternative preserves the full fine hand grid at native font size.
    inside=182
    lines=['╭'+'─'*inside+'╮']
    lines+=['│'+l.rstrip().center(inside)+'│' for l in title]
    lines+=['│'+' '*inside+'│']
    lines+=['│'+'  '+l+'  '+'│' for l in hands]
    lines+=['╰'+'─'*inside+'╯']
    return {'assets/creation-static.svg':svg(title,hands),
            'art/README-static.md':'<!-- Generated editable text alternative; wide grids can scroll. -->\n<pre>\n'+escape('\n'.join(lines))+'\n</pre>\n'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true')
    args=p.parse_args();stale=[]
    for name,content in outputs().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8');print('Wrote',name)
    if stale:p.exit(1,'Stale outputs: '+', '.join(stale)+'\n')
    if args.check:print('Static assets match the canonical text.')

if __name__=='__main__':main()
