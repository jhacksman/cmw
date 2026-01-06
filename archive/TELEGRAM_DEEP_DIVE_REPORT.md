# Telegram Archive Deep Dive Report

**Date:** 2026-01-06  
**Archive:** ~31,000 messages from Crypto Rescue Telegram group  
**Focus:** Extracting password clues from Dean Pierce (px) and community discussions

## Critical Quotes from Dean (px)

### The "Dumbest Password" Theme

**[318] 2021-03-16:**
> "I just know it's going to be the dumbest freaking password. Like 'pooooooooooooooop' or something."

**[320] 2021-03-16:**
> "99% sure that if it ever cracks it's going to be something embarrassingly stupid."

**[724] 2021-08-27:**
> "when bitcoin-qt first added wallet encryption, I tried to set a dumb one, but it made me set something better, so I came up with the dumbest passphrase I could that matched the requirements."

**[959] 2021-12-16:**
> "There's two options, it's either never going to crack, or it's going to be something really really stupid, heh."

### Length Estimates

**[730] 2021-08-27:**
> "Yeah, but it was probably like 20 chars, I think the minimum that bitcoin-qt wanted was like 16."

**[939] 2021-12-16:**
> "I set the password *right* after they added the feature. I think it was something like 16 characters. I don't think they were doing phrases like that yet. I definitely set my password to the weakest possible thing I could out of spite."

### Specific Examples Given

**[751] 2021-08-27:**
> "More like 'this is a very bad password' it's not some BDSM thing :-p"

**[955] 2021-12-16:**
> "I think a mutation of 'bad password' is more likely."

**[960] 2021-12-16:**
> "I spent some time cracking an old LUKS password a couple years ago and it ended up being 'poop123'. Most of my LUKS passwords are actually pretty good though."

### Word Preferences

**[1136-1138] 2022-08-15 - Social Engineering Exchange:**
- Marek: "I have seen you on a Youtube video from a conference. U used offen the word 'stupid' in your example Code. Did you offen use this word in the past for your password instead of 'bad'?"
- px: "Yeah for sure, also 'dumb'"

### Separator Preferences

**[1770] 2025-04-12:**
> "Usually spaces, sometimes dots, rarely dashes, don't think I've ever used underscores"

### Timing

**[950] 2021-12-16:**
> "I'm pretty sure the first password I tried to set didn't work, and it told me to make a more complex one."

**[1550] 2023-08-02:**
> "I think it was whatever was released around June 2011. Should have been one of the first releases with password support"

## Community Efforts Documented

**[500] 2021-05-06:**
> "Now my gpu is on 100% with worst 2 billion passes"

**[504] 2021-05-06:**
> "I used hashcat a lot but many years ago. Now it is running for 7 hours for the billion list. It takes 2 days on my rtx 2060"

**[957] 2021-12-16 - Drizzt:**
> "I've been at this for months but my god If we haven't exhausted options yet. I've tried so many custom wordlists."

**[1097] 2022-08-03 - Præluceo Bonaparte:**
> "I tried a seed dictionary based on those and I know others did too, and I ran 2x3090s against it for a week without success"

**[294] 2021-02-26 - px:**
> "Solar Designer apparently spent like a month or so on it with no luck, which has me slightly concerned. I'm sure when it cracks it's going to be something so dumb."

## Key Insights Summary

### High-Confidence Patterns

1. **"this is a very bad password"** - Dean explicitly gave this as an example
2. **"bad password" mutation** - Dean said this is "more likely"
3. **"pooooooooooooooop"** - Dean's own example of what it might be
4. **"poop123"** - Confirmed as his actual LUKS password pattern
5. **~16-20 characters** - Dean's estimate of the length
6. **Spaces or dots** as separators (never underscores)
7. **"stupid" and "dumb"** - Confirmed words he uses in passwords

### The "Forced Complexity" Clue

Dean said he tried to set a dumb password but "it made me set something better." This suggests:
- The password meets some minimum complexity requirement
- It's the "dumbest" thing that still passes validation
- Likely has some variation (case, numbers, or special chars) to meet requirements

### Unexplored Patterns Based on This Analysis

1. **"this is a bad password"** variations (16 chars without "very")
2. **"this is a dumb password"** variations
3. **"this is a stupid password"** variations
4. **"bad.password"** with dots instead of spaces
5. **Elongated poop patterns** exactly 16-20 chars
6. **"poop" + numbers** patterns (like his LUKS "poop123")
7. **Case variations** of the above to meet complexity

### What's Likely Been Tried

- Basic "this is a very bad password" (too obvious, surely tried)
- Common wordlists (rockyou, etc.)
- Simple poop/potato patterns
- Basic leetspeak variations

### What Might NOT Have Been Tried

1. **Exact 16-character patterns** - Dean said "I think it was something like 16 characters"
2. **Period-separated phrases** - "this.is.a.bad.password" (17 chars)
3. **Minimal complexity additions** - just enough to pass validation
4. **"bad password" without "this is"** - shorter, might fit 16 chars
5. **Elongated single words** to exactly 16 chars

## Recommended Next Generator Focus

Based on this deep dive, the highest-priority unexplored space is:

1. **Exactly 16-character patterns** across all hypotheses
2. **Period-separated versions** of "bad password" phrases
3. **"poop" + trailing numbers** patterns (poop123, poop1234, etc.)
4. **Minimal complexity variations** - just one capital or one number

The key insight is Dean's repeated emphasis on "16 characters" and being forced to make it "better" than his first attempt. The password is likely the absolute minimum complexity that passed validation.
