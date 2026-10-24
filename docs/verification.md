# Static header verification — 24 October 2026

This records the header-only revision. Subsequent profile-content changes are
covered separately in `profile-verification.md`.

This revision replaces the animation approach with static text-glyph artwork.
Earlier animation verification is superseded by the owner's observed playback
failure and request to stop pursuing motion.

- Both source/asset tests pass: deterministic generation, valid SVG, absence of
  animation/scripts/external content, and every hand glyph matches the canonical
  text at its assigned position.
- The hands contain 178 columns × 24 rows, preserving the reference's curved left
  index, separated hanging fingers, extended right index and negative space.
- The original six-row wordmark is preserved. It uses a grid exactly twice the
  hand character grid so the title retains its established visual proportions.
- In the header-only revision, README content after the original header was
  byte-for-byte unchanged. Later profile changes were separately requested.
- Desktop static preview inspected at 930-pixel artwork width. Actual GitHub
  branch rendering and a mobile viewport were also inspected before delivery.
- The text-only alternative is deliberately wide and scrollable; the README SVG
  scales down as a complete composition. Individual stipples become fine on
  phones, while the overall hand silhouettes remain visible.

No animation playback is required or claimed. The live profile remains unchanged
until the pull request is merged. Browser checks use the Codex in-app browser;
physical phone and cross-browser font comparisons have not been performed.

![Original and refined static artwork](previews/before-after.png)

![Static GitHub README on mobile](previews/github-mobile.png)
