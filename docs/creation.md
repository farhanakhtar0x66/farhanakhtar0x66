# AKHTAR — static character artwork

The header is now entirely static. It preserves the original outlined wordmark,
stippled hands, thin frame and Mocha colors. The artificial finger extensions,
creation spark and all animation code have been removed.

The hands use a finer 178-column × 24-row character grid recovered from the
owner's supplied reference, with manual edits to the curved left index contour
and fingertip pad. The left fingers droop naturally; the right index extends
across the open space above its curled fingers. The fingers are not stretched
toward each other or aligned into a horizontal bridge.

## Editable sources

- `art/creation.txt`: the full-resolution hands, using `•`, `.` and spaces.
- `art/wordmark.txt`: the original six-row outlined AKHTAR lettering.
- `art/README-static.md`: generated, entirely text-only alternative.

```sh
python3 scripts/generate_creation.py
python3 scripts/generate_creation.py --check
python3 -m unittest discover -s tests -v
```

Python 3.9+; no packages required. The reference-grid recovery was a one-time
preparation step; regenerating the header needs only these editable text files.

The README displays `assets/creation-static.svg`. It contains real text glyphs,
explicit character positions, and a solid background. No traced paths, raster
artwork, scripts, animation, remote fonts, or external services. The wordmark
uses twice the hand grid's cell size to preserve its original proportions while
the finer hand grid retains finger joints that the old coarse grid discarded.

Trade-off: GitHub displays the SVG as an image; its text is editable in the
canonical sources but is not directly selectable in the README image. The
linked text-only alternative is selectable and scrolls horizontally where
necessary. A dense hand grid cannot retain this detail in a narrow plain `<pre>`
block. The SVG scales the complete composition to the available width.

The artwork is static for every viewer, including those requesting reduced
motion. Descriptive alt text accompanies the README image. The rest of the
README is preserved byte-for-byte after its original header.
