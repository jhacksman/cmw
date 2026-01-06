# Pierce403 (Dean Pierce) GitHub Writing Style Analysis

## Overview
Comprehensive analysis of pierce403's GitHub account (169 repos) to identify writing patterns, vocabulary, and style that could inform password generation for the CrackMyWallet challenge.

## Key Patterns Identified

### 1. "X is/are hard" Pattern (HIGH PRIORITY)
Dean frequently uses this self-deprecating pattern in commit messages:
- "tables are hard" (nakatomi, ponzi.finance)
- "spelling is hard" (roboform-wordlists)
- "datatypes are hard" (nakatomi)
- "numbers are hard" (ponzi.finance)
- "markdown is hard" (crypto.me, discoball)
- "flask is hard" (cors.io)
- "typing is hard"

**Password candidates to explore:**
- "passphrases are hard"
- "passwords are hard"
- "passphrase is hard"
- "password is hard"
- "passphrases are dumb"
- "passwords are dumb"
- "security is hard"
- "crypto is hard"
- "bitcoin is hard"

### 2. "X is/are stupid/dumb" Pattern (HIGH PRIORITY)
- "stupid string bugs" (btclotto)
- "stupid javascript" (ponzi.finance)
- "stupid javascript object comparisons" (ponzi.finance)
- "stupid modal stuff" (stupid.site)
- "javascript is dumb" (ponzi.finance)
- "fixing dumbness" (keyhunter)
- "CSP is dumb" (nweb)
- "stupid postgres" (nweb)

**Password candidates:**
- "this is a stupid passphrase"
- "this passphrase is stupid"
- "stupid passphrase"
- "dumb passphrase"
- "this is dumb"
- "passwords are stupid"

### 3. "derp" Pattern (HIGH PRIORITY - 2011 era slang)
- "heh, derp" (platypus)
- "derp, args" (birdfeeder)
- "markdown derp" (crypto.me)
- "derped the inc/dec" (bbly.io)
- "derp" (multiple repos)
- Also has repo named "eliza-derp"

**Password candidates:**
- "derpy passphrase"
- "derp derp derp"
- "this is derpy"
- "derpy password"

### 4. "meh" Pattern
- "meh" (stupid.site)
- "more meh" (stupid.site)

### 5. "yay" Pattern
- "yay" (nakatomi)
- "yay logic" (crypto.me)
- "yay room number"
- "yay cleaning" (cors.io)
- "yay apache 2" (cors.io)
- "yay CORS" (cors.io)
- "yay, dragon context" (dracoria)

### 6. "whoops" Pattern
- "whoops. ABI thing" (stupid.site)
- "whoops, too many indexes" (badger.ninja)
- "whoops, forgot about updating the function" (discoball)
- "whoops rename to discoTable" (discoball)
- "whoops, fixed agents treeview bug"

### 7. 2011 Era Slang (CRITICAL - wallet created Sept 2011)
- "added potato" (gnuguru) - 2011 meme reference
- "added the lol" (badger.ninja)
- "derp" (multiple)
- "lulz" (mentioned in Signal chat as popular in 2011)
- "rofl" (mentioned in Signal chat)

### 8. Casual Grammar Patterns
- "okay, I had did that wrongly" (stupid.site) - intentionally bad grammar
- "first commit!wq" (btclotto) - vim typo left in
- "firsot comimt" (bbly.io) - intentional typo
- "first tyop" (dracoria) - intentional typo
- "frist psot" (ponzi.finance) - intentional typo/meme

### 9. Elongated Characters
- "POOOOOL" (503.party)
- "HABITAT" (503.party)
- "MORE BOLD"

### 10. Code Comments Found
- "fixmelol!" (btclotto/src/btcadmin.py) - CSRF token placeholder
- "lame, the address was invalid" (btclotto/src/lotto.py)

### 11. Other Notable Phrases
- "time to get stupid" (stupid.site)
- "everything is terrible" (cors.io)
- "so much suck" (cors.io)
- "computers are fun" (cors.io)
- "do you believe in miracles?" (cors.io)
- "hackers hack" (hack.guru)
- "omg hackers" (badger.ninja)
- "copy pasta" (badger.ninja)
- "fell off a truck" (roboform-wordlists)
- "all hail the Metal Lord!" (dracoria)
- "decentralize all the things" (discoball)
- "refactored the shit out of everything" (bbly.io)
- "fuck 12" (503.party)

### 12. Project Names That Could Be Password-Related
- stupid.site - "time to get stupid"
- hack.guru - "hackers hack"
- passwords.today
- crackmywallet (the challenge itself)

## Social Media Findings

### Mastodon (@deanpierce@defcon.social)
- **CRITICAL: Has potato emoji 🥔 in display name** - confirms "potato" is significant to Dean
- Bio: "Security researcher from Portland Oregon. Locally affiliated with PDX2600, RainSec, Sophsec, CtrlH, PDX Bitcoin, BSidesPDX, HackBoat"
- 292 posts, joined Nov 2022

### deanpierce.net Website
- Project "Seeds of Contempt" - contempt/spite theme aligns with "spite password" theory
- Talk titles show casual naming: "They Put Money on the Internet!", "DIY Black Badge"
- Project names: stupid.site, hack.guru, ponzi.finance, crackmywallet

## Blog Writing Style (pxdojo.net)

### 2011 Blog Post (December 28, 2011 - CRITICAL: closest to wallet creation)
"A simple mtgox auto trading bot in python"
- "Just for kicks" - casual expression
- "dead simple" - casual technical language
- "take no time at all" - casual expression
- "Good luck, and be careful not to shoot your foot off!" - casual warning
- "write some damn code" - casual/expletive
- "oh no!!" - error handling message in code
- Variable names: "width", "girth", "high_scrape", "low_scrape" - casual naming

### 2017 Blog Posts
- "Shitposting on reddit" (self-description in Qubes post)
- "Shut up, that's why" (Qubes post)
- "if it's stupid, and it works, it's not stupid" (Qubes post)
- "#YOLO" (Qubes post)
- "derpy" used in technical analysis (Ants Don't Have Blood post)
- "pain in the ass" (SQLMap post)
- "the ever-loving crap out of" (Qubes post)
- "the derp-de-doo who implemented this feature" (Ants post)

## Signal Chat Hints (from user's conversation with Dean)
- Passphrase likely has spaces or periods between words
- More words than usual (4-7 instead of 3-4)
- Trailing chars: 1, 3, maybe 6 - exclamations, question marks, tildes, backticks
- Leetspeak: p455, p@$$, @ for a, $ for s
- No pipe in passwords
- No 7 for R
- Set "out of spite" - deliberately weak
- "This is a really dumb passphrase" or similar
- Maybe "bad" instead of "dumb"

## Recommended Password Generation Priorities

### Priority 1: "X is/are hard/dumb/stupid" patterns
```
passphrases are hard
passwords are hard
passphrase is hard
password is hard
passphrases are dumb
passwords are dumb
passphrase is dumb
password is dumb
passphrases are stupid
passwords are stupid
this passphrase is hard
this password is hard
security is hard
crypto is hard
bitcoin is hard
```

### Priority 2: Self-deprecating spite phrases
```
this is a dumb passphrase
this is a stupid passphrase
this is a bad passphrase
this is a really dumb passphrase
this is a really bad passphrase
this passphrase is dumb
this passphrase is stupid
this passphrase is bad
dumb passphrase
stupid passphrase
bad passphrase
```

### Priority 3: 2011 era slang integration
```
derpy passphrase
this is derpy
derp derp derp
lulz passphrase
potato passphrase
this is so derpy
derpy password
potato potato potato
this is potato
derp de doo
```

### Priority 3.5: Blog-derived phrases (2011 era)
```
just for kicks
dead simple
shoot your foot off
oh no
write some damn code
if its stupid and it works
shut up thats why
shitposting on reddit
```

### Priority 4: Elongated/emphasis patterns
```
this is a baaaad passphrase
this is a duuumb passphrase
baaaaaad password
stuuuupid passphrase
```

### Priority 5: Casual grammar patterns
```
this passphrase is dumb okay
okay this is dumb
meh passphrase
yay passphrase
whoops bad password
```

## Separators to Try
- Space (most likely per Dean)
- Period (second most likely)
- No separator
- Dash
- Underscore

## Trailing Patterns to Try
- ! (1-6 times)
- ? (1-6 times)
- ~ (1-6 times)
- ` (1-6 times)
- 1, 11, 111, 1!, 1!!, etc.
- 3, 33, 333
- 6, 66, 666

## Case Variations
- all lowercase (most likely)
- First Letter Capitalized
- ALL CAPS
- Mixed case

## Leetspeak Variations
- a -> @
- s -> $
- a -> 4
- s -> 5
- e -> 3
- o -> 0
- Combinations: p@$$phr@$e, p455phr453, etc.

## Additional Findings from Complete Analysis

### Confirmed Patterns
1. **Potato is significant** - Dean has potato emoji in Mastodon display name, "added potato" in commits
2. **"X is hard" is a consistent pattern** - found across many repos: tables, spelling, datatypes, numbers, markdown, flask, typing, copypasta, grammar
3. **Self-deprecating humor** - consistent across all platforms (GitHub, blog, socials)
4. **Casual/expletive language** - "damn", "shit", "fuck", "crap" appear in commits and blog
5. **2011 era slang** - derp, potato, lulz were popular when wallet was created

### Key Insight
The wallet was encrypted after September 27, 2011 (Bitcoin 0.4.0 release). Dean's December 2011 blog post shows his writing style at that exact time period - casual, self-deprecating, using phrases like "just for kicks", "dead simple", and "shoot your foot off".

### Most Likely Password Structures (based on all evidence)
1. Self-deprecating phrase about the passphrase itself: "this is a [bad/dumb/stupid/derpy] passphrase"
2. "X is/are hard/dumb/stupid" pattern: "passphrases are hard", "passwords are dumb"
3. 2011 slang integration: "derpy passphrase", "potato passphrase"
4. Spite-based: deliberately weak, possibly mocking the security prompt

---
Last updated: 2026-01-06 (added website/social analysis)
