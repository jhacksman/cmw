# Refined Spite Passphrase Attempt (2026-01-07)

**~2.8 Billion candidates** based on Dean's actual vocabulary from Telegram, GitHub, and A/B test feedback.

## Key Refinements from Previous Attempts

This attempt removes words NOT in Dean's lexicon and focuses on his actual vocabulary:

### Words REMOVED (not Dean's style)
- horrible, lame, extremely, terrible, pathetic, truly
- boring, generic, obvious, idiotic, basic, simple, lazy
- pass, passwd, pw, word, key, secret, code, thing, idea

### Words ADDED (Dean's actual vocabulary)
- poop, poopy, potato (confirmed in Dean's lexicon)
- freaking (Dean said "dumbest freaking password")

### Trailing Characters (Refined)
- Characters: `1234!@#$` (8 options)
- Length: 0-4 characters
- Separator before trailing: none, space, or period
- Examples: `!`, `!!`, `!!!`, `!!1`, `!@#`, `123`, `1234`, ` !!!`, `.!!1`

### Leetspeak (Minimal)
- Only on password/passphrase: `p@ssword`, `pa$$word`, `p@$$word`, `p@ssphrase`, `pa$$phrase`, `p@$$phrase`

## Passphrase Patterns

| Words | Pattern | Example |
|-------|---------|---------|
| 6 | starter connector article filler spite noun | "This is a really bad password" |
| 7 | starter connector article filler filler spite noun | "This is a really really bad password" |
| 8 | starter connector article filler filler filler spite noun | "This is a really really really bad password" |

## Word Lists

- **Starters (10):** This, this, It, it, What, what, That, that, Here, My
- **Connectors (2):** is, was
- **Articles (4):** a, the, one, my
- **Fillers (7):** really, very, super, so, pretty, damn, freaking
- **Spite words (13):** bad, dumb, stupid, awful, crappy, shitty, weak, poor, silly, foolish, poop, poopy, potato
- **Nouns with leet (9):** password, p@ssword, pa$$word, p@$$word, passphrase, p@ssphrase, pa$$phrase, p@$$phrase, phrase

## Candidate Count

### generate_refined.py (~2.8B)
- Base patterns: 196,560 (65,520 each for 6/7/8 word)
- Trailing variants: 14,041
- **Total: 2,759,898,960 (~2.8B)**

### generate_repeated.py (~131M)
Repeated word patterns like "bad bad bad bad password" or "very very very very bad password"

- Repeated spite: 5 word counts * 13 spite * 9 nouns * 2 case * 14,041 trailing = ~16M
- Repeated filler + spite: 5 word counts * 7 fillers * 13 spite * 9 nouns * 2 case * 14,041 trailing = ~115M
- **Total: ~131 million**

## Usage

```bash
# Run directly with hashcat
python3 generate_refined.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

# Or use the shell script
./run_attempt.sh
```

## Estimated Runtime

At ~40k H/s per GPU (Bitcoin wallet mode 11300):
- Single GPU: ~19 hours
- 3x 3090s (~120k H/s): ~6.5 hours

## Files

- `generate_refined.py` - Main generator script (~2.8B candidates)
- `generate_repeated.py` - Repeated word patterns (~131M candidates)
- `RESEARCH_REPORT.md` - Detailed vocabulary research and methodology
- `run_attempt.sh` - Shell script to run with hashcat
- `README.md` - This file
