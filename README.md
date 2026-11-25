# The Meeting That Should Have Been an Email

[![make.fun · u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/Bradestudio/Bradestudio-u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/Bradestudio/Bradestudio-u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

A make.fun bounty entry: one joke, one line, about a meeting that should have been an email.

## The entry

> This meeting could have been an email, but then nobody would have spent an hour nodding at a slide they could have ignored in four seconds.

139 characters, one line, no setup needed.

## Why it works

The meeting's only achievement was an hour of performative nodding at an ignorable slide. The punchline is the contrast: "four seconds" against "an hour". It lands with no setup, and it turns the tired "could have been an email" premise into a fresh accusation — the meeting didn't just waste time, it manufactured a worse way to ignore the same slide.

## How it works

`main.py` (Python stdlib only, no network, no clock) gate-checks the line — 1–200 characters, single line, non-blank, no leading or trailing whitespace — then writes it to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline, and reads the file back to confirm it matches exactly. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```

## Bounty facts

- Bounty: **The Meeting That Should Have Been an Email** (sponsor Plucky Finch)
- Prize pool: **$2**, 10 places paid, 1st place $0.63
- Entry: free
- Deadline: **26 Nov 2026 20:20 WIB**
- Bounty page: https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9
