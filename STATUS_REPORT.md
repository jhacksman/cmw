# CrackMyWallet Status Report

**Date:** January 7, 2026  
**Total Candidates Tested:** ~17+ billion  
**Result:** No hits

## Current Status

All planned attempts have been run and exhausted. The wallet password remains uncracked despite testing approximately 17 billion candidates across multiple hypothesis-driven generators.

## Tested Attempts Summary

### Phase 1: Initial Hypotheses (Jan 5, 2026)

**2026-01-05-tested (~600M candidates)**
- Pattern: "this is a [adjective] [noun]" variations
- Separators: spaces
- Result: Exhausted, no hits

**2026-01-05-spite-password-tested (~11K candidates)**
- Pattern: Claude's initial spite password hypothesis
- Separators: spaces
- Result: Exhausted, no hits

**2026-01-05-10b-combined (~10.4B candidates)**
- Pattern: Combined spite hypotheses with extensive variations
- Separators: spaces and periods
- Result: Exhausted, no hits

### Phase 2: Research-Based Attempts (Jan 6, 2026)

**2026-01-06-2b-research-based (~2.2B candidates)**
- Pattern: Patterns derived from GitHub commits, website, and social media analysis
- Covered: "X is hard" patterns, self-deprecating phrases, 2011 slang
- Result: Exhausted, no hits

**2026-01-06-569m-elongated-patterns (~569M candidates)**
- Pattern: Elongated potato/poop variations (pooooop, potaaaato)
- Trailing: digits and symbols
- Result: Exhausted, no hits

**2026-01-06-8word-dumbest (~950M candidates)**
- Pattern: 8-word "dumbest" passphrases
- Trailing: 403, 404, 405 variations
- Result: Exhausted, no hits

### Phase 3: Refined Spite Passphrases (Jan 7, 2026)

**2026-01-07-top5-phrases (~26M candidates)**
- Pattern: Top 5 "this is a..." phrases with password/passphrase variants
- Separators: consistent spaces OR periods throughout
- Trailing: 0-6 chars from 1234!@#$
- Result: Exhausted, no hits

**2026-01-07-refined-spite (~2.8B candidates)**
- Pattern: 6/7/8 word patterns using Dean's confirmed vocabulary
- Fillers: really, very, super, so, pretty, damn, freaking
- Spite words: bad, dumb, stupid, awful, crappy, shitty, weak, poor, silly, foolish, poop, poopy, potato
- Separators: spaces and periods
- Trailing: 0-4 chars from 1234!@#$
- Result: Exhausted, no hits

**2026-01-07-top22-8word (~52.7M candidates)**
- Pattern: 22 prioritized eight-word phrases
- Structure: "this is a [filler] [filler] [filler] [spite] password/passphrase"
- Separators: consistent spaces OR periods
- Trailing: 0-6 chars from 1234!@#$
- Result: Exhausted, no hits

**2026-01-07-spite-passphrases (~100M+ candidates)**
- Pattern: Various 6/7/8 word generators
- Result: Exhausted, no hits

## Key Clues from Dean (Mapped to Coverage)

| Clue | Source | Covered By |
|------|--------|------------|
| "dumbest freaking password" | Telegram | refined-spite, top22-8word |
| "embarrassingly stupid" | Telegram | refined-spite, 10b-combined |
| "this is a very bad password" | Telegram | top5-phrases, top22-8word, refined-spite |
| "mutation of 'bad password'" | Telegram | All spite attempts |
| "made me set something longer" | Telegram | 6/7/8 word patterns |
| Uses "really", "very", "dumb", "stupid", "bad" | A/B test | All refined attempts |
| Potato emoji in Mastodon | Social | refined-spite, elongated-patterns |
| "poop123" was LUKS password | Telegram | elongated-patterns, refined-spite |
| "X is hard" GitHub pattern | GitHub | 2b-research-based |
| Trailing chars: 1234!@#$ | Signal chat | top5, top22, refined-spite |
| Separators: spaces or periods | Signal chat | All recent attempts |

## Patterns NOT Yet Extensively Tested

Based on the research files, the following patterns have received less coverage:

1. **Short spite phrases (2-4 words)** - "bad password", "dumb passphrase" with heavy trailing
2. **"X is hard/dumb" standalone patterns** - "passphrases are hard", "passwords are dumb" (not in "this is a..." format)
3. **Derp/derpy patterns** - "derpy passphrase", "this is derpy"
4. **2011 blog phrases** - "just for kicks", "dead simple"
5. **Mixed separator patterns** - underscores, dashes (though Dean said spaces/periods most likely)
6. **Different starters** - "my", "a", "one" instead of "this is a"

## Questions for Dean to Narrow Search Space

These questions could significantly reduce the search space:

1. **Separator certainty:** Are you 100% sure it's spaces or periods? Could it be no separator at all (concatenated)?

2. **Trailing certainty:** Do you remember if there were trailing characters? If so, was it numbers, symbols, or both?

3. **Word count:** Is 8 words your best guess, or could it be shorter (4-5 words)?

4. **Capitalization:** First word capitalized, or all lowercase?

5. **"password" vs "passphrase":** Which word feels more right? Or could it be something else entirely like "phrase" or "pwd"?

6. **The spite word:** "bad", "dumb", or "stupid" - which feels most like something you'd use in 2011?

7. **Filler words:** Did you use repetition (really really really) or variety (really very super)?

8. **2011 context:** Were you thinking about Bitcoin specifically, or was it more generic frustration at the length requirement?

9. **Memorable numbers:** 403, 2011, or any other numbers that were significant to you then?

10. **Recovery artifacts:** Have you checked old password managers, browser saved passwords, shell history, or email drafts from that period?

## Hardware Performance

- 3x NVIDIA 3090 GPUs
- ~270,000 hashes/second for Bitcoin wallet mode (hashcat -m 11300)
- 1 billion candidates = ~62 minutes
- 10 billion candidates = ~10.3 hours

## Next Steps

1. Review the "Patterns NOT Yet Extensively Tested" section above
2. Get answers to the clarifying questions from Dean
3. Based on answers, create more targeted generators with smaller search spaces
4. Consider legitimate recovery avenues (old backups, password managers, notes)

---
*Report generated: January 7, 2026*
