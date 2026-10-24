#!/usr/bin/env python3
"""Build the self-contained profile badges from vendored Devicon SVGs."""

from __future__ import annotations

import argparse
from copy import deepcopy
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "stack"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

# slug, vendored logo, label, intrinsic width, accent
BADGES = (
    ("rust", "rust", "Rust", 108, "#fab387"),
    ("python", "python", "Python", 124, "#f9e2af"),
    ("c", "c", "C", 100, "#b4befe"),
    ("java", "java", "Java", 108, "#fab387"),
    ("typescript", "typescript", "TypeScript", 156, "#89b4fa"),
    ("shell", "bash", "Shell", 116, "#a6e3a1"),
    ("cpp-learning", "cplusplus", "C++", 164, "#f9e2af"),
    ("git", "git", "Git", 100, "#fab387"),
    ("linux", "linux", "Linux", 116, "#b4befe"),
)


def render(slug: str, logo: str, label: str, width: int, accent: str) -> str:
    source = ET.parse(OUTPUT / "source" / f"{logo}-original.svg").getroot()
    icon = deepcopy(source)
    icon.set("x", "12")
    icon.set("y", "7")
    icon.set("width", "22")
    icon.set("height", "22")
    icon.set("aria-hidden", "true")
    # Preserve every upstream path. Lift only dark monochrome marks for contrast.
    if logo == "rust":
        icon.set("fill", accent)
    elif logo == "bash":
        for node in icon.iter():
            if node.get("fill") == "#293138":
                node.set("fill", "#cdd6f4")
            elif node.get("fill") == "#4fa847":
                node.set("fill", "#a6e3a1")

    title = f"{label} — learning" if slug == "cpp-learning" else label
    learning = (
        '<text x="84" y="22.5" font-size="11" fill="#f9e2af">learning</text>\n'
        if slug == "cpp-learning" else ""
    )
    return (
        f'<svg xmlns="{NS}" width="{width}" height="36" viewBox="0 0 {width} 36" '
        'role="img" aria-labelledby="title">\n'
        f'<title id="title">{escape(title)}</title>\n'
        '<!-- Logo: Devicon, Copyright (c) 2015 konpa, MIT. '
        'Full license and unmodified source: assets/stack/source/. -->\n'
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="35" rx="5" '
        'fill="#1e1e2e" stroke="#313244"/>\n'
        f'<path d="M1 9V27" stroke="{accent}" stroke-width="2"/>\n'
        f'{ET.tostring(icon, encoding="unicode")}\n'
        '<g font-family="DejaVu Sans Mono,Consolas,monospace" font-weight="500" '
        'font-size="13" fill="#cdd6f4">\n'
        f'<text x="45" y="22.5">{escape(label)}</text>\n'
        f'{learning}</g>\n</svg>\n'
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if committed badges differ")
    args = parser.parse_args()
    stale = []
    for badge in BADGES:
        path = OUTPUT / f"{badge[0]}.svg"
        expected = render(*badge)
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(expected, encoding="utf-8")
    if stale:
        parser.exit(1, "Stale badges: " + ", ".join(stale) + "\nRun python3 scripts/generate_stack.py\n")
    print(f"{'Checked' if args.check else 'Generated'} {len(BADGES)} stack badges.")


if __name__ == "__main__":
    main()
