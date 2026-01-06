# 8-Word "Dumbest Possible" Passphrase Attempt

**Estimated candidates:** ~1M
**Target:** 8-word passphrases that meet the Bitcoin advisory "eight or more words"

## Rationale

Based on Telegram deep dive findings, Dean was **guided** (not forced) by the Bitcoin encryption advisory which suggested "10 or more characters, OR eight or more words." If Dean went the 8-word route instead of the 10-character route, he would have picked the absolute dumbest 8-word phrase possible.

### Key Evidence

From Telegram archive:
- **[751]** "More like 'this is a very bad password' it's not some BDSM thing :-p" (6 words)
- **[955]** "I think a mutation of 'bad password' is more likely"
- **[724]** "I came up with the dumbest passphrase I could that matched the requirements"
- **[320]** "99% sure that if it ever cracks it's going to be something embarrassingly stupid"

## Patterns Generated

1. **Extended "this is a very bad password"** - Adding 2 words to make 8 (e.g., "this is a very bad password for real")
2. **Sentence-style 8-word phrases** - Complete dumb sentences (e.g., "this is the dumbest password I could think")
3. **Dean's commit-style phrases** - Based on his GitHub patterns (e.g., "tables are hard and so is this")
4. **Repeated words** - Single word 8 times (e.g., "bad bad bad bad bad bad bad bad")
5. **Mixed repeated** - Two words alternating or split (e.g., "bad bad bad bad dumb dumb dumb dumb")
6. **Adjective combinations** - "this is a [adj] [adj] [adj] [adj] password" with 10^4 combinations
7. **Number/letter words** - Simple sequences (e.g., "one two three four five six seven eight")

## Variations Applied

- **Separators:** space (most likely), dot (sometimes)
- **Case:** lowercase, UPPERCASE, Title Case, First word capitalized
- **Trailing chars:** none, !, ?, ~, `, 1, 2, 3, !!, ???, 123

## Usage

```bash
# Estimate candidate count
./run_attempt.sh --estimate

# Run against hashcat
./run_attempt.sh

# Or pipe to file first
python3 generate_8word.py > wordlist.txt
hashcat -m 11300 -a 0 -w 3 -O hash.txt wordlist.txt
```

## Files

- `generate_8word.py` - Generator script
- `run_attempt.sh` - Shell wrapper for hashcat
- `hash.txt` - Bitcoin wallet hash (mode 11300)
- `README.md` - This file
