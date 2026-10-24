# DSA repo, LeetCode card, stack logos, and project catalogue

## DSA solutions

The public repository is [dsa-cpp](https://github.com/farhanakhtar0x66/dsa-cpp).
It starts with zero uploaded solutions, topic folders, C++20 and notes templates,
and a generated solution index. Its Solutions workflow checks each `.cpp` file
independently for syntax and updates the marked README index on main pushes.
The index counts uploaded files; it does not claim judge acceptance.

## LeetCode activity

The owner supplied the public username **farhanakhtar0x66**. Its public API was
read successfully on 24 October 2026 and initially showed zero accepted
problems and an empty submission calendar. Those real values seed the cards.

The card generator and refresh workflow live in `dsa-cpp`, alongside a dated
`data/leetcode.json` snapshot. This profile embeds the generated SVGs from that
repository's main branch. No cross-repository write token or external card
service is needed. The desktop and mobile assets have separate layouts.

Accepted totals are unique accepted problems. The calendar and streak count
all submissions, including unsuccessful attempts, using UTC day buckets from
LeetCode's public calendar. Current streak accepts activity today or yesterday;
best run and active-day totals use the visible past-year window. This is a
calculated submission-day streak, not a claim of accepted solutions every day.

Refresh is scheduled at 07:47 and 19:47 IST, with manual refresh available in
GitHub Actions. Runs and image caches can be delayed. A visible snapshot time
makes stale data identifiable. Failed API/account requests fail the workflow
and retain the last successful committed snapshot; they never generate
invented zero counts. No LeetCode password or session cookie is used.

The initial GitHub LeetCode refresh and Solutions runs both completed
successfully. Generator tests cover honest zero states, unavailable users,
streak gaps, the past-year boundary, and calendar response overlap.

## Language logos

The SVG badges are self-hosted under `assets/stack/`. They use the official
Devicon vector shapes, with the MIT license and original source files vendored
alongside them. Backgrounds, borders, and typography match Catppuccin Mocha.
C++ is explicitly marked as learning. See `stack-assets.md` for sources.

```sh
python3 scripts/generate_stack.py
python3 scripts/generate_stack.py --check
```

## Projects

The **My Projects** button opens `projects/README.md`. It covers all currently
public owned repositories, including the new DSA repository. The two JalNet
repos share a project panel. Team projects and the Omarchy fork are identified.
Private repositories and repositories merely collaborated on are not listed.

The catalogue uses original copy and a theme-matched directory masthead.
Project screenshots link directly to existing public images in the owner's
project repositories. No screenshots or text from the inspiration profile were
copied. The approved AKHTAR / hands header is unchanged.

Inspiration: [SanTiwari07](https://github.com/SanTiwari07), specifically the clear
project entry points and demonstrations, plus the owner's supplied card and
logo-row references.
