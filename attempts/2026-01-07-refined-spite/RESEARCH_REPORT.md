# Refined Spite Passphrase Research Report

## Overview

This report documents the vocabulary and patterns extracted from Dean Pierce's actual writing across GitHub, Telegram, blog posts, and social media to inform a refined passphrase generator.

## Key Quotes from Dean (Telegram)

These are Dean's own words about his password:

1. **"I just know it's going to be the dumbest freaking password."**
2. **"99% sure that if it ever cracks it's going to be something embarrassingly stupid."**
3. **"More like 'this is a very bad password' it's not some BDSM thing"**
4. **"I think a mutation of 'bad password' is more likely."**
5. **"There's two options, it's either never going to crack, or it's going to be something really really stupid, heh."**
6. **"Yeah for sure, also 'dumb'"** (when asked about alternatives to "bad")
7. **"when bitcoin-qt first added wallet encryption, I tried to set a dumb one, but it made me set something longer"**

## Dean's Confirmed Vocabulary (from all sources)

### Words Dean Actually Uses

**Casual expressions (high frequency in Telegram):**
- yeah, maybe, probably, definitely, pretty, actually, really, sure, nice, good, weird, curious, fun

**Self-deprecating adjectives Dean uses:**
- dumb, stupid, bad, crappy, shitty, weak, poor, silly, foolish, awful

**Words Dean does NOT typically use (remove from lists):**
- horrible, lame, extremely, terrible, pathetic, truly, boring, generic, obvious, idiotic, basic, simple, lazy

**2011 era words confirmed in Dean's lexicon:**
- poop (confirmed: "poop123" was his LUKS password)
- poopy
- potato (has potato emoji in Mastodon display name, "added potato" in commits)
- derp, derpy (multiple GitHub commits)

### Password-related nouns Dean would use
- password
- passphrase
- phrase

### Words to EXCLUDE (not in Dean's lexicon per user feedback)
- pass, passwd, pw, word, key, secret, code, thing, idea
- horrible, lame, extremely, terrible, pathetic, truly
- boring, generic, obvious, idiotic, basic, simple, lazy

## Passphrase Structure (from A/B test and Signal chat)

### Confirmed by Dean:
- **Separators:** Spaces (most likely), maybe periods
- **Capitalization:** First word capitalized
- **Word count:** 6-8 words (Bitcoin 0.4.0 suggested "8 or more words" but Dean may have tested with fewer)

### Trailing Characters (refined per user feedback)
- Characters to use: `1234!@#$` (8 options)
- Length: 0-6 characters
- Optional separator before trailing: space or period
- Examples: `!`, `!!`, `!!!`, `!!1`, `!@#`, `123`, `1234`, `!@#$`, ` !!!`, `.!!1`

### Leetspeak (minimal)
- Only on "password" or "passphrase"
- @ for a, $ for s
- Examples: p@ssword, pa$$word, p@$$word, p@ssphrase, pa$$phrase, p@$$phrase

## Refined Word Lists

### STARTERS (words Dean would start a sentence with)
```
This, this, It, it, What, what, That, that, Here, My
```

### CONNECTORS
```
is, was
```

### ARTICLES
```
a, the, one, my
```

### FILLERS (words Dean actually uses for emphasis)
```
really, very, super, so, pretty, damn, freaking
```

### SPITE WORDS (Dean's actual vocabulary)
```
bad, dumb, stupid, awful, crappy, shitty, weak, poor, silly, foolish, poop, poopy, potato
```

### NOUNS (password-related only)
```
password, passphrase, phrase
```

## Passphrase Patterns

### 6-word pattern (1 filler)
```
This is a [filler] [spite] [noun]
Example: "This is a really bad password"
```

### 7-word pattern (2 fillers)
```
This is a [filler] [filler] [spite] [noun]
Example: "This is a really really bad password"
```

### 8-word pattern (3 fillers)
```
This is a [filler] [filler] [filler] [spite] [noun]
Example: "This is a really really really bad password"
```

## Trailing Character Combinations

Using characters `1234!@#$` (8 options), generate all combinations from 0-4 characters:
- Empty (no trailing)
- 1 char: 1, 2, 3, 4, !, @, #, $ (8)
- 2 chars: 11, 12, !!, !1, @#, etc. (64)
- 3 chars: 111, !!!, !@#, 123, etc. (512)
- 4 chars: 1234, !@#$, !!!!, etc. (4096)

Total trailing combinations: 1 + 8 + 64 + 512 + 4096 = 4,681

With optional space or period separator before trailing:
- No trailing: 1 variant
- With trailing: 4,680 * 3 separators = 14,040 variants
- Total: 14,041 trailing variants

## Candidate Count (Final)

- Starters: 10
- Connectors: 2
- Articles: 4
- Fillers: 7
- Spite words: 13
- Nouns with leetspeak: 9
- Trailing variants: 14,041

Base patterns (without trailing):
- 6-word: 10 * 2 * 4 * 7 * 13 * 9 = 65,520
- 7-word: 10 * 2 * 4 * 7 * 13 * 9 = 65,520
- 8-word: 10 * 2 * 4 * 7 * 13 * 9 = 65,520
- Total base: 196,560

**Total with trailing: 196,560 * 14,041 = 2,759,898,960 (~2.8 billion candidates)**

## Recommendations

1. Focus on 8-word pattern first (matches Bitcoin 0.4.0 suggestion)
2. Use "really" as primary filler (Dean's example used it)
3. Use "bad" as primary spite word (Dean's example)
4. Include "dumb" and "stupid" as alternatives
5. Include poop/poopy/potato for 2011 era flavor
6. Minimal leetspeak, only on password/passphrase
7. Trailing combinations using 1234!@#$ up to 6 chars

---
Last updated: 2026-01-07
