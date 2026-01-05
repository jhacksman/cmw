# Priority Analysis - Untried Passphrase Patterns

This document provides a data-driven analysis of passphrase patterns that should be tried next, based on all available evidence from Dean Pierce (px).

## Executive Summary

Based on analysis of Dean's statements across Telegram, Signal, and crackmywallet.org, the most likely passphrase patterns that may not have been systematically tried are:

1. **Exact phrase variations with trailing characters** - Dean's specific trailing char patterns (1, 3, 6 chars)
2. **Period-separated phrases** - "this.is.a.bad.password" style
3. **Dean's specific leetspeak** - p455, p@$$ (not generic leet rules)
4. **Elongated character patterns** - "pooooooooooooooop" style

## Evidence-Based Priority Ranking

### Priority 1: Core Phrases with Dean's Trailing Patterns (HIGHEST)

**Evidence:**
- Dean said: "Likely 1, 3, maybe 6, exclamations or question marks sometimes tildes or back ticks"
- This is very specific guidance that may not have been systematically applied

**Patterns:**
```
this is a bad password!
this is a bad password!!!
this is a bad password!!!!!!
this is a bad password?
this is a bad password~
this is a bad password`
this is a bad password123
```

**Estimated keyspace:** ~5,000 candidates
**Script:** `scripts/generate_trailing_combos.py`

### Priority 2: Period-Separated Phrases (HIGH)

**Evidence:**
- Dean said: "Usually spaces, sometimes dots, rarely dashes"
- Period separation may not have been systematically tried with all phrase variations

**Patterns:**
```
this.is.a.bad.password
this.is.a.bad.passphrase
bad.password
this.is.a.dumb.password
this.is.a.very.bad.password
```

**Estimated keyspace:** ~3,000 candidates
**Script:** `scripts/generate_candidates.py` (included in all priorities)

### Priority 3: Dean's Specific Leetspeak (HIGH)

**Evidence:**
- Dean confirmed: "I've leetified pass as p455, p@$$, and combinations like that"
- Dean confirmed: "@ for a and $ for s sometimes"
- Dean explicitly said he NEVER uses 7 for r

**Patterns:**
```
this is a bad p455word
this is a bad p@$$word
thi$ i$ @ b@d p@$$word
b@d p@$$word
```

**Important:** Generic leet rules (like best64) may not have specifically targeted Dean's confirmed patterns.

**Estimated keyspace:** ~50,000 candidates
**Script:** `scripts/generate_candidates.py --priority 3`

### Priority 4: Elongated/Repeated Characters (MEDIUM-HIGH)

**Evidence:**
- Dean said: "I just know it's going to be the dumbest freaking password. Like 'pooooooooooooooop' or something"
- This is a direct hint that may have been overlooked

**Patterns:**
```
pooooooooooooooop
baaaaaad password
duuuuumb password
this is baaaaaad
sooooo bad
```

**Estimated keyspace:** ~2,000 candidates
**Script:** `scripts/generate_elongated.py`

### Priority 5: 2011 Era Slang (MEDIUM)

**Evidence:**
- Dean mentioned the DEFCON 19 timeframe (August 2011)
- Era slang: "derpy was popularized around that time. lulz was peak popular, rofl, potato"

**Patterns:**
```
this is a derpy password
derpy passphrase
this is such a derpy passphrase
lulzy password
```

**Estimated keyspace:** ~10,000 candidates
**Script:** `scripts/generate_candidates.py --priority 2`

### Priority 6: Extended Phrases (5-7 words) (MEDIUM)

**Evidence:**
- Dean said his word count is "definitely higher than my average passphrase word count, which is usually more like 3 or 4"
- This suggests 5-7 words

**Patterns:**
```
this is a really really bad password
this is a very very dumb passphrase
this is the dumbest password ever
```

**Estimated keyspace:** ~5,000 candidates
**Script:** `scripts/generate_candidates.py --priority 5`

### Priority 7: DEFCON Context (LOW)

**Evidence:**
- Wallet encrypted around DEFCON 19 timeframe
- Less direct evidence this influenced the passphrase

**Patterns:**
```
defcon password
my defcon password
vegas password
```

**Estimated keyspace:** ~500 candidates
**Script:** `scripts/generate_candidates.py --priority 6`

## What Has Been Exhausted (Do NOT Retry)

Based on crackmywallet.org and community reports:

| Pattern | Status |
|---------|--------|
| All digits 1-9 chars | EXHAUSTED |
| All lowercase 1-7 chars | EXHAUSTED |
| All ASCII 1-6 chars | EXHAUSTED |
| rockyou.txt + best64/d3ad0ne/dive | EXHAUSTED |
| weakpass2a + best64 | EXHAUSTED |

## Recommended Attack Order

1. Run `scripts/generate_candidates.py --priority 1` (core phrases + trailing)
2. Run `scripts/generate_trailing_combos.py` (systematic trailing)
3. Run `scripts/generate_candidates.py --priority 3` (Dean's leetspeak)
4. Run `scripts/generate_elongated.py` (repeated chars)
5. Run `scripts/generate_candidates.py --priority 2` (era slang)
6. Run `scripts/generate_candidates.py --priority 5` (extended phrases)
7. Run `scripts/generate_candidates.py --priority 6` (DEFCON context)

## Hashcat Command

```bash
# Generate wordlist
python scripts/generate_candidates.py > candidates.txt

# Run hashcat
hashcat -m 11300 -a 0 hash.txt candidates.txt

# With rules for additional mutations
hashcat -m 11300 -a 0 hash.txt candidates.txt -r rules/best64.rule
```

## Hash for Reference

```
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
```

## Key Insights Summary

| Insight | Source | Confidence |
|---------|--------|------------|
| It's a PASSPHRASE (multiple words) | Dean (Telegram) | HIGH |
| 4-7 words | Dean (Telegram) | HIGH |
| Spaces most likely, periods sometimes | Dean (Signal) | HIGH |
| Self-deprecating theme | Dean (crackmywallet.org) | HIGH |
| Trailing: 1, 3, or 6 chars (!, ?, ~, `) | Dean (Signal) | HIGH |
| Leetspeak: p455, p@$$ | Dean (Signal) | HIGH |
| NEVER 7 for r | Dean (Signal) | HIGH |
| NEVER pipe character | Dean (Signal) | HIGH |
| "pooooooooooooooop" style possible | Dean (Telegram) | MEDIUM |
| DEFCON 19 context | Dean (Telegram) | LOW |

## Gaps Requiring Verification

The following areas need verification of whether they were actually tried:

1. **Jack's 100B permutations** - What exact generator/grammar was used?
2. **Solar Designer's month** - What approach did he take?
3. **Hashtopolis runs** - Were any coordinated runs completed?

If you have information about these attempts, please update the COVERAGE_INDEX.md file.
