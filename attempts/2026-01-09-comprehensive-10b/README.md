# Comprehensive 10-Family Generator - ~7.3B Candidates

**Date:** 2026-01-09
**Status:** Ready to test
**Priority:** HIGHEST - Comprehensive coverage across all hypothesis families

## Overview

This generator combines **10 hypothesis families** into one comprehensive attack, generating ~7.3 billion candidates through intelligent trailing brute force.

**Strategy:**
- **Base patterns:** ~135,380 (10 families)
- **Trailing patterns:** 54,241 (0-4 chars from `0123456789!?~`.`)
- **Total:** 135,380 × 54,241 = **~7,343,146,580 candidates (~7.3B)**
- **Runtime:** ~7.6 hours at 270k H/s

---

## 10 Hypothesis Families

### Family 1: Core Self-Deprecating Phrases (~17k)
Dean's exact theme: self-deprecating statements about password weakness.

**Examples:**
```
bad password
this is a really bad password
embarrassingly stupid passphrase
dumbest freaking password
my awful password
```

### Family 2: Leetspeak Variations (~2.1k)
Dean's confirmed patterns: a→@/4, s→$/5, e→3, i→1, o→0.

**Examples:**
```
this is a really b@d password
$tupid p@$$word
b4d p455phr@$e
this is a very 5tupid password
```

### Family 3: Number/Year Infixes (~2.3k)
Numbers in middle of phrases: 1, 2, 3, 123, 42, 69, 2011, 2012, 2010, 1337.

**Examples:**
```
this 2011 is a bad password
this is 123 a bad password
really 2012 bad password
```

### Family 4: Emphasis Caps & Alternatives (~1k)
ALL CAPS emphasis, inverted structures, doubled words, Bitcoin theme.

**Examples:**
```
this is a BAD password
password is bad
bad bad password
this is a bad bitcoin password
```

### Family 5: Extended Phrase Variations (~18k)
Expanded vocabulary: 15 adjectives × 7 nouns × 6 new structures.

**Adjectives:** bad, dumb, stupid, shitty, crappy, awful, terrible, lame, weak, silly, ridiculous, pathetic, horrible, useless, garbage

**Nouns:** password, passphrase, pass, passwd, pw, key, secret

**Examples:**
```
yet another bad password
just a stupid passphrase
another crappy key
the most pathetic password
worlds worst password
```

### Family 6: Phonetic Variations & Typos (~20k)
Common misspellings and phonetic alternatives.

**Examples:**
```
this is a pasword
stoopid passphrase
this is a passphraze
duhm password
```

### Family 7: Keyboard Patterns (~15k)
qwerty, asdf, and other keyboard sequences embedded in phrases.

**Examples:**
```
qwerty password
password asdf
this is qwer
asdfg passphrase
```

### Family 8: Year Range 2000-2025 (~22k)
Full four-digit year coverage as infixes.

**Examples:**
```
this 2005 is a bad password
bad password 2015
2020 stupid passphrase
```

### Family 9: Case Permutations (~18k)
Strategic capitalization combinations.

**Examples:**
```
BAD PASSWORD
bad PASSWORD
BAD password
bAd PaSsWoRd
```

### Family 10: Prefix Patterns (~20k)
Numbers/symbols at beginning instead of end.

**Examples:**
```
123 bad password
2011 this is a bad password
! stupid passphrase
```

---

## Trailing Brute Force

**Character set:** `0123456789!?~`.` (15 characters)
**Lengths:** 0-4 characters
**Total patterns:** 54,241

**Coverage:**
- All single digits (0-9)
- All 2-digit combinations (00-99)
- All 3-digit combinations (000-999)
- All 4-digit combinations (0000-9999)
- Common patterns: 123!, 2011?, etc.
- Mixed patterns: !1, 123., 456!, etc.

---

## Runtime Estimate

At 270k H/s (3x RTX 3090s):
- **Candidates:** 7,343,146,580
- **Time:** ~7.6 hours

---

## Usage

### View candidate count
```bash
python3 generate.py --count
```

### Generate sample
```bash
python3 generate.py --sample
```

### Run full attack
```bash
./run_attempt.sh
```

---

## Why This Is Comprehensive

This generator represents the **most thorough coverage** of Dean's potential password space:

1. **All confirmed patterns** from Dean's quotes
2. **Alternative mutations** (phonetic, keyboard, case)
3. **Contextual variations** (years, Bitcoin theme)
4. **Structural alternatives** (prefix, infix, inverted)
5. **Extended vocabulary** (more adjectives, nouns)
6. **Complete trailing brute force** (0-4 chars from 15-char set)

**Evidence base:** Every family derives from Dean's confirmed habits or contextually plausible variations.

---

## Files

- `generate.py` - Main generator (~7.3B candidates, 10 families)
- `run_attempt.sh` - Hashcat runner script
- `README.md` - This file

---

**Confidence Level:** HIGHEST

This is the most comprehensive attack possible given Dean's constraints, combining all hypothesis families into one systematic approach.
