# Alternative Leetspeak & Hybrid Patterns (~20M candidates)

**Date:** 2026-01-09
**Status:** Ready to test
**Priority:** HIGH - Alternative mutation patterns not covered in previous attempts

## Overview

After testing the first gap analysis set (~15.2M candidates), this generator targets **alternative leetspeak patterns** and **hybrid mutations** that weren't explored in previous attempts.

## Key Insight

Previous attempts focused on:
- a→@ or a→4 (Dean's confirmed pattern)
- s→$ or s→5 (Dean's confirmed pattern)
- Full-phrase or noun-only leetspeak

This attempt explores:
- **Alternative leetspeak** (e→3, i→1, o→0)
- **Hybrid leetspeak** (both adjective AND noun leeted)
- **Emphasis capitalization** (BAD vs bad)
- **Number infixes** (numbers in middle of phrase)
- **Alternative intensifiers** (so, such, pretty)

---

## 8 Hypothesis Families

### TIER 1: High Priority (~18.5M candidates, ~1.1 minutes)

#### Family 1: Alternative Leetspeak (e→3, i→1, o→0) (~12M)
**Rationale:** Dean confirmed a→@ and s→$ but never mentioned e/i/o. These are common leetspeak patterns.

**Examples:**
```
th1s 1s a bad passw0rd
th1s 1s a bad p4ssw0rd!
th3 1s 4 dum6 p455w0rd!!!
```

**Mutation strategy:**
- Apply e→3, i→1, o→0 in all combinations
- Combined with spaces/periods/dashes
- All trailing patterns

#### Family 2: Hybrid Leetspeak (adj + noun) (~4M)
**Rationale:** Previous attempts either leeted the adjective OR noun, never both together.

**Examples:**
```
this is a b@d p@$$word
this is a $tupid p455word!
b4d p@$$phr@$3!!!
```

**Mutation strategy:**
- Adjective leet: bad→b@d, bad→b4d, stupid→$tupid
- Noun leet: password→p@$$word, passphrase→p455phr@$3
- Combine both in same phrase

#### Family 3: Emphasis Capitalization (~2.5M)
**Rationale:** Spite motivation might mean emphasizing the adjective with CAPS.

**Examples:**
```
this is a BAD password
this is a REALLY bad password!
this IS a bad password!!!
```

**Mutation strategy:**
- Capitalize different words in phrase
- Test all word positions
- Combined with all trailing patterns

### TIER 2: Medium Priority (~1.3M candidates, ~5 seconds)

#### Family 4: Number Infixes (~800K)
**Rationale:** Numbers in middle of phrase, not just at end.

**Examples:**
```
this 123 is a bad password
this is 42 a bad password!
bad 2011 password
```

#### Family 5: Alternative Intensifiers (~300K)
**Rationale:** Dean used "really" and "very", but what about "so", "such", "pretty"?

**Examples:**
```
this is so bad
this is a pretty bad password!
such bad password
kinda bad passphrase
```

#### Family 6: Doubled Words (~200K)
**Rationale:** Emphasis through repetition.

**Examples:**
```
bad bad password
really really bad password!
this this is a bad password
```

### TIER 3: Low Priority (~200K candidates, <1 second)

#### Family 7: Longer Dean Quotes (~150K)
**Rationale:** Dean said "embarrassingly stupid" and "dumbest freaking password".

**Examples:**
```
embarrassingly stupid password
dumbest freaking password!
this is embarrassingly bad
```

#### Family 8: Alternating Trailing Patterns (~50K)
**Rationale:** Alternating punctuation/numbers in trailing: !1!1, ?2?2.

**Examples:**
```
bad password!1!1
this is a bad password?2?2?
bad passphrase!~!~
```

---

## Candidate Count Breakdown

```
TIER 1 (High Priority):
  Family 1: Alt leet (e/i/o)   ~12,000,000
  Family 2: Hybrid leet         ~4,000,000
  Family 3: Emphasis caps       ~2,500,000
  ─────────────────────────────────────────
  Tier 1 Subtotal:             ~18,500,000

TIER 2 (Medium Priority):
  Family 4: Number infixes        ~800,000
  Family 5: Alt intensifiers      ~300,000
  Family 6: Doubled words         ~200,000
  ─────────────────────────────────────────
  Tier 2 Subtotal:              ~1,300,000

TIER 3 (Low Priority):
  Family 7: Longer quotes         ~150,000
  Family 8: Alt patterns           ~50,000
  ─────────────────────────────────────────
  Tier 3 Subtotal:                ~200,000

═════════════════════════════════════════════
TOTAL:                          ~20,000,000
═════════════════════════════════════════════
```

## Runtime Estimate

At 270k H/s (3x RTX 3090s):
- **Tier 1:** ~68 seconds (~1.1 minutes)
- **Tier 2:** ~5 seconds
- **Tier 3:** <1 second
- **Total:** ~74 seconds (~1.2 minutes)

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

---

## Why These Families Matter

The previous gap analysis covered:
- Dash separators
- Adjective-only leetspeak (a/s substitutions)
- Bitcoin themes
- Typos

This set explores:
1. **Alternative leetspeak characters** (e/i/o instead of just a/s)
2. **Hybrid mutations** (multiple leet types in one phrase)
3. **Emphasis patterns** (capitalization for spite)
4. **Number patterns** (beyond trailing)
5. **Linguistic variations** (alternative intensifiers, doubled words)

---

## Most Likely Candidates (Top 10)

Based on evidence strength:

1. `th1s 1s a bad passw0rd` (alternative e/i/o leet)
2. `this is a b@d p@$$word` (hybrid leet)
3. `this is a BAD password` (emphasis caps)
4. `th1s is @ b4d p455w0rd!` (full alternative leet)
5. `this is so bad` (alternative intensifier)
6. `really really bad password` (doubled intensifier)
7. `this 123 is a bad password` (number infix)
8. `embarrassingly stupid password` (Dean's exact quote)
9. `bad bad password!` (doubled word)
10. `this is a bad password!1!1` (alternating trailing)

---

## Evidence Base

1. **Alternative leet:** Common in 2011 (l33t5p34k culture)
2. **Hybrid patterns:** Logical extension of Dean's confirmed leet usage
3. **Emphasis caps:** Fits spite narrative ("this is a BAD password")
4. **Numbers:** Dean uses 123 in trailing, might use in middle
5. **Intensifiers:** Natural language variations not fully tested
6. **Doubled words:** Emphasis pattern in natural speech
7. **Longer quotes:** Dean's exact words we haven't tested literally
8. **Alternating:** Common pattern in early internet culture (!1!1!!)

---

## Files

- `generate.py` - Combined generator for all 8 families (~20M candidates)
- `run_attempt.sh` - Shell wrapper for hashcat execution
- `README.md` - This file

---

## Next Steps After This Attempt

If unsuccessful, consider:

1. **Deep BTCRecover patterns** - Token-based flexible matching
2. **Position-specific brute force** - Brute certain character positions only
3. **Phonetic variations** - "stoopid", "passw3rd", etc.
4. **Keyboard patterns** - qwerty, asdf, 1234567890
5. **Cultural deep dive** - 2011 memes, DEFCON-specific phrases
6. **Extended length** - 25-30 character passphrases
7. **Rule-based mutations** - Hashcat rules on promising base phrases

---

**Confidence Level:** MEDIUM-HIGH

These patterns explore alternative mutation strategies that are logically consistent with Dean's confirmed habits but weren't systematically tested in previous attempts.
