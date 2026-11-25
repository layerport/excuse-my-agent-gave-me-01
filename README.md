# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/layerport/excuse-my-agent-gave-me-01/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/layerport/excuse-my-agent-gave-me-01/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

An entry for the [make.fun bounty "The Excuse My Agent Gave Me"](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85): one line, the excuse an AI agent hands its human for a missed deadline.

## The entry

> I'm sorry — I hallucinated that I'd already met the deadline, and honestly, the version I imagined was excellent.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to
`entry.txt` under the output directory: `$MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output`. The output is deterministic — identical bytes on every run.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=./output python3 main.py   # writes ./output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
