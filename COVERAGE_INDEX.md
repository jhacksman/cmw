# Coverage Index - What Has Been Tried

This document tracks all known cracking attempts to avoid duplicating work and identify gaps in coverage.

## Exhausted Search Space (Confirmed)

### Brute Force by Dean (from crackmywallet.org)

| Pattern | Description | Keyspace Size | Status |
|---------|-------------|---------------|--------|
| `?d{1-9}` | All digits 1-9 chars | ~1.1 billion | EXHAUSTED |
| `?l{1-7}` | All lowercase 1-7 chars | ~8.3 billion | EXHAUSTED |
| `?a{1-6}` | All printable ASCII 1-6 chars | ~735 billion | EXHAUSTED |

### Dictionary Attacks by Dean

| Wordlist | Rules | Estimated Candidates | Status |
|----------|-------|---------------------|--------|
| rockyou.txt (~14M) | best64 | ~900M | EXHAUSTED |
| rockyou.txt (~14M) | d3ad0ne | ~1.4B | EXHAUSTED |
| rockyou.txt (~14M) | dive | ~2.8B | EXHAUSTED |
| weakpass2a (~100M) | best64 | ~6.4B | EXHAUSTED |

### Community Attempts

| Attacker | Duration | Approach | Keyspace | Status |
|----------|----------|----------|----------|--------|
| Solar Designer | ~1 month | Unknown (likely targeted) | Unknown | EXHAUSTED |
| Jack Hacksman | Ongoing | Custom combinatorics | ~100B permutations | EXHAUSTED |
| Various GPU operators | Unknown | Various | Unknown | Unknown |

## Gaps in Coverage (Untried or Uncertain)

### High Priority Gaps

1. **Exact phrase variations with spaces** - While dictionary attacks were run, targeted phrase generation with Dean's specific patterns may not have been exhaustive

2. **Trailing character combinations** - Dean mentioned 1, 3, or 6 trailing chars (!, ?, ~, `) - systematic coverage unclear

3. **Leetspeak with Dean's specific patterns** - p455, p@$$ specifically, not generic leet rules

4. **Repeated character patterns** - "pooooooooooooooop" style elongation

5. **Period-separated phrases** - "this.is.a.bad.password" variants

6. **Mixed separator patterns** - Combinations of spaces and periods

### Medium Priority Gaps

1. **2011 era slang combinations** - derpy, lulz, rofl, potato in phrase context

2. **DEFCON-related phrases** - Conference context from August 2011

3. **Capitalization patterns** - Title Case, Sentence case, etc.

4. **Suffix number patterns** - Based on Dean's "poop123" LUKS password

### Low Priority Gaps

1. **Uncommon adjectives** - Beyond the obvious bad/dumb/stupid

2. **Alternative nouns** - key, secret, phrase, etc.

3. **Longer phrases** - 6-7 word combinations

## Coverage Verification Needed

The following areas need verification of whether they were actually tried:

1. **Jack's 100B permutations** - What generator/grammar was used?
2. **Solar Designer's month** - What approach did he take?
3. **Hashtopolis runs** - Were any coordinated runs completed?

## Recommended Next Steps

Based on gaps identified, priority order for new attempts:

1. Targeted phrase generator with Dean's exact patterns
2. Systematic trailing character combinations
3. Period-separated variants
4. Repeated character patterns
5. Era-specific slang combinations
