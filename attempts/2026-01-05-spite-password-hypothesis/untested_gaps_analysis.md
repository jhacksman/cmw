# Untested Search Space Gaps (<= 1 Billion Candidates)

## What Dean Actually Tested

From README.md confirmed tests:
- `?d 1-9` → Digits 1-9 chars (last: 10^9 = 1 billion)
- `?l 1-7` → Lowercase 1-7 chars (last: 26^7 = 8 billion) 
- `?a 1-6` → All ASCII 1-6 chars (last: 95^6 = 735 billion)
- rockyou.txt + best64/d3ad0ne/dive
- weakpass2a + best64

## Untested Gaps (<= 1B Each)

### Gap 1: 8 Lowercase (Partitioned by First Letter)
- Total: 26^8 = 208 billion (TOO BIG)
- **Solution:** Partition by first char
- Example: `a?l?l?l?l?l?l?l` = 26^7 = 8 billion per letter
- **Problem:** Still too big (8B > 1B)

### Gap 2: Common Word + Padding (BEST OPTION)
Based on "weakest possible thing out of spite":

**8-char base words + 1-2 char padding:**
- `password` + 1 char = 95 variants (all ASCII)
- `password` + 2 chars = 9,025 variants
- `badpass` + 2 chars = 9,025 variants
- etc.

### Gap 3: Keyboard Patterns Extended
Dean tested up to 7 lowercase, but NOT:
- `qwertyui` (8 chars) + variants
- `asdfghjk` (8 chars) + variants  
- Keyboard diagonals 8+ chars

### Gap 4: Repeated Char + Padding
Dean mentioned "pooooooooooooooop":
- `aaaaaaa` + 1 char = 95 variants (7 a's + 1 char)
- `aaaaaaa` + 2 chars = 9,025 variants
- `1111111` + 1 char = 95 variants
- etc.

### Gap 5: Leetspeak 8-Char Variations
Dean's patterns (p455, p@$$) but 8+ chars:
- `p@ssword` (8 chars) + variations
- `p@ssw0rd` (8 chars) + variations
- `b@dp@ss` + padding
- Total: Can limit to specific patterns

## Calculation: What Fits in 1 Billion?

### Option A: Specific Base + 2 Chars
- Base word (8 chars) + 2 ASCII chars
- Example: `password??` where ?? = any 2 ASCII
- Keyspace: 95^2 = 9,025 per base word
- Can do ~100,000 base words in 1B

### Option B: 7 Chars + 1 ASCII
- Any 7 lowercase + 1 ASCII char
- Keyspace: 26^7 * 95 = 760 billion (TOO BIG)
- Partition needed

### Option C: Hybrid Patterns
- Common word (6 chars) + 2 lowercase + 1 digit
- Example: `badpassXY#` where X,Y = lowercase
- Keyspace per base: 26^2 * 10 = 6,760

## Recommended: Generate These First

1. **password + 2 chars** (9,025 combos)
2. **Password + 2 chars** (9,025 combos, uppercase P)
3. **badpass + 3 chars** (857,375 combos if lowercase+digit+symbol)
4. **qwertyui + 2 chars** (9,025 combos)
5. **Repeated 7 + 2 chars** (aaaaaaa?? = 9,025 combos)

Total for top 5: ~52,000 candidates (VERY MANAGEABLE)
