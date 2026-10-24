# Maintaining this profile

GitHub displays the root `README.md` of this public repository on
[Farhan's profile](https://github.com/farhanakhtar0x66). Review changes through a
pull request before merging into the default branch.

## Edit the profile

- **Introduction:** keep it short, personal, and accurate.
- **Selected work:** three projects, each with a concrete description and useful
  links. Put additional experiments in the disclosure.
- **Learning:** keep the C++/DSA status honest. The current plan begins the week
  of 26 October 2026; update the paragraph and TOML `next` field as work starts.
- **Toolbox:** distinguish languages already used from those being learned.
- **Contact:** use only real public destinations; add coding-profile links when
  the owner supplies them.

The learning roadmap lives in `learning/cpp-dsa.md`. It is a plan, not a progress
tracker. Link a practice repository once one exists rather than publishing
unverified problem counts or completed milestones.

## Edit the static header

Edit `art/creation.txt` for the hands or `art/wordmark.txt` for the lettering.
The fine grid preserves the reference's finger detail. Then run:

```sh
python3 scripts/generate_creation.py
python3 -m unittest discover -s tests -v
```

The generator uses the Python standard library. It updates
`assets/creation-static.svg` and the selectable `art/README-static.md` alternative.
Commit the generated files with their sources. Increment the README image's
version query if GitHub is showing an old cached asset.

The SVG is deliberately static. It contains text glyphs and no runtime code,
remote fonts, image services, or animation. Older `terminal-hero.*` assets and
`scripts/render_hero.py` are legacy artwork and are not used by this README.

## Before merging

Run `python3 scripts/generate_creation.py --check`, the tests above, and
`git diff --check`. Open the branch README on GitHub and inspect the full header,
section links, project links, disclosure, and learning-plan link. Check a narrow
viewport as well as desktop. Keep the header static and the rest of the profile
readable as ordinary text.

The current design rationale and consulted references are recorded in
`docs/profile-design.md`; layout checks are recorded in
`docs/profile-verification.md`.
