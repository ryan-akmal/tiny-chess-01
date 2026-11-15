# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ryan-akmal/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ryan-akmal/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A tiny chess engine in 4,090 bytes of Python. 0x88 board, iterative-deepening
alpha-beta search to a fixed node budget (90,000 nodes a move early, 40,000
late), transposition table, MVV-LVA move ordering, quiescence over captures
and promotions with check evasions, and an incremental material plus
piece-square evaluation. It plays the house gauntlet through the make.fun env
over HTTP, deterministically: no clock, no unseeded randomness.

Practice trial (trial-0, 6 games): 3-0-3, Elo 1,279 — beats depth-2, depth-3
and depth-4, loses to nodes-100k, nodes-250k and nodes-500k.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tf75e7z1&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
