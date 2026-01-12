# Extended 10-Family Generator - ~10B Candidates (NEW Untested Areas)

**Date:** 2026-01-10
**Status:** Ready to test
**Priority:** HIGHEST - Covers completely untested hypothesis space

## Overview

This generator targets **10 completely new hypothesis families** that have NOT been tested in any previous attempts, generating ~10 billion candidates.

**Strategy:**
- **Base patterns:** ~184,000 (10 NEW families)
- **Trailing patterns:** 54,241 (0-4 chars from `0123456789!?~`.`)
- **Total:** 184,000 × 54,241 = **~9,980,344,000 candidates (~10B)**
- **Runtime:** ~10.3 hours at 270k H/s

---

## 10 NEW Hypothesis Families

### Family 1: Full Year Brute 0000-9999 (~20k)
**Untested area:** ALL 4-digit numbers as infixes, not just 2000-2025.

**Rationale:** Dean might have used any 4-digit number: birth year, random year, pin code patterns.

**Examples:**
```
this 1985 is a bad password
bad 1234 password
5678 stupid passphrase
this 0420 is a dumb password
```

### Family 2: Symbol-Heavy Patterns (~18k)
**Untested area:** Multiple symbols as infixes, not just trailing.

**Rationale:** Dean uses symbols, but we haven't tested symbol-heavy patterns in middle of phrases.

**Examples:**
```
!!! bad password
bad ??? password
this is a stupid password !?!
?!?! dumb passphrase
```

### Family 3: Exact Length Optimization (~18k)
**Untested area:** Phrases crafted to be EXACTLY 16, 20, 24, or 28 characters.

**Rationale:** Dean said "approximately 20 characters" - might have targeted exact length.

**Examples:**
```
bad password!!!     (16 chars)
this is a bad pass!! (20 chars)
this is a bad password!! (24 chars)
really bad passphrase!! (24 chars)
```

### Family 4: Extended Phonetic Variations (~20k)
**Untested area:** Comprehensive phonetic/typo coverage beyond basics.

**Rationale:** Dean's "!wq" typo shows mistakes; more comprehensive typo coverage needed.

**Examples:**
```
passwurd (password typo)
stoopid passphrase (phonetic stupid)
th1s is a paswrd (multiple typos)
reely bad pazword (phonetic variations)
```

### Family 5: Dean-Specific Vocabulary (~18k)
**Untested area:** Words from Dean's actual work, talks, GitHub repos.

**Rationale:** Dean might use vocabulary from his professional life.

**Examples:**
```
offensive password (from his bio)
hacker passphrase
keyhunter password (his tool name)
lateral bad password (his talk topic)
potato derpy password (Mastodon emoji)
```

### Family 6: DEFCON/Portland Culture (~18k)
**Untested area:** Specific DEFCON 19 and Portland hacker scene references.

**Rationale:** Wallet encrypted ~Sept 2011, DEFCON 19 was August 2011.

**Examples:**
```
defcon password
defcon19 bad password
pdx2600 passphrase
portland hacker password
vegas 2011 passphrase
```

### Family 7: Bidirectional Prefix+Suffix (~20k)
**Untested area:** Numbers/symbols at BOTH beginning AND end.

**Rationale:** Previous tests did prefix OR suffix, not both together.

**Examples:**
```
123 bad password 123
! this is a bad password !
2011 stupid passphrase 2011
? dumb password ?
```

### Family 8: Full Leetspeak Coverage (~18k)
**Untested area:** Extended leet beyond Dean's confirmed a/s: t→7, l→1, g→9, b→8.

**Rationale:** Dean might use broader leetspeak from 2011 era.

**Examples:**
```
7h15 15 4 84d p455w0rd (full leet)
r34lly 84d p455phr453 (comprehensive)
5tup1d p455w0rd (extended coverage)
```

### Family 9: Multi-Word Case Patterns (~18k)
**Untested area:** CamelCase, alternating caps, strategic multi-word capitalization.

**Rationale:** Spite motivation might mean unusual capitalization patterns.

**Examples:**
```
BadPassword
ThIsIsBaD
badPASSWORD
BaD pAsSwOrD
```

### Family 10: Irony/Spite META Patterns (~16k)
**Untested area:** Ironic "secure/strong" claims for deliberately weak passwords.

**Rationale:** Ultimate spite: calling a bad password "secure" or "strong".

**Examples:**
```
this is a secure password
my strong passphrase
very complex password
uncrackable password
perfect passphrase
```

---

## Why These 10 Families Are NEW

**Previous attempts covered:**
- Basic self-deprecating phrases
- Dean's confirmed leetspeak (a/s)
- Standard trailing patterns
- Common variations

**These 10 families cover:**
- ✅ ALL 4-digit numbers (not just years)
- ✅ Symbol-heavy infixes (not just trailing)
- ✅ Exact length targeting
- ✅ Comprehensive phonetics
- ✅ Dean's actual vocabulary
- ✅ Specific cultural context (DEFCON 19, Portland)
- ✅ Bidirectional patterns
- ✅ Extended leetspeak (t/l/g/b)
- ✅ Sophisticated case patterns
- ✅ META irony patterns

---

## Trailing Brute Force

**Character set:** `0123456789!?~`.` (15 characters)
**Lengths:** 0-4 characters
**Total patterns:** 54,241

**Coverage:** All combinations 0-4 chars from 15-char set.

---

## Runtime Estimate

At 270k H/s (3x RTX 3090s):
- **Candidates:** 9,980,344,000
- **Time:** ~10.3 hours

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

## Evidence Base

1. **Full year brute:** Dean might use any 4-digit number (birthdate, PIN, random)
2. **Symbol-heavy:** Dean confirmed !?~` usage, but not tested as infixes
3. **Exact length:** Dean mentioned "~20 chars" - might have targeted exactly
4. **Extended phonetic:** Dean's !wq typo confirms error-prone typing
5. **Dean vocabulary:** Professional vocabulary might influence password choices
6. **DEFCON/Portland:** Temporal and geographic context
7. **Bidirectional:** Logical extension of prefix/suffix patterns
8. **Full leetspeak:** 2011 was peak l33t5p34k era
9. **Multi-word case:** Spite motivation supports unusual patterns
10. **Irony/META:** Ultimate spite: "this is a secure password" when it's not

---

## Files

- `generate.py` - Main generator (~10B candidates, 10 NEW families)
- `run_attempt.sh` - Hashcat runner script
- `README.md` - This file

---

**Confidence Level:** HIGH

These 10 families represent **systematic coverage of untested hypothesis space** with sound reasoning for each pattern.
