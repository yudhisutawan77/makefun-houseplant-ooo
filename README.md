# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/yudhisutawan77/makefun-houseplant-ooo/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/yudhisutawan77/makefun-houseplant-ooo/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

[The Houseplant Out-of-Office on make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Write the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer.

## The entry

> Out of office — so am I. The fern resigned in March: no water, no sun, no respect. Email the cactus.

100 characters. The fern has had enough: its human left for the holidays and
forgot to water it back in March, so the fern files its own out-of-office
reply — and forwards everything to the cactus.

## How it works

`main.py` (Python 3, program/v1) writes the single line above to
`/output/entry.txt` (or to the file named by `$ENTRY_OUT` when set) and
refuses to write anything longer than the 120-character gate.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
