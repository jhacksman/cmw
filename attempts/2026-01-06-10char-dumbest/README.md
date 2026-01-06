# 10-Character "Dumbest Possible" Password Attempt

**Date:** 2026-01-06  
**Estimated candidates:** ~727M  
**Status:** UNTRIED

## Rationale

Based on Telegram deep dive findings, Dean was GUIDED (not forced) by the advisory "10 or more characters, or 8 or more words". He said he tried to set "the dumbest passphrase I could that matched the requirements."

Key evidence:
- Dean's LUKS password was "poop123"
- He said "pooooooooooooooop" as an example
- He said "this is a very bad password" as an example
- He confirmed using words like "stupid", "dumb", "bad"
- He estimated "something like 16 characters" but also mentioned the minimum was "like 16" (actually 10)

## Patterns Covered

1. **Elongated poop/potato/poopy** (10-15 chars) - Dean's explicit example
2. **"bad password" phrases** with space/dot separators and trailing chars
3. **"this is" patterns** - truncated versions of "this is a bad password"
4. **Keyboard patterns** - qwertyuiop (exactly 10 chars)
5. **"password" + digits** - password00 through password9999
6. **Simple repeated chars** - aaaaaaaaaa, 0000000000, etc.
7. **poop + digits** - poop000000 through poop99999999 (biggest category)
8. **potato + digits** - potato0000 through potato999999

## Usage

```bash
# Estimate candidate count
./run_attempt.sh --estimate

# Run with hashcat (streams directly, no intermediate file)
./run_attempt.sh

# Or manually pipe to hashcat
python3 generate_10char.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```

## NO MIXING Rule

All leetspeak variants are consistent within a word:
- `poop` or `p00p` or `POOP` (never `pO0p`)
- `potato` or `p0tat0` or `P0TAT0` (never `pOtat0`)
