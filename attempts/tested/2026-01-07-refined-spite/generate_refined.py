#!/usr/bin/env python3
"""
Refined Spite Passphrase Generator (~2.8 Billion candidates)

Based on Dean's actual vocabulary from Telegram, GitHub, and A/B test feedback.

Key refinements:
- Only words Dean actually uses
- Trailing: 0-4 chars from 1234!@#$ with optional space/period separator
- Compound fillers: 3 for 8-word, 2 for 7-word, 1 for 6-word
- Minimal leetspeak (only on password/passphrase)
- No elongated patterns (Dean's "poooooop" was a joke)

Trailing rules:
- Characters: 1234!@#$ (8 options)
- Length: 0-4 characters
- Separator before trailing: none, space, or period

Target: ~2.8 billion candidates across 6, 7, 8 word patterns
"""

import sys
from itertools import product

# === REFINED WORD LISTS (Dean's actual vocabulary) ===

STARTERS = ["This", "this", "It", "it", "What", "what", "That", "that", "Here", "My"]  # 10

CONNECTORS = ["is", "was"]  # 2

ARTICLES = ["a", "the", "one", "my"]  # 4

# Fillers Dean actually uses for emphasis
FILLERS = ["really", "very", "super", "so", "pretty", "damn", "freaking"]  # 7

# Spite words from Dean's actual vocabulary (excluding words not in his lexicon)
SPITE_WORDS = [
    "bad", "dumb", "stupid", "awful", "crappy", "shitty", 
    "weak", "poor", "silly", "foolish",
    "poop", "poopy", "potato"
]  # 13

# Leetspeak variants for password/passphrase only
NOUNS_LEET = [
    "password", "p@ssword", "pa$$word", "p@$$word",
    "passphrase", "p@ssphrase", "pa$$phrase", "p@$$phrase",
    "phrase"
]  # 9

# Trailing character set: 1234!@#$
TRAILING_CHARS = "1234!@#$"

# Separators before trailing (none, space, period)
TRAILING_SEPARATORS = ["", " ", "."]

def generate_trailing_combinations(max_len=4):
    """Generate all trailing combinations from 0 to max_len chars"""
    combinations = [""]  # Empty (no trailing)
    
    for length in range(1, max_len + 1):
        for combo in product(TRAILING_CHARS, repeat=length):
            combinations.append("".join(combo))
    
    return combinations

# Pre-generate trailing combinations (0-4 chars)
TRAILING_COMBOS = generate_trailing_combinations(4)

def output_with_trailing(base_phrase):
    """Output phrase with all trailing combinations and separators"""
    # First output with no trailing (no separator needed)
    print(base_phrase)
    
    # Then output with each trailing combination and each separator
    for trail in TRAILING_COMBOS[1:]:  # Skip empty
        for sep in TRAILING_SEPARATORS:
            print(f"{base_phrase}{sep}{trail}")

def generate_6word():
    """
    6-word pattern: starter connector article filler spite noun
    Example: "This is a really bad password"
    """
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for filler in FILLERS:
                    for spite in SPITE_WORDS:
                        for noun in NOUNS_LEET:
                            base = f"{starter} {conn} {art} {filler} {spite} {noun}"
                            output_with_trailing(base)

def generate_7word():
    """
    7-word pattern: starter connector article filler filler spite noun
    Example: "This is a really really bad password"
    """
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for filler in FILLERS:  # Same filler repeated
                    for spite in SPITE_WORDS:
                        for noun in NOUNS_LEET:
                            base = f"{starter} {conn} {art} {filler} {filler} {spite} {noun}"
                            output_with_trailing(base)

def generate_8word():
    """
    8-word pattern: starter connector article filler filler filler spite noun
    Example: "This is a really really really bad password"
    """
    for starter in STARTERS:
        for conn in CONNECTORS:
            for art in ARTICLES:
                for filler in FILLERS:  # Same filler repeated 3x
                    for spite in SPITE_WORDS:
                        for noun in NOUNS_LEET:
                            base = f"{starter} {conn} {art} {filler} {filler} {filler} {spite} {noun}"
                            output_with_trailing(base)

def main():
    """
    Generate all patterns: 6, 7, and 8 word
    
    Candidate count calculation:
    - Trailing combos (0-4 chars): 1 + 8 + 64 + 512 + 4096 = 4,681
    - With separators: 1 + (4680 * 3) = 14,041 trailing variants
    
    Base counts (without trailing):
    - 6-word: 10 * 2 * 4 * 7 * 13 * 9 = 65,520
    - 7-word: 10 * 2 * 4 * 7 * 13 * 9 = 65,520
    - 8-word: 10 * 2 * 4 * 7 * 13 * 9 = 65,520
    - Total base: 196,560
    
    Total with trailing: 196,560 * 14,041 = 2,759,898,960 (~2.8B)
    """
    generate_8word()  # Start with 8-word (most likely per Bitcoin 0.4.0)
    generate_7word()
    generate_6word()

if __name__ == "__main__":
    main()
