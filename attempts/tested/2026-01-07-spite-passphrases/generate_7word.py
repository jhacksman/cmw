#!/usr/bin/env python3
"""
7-Word Spite Passphrase Generator (~1 Billion candidates)

Based on Dean's A/B test feedback:
- Space separators
- First word capitalized
- Punctuation trailing (!, ?, ~, `)
- Light leetspeak (@ for a, $ for s, 0 for o)
- Spite theme ("bad", "dumb", "stupid")
- Filler words ("really", "very", "super", "super duper")

Target: ~1 billion candidates
"""

import sys

# Starters
STARTERS = [
    "This", "this", "It", "it", "What", "what", "That", "that", 
    "Here", "My", "Such", "One"
]  # 12

# Connectors
CONNECTORS = ["is", "was", "seems", "looks", "feels"]  # 5

# Articles
ARTICLES = ["a", "the", "one", "my", "such", "another"]  # 6

# Single filler words
SINGLE_FILLERS = [
    "really", "very", "super", "so", "such", "truly", "quite",
    "extremely", "incredibly", "absolutely", "totally", "completely",
    "pretty", "rather", "damn", "freaking", "seriously", "honestly"
]  # 18

# Compound fillers (count as 2 words)
COMPOUND_FILLERS = [
    "super duper", "really really", "very very", "so so",
    "really truly", "truly truly", "super super", "damn damn",
    "really very", "very truly", "so very", "pretty damn"
]  # 12

# Spite/negative adjectives
SPITE_WORDS = [
    "bad", "dumb", "stupid", "terrible", "awful", "horrible",
    "crappy", "shitty", "lame", "weak", "poor", "pathetic",
    "lazy", "simple", "basic", "easy", "obvious", "generic",
    "boring", "silly", "foolish", "idiotic"
]  # 22

# Password-related nouns
NOUNS = [
    "password", "passphrase", "pass", "passwd", "pw",
    "phrase", "word", "key", "secret", "code", "thing", "idea"
]  # 12

# Trailing punctuation
TRAILING = ["", "!", "?", "~", "`", ".", "!!", "...", "!?", "??"]  # 10

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
    Generate 7-word spite passphrases
    
    Pattern 1: "This is a super duper bad password" (starter connector article compound spite noun) = 7 words
    12 * 5 * 6 * 12 * 22 * 12 * 10 * 4 = 45,619,200
    
    Pattern 2: "This is a really really bad password" (starter connector article filler filler spite noun) = 7 words
    12 * 5 * 6 * 18 * 18 * 22 * 12 * 10 * 4 = 410,572,800
    
    Pattern 3: "This is really really really bad password" (starter connector filler filler filler spite noun) = 7 words
    12 * 5 * 18 * 18 * 18 * 22 * 12 * 10 * 4 = 615,859,200
    
    Total: ~1.07B
    """
    
    # Pattern 1: starter connector article compound spite noun (7 words with compound=2)
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
    
    # Pattern 2: starter connector article filler filler spite noun (7 words)
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
    
    # Pattern 3: starter connector filler filler filler spite noun (7 words)
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

if __name__ == "__main__":
    generate()
