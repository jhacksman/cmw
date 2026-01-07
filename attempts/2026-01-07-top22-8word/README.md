# Top 22 Eight-Word Phrases Attempt (2026-01-07)

**~52.7M candidates** - The 22 most likely 8-word phrases based on Dean's quotes.

## Base Phrases (22 patterns x 2 nouns = 44 phrases)

All phrases are exactly 8 words, prioritized by likelihood.

### Tier 1: Most Likely (based on Dean's exact quotes)
1. this is a really really really bad password/passphrase
2. this is a very very very bad password/passphrase
3. this is a really really really dumb password/passphrase
4. this is a really really really stupid password/passphrase
5. this is a super super super bad password/passphrase

### Tier 2: Variations with different spite words
6. this is a very very very dumb password/passphrase
7. this is a very very very stupid password/passphrase
8. this is a super super super dumb password/passphrase
9. this is a super super super stupid password/passphrase
10. this is a really really bad bad password/passphrase
11. this is a very very bad bad password/passphrase

### Tier 3: Different starters
12. this was a really really really bad password/passphrase
13. that is a really really really bad password/passphrase
14. it is a really really really bad password/passphrase
15. this is my really really really bad password/passphrase
16. this is one really really really bad password/passphrase

### Tier 4: Mixed fillers
17. this is a really really very bad password/passphrase
18. this is a really very very bad password/passphrase
19. this is a super really really bad password/passphrase
20. this is a damn damn damn bad password/passphrase
21. this is a freaking freaking freaking bad password/passphrase
22. this is a pretty pretty pretty bad password/passphrase

## Word Separators

Two word separator styles (consistent throughout phrase):
- **Spaces:** `this is a really really really bad password 123`
- **Periods:** `this.is.a.really.really.really.bad.password.123`

## Trailing Configuration

- Characters: `1234!@#$` (8 options)
- Length: 0-6 characters
- Separator before trailing matches word separator

## Candidate Count

- 44 base phrases (22 patterns x 2 nouns)
- 2 case variants (lowercase + capitalized)
- 2 word separators (space, period)
- 299,593 trailing combinations (0-6 chars)

**Total: 44 x 2 x 2 x 299,593 = 52,728,368 (~52.7M)**

## Runtime

At 270k H/s (3x 3090s): ~3.3 minutes

## Usage

```bash
python3 generate_top22.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```

## Files

- `generate_top22.py` - Main generator script
- `run_attempt.sh` - Shell script to run with hashcat
- `README.md` - This file
