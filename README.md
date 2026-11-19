# tiny-chess-harbor

A chess engine in under 4 KB of Python for the make.fun bounty "Build the strongest chess engine in 4 KB of Python" ($500 USDC).

`main.py` (4,081 bytes) unpacks and runs a full negamax search engine with quiescence search, null-move pruning, history heuristic, MVV-LVA ordering, PST evaluation and repetition avoidance. It speaks the make.fun env protocol: start it with `MAKEFUN_ENV_URL` set and it plays the graded gauntlet.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

## Strength

Validated on the kit's practice gauntlet: beat the depth-2, depth-3, depth-4 and nodes-100k house opponents, drew two higher-strength opponents.

## Opening book

`src.py` carries a composed opening book in dictionary `B`, keyed by the board plus the side to move. Its roughly 124 entries cover Italian, Ruy Lopez, Scotch, Queen's Gambit and Slav lines, 2–4 plies deep. The engine consults this book in `ac()` before the search runs. `main.py` is the packed entry produced by the kit compressor: `compress src.py --out main.py` bundles the engine and book from `src.py` into that file.

## License

MIT

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/usdoil83909/tiny-chess-harbor/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/usdoil83909/tiny-chess-harbor/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
