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

if __name__ == '__main__':
    unittest.main()
