# Elongated Potato/Poop Pattern Attempt

**Target:** ~569M candidates

## Hypothesis

Based on Dean's Telegram quote: "Like 'pooooooooooooooop' or something" and his confirmed use of potato references (emoji in Mastodon profile), this attempt targets elongated versions of potato/poop-related words.

## Key Constraints

**NO MIXING RULE:** All instances of a character type use the SAME leetspeak variant throughout the word. This matches Dean's pattern with separators (space OR period, never mixed).

### Leetspeak Mappings (Consistent Per Word)
- p: p, P (2 options)
- o: o, O, 0 (3 options)
- t: t, T (2 options) - Dean confirmed NEVER uses 7
- a: a, A, 4, @ (4 options)
- y: y, Y (2 options)

### Words Covered
1. **potato** (p-o-t-a-t-o): 5,280 base patterns
2. **poop** (p-o-o-p): 792 base patterns
3. **poopy** (p-o-o-p-y): 1,452 base patterns
4. **pootato** (p-o-o-t-a-t-o): 26,400 base patterns
5. **poopoo** (p-o-o-p-o-o): 18,150 base patterns

### Modifiers
- **Length:** 10-20 characters (elongated by repeating o's)
- **Trailing:** 0-6 characters from !?~` (Dean's confirmed trailing chars)
- **Leading:** "" or "this is a " (space separator per user's rule)

## Candidate Count

- Base words: 52,074
- Trailing options: 5,461
- Leading options: 2
- **Total: 568,752,228 (~569M)**

## Usage

```bash
# Verify count
./run_attempt.sh --estimate

# Run with hashcat (streams directly)
./run_attempt.sh

# Save to file first
./run_attempt.sh > wordlist.txt
```

## Example Candidates

```
potatooooo
p0tat000000000000
P0TAT0000000000!!!
this is a p00000000p
this is a P00PY~~~~~
p0000000000000tat0
```

## Files

- `generate_569m.py` - Python generator script
- `run_attempt.sh` - Shell wrapper for hashcat
- `hash.txt` - Bitcoin wallet hash (mode 11300)
