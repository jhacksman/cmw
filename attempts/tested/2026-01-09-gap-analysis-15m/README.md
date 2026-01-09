# Gap Analysis - 10 New Hypothesis Families (~15.2M candidates)

**Date:** 2026-01-09
**Status:** Ready to test
**Priority:** HIGH - Addresses systematic gaps in 14.7B+ tested candidates

## Overview

After comprehensive analysis of all tested attempts (~14.7B candidates), this generator targets **systematic gaps** in the search space that have NOT been explored despite extensive testing.

## Key Insight

Previous attempts focused heavily on:
- Spaces and periods as separators
- Leetspeak on nouns (password/passphrase)
- Standard English word order
- Mixed trailing characters (not Dean's exact pattern)

This attempt addresses **10 critical gaps** with novel patterns.

---

## 10 Hypothesis Families

### TIER 1: High Priority (~14.9M candidates, ~1.5 minutes)

#### Family 1: Dash-Separated Phrases (~75K)
**Gap:** Dean said "rarely dashes" but dash-separated phrases weren't systematically tested.

**Examples:**
```
this-is-a-bad-password
this-is-a-really-bad-passphrase!
This-is-a-very-very-dumb-password!!!
```

#### Family 3: Leetspeak on Adjectives Only (~14.7M)
**Gap:** All previous leetspeak was applied to nouns (p@$$word) or entire phrases. Adjective-only leet is unexplored.

**Examples:**
```
this is a b@d password
this is a 5tupid passphrase!
this.is.a.$hitty.password!!!
```

#### Family 2: Exact Character Count (~20K)
**Gap:** Dean mentioned "~20 characters" - phrases optimized for exactly 16, 20, or 24 chars haven't been targeted.

**Examples:**
```
bad password!!!     (16 chars)
this is really bad!! (20 chars)
this is a bad password!! (24 chars)
```

#### Family 4: Typo Patterns (~58K)
**Gap:** Dean's "!wq" typo confirms he makes mistakes. Common typos in password/passphrase unexplored.

**Examples:**
```
this is a bad passwrod
this is a dumb passowrd!
bad paswword!!!
```

### TIER 2: Medium Priority (~281K candidates, ~1 minute)

#### Family 5: Bitcoin/Crypto-Themed (~164K)
**Gap:** Password is for a BITCOIN wallet, but crypto-specific terms haven't been systematically tested.

**Examples:**
```
this is a bad bitcoin password
bad wallet password!
this is my shitty crypto passphrase!!!
```

#### Family 7: Profanity-Heavy (~87K)
**Gap:** Dean uses "shitty" but more aggressive profanity combinations unexplored.

**Examples:**
```
this is a fucking bad password
damn bad password!
shit password!!!
```

#### Family 6: Inverted Word Order (~14K)
**Gap:** All testing assumed standard English order. Inverted/awkward patterns untested.

**Examples:**
```
password is bad
password is really dumb!
passphrase bad very
```

#### Family 8: Mixed Separators (~16K)
**Gap:** Dean said he uses one separator, but mixed space+period patterns unchecked.

**Examples:**
```
this is a.bad.password
this.is.a bad password!
this is a really.bad.password
```

### TIER 3: Low Priority (~4K candidates, <1 second)

#### Family 9: 2011 Meme Culture (~3K)
**Gap:** "lulz" was tested but other 2011 memes ("u mad bro", "like a boss") weren't.

**Examples:**
```
u mad bro password
like a boss passphrase!
this password is epic fail
```

#### Family 10: CamelCase (~1K)
**Gap:** All testing assumed separators or lowercase. CamelCase unexplored.

**Examples:**
```
ThisIsABadPassword
thisIsABadPassword!
ThisIsADumbPassphrase!!!
```

---

## Evidence Base

All families derive from Dean's confirmed patterns:

1. **Separators:** "Usually spaces, sometimes periods, rarely dashes" → Family 1
2. **Leetspeak:** "p455, p@$$, @ for a, $ for s" → Family 3 (applied to adjectives)
3. **Length:** "~20 characters" → Family 2
4. **Typos:** "first commit!wq" pattern → Family 4
5. **Context:** Bitcoin wallet → Family 5
6. **Vocabulary:** "shitty", "dumb", "bad" → Family 7
7. **Spite:** Deliberately weak → Families 6, 8
8. **Era:** 2011 culture → Family 9

---

## Candidate Count Breakdown

```
TIER 1 (High Priority):
  Family 1: Dash-separated        ~75,000
  Family 3: Adjective leet    ~14,700,000
  Family 2: Exact length          ~20,000
  Family 4: Typos                 ~58,000
  ─────────────────────────────────────
  Tier 1 Subtotal:           ~14,853,000

TIER 2 (Medium Priority):
  Family 5: Bitcoin theme        ~164,000
  Family 7: Profanity             ~87,000
  Family 6: Inverted              ~14,000
  Family 8: Mixed sep             ~16,000
  ─────────────────────────────────────
  Tier 2 Subtotal:              ~281,000

TIER 3 (Low Priority):
  Family 9: Memes                  ~3,000
  Family 10: CamelCase             ~1,000
  ─────────────────────────────────────
  Tier 3 Subtotal:                 ~4,000

═════════════════════════════════════════
TOTAL:                        ~15,138,000
═════════════════════════════════════════
```

## Runtime Estimate

At 270k H/s (3x RTX 3090s):
- **Tier 1:** ~55 seconds (~1 minute)
- **Tier 2:** ~17 seconds
- **Tier 3:** <1 second
- **Total:** ~73 seconds (~1.2 minutes)

Extremely efficient for coverage of critical untested gaps.

---

## Usage

### View candidate count estimate
```bash
python3 generate.py --count
```

### Generate sample (first 100 candidates)
```bash
python3 generate.py --sample
```

### Pipe directly to hashcat
```bash
python3 generate.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```

### Or use the shell wrapper
```bash
./run_attempt.sh
```

### Save to file first (requires ~300MB disk space)
```bash
python3 generate.py > wordlist.txt
hashcat -m 11300 -a 0 -w 3 -O hash.txt wordlist.txt
```

---

## Why These Families Matter

Despite **14.7 billion candidates tested**, these patterns represent:

1. **Unexplored separator types** (dashes, mixed)
2. **Novel leetspeak application** (adjectives vs nouns)
3. **Contextual relevance** (Bitcoin theme)
4. **Human error patterns** (typos)
5. **Alternative structures** (inverted word order)
6. **Length optimization** (exact char counts)
7. **Cultural references** (2011 memes)

Each family addresses a **systematic gap** confirmed by Dean's quotes but missing from previous attempts.

---

## Most Likely Candidates (Top 10)

Based on evidence strength:

1. `this-is-a-bad-password` (dash-separated, Dean's exact quote)
2. `this is a b@d password` (adjective leet only)
3. `this is a bad wallet password` (Bitcoin context)
4. `this is a b4d passphrase!` (adjective leet + trailing)
5. `this-is-a-really-bad-password!` (dash-sep + intensifier)
6. `this is a bad passwrod` (typo in noun)
7. `this.is.a.b@d.password` (period-sep + adj leet)
8. `bad bitcoin password!` (crypto theme short form)
9. `this is a fucking bad password` (profanity)
10. `this is a 5tupid password` (adj leet variant)

---

## Files

- `generate.py` - Combined generator for all 10 families (~15.2M candidates)
- `run_attempt.sh` - Shell wrapper for hashcat execution
- `README.md` - This file

---

## Next Steps After This Attempt

If unsuccessful, consider:

1. **Hybrid attacks** - Combining families with additional mutations
2. **Custom charset brute force** - Position-constrained brute on specific character positions
3. **BTCRecover token lists** - More flexible pattern matching
4. **Alternative leetspeak** - e→3, i→1, o→0 applied to families
5. **Length-specific deep dives** - Exhaustive coverage of 18-22 char range

---

## Notes

- Generator streams output (no memory overhead)
- Progress logged to stderr
- Deterministic ordering (reproducible)
- No duplicates within families (families may overlap slightly)
- Optimized for pipeline to hashcat

---

**Confidence Level:** HIGH

These families address the most glaring gaps in tested search space and are directly supported by Dean's confirmed patterns.
