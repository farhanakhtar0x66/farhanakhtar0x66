# Stack badge assets

These SVGs are self-hosted and contain the actual vector logo geometry from
[Devicon](https://github.com/devicons/devicon). They use the profile's Catppuccin
Mocha base (`#1e1e2e`), surface border (`#313244`), text (`#cdd6f4`), and restrained
accent colors. Rust and Bash are lifted to readable theme colors; other logos
retain upstream colors. Every path is preserved. The separate C++ badge says
“learning” and belongs with learning content, not the languages-in-use row.

| File in `assets/stack/` | Size | Vendored Devicon logo |
| --- | --- | --- |
| `rust.svg` | 108 × 36 | `rust/rust-original.svg` |
| `python.svg` | 124 × 36 | `python/python-original.svg` |
| `c.svg` | 100 × 36 | `c/c-original.svg` |
| `java.svg` | 108 × 36 | `java/java-original.svg` |
| `typescript.svg` | 156 × 36 | `typescript/typescript-original.svg` |
| `shell.svg` | 116 × 36 | `bash/bash-original.svg` |
| `cpp-learning.svg` | 164 × 36 | `cplusplus/cplusplus-original.svg` |
| `git.svg` | 100 × 36 | `git/git-original.svg` |
| `linux.svg` | 116 × 36 | `linux/linux-original.svg` |

Use separate `<img>` elements with `height="36"` and descriptive alt text so
GitHub wraps badges naturally. Intrinsic width and viewBox are set on each badge;
the labels have spare space for local monospace font fallbacks. No remote fonts,
scripts, linked images, raster content, or external rendering services are used.

## Rebuild

```sh
python3 scripts/generate_stack.py
python3 scripts/generate_stack.py --check
```

The generator uses only the Python standard library and local vendored files.
`--check` compares all nine generated files without writing them.

## Provenance and license

Original SVGs were retrieved through the GitHub connector on 2026-10-24 from
`https://github.com/devicons/devicon/blob/master/icons/<logo>/<logo>-original.svg`.
Unmodified originals are in `assets/stack/source/`; their SHA-256 hashes are
recorded in `assets/stack/source/SHA256SUMS` so the exact source content is
inspectable even if upstream changes. Devicon's upstream
[MIT license](https://github.com/devicons/devicon/blob/master/LICENSE), copyright
(c) 2015 konpa, is retained in `assets/stack/source/LICENSE-devicon.txt`.
The generated files also identify that license in their comments. Logos are
trademarks of their respective owners; their inclusion identifies technologies
and does not imply endorsement.
