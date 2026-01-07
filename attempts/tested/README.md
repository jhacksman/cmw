# Tested Attempts

This folder contains password cracking attempts that have already been run and exhausted.

## Completed Attempts (Chronological)

| Folder | Candidates | Hypothesis | Separators | Trailing | Status |
|--------|------------|------------|------------|----------|--------|
| 2026-01-05-tested | ~600M | "this is a [adj] [noun]" patterns | spaces | various | Exhausted |
| 2026-01-05-spite-password-tested | ~11K | Claude's spite password hypothesis | spaces | minimal | Exhausted |
| 2026-01-05-10b-combined | ~10.4B | Combined spite hypotheses | spaces/periods | various | Exhausted |
| 2026-01-06-2b-research-based | ~2.2B | GitHub/website analysis patterns | spaces/periods | various | Exhausted |
| 2026-01-06-569m-elongated-patterns | ~569M | Elongated potato/poop (pooooop) | none | digits/symbols | Exhausted |
| 2026-01-06-8word-dumbest | ~950M | 8-word "dumbest" with 403/404/405 | spaces | 403/404/405 | Exhausted |
| 2026-01-07-top5-phrases | ~26M | Top 5 "this is a..." phrases | spaces/periods | 0-6 chars (1234!@#$) | Exhausted |
| 2026-01-07-refined-spite | ~2.8B | 6/7/8 word patterns, Dean's vocab | spaces/periods | 0-4 chars (1234!@#$) | Exhausted |
| 2026-01-07-top22-8word | ~52.7M | 22 eight-word prioritized phrases | spaces/periods | 0-6 chars (1234!@#$) | Exhausted |
| 2026-01-07-spite-passphrases | ~100M+ | Various 6/7/8 word generators | spaces | various | Exhausted |

## Total Tested

Approximately **17+ billion** candidates have been tested from these attempts.

## Key Patterns Covered

The following patterns have been extensively tested:

1. **"This is a [filler] [spite] password/passphrase"** - 6/7/8 word variants with really/very/super fillers and bad/dumb/stupid spite words
2. **Elongated patterns** - poooooop, potaaaato with varying o/a counts
3. **Trailing combinations** - 0-6 chars from 1234!@#$ with space/period separators
4. **Case variants** - lowercase and first-word capitalized
5. **Leetspeak on nouns** - p@ssword, pa$$word, p@$$phrase variants

## Notes

- All attempts in this folder have been run through hashcat against the crackmywallet.org hash
- None of these attempts found the correct passphrase
- Hardware: 3x 3090s at ~270k H/s for Bitcoin wallet mode (11300)
- See individual folder READMEs for detailed methodology
