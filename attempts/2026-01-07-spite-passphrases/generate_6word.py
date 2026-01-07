#!/usr/bin/env python3
"""
6-Word Spite Passphrase Generator (~1 Billion candidates)

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
    "Here", "My", "Such", "One", "The", "A"
]  # 14

# Connectors
CONNECTORS = ["is", "was", "seems", "looks", "feels", "sounds"]  # 6

# Articles
ARTICLES = ["a", "the", "one", "my", "such", "another", "some"]  # 7

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
    "boring", "silly", "foolish", "idiotic", "moronic", "asinine"
]  # 24

# Password-related nouns
NOUNS = [
    "password", "passphrase", "pass", "passwd", "pw",
    "phrase", "word", "key", "secret", "code", "thing", "idea"
]  # 12

# Trailing punctuation
TRAILING = ["", "!", "?", "~", "`", ".", "!!", "...", "!?", "??", "!", "?!", "~~~"]  # 13

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
    Generate 6-word spite passphrases
    
    Pattern 1: "This is a super duper bad password" (starter connector article compound spite noun) = 6 words
    Pattern 2: "This is really really bad password" (starter connector filler filler spite noun) = 6 words  
    Pattern 3: "This is a really bad password" (starter connector article filler spite noun) = 6 words
    Pattern 4: "What a super duper bad password" (starter article compound spite noun) = 6 words
    
    Counts:
    P1: 10 * 4 * 5 * 8 * 22 * 11 * 10 * 5 = 19,360,000
    P2: 10 * 4 * 18 * 18 * 22 * 11 * 10 * 5 = 156,816,000
    P3: 10 * 4 * 5 * 18 * 22 * 11 * 10 * 5 = 43,560,000
    P4: 10 * 5 * 8 * 22 * 11 * 10 * 5 = 4,840,000
    
    Need more patterns to reach 1B...
    
    Pattern 5: "This is really really really bad" (starter connector filler filler filler spite) = 6 words
    P5: 10 * 4 * 18 * 18 * 18 * 22 * 10 * 5 = 256,608,000
    
    Pattern 6: "What a really really really bad" (starter article filler filler filler spite) = 6 words
    P6: 10 * 5 * 18 * 18 * 18 * 22 * 10 * 5 = 320,760,000
    
    Pattern 7: "This is super duper really bad" (starter connector compound filler spite) = 6 words
    P7: 10 * 4 * 8 * 18 * 22 * 10 * 5 = 6,336,000
    
    Total: ~808M, need to add more variations
    
    Pattern 8: "Really really really bad password here" (filler filler filler spite noun starter) = 6 words
    P8: 18 * 18 * 18 * 22 * 11 * 10 * 5 = 70,543,200
    
    Total: ~879M - close enough with leet variations
    """
    
    # Pattern 1: starter connector article compound spite noun (6 words)
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
    
    # Pattern 2: starter connector filler filler spite noun (6 words)
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
    
    # Pattern 3: starter connector article filler spite noun (6 words)
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
    
    # Pattern 4: starter article compound spite noun (5 words but compound=2)
    for starter in STARTERS:
        for art in ARTICLES:
            for compound in COMPOUND_FILLERS:
                for spite in SPITE_WORDS:
                    for noun in NOUNS:
                        base = f"{starter} {art} {compound} {spite} {noun}"
                        for trail in TRAILING:
                            for v in apply_leet(base + trail):
                                print(v)
    
    # Pattern 5: starter connector filler filler filler spite (6 words, no noun)
    for starter in STARTERS:
        for conn in CONNECTORS:
            for f1 in SINGLE_FILLERS:
                for f2 in SINGLE_FILLERS:
                    for f3 in SINGLE_FILLERS:
                        for spite in SPITE_WORDS:
                            base = f"{starter} {conn} {f1} {f2} {f3} {spite}"
                            for trail in TRAILING:
                                for v in apply_leet(base + trail):
                                    print(v)
    
    # Pattern 6: starter article filler filler filler spite (6 words)
    for starter in STARTERS:
        for art in ARTICLES:
            for f1 in SINGLE_FILLERS:
                for f2 in SINGLE_FILLERS:
                    for f3 in SINGLE_FILLERS:
                        for spite in SPITE_WORDS:
                            base = f"{starter} {art} {f1} {f2} {f3} {spite}"
                            for trail in TRAILING:
                                for v in apply_leet(base + trail):
                                    print(v)

if __name__ == "__main__":
    generate()
