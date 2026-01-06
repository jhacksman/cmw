# 10 Billion Password Attempt - Combined Hypotheses

Generated: 2026-01-05

## Overview

This attempt generates approximately **10.4 billion** passphrase candidates combining two hypotheses:

1. **Spite Passphrase Hypothesis** - Short, deliberately weak multi-word phrases based on Dean's Signal chat hints
2. **Simple Spite Hypothesis** - 10-16 character simple patterns based on Dean's Telegram "spite" quote

## Evidence Used

From Dean's Signal chat:
- "Spaces. Maybe periods." for separators
- "4-7 words" (more than his usual 3-4)
- Trailing chars: "1, 3, maybe 6" - !, ?, ~, `
- Leetspeak: "p455, p@$$" - @ for a, $ for s, NEVER 7 for r

From Dean's Telegram:
- "I definitely set my password to the weakest possible thing I could out of spite"
- "I think it was something like 16 characters"

## Improvements Over Previous 600M Attempt

- NO deduplication set (streams directly, hashcat handles dupes)
- Full leetspeak expansion (not limited)
- Shorter phrases (2-5 words) included
- Simple 10-16 char patterns included
- More trailing pattern combinations (~200 patterns)
- More case variations (~10 variations)

## Estimated Breakdown

- Base phrases: ~148,000
- Passphrase candidates: ~10.4 billion
- Simple spite patterns: ~9,000
- Elongated patterns: ~208,000
- Trailing patterns: 201
- Adjectives: 101
- Nouns: 20

## Usage

```bash
# Estimate count
python3 generate_10b.py --estimate

# Generate to file
python3 generate_10b.py > wordlist.txt

# Generate limited sample
python3 generate_10b.py --limit 1000

# Pipe directly to hashcat
python3 generate_10b.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

# Use shell wrapper
./run_attempt.sh --estimate
./run_attempt.sh > wordlist.txt
```

## Memory Requirements

This script streams output without storing candidates in memory, so it should run on any system regardless of RAM. However, if you want to save to a file first, you'll need approximately 200-300GB of disk space for the full wordlist.

## Status

- [ ] Generated
- [ ] Tested against wallet
