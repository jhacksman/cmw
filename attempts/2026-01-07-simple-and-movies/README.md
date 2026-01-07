# Simple Phrases + Movie References Attempt

**Date:** January 7, 2026  
**Candidates:** ~55.1M  
**Runtime:** ~3.4 minutes at 270k H/s

## Hypothesis

Two ideas combined:
1. Simple "this is a passphrase/password" without any pejorative (no "bad", "dumb", etc.)
2. Classic hacker movie references from Sneakers (1992) and Hackers (1995)

Dean would definitely know these movies - they're foundational hacker culture films.

## Simple Phrases (No Pejorative)

- "this is a passphrase"
- "this is a password"
- "this is my passphrase"
- "this is my password"

## Sneakers (1992) References

- "my voice is my passport" - Classic biometric bypass line
- "my voice is my passport verify me" - Full quote
- "no more secrets" - Key phrase about the decryption device
- "its all just electrons" - Cosmo's quote
- "too many secrets" - Anagram of "setec astronomy"

## Hackers (1995) References

- "hack the planet" - Movie tagline
- "mess with the best die like the rest" - Zero Cool's line
- "the pool on the roof must have a leak" - Social engineering line
- "zero cool" - Dade's original handle
- "crash override" - Dade's new handle
- "acid burn" - Kate's handle
- "cereal killer" - Character handle
- "lord nikon" - Character handle
- "phantom phreak" - Character handle
- "type cookie you idiot" - Famous line
- "love", "sex", "secret", "god" - The four most common passwords mentioned in the movie

## Configuration

- **Separators:** Spaces OR periods (consistent throughout)
- **Case:** lowercase and First-word-capitalized
- **Trailing:** 0-6 chars from `1234!@#$`
- **Trailing attachment:** With and without space/separator before trailing

## Candidate Count

- 23 base phrases
- 2 separators (spaces, periods)
- 2 case variants
- ~299,593 trailing combinations
- 2 trailing attachment styles (with/without separator)
- Total: ~55.1M candidates

## Run Command

```bash
python3 generate_simple_and_movies.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```

Or save to file first:
```bash
python3 generate_simple_and_movies.py > wordlist.txt
hashcat -m 11300 -a 0 -w 3 -O hash.txt wordlist.txt
```
