#!/usr/bin/env python3
"""
Most Common 6/7/8-Word Spite Passphrase Generator (~100 Million candidates)

Based on Dean's A/B test feedback:
- Space separators
- First word capitalized
- Punctuation trailing (!, ?, ~, `)
- Light leetspeak (@ for a, $ for s, 0 for o)
- Spite theme ("bad", "dumb", "stupid")
- Filler words ("really", "very", "super", "super duper")

This script focuses on the MOST LIKELY patterns based on Dean's actual guess:
"this is a really really really bad password"

Target: ~100 million candidates
"""

import sys

# Most common starters (based on Dean's guess)
STARTERS = ["This", "this", "It", "it", "What", "what"]  # 6

# Most common connectors
CONNECTORS = ["is", "was"]  # 2

# Most common articles
ARTICLES = ["a", "the", "my"]  # 3

# Most common filler words (Dean used "really" repeatedly)
SINGLE_FILLERS = [
    "really", "very", "super", "so", "truly", "quite",
    "extremely", "totally", "completely", "damn"
]  # 10

# Compound fillers (count as 2 words)
COMPOUND_FILLERS = [
    "super duper", "really really", "very very", "so so",
    "really truly", "super super"
]  # 6

# Most common spite words (Dean used "bad")
SPITE_WORDS = [
    "bad", "dumb", "stupid", "terrible", "awful", "horrible",
    "crappy", "shitty", "lame", "weak", "poor", "pathetic"
]  # 12

# Most common nouns (Dean used "password")
NOUNS = ["password", "passphrase", "pass", "passwd", "pw", "phrase"]  # 6

# Trailing punctuation
TRAILING = ["", "!", "?", "~", "`", ".", "!!"]  # 7

def apply_leet(phrase):
    """Generate leetspeak variants - yields variants one at a time"""
    yield phrase
    
    # @ for a
    if 'a' in phrase.lower():
        yield phrase.replace('a', '@').replace('A', '@')
    
    # $ for s
    if 's' in phrase.lower():
        yield phrase.replace('s', '$').replace('S', '$')
    
    # 0 for o
    if 'o' in phrase.lower():
        yield phrase.replace('o', '0').replace('O', '0')
    
    # 3 for e
    if 'e' in phrase.lower():
        yield phrase.replace('e', '3').replace('E', '3')

def generate():
    """
    Generate most common 6/7/8-word spite passphrases
    
    6-WORD PATTERNS:
    Pattern 6a: "This is a really bad password" (starter connector article filler spite noun)
    6 * 2 * 3 * 10 * 12 * 6 * 7 * 4 = 725,760
    
    Pattern 6b: "This is really really bad password" (starter connector filler filler spite noun)
    6 * 2 * 10 * 10 * 12 * 6 * 7 * 4 = 2,419,200
    
    7-WORD PATTERNS:
    Pattern 7a: "This is a super duper bad password" (starter connector article compound spite noun)
    6 * 2 * 3 * 6 * 12 * 6 * 7 * 4 = 435,456
    
    Pattern 7b: "This is a really really bad password" (starter connector article filler filler spite noun)
    6 * 2 * 3 * 10 * 10 * 12 * 6 * 7 * 4 = 7,257,600
    
    Pattern 7c: "This is really really really bad password" (starter connector filler filler filler spite noun)
    6 * 2 * 10 * 10 * 10 * 12 * 6 * 7 * 4 = 24,192,000
    
    8-WORD PATTERNS:
    Pattern 8a: "This is a really really really bad password" (starter connector article filler filler filler spite noun)
    6 * 2 * 3 * 10 * 10 * 10 * 12 * 6 * 7 * 4 = 72,576,000
    
    Pattern 8b: "This is a super duper really bad password" (starter connector article compound filler spite noun)
    6 * 2 * 3 * 6 * 10 * 12 * 6 * 7 * 4 = 4,354,560
    
    Total: ~112M candidates
    """
    
    # === 6-WORD PATTERNS ===
    
    # Pattern 6a: starter connector article filler spite noun (6 words)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for filler in SINGLE_FILLERS:
                    for spite in SPITE_WORDS:
                        for noun in NOUNS:
                            base = f"{starter} {conn} {art} {filler} {spite} {noun}"
                            for trail in TRAILING:
                                for v in apply_leet(base + trail):
                                    print(v)
    
    # Pattern 6b: starter connector filler filler spite noun (6 words)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for f1 in SINGLE_FILLERS:
                for f2 in SINGLE_FILLERS:
                    for spite in SPITE_WORDS:
                        for noun in NOUNS:
                            base = f"{starter} {conn} {f1} {f2} {spite} {noun}"
                            for trail in TRAILING:
                                for v in apply_leet(base + trail):
                                    print(v)
    
    # === 7-WORD PATTERNS ===
    
    # Pattern 7a: starter connector article compound spite noun (7 words with compound=2)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for compound in COMPOUND_FILLERS:
                    for spite in SPITE_WORDS:
                        for noun in NOUNS:
                            base = f"{starter} {conn} {art} {compound} {spite} {noun}"
                            for trail in TRAILING:
                                for v in apply_leet(base + trail):
                                    print(v)
    
    # Pattern 7b: starter connector article filler filler spite noun (7 words)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for f1 in SINGLE_FILLERS:
                    for f2 in SINGLE_FILLERS:
                        for spite in SPITE_WORDS:
                            for noun in NOUNS:
                                base = f"{starter} {conn} {art} {f1} {f2} {spite} {noun}"
                                for trail in TRAILING:
                                    for v in apply_leet(base + trail):
                                        print(v)
    
    # Pattern 7c: starter connector filler filler filler spite noun (7 words)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for f1 in SINGLE_FILLERS:
                for f2 in SINGLE_FILLERS:
                    for f3 in SINGLE_FILLERS:
                        for spite in SPITE_WORDS:
                            for noun in NOUNS:
                                base = f"{starter} {conn} {f1} {f2} {f3} {spite} {noun}"
                                for trail in TRAILING:
                                    for v in apply_leet(base + trail):
                                        print(v)
    
    # === 8-WORD PATTERNS ===
    
    # Pattern 8a: starter connector article filler filler filler spite noun (8 words)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for f1 in SINGLE_FILLERS:
                    for f2 in SINGLE_FILLERS:
                        for f3 in SINGLE_FILLERS:
                            for spite in SPITE_WORDS:
                                for noun in NOUNS:
                                    base = f"{starter} {conn} {art} {f1} {f2} {f3} {spite} {noun}"
                                    for trail in TRAILING:
                                        for v in apply_leet(base + trail):
                                            print(v)
    
    # Pattern 8b: starter connector article compound filler spite noun (8 words with compound=2)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for compound in COMPOUND_FILLERS:
                    for filler in SINGLE_FILLERS:
                        for spite in SPITE_WORDS:
                            for noun in NOUNS:
                                base = f"{starter} {conn} {art} {compound} {filler} {spite} {noun}"
                                for trail in TRAILING:
                                    for v in apply_leet(base + trail):
                                        print(v)

if __name__ == "__main__":
    generate()
