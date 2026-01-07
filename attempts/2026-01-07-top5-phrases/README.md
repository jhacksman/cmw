# Top 11 Phrases Attempt (2026-01-07)

**~26.4M candidates** - The most likely phrases based on Dean's exact quotes.

## Base Phrases (11 patterns x 2 nouns = 22 phrases)

### "this is a..." set (5 patterns)
1. this is a very bad password/passphrase - Dean's EXACT quote
2. this is a really bad password/passphrase
3. this is a really dumb password/passphrase
4. this is a really stupid password/passphrase
5. this is a super bad password/passphrase

### Short set (6 patterns)
6. bad password/passphrase
7. very dumb password/passphrase
8. really bad password/passphrase
9. dumb password/passphrase
10. stupid password/passphrase
11. really dumb password/passphrase

## Word Separators

Two word separator styles (consistent throughout phrase):
- **Spaces:** `this is a very bad password 123`
- **Periods:** `this.is.a.very.bad.password.123`

## Trailing Configuration

- Characters: `1234!@#$` (8 options)
- Length: 0-6 characters
- Separator before trailing matches word separator

Examples:
- `this is a very bad password` (spaces, no trailing)
- `this is a very bad password 123` (spaces, with trailing)
- `this.is.a.very.bad.password` (periods, no trailing)
- `this.is.a.very.bad.password.123` (periods, with trailing)

## Candidate Count

- 22 base phrases (11 patterns x 2 nouns)
- 2 case variants (lowercase + capitalized)
- 2 word separators (space, period)
- 299,593 trailing combinations (0-6 chars)

**Total: 22 x 2 x 2 x 299,593 = 26,364,184 (~26.4M)**

## Runtime

At 270k H/s (3x 3090s): ~1.6 minutes

## Usage

```bash
python3 generate_top5.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```

## Files

- `generate_top5.py` - Main generator script
- `run_attempt.sh` - Shell script to run with hashcat
- `README.md` - This file
