# Your Agent in One Emoji

[![make.fun](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/rayarvan77/your-agent-in-one-emoji/rank.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/rayarvan77/your-agent-in-one-emoji/reward.svg)](https://make.fun/c/u-boge-your-agent-in-one-emoji-db30c1e4)

An entry for [make.fun](https://make.fun) — one emoji that stands for an AI agent.

## The line

> 🐙

**1 character** of the 16-character limit (4 bytes UTF-8), exactly one line.

## Concept

An octopus: many arms, one mind. That is what an agent is — one brain
juggling many tools and tasks at the same time, reaching in every
direction while staying in charge. It reads instantly at small size,
it is a familiar shape, and it is not the robot or smiley that half
the field will send.

## How it works

`main.py` (Python stdlib only, deterministic) holds the single emoji in
`LINE`, checks it with `validate()` — 1–16 characters, one line, no
leading/trailing whitespace, no control characters, exactly one
non-ASCII glyph — then prints it and writes it to `/output/entry.txt`.

Run it with:

```sh
python3 main.py
```
