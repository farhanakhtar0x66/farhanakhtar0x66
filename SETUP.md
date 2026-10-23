# Publish your GitHub profile

GitHub shows `README.md` from a **public repository named exactly `farhanakhtar0x66`** on your profile.

## Fast setup (GitHub CLI installed)

1. Extract this package and open your terminal inside its root folder.
2. Check that you're signed in to the correct GitHub account:

   ```bash
   gh auth status
   ```

3. Run:

   ```bash
   git init -b main
   git add README.md assets/ scripts/ SETUP.md
   git commit -m "feat: design terminal-themed GitHub profile"
   gh repo create farhanakhtar0x66 --public --description "Personal GitHub profile" --source=. --remote=origin --push
   ```

4. Visit https://github.com/farhanakhtar0x66 and refresh. Your profile README should appear above pinned repositories.

If you prefer the GitHub website: go to https://github.com/new, create a **Public** repository named `farhanakhtar0x66` with **no auto-generated README**, then add this folder's files using Git/GitHub Desktop, or upload `README.md` and the `assets/` folder using GitHub's web interface.

## Change the animated header

Edit `scripts/render_hero.py` (phrases, colors, art), then run:

```bash
python -m pip install pillow
python scripts/render_hero.py
git add assets/ scripts/render_hero.py && git commit -m "style: refine animated banner" && git push
```

The GIF runs without JavaScript, a token, external API, or GitHub Actions; the generator is not required for displaying it. The `terminal-hero-static.png` is an accessible still-frame alternative if you prefer to remove animation.

## Clean up your pins (manually on GitHub)

On your GitHub profile, click **Customize your pins** and prioritize:

1. Anpasser
2. Hayate
3. JalNet submission
4. Dotfiles
5. Terminal ASCII Screensaver

`neuromesh` is currently private, so it won't work as a public showcase link. Change that only when you decide it's ready to be public.

## Design notes

- Palette: Catppuccin Mocha, matte colors, no gradients.
- One animated banner rather than competing stats cards or an animated "contribution snake."
- Readable in GitHub's light and dark modes (the banner itself is intentionally dark).
- Reusable self-hosted assets, no third-party uptime or request limits.
