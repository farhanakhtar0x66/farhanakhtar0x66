# The moment before creation

The outlined AKHTAR wordmark and stippled hands remain character art. The index
fingers have manually tapered contours and a smaller gap. Palms, curled digits,
lettering and frame remain stationary. No new cursor, reveal or lettering flash.

## Editing and building

Edit `art/creation.txt`, then run:

```sh
python3 scripts/generate_creation.py
python3 -m unittest discover -s tests -v
```

Python 3.9+; standard library only. `--check` verifies checked-in outputs without
writing files. Every source row is exactly 93 single-width cells, including its
border. The wordmark is the original six-row block, centered as a unit.

- `assets/creation.svg`: actual monospaced `<text>` glyphs, explicit cell positions.
- `assets/creation-static.svg`: the same composition without animation.
- `art/README-static.md`: an entirely text-only `<pre>` alternative.

The canonical source contains Unicode box-drawing and stipple glyphs, all one
cell wide in the intended monospace fonts. This is UTF-8 text art rather than
strict seven-bit ASCII. No traced paths, raster images, remote fonts, scripts,
external services, gradients, or runtime packages are used by the new header.
Existing `terminal-hero.*` assets and `render_hero.py` are older, unused artwork;
they remain untouched.

## Timing

The CSS loop lasts ten seconds. From 0–6 seconds everything is still. From
6–7.2 seconds the distal index contours approach by four SVG units each (less
than half a cell); they hold until 7.8 seconds. A single lavender middle dot
fades in and out from 7.2–8 seconds. The fingers return by 8.8 seconds, then stay
still across the loop boundary. The fingertips never touch. No rapid flashing.

## Rendering trade-off and accessibility

Plain Markdown text cannot animate. The README embeds a repository-hosted SVG
image, preserving selectable/editable text in the source and a linked text-only
alternative. The SVG is an image to assistive technology, with descriptive alt
text in the README and its own title/description. Internal CSS disables all
motion for `prefers-reduced-motion: reduce`; the README `<picture>` also selects
the static SVG for that preference where GitHub preserves the source selector.
Without CSS animation the complete still scene remains visible.

The fixed Mocha mantle and text colors preserve contrast on light and dark
GitHub pages. The SVG scales proportionally to available width, including its
frame and all fingers; it does not depend on the README's font metrics. Small
screens retain the complete composition. The linked text version provides
full-size characters and may scroll horizontally on phones.

GitHub's [image documentation](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files)
says SVG inline scripting and animation are unsupported in its file viewer.
That statement alone does not establish behavior for an SVG embedded as a
README image. Actual branch README playback must be tested separately; see
`docs/verification.md` for observed results and limits. Browser preferences,
image-proxy caching and future GitHub behavior can affect playback. A still
scene is always a valid fallback. No GIF should be substituted unless embedded
SVG playback has actually failed.

Composition reference: [Vatican Museums — Creation of Adam](https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/cappella-sistina/volta/storie-centrali/creazione-di-adamo.html),
plus the owner's supplied stippled-hand reference. This work retains the existing
repository artwork and manually revises its fingertips rather than converting
or embedding a painting image.
