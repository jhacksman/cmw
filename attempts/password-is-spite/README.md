# "This password/passphrase is [brute spite]" Structure (~33B candidates)

Brute forces the spite slot with 1-5 lowercase chars (21 letters, excluding j, q, x, z, v).

Pattern: "this password is really [BRUTE 1-5 chars]"

## Structure

This is a NEW phrase structure not systematically tested before:
- "this password is really dumb" -> "this password is really [brute]"
- "this passphrase is very bad" -> "this passphrase is very [brute]"

## Dean's Exact Trailing Pattern

From Dean's quote: "Likely 1, 3, maybe 6, exclamations or question marks sometimes tildes or back ticks"

Single char repeated, not mixed:
- 0 chars: (none)
- 1 char: `!`, `?`, `~`, `` ` ``
- 3 chars: `!!!`, `???`, `~~~`, `` ``` ``
- 6 chars: `!!!!!!`, `??????`, `~~~~~~`, `` `````` ``

**Total: 13 trailing combinations**

## Brute Force Spite Slot

- Charset: 21 lowercase letters (a-z minus j, q, x, z, v)
- Lengths: 1-5 characters
- Total brute combinations: ~4.3M

## Phrase Templates (26 total)

For each noun (password, passphrase):
- No intensifier: "this password is [BRUTE]"
- Single: "this password is very/really/super [BRUTE]"
- Double: "this password is really really [BRUTE]"
- Triple: "this password is really really really [BRUTE]"
- Quad: "this password is really really really really [BRUTE]"

## Variations

- **Separators:** spaces, periods (consistent throughout)
- **Case:** lowercase, First cap
- **Trailing:** Dean's exact pattern (0, 1, 3, or 6 of same char)
- **Trailing separator:** none, or matching word separator
- **Leetspeak:** p@$$word/p455word, p@$$phr@$e/p455phr45e

## Candidate Count

**Total: ~33.4B candidates**

## Runtime

At 270k H/s (3x 3090): **~34 hours**

## Usage

```bash
# Generate all candidates (streams to stdout)
python3 generate.py

# Pipe directly to hashcat
python3 generate.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

# Check count
python3 generate.py --count
```
