# Future Password Cracking Plans

This document outlines future approaches to explore if the current attempt doesn't succeed.

## Current Attempt: password-is-spite (~33B)

Brute forcing the spite slot in "this password is [intensifier] [BRUTE 1-5 chars]" structure.

## Future Directions

### 1. Brute Force Intensifier Slot Instead

Pattern: "this password is [BRUTE 1-5 chars] bad/dumb"

Instead of brute forcing the spite word, brute force the intensifier position while keeping Dean's confirmed spite words (bad, dumb).

Estimated: Similar ~33B candidates

### 2. Add Digit Trailing (Dean's "poop123" Pattern)

Dean mentioned "poop123" as an example, suggesting digits at the end are plausible.

Expand trailing to include:
- Current: !?~` (0, 1, 3, 6 repeats)
- Add: 1-3 digit suffix (000-999)

This would multiply candidates by ~1000x, so would need to be combined with a smaller base set.

### 3. Minimum Compliance Patterns

Based on Bitcoin-Qt's "10 or more random characters, or eight or more words" prompt:

- Exactly 10 character passwords (hitting minimum)
- Exactly 8 word passphrases (hitting minimum)
- Repetitive patterns to inflate length: "bad bad bad bad bad bad bad bad"

### 4. Meta-Commentary About Requirements

Phrases that comment on the requirement itself:
- "this passphrase is too long"
- "why do i need eight words"
- "this is a dumb requirement"

### 5. Prompt-Based Variations

The Bitcoin-Qt prompt said "Enter a passphrase to encrypt your wallet."

Variations on this prompt text:
- "enter a passphrase"
- "encrypt your wallet"
- "passphrase to encrypt"

### 6. Short Sarcastic Tokens (Exactly 10 Chars)

If Dean was hitting a 10-char minimum:
- "badpasswd!" (10 chars)
- "dumbpassw!" (10 chars)
- Truncated words + punctuation to hit exactly 10

### 7. Dean's Confirmed Vocabulary Deep Dive

Words Dean has actually used in his writing:
- From Telegram: "poop", "potato", "derp", "derpy"
- From GitHub: coding-related terms
- From website: security/crypto terminology

### 8. Mixed Intensifier Patterns

Instead of repeating the same intensifier:
- "this password is really very bad"
- "this password is super really dumb"

### 9. Typo Variations

Common typos of the base phrases:
- "thsi password is really bad"
- "this passwrod is really bad"

### 10. No-Space Variants

All words concatenated:
- "thispasswordisreallybad"
- "ThisPasswordIsReallyBad" (camelCase)

## Priority Order

1. Current attempt (password-is-spite ~33B) - IN PROGRESS
2. Brute force intensifier slot
3. Minimum compliance (exactly 10 chars or 8 words)
4. Digit trailing expansion
5. Meta-commentary phrases
6. Short sarcastic tokens

## Notes

- Always use Dean's exact trailing pattern (0, 1, 3, or 6 of SAME char)
- No mixing within leetspeak (all @ or all 4, not mixed)
- Separator consistency (spaces or periods throughout)
- First cap or lowercase only (not ALL CAPS)
