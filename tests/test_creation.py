"""Asset contract: layout safety and reproducibility, not visual quality."""
import subprocess
import sys
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class CreationTests(unittest.TestCase):
    def test_assets_are_current_and_safe(self):
        generator = ROOT / 'scripts/generate_creation.py'
        self.assertTrue(generator.exists(), 'creation generator is missing')
        subprocess.run([sys.executable, str(generator), '--check'], check=True)
        for name in ('creation.svg', 'creation-static.svg'):
            source = (ROOT / 'assets' / name).read_text()
            tree = ET.fromstring(source)
            self.assertTrue(tree.findall('.//{http://www.w3.org/2000/svg}text'))
            for forbidden in ('<script', '<image', '<path', 'foreignObject', '@import', 'url('):
                self.assertNotIn(forbidden, source)
        self.assertIn('prefers-reduced-motion', (ROOT/'assets/creation.svg').read_text())

    def test_distal_tip_moves_and_spark_is_centered_in_clear_gap(self):
        tree = ET.fromstring((ROOT / 'assets/creation.svg').read_text())
        nodes = tree.findall('.//{http://www.w3.org/2000/svg}text')
        tips = [n for n in nodes if n.get('y') == '317']
        left = max(float(x) for n in tips if n.get('class') == 'left' for x in n.get('x').split())
        right = min(float(x) for n in tips if n.get('class') == 'right' for x in n.get('x').split())
        # The final '.' of the left index must move with the rest of its tip.
        self.assertEqual(left, 22 + 45*9)
        spark = next(n for n in nodes if n.get('class') == 'spark')
        self.assertEqual(float(spark.get('x')), (left + right)/2)
        self.assertGreaterEqual(right - left - 8 - 9, 9)  # one clear cell even at closest approach

if __name__ == '__main__':
    unittest.main()
