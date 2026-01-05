# Crack My Wallet - Methodology Document

This document summarizes all known attempts to crack Dean Pierce's Bitcoin wallet passphrase and provides recommendations for future attempts.

## Summary of Exhausted Search Space

### Brute Force Attempts (by Dean)

| Pattern | Range | Status |
|---------|-------|--------|
| Digits only (`?d`) | 1-9 characters | EXHAUSTED |
| Lowercase only (`?l`) | 1-7 characters | EXHAUSTED |
| All ASCII (`?a`) | 1-6 characters | EXHAUSTED |

### Dictionary Attacks (by Dean)

| Wordlist | Rules Applied | Status |
|----------|---------------|--------|
| rockyou.txt | best64 | EXHAUSTED |
| rockyou.txt | d3ad0ne | EXHAUSTED |
| rockyou.txt | dive | EXHAUSTED |
| weakpass2a | best64 | EXHAUSTED |

### Community Attempts

- Solar Designer (famous password cracker) spent approximately one month without success
- Multiple GPU rig operators have attempted various attacks
- Various custom combinatorics generators have been built and run

## What We Know About the Passphrase

### From Dean's Direct Statements

1. **Type**: It's a PASSPHRASE (multiple words), not a single password
2. **Word Count**: More than Dean's usual 3-4 words, likely 4-7 words
3. **Separators**: Usually spaces, sometimes periods, rarely dashes, never underscores
4. **Theme**: Self-deprecating statement about password weakness
5. **Length**: Approximately 20 characters (Bitcoin-Qt minimum was ~16)
6. **Complexity**: Likely lowercase with possible mutations
7. **Leetspeak patterns**: Dean has used "p455", "p@$$", and combinations
8. **Trailing characters**: Likely 1, 3, or maybe 6 characters - exclamations (!), question marks (?), tildes (~), or backticks (`)

### Timeline Evidence

- **Encryption Date**: After September 27, 2011 (Bitcoin 0.4.0 release)
- **Context**: DEFCON 19 was August 4-7, 2011
- **Last Used**: Throughout 2012, forgotten by end of 2013
- **Cultural Context**: "derpy", "lulz", "rofl", "potato" were popular slang

### Dean's Exact Quotes

> "It's possible that the answer is some mutation of the passphrase 'this is a bad password', 'bad password', or some other self degrading statement commenting on the weakness of the password."

> "99% sure that if it ever cracks it's going to be something embarrassingly stupid"

> "I just know it's going to be the dumbest freaking password. Like 'pooooooooooooooop' or something"

> "Usually spaces, sometimes dots, rarely dashes, don't think I've ever used underscores"

> "More like 'this is a very bad password' it's not some BDSM thing"

## Recommended Attack Strategies (Priority Order)

### Priority 1: Core Phrase Variations

Focus on variations of the core self-deprecating phrases Dean mentioned:

```
Base phrases:
- this is a bad password
- this is a bad passphrase
- bad password
- bad passphrase
- this is a dumb password
- this is a dumb passphrase
- this is a really bad password
- this is a really dumb passphrase
- this is a very bad password
- this is a very dumb passphrase
```

Apply these mutations:
1. Separator variations: spaces, periods, no separator
2. Case variations: all lower, Title Case, first letter caps
3. Trailing characters: !, 1, 123, etc.

### Priority 2: 2011 Era Slang Variations

Incorporate slang that was popular in 2011:

```
Adjectives to substitute:
- derpy (very popular in 2011)
- lulzy
- lame
- crappy
- shitty
- silly
- stupid
- terrible
- awful
- weak
- lazy
- embarrassing
- pathetic
```

Example phrases:
```
this is a derpy password
this is a derpy passphrase
derpy password
this is really derpy
such a derpy passphrase
```

### Priority 3: Extended Phrase Patterns

Try longer phrases that fit the "more words than usual" hint:

```
Patterns (4-7 words):
- this is a really [adj] [noun]
- this is a very [adj] [noun]
- this is such a [adj] [noun]
- what a [adj] [noun] this is
- i have a [adj] [noun]
- my [adj] [noun] is [adj]
```

### Priority 4: 1337speak Mutations

Apply leetspeak transformations to promising candidates. Dean specifically mentioned using these patterns:

```
Dean's known patterns:
- p455 (pass)
- p@$$ (pass)
- Combinations of the above

Common substitutions:
a -> 4, @
e -> 3
i -> 1, !
o -> 0
s -> 5, $
t -> 7
```

Example:
```
th1s 1s 4 b4d p4ssw0rd
7h1s 1s 4 b4d p4ssw0rd
this is a bad p455word
this is a bad p@$$word
```

### Priority 4b: Trailing Characters

Dean mentioned he typically adds 1, 3, or maybe 6 characters at the end:

```
Trailing patterns to try:
- ! (single exclamation)
- !!! (triple exclamation)
- ? (question mark)
- ??? (triple question mark)
- ~ (tilde)
- ` (backtick)
- 1
- 123
- 111
- !!!!!!
```

Example:
```
this is a bad password!
this is a bad password!!!
this is a bad password?
this is a bad password~
this is a bad password`
this is a bad password123
```

### Priority 5: Repeated Character Patterns

Dean mentioned "pooooooooooooooop" as an example of something stupid:

```
Patterns to try:
- baaaaaad password
- duuuuumb password
- this is baaaaaad
- sooooo bad
```

### Priority 6: DEFCON Context

Phrases that might relate to DEFCON 19 or hacker culture:

```
- defcon password
- hacker password
- this is my defcon password
- vegas password
- conference password
```

## Hashcat Commands

### Basic Attack

```bash
hashcat -m 11300 -a 0 hash.txt wordlist.txt
```

### With Rules

```bash
hashcat -m 11300 -a 0 hash.txt wordlist.txt -r rules/best64.rule
```

### Combinator Attack (for multi-word phrases)

```bash
hashcat -m 11300 -a 1 hash.txt words1.txt words2.txt
```

### Prince Attack (for passphrase generation)

```bash
hashcat -m 11300 -a 0 hash.txt wordlist.txt --prince
```

## Tools and Resources

- **hashcat**: Primary cracking tool, use mode 11300
- **bitcoin2john**: Extract hash from wallet.dat (already done)
- **PRINCE**: Passphrase generator for hashcat
- **Hashtopolis**: Distributed cracking coordination
- **Custom generators**: Build phrase generators based on patterns above

## Recommended Wordlist Generation Script

```python
#!/usr/bin/env python3
"""Generate passphrase candidates for crackmywallet.org"""

adjectives = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak", "simple",
    "easy", "lazy", "derpy", "lulzy", "lame", "crappy", "shitty",
    "silly", "ridiculous", "embarrassing", "pathetic", "horrible"
]

nouns = ["password", "passphrase", "pass", "passwd", "secret", "key"]

prefixes = [
    "this is a",
    "this is a really",
    "this is a very",
    "this is such a",
    "what a",
    "such a",
    "my",
    "a really",
    "a very",
    ""
]

separators = [" ", ".", "-", ""]

def generate():
    candidates = set()
    
    for prefix in prefixes:
        for adj in adjectives:
            for noun in nouns:
                for sep in separators:
                    if prefix:
                        phrase = f"{prefix}{sep}{adj}{sep}{noun}"
                    else:
                        phrase = f"{adj}{sep}{noun}"
                    
                    # Add variations
                    candidates.add(phrase.lower())
                    candidates.add(phrase.title())
                    candidates.add(phrase.lower() + "!")
                    candidates.add(phrase.lower() + "1")
                    candidates.add(phrase.lower() + "123")
    
    return candidates

if __name__ == "__main__":
    for candidate in sorted(generate()):
        print(candidate)
```

## Contributing Your Attempts

If you run a significant cracking attempt, please document:

1. What wordlists/patterns you tried
2. What rules you applied
3. How much search space you covered
4. How long you ran the attack
5. What hardware you used

Dean has offered partial bounty (1 BTC) for well-documented search space coverage that helps narrow down the solution.

## Contact

- **Dean Pierce**: [@deanpierce](https://twitter.com/deanpierce)
- **Telegram**: https://t.me/CryptoRescue
- **Website**: https://crackmywallet.org/
