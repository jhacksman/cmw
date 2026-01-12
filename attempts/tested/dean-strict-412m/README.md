# Dean-Strict Password Attempt (~6.7M candidates)

Based STRICTLY on Dean's confirmed quotes - no assumptions.

## Dean's Exact Quotes

**Separators:**
> "Spaces. Maybe periods."

**Trailing:**
> "Likely 1, 3, maybe 6, exclamations or question marks sometimes tildes or back ticks"

**Leetspeak:**
> "I've leetified pass as p455, p@$$, and combinations like that"
> "@ for a and $ for s sometimes as well"

**Example phrase:**
> "More like 'this is a very bad password'"

**Alternatives:**
> "also 'dumb'" (when asked about alternatives to "bad")
> "really really stupid"

## Base Phrases (58 total)

### Set 1: "this is a [intensifier] [spite] password/passphrase"
- No intensifier: this is a bad/dumb/stupid password/passphrase (6)
- Single intensifier: this is a very/really bad/dumb/stupid password/passphrase (12)
- Double intensifier: this is a very very/really really bad/dumb/stupid password/passphrase (12)

### Set 2: Short versions
- No intensifier: bad/dumb/stupid password/passphrase (6)
- Double intensifier: very very/really really bad/dumb/stupid password/passphrase (12)

### Set 3: Prompt-based "Enter a [spite] passphrase to encrypt your wallet"
- Original: Enter a passphrase to encrypt your wallet (1)
- With spite: Enter a bad/dumb/stupid passphrase to encrypt your wallet (3)
- With intensifier: Enter a very/really bad/dumb/stupid passphrase to encrypt your wallet (6)

## Variations

- **Separators:** spaces, periods (consistent throughout)
- **Case:** lowercase, First cap
- **Trailing chars:** `!?~\`` (0-6 chars)
- **Trailing separator:** none, or matching word separator
- **Leetspeak (password only):** password, p@$$word, p455word
- **Leetspeak (passphrase only):** passphrase, p@$$phr@$e, p455phr45e

## Rules

1. No mixing leetspeak within words (all @ or all 4, not mixed)
2. Trailing separator matches word separator (space phrases get space, period phrases get period)
3. Only Dean-confirmed trailing chars: `!?~\``

## Candidate Count

- Base phrases: 58
- Noun variants (leet): 3 per password/passphrase type
- Separators: 2
- Case: 2
- Trailing combinations: 5,461 (0-6 chars from 4 chars)
- Trailing separators: 2 (none or matching)

**Total: ~6.7 million candidates**

## Runtime

At 270k H/s (3x 3090): ~25 seconds

## Usage

```bash
# Generate all candidates
python3 generate.py > wordlist.txt

# Pipe directly to hashcat
python3 generate.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

# Check count
python3 generate.py --count
```
