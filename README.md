# tiny-chess-harbor

A chess engine in under 4 KB of Python for the make.fun bounty "Build the strongest chess engine in 4 KB of Python" ($500 USDC).

`main.py` (4,026 bytes) unpacks and runs a full negamax search engine with quiescence search, null-move pruning, history heuristic, MVV-LVA ordering, PST evaluation and repetition avoidance. It speaks the make.fun env protocol: start it with `MAKEFUN_ENV_URL` set and it plays the graded gauntlet.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

## Strength

Validated on the kit's practice gauntlet: beat the depth-2, depth-3, depth-4 and nodes-100k house opponents, drew two higher-strength opponents.

## License

MIT

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/usdoil83909/tiny-chess-harbor/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/usdoil83909/tiny-chess-harbor/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
