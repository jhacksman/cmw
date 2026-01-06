# 2-3B Research-Based Password Attempt

**Date**: 2026-01-06
**Status**: Untried
**Estimated Candidates**: ~2.2 billion

## Overview

This attempt focuses on patterns identified from comprehensive research of pierce403's GitHub, blog, and social media that were NOT fully covered in the previous 10B attempt.

## Key Patterns Targeted

### Priority 1: "X is/are hard" Pattern (Dean's Signature)
Dean frequently uses this self-deprecating pattern in commit messages:
- "tables are hard", "spelling is hard", "datatypes are hard", etc.
- Extended to: "passphrases are hard", "passwords are dumb", etc.

### Priority 2: Potato Patterns
Confirmed significant - Dean has potato emoji in Mastodon display name and "added potato" in commits.

### Priority 3: 2011 Blog-Derived Phrases
From December 2011 blog post (closest to wallet creation):
- "just for kicks", "dead simple", "shoot your foot off", "write some damn code"

### Priority 4: Expletive Patterns
- "damn", "shit", "fuck", "crap" combined with passphrase/password

### Priority 5: Vim Typos
Dean's "first commit!wq" pattern - vim typo endings

### Priority 6: Derp Patterns
- "derp de doo", "herp derp", "derpity derp", etc.

### Priority 7: 2011 Memes
- "lulz", "rofl", "epic fail", "u mad bro", etc.

## Usage

```bash
# Show estimate
./run_attempt.sh --estimate

# Run with hashcat (pipes directly)
./run_attempt.sh

# Save wordlist to file first
./run_attempt.sh --to-file wordlist.txt
```

## Files

- `generate_2b.py` - Password candidate generator (~2.2B candidates)
- `hash.txt` - Bitcoin wallet hash for hashcat
- `run_attempt.sh` - Shell script to run the attempt

## Optimizations

- Streaming output (no memory-hungry deduplication)
- Deterministic ordering for reproducibility
- Optimized for DGX Spark (GB10 Grace Blackwell) with unified memory

## Evidence Base

From Signal chat with Dean (px):
- Spaces or periods between words
- 4-7 words (more than usual 3-4)
- Trailing chars: 1, 3, or 6 - !, ?, ~, `
- Leetspeak: p455, p@$$, @ for a, $ for s
- Set "out of spite" - deliberately weak
- ~16 characters mentioned

From Telegram:
- "I definitely set my password to the weakest possible thing I could out of spite"
