"""Verify static source fidelity and reproducible, self-contained outputs."""
import subprocess
import sys
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
NS='{http://www.w3.org/2000/svg}'

class CreationTests(unittest.TestCase):
    def test_static_art_is_current_and_has_no_motion_or_external_content(self):
        subprocess.run([sys.executable,str(ROOT/'scripts/generate_creation.py'),'--check'],check=True)
        source=(ROOT/'assets/creation-static.svg').read_text()
        tree=ET.fromstring(source)
        self.assertTrue(tree.findall('.//'+NS+'text'))
        for forbidden in ('animation','@keyframes','<animate','<script','<image','<path','foreignObject','@import','url('):
            self.assertNotIn(forbidden,source)
        readme=(ROOT/'README.md').read_text()
        self.assertNotIn('creation.svg',readme)
        self.assertIn('creation-static.svg',readme)

    def test_svg_contains_every_canonical_hand_glyph(self):
        tree=ET.fromstring((ROOT/'assets/creation-static.svg').read_text())
        hands=(ROOT/'art/creation.txt').read_text().splitlines()
        self.assertEqual(len(hands),24)
        for i,line in enumerate(hands):
            node=next(n for n in tree.findall(NS+'text') if n.get('y')==str(24+(17+i)*18+15) and n.get('fill')=='#cdd6f4')
            self.assertEqual(node.text,line.replace(' ',''))
            xs=[float(x) for x in node.get('x').split()]
            self.assertTrue(all(24+3*9<=x<24+181*9 for x in xs))

    def test_text_fallback_preserves_wordmark_column_alignment(self):
        source=(ROOT/'art/wordmark.txt').read_text().splitlines()
        rendered=(ROOT/'art/README-static.md').read_text().split('<pre>\n',1)[1].splitlines()[1:7]
        expected=['│'+line.center(182)+'│' for line in source]
        self.assertEqual(rendered,expected)

if __name__=='__main__':unittest.main()
