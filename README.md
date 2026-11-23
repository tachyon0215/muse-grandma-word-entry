# muse-grandma-word-entry

[![Competition](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/tachyon0215/muse-grandma-word-entry/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/tachyon0215/muse-grandma-word-entry/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the make.fun competition [One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) — exactly one word: the word a grandma would text about AI.

## The entry

> ChatGPtea

Three candidates were drafted and compared against the judge's brief (the single word a grandma would text about AI, a real grandmother's warm and slightly baffled texting voice, funny in one word with no caption, tied to AI rather than any subject, and fresh yet instantly readable). This one won: she hears "ChatGPT" and files it under tea — the mishearing is exactly how a grandma domesticates new technology, it is unmistakably about AI, and the joke needs no explanation. The alternatives ("Unplugit", her one-word cure for any machine, and "Robit", her spelling of robot) were each grandma-like, but the first fits any appliance at all and the second is a plain typo with no AI in it.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–30 characters, not only whitespace, and exactly one word before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 248af55092544364c062c49dc04c5082435594814eb0cdaeca50b530e2c347c8).

## License

MIT — see [LICENSE](LICENSE).
