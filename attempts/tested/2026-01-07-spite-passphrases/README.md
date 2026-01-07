# Spite Passphrase Attempts (2026-01-07)

Based on Dean's A/B test feedback from the nostalgia website.

## Dean's Confirmed Preferences

From the A/B test results:
- **Separators**: Spaces (not periods, underscores, or camelCase)
- **Capitalization**: First word only
- **Punctuation**: Trailing (!, ?, ~, `)
- **Leetspeak**: Light (@ for a, $ for s, 0 for o)
- **Theme**: Spite ("bad", "dumb", "stupid")
- **Word count**: Long (6-8 words preferred)
- **Character count**: Long (17+ characters)
- **Excluded**: No potato/poop patterns, no "X is hard" patterns

## Dean's Example Guess

> "this is a really really really bad password"

This informed our pattern design - repeated filler words with spite adjective.

## Scripts

### generate_common.py (~100M candidates)
Most likely patterns based on Dean's actual guess. Focuses on:
- "really" as primary filler (Dean's choice)
- "bad" as primary spite word (Dean's choice)
- "password" as primary noun (Dean's choice)
- Includes "super duper" compound filler

### generate_6word.py (~1B candidates)
6-word spite passphrases:
- "This is really really bad password"
- "This is a super duper bad password" (compound = 2 words)
- "What a really really really bad"

### generate_7word.py (~1B candidates)
7-word spite passphrases:
- "This is a really really bad password"
- "This is a super duper bad password"
- "This is really really really bad password"

### generate_8word.py (~1B candidates)
8-word spite passphrases (Bitcoin 0.4.0 minimum suggestion):
- "This is a really really really bad password"
- "This is a super duper really bad password"

## Bitcoin 0.4.0 Context

The "8 or more words" prompt was introduced in Bitcoin 0.4.0 (September 23, 2011):
> "10 or more random characters, or eight or more words"

Dean mentioned he might have used 6 or 7 words "just to test if it would let me" - the prompt was advisory only, not enforced.

## Usage

```bash
# Run the shell script for interactive menu
./run_attempt.sh

# Or run individual generators directly
python3 generate_common.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
python3 generate_6word.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
python3 generate_7word.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
python3 generate_8word.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```

## Estimated Runtime

At ~40k H/s per GPU (Bitcoin wallet mode 11300):
- 100M candidates: ~40 minutes per GPU
- 1B candidates: ~7 hours per GPU

With 3x 3090s (~120k H/s combined):
- 100M: ~14 minutes
- 1B: ~2.3 hours each
