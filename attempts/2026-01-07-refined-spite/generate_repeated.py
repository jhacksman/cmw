#!/usr/bin/env python3
"""
Repeated Word Passphrase Generator

Patterns like:
- "bad bad bad bad password" (repeated spite word + noun)
- "very very very very very very bad password" (repeated filler + spite + noun)

Word counts: 4, 5, 6, 7, 8 words
Trailing: 0-4 chars from 1234!@#$
"""

import sys
from itertools import product

# Spite words to repeat
SPITE_WORDS = [
    "bad", "dumb", "stupid", "awful", "crappy", "shitty",
    "weak", "poor", "silly", "foolish",
    "poop", "poopy", "potato"
]  # 13

# Filler words to repeat
FILLERS = ["really", "very", "super", "so", "pretty", "damn", "freaking"]  # 7

# Nouns with leetspeak variants
NOUNS = [
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

def generate_repeated_spite():
    """
    Pattern: repeated spite word + noun
    Examples:
    - "bad bad bad bad password" (4 words: 3 spite + 1 noun)
    - "bad bad bad bad bad password" (5 words: 4 spite + 1 noun)
    - "bad bad bad bad bad bad password" (6 words: 5 spite + 1 noun)
    - "bad bad bad bad bad bad bad password" (7 words: 6 spite + 1 noun)
    - "bad bad bad bad bad bad bad bad password" (8 words: 7 spite + 1 noun)
    """
    # 4-8 word patterns (3-7 repeated spite words + 1 noun)
    for repeat_count in range(3, 8):  # 3 to 7 repetitions
        for spite in SPITE_WORDS:
            for noun in NOUNS:
                repeated = " ".join([spite] * repeat_count)
                # Capitalize first word
                repeated_cap = spite.capitalize() + " " + " ".join([spite] * (repeat_count - 1))
                
                # Lowercase version
                base = f"{repeated} {noun}"
                output_with_trailing(base)
                
                # First word capitalized version
                base_cap = f"{repeated_cap} {noun}"
                output_with_trailing(base_cap)

def generate_repeated_filler_spite():
    """
    Pattern: repeated filler + spite + noun
    Examples:
    - "very very bad password" (4 words: 2 filler + 1 spite + 1 noun)
    - "very very very bad password" (5 words: 3 filler + 1 spite + 1 noun)
    - "very very very very bad password" (6 words: 4 filler + 1 spite + 1 noun)
    - "very very very very very bad password" (7 words: 5 filler + 1 spite + 1 noun)
    - "very very very very very very bad password" (8 words: 6 filler + 1 spite + 1 noun)
    """
    # 4-8 word patterns (2-6 repeated fillers + 1 spite + 1 noun)
    for repeat_count in range(2, 7):  # 2 to 6 repetitions
        for filler in FILLERS:
            for spite in SPITE_WORDS:
                for noun in NOUNS:
                    repeated = " ".join([filler] * repeat_count)
                    # Capitalize first word
                    repeated_cap = filler.capitalize() + " " + " ".join([filler] * (repeat_count - 1))
                    
                    # Lowercase version
                    base = f"{repeated} {spite} {noun}"
                    output_with_trailing(base)
                    
                    # First word capitalized version
                    base_cap = f"{repeated_cap} {spite} {noun}"
                    output_with_trailing(base_cap)

def main():
    """
    Generate repeated word patterns
    
    Candidate count calculation:
    
    Repeated spite patterns:
    - 5 word counts (4-8) * 13 spite * 9 nouns * 2 case variants * 14,041 trailing
    = 5 * 13 * 9 * 2 * 14,041 = 16,427,970
    
    Repeated filler + spite patterns:
    - 5 word counts (4-8) * 7 fillers * 13 spite * 9 nouns * 2 case variants * 14,041 trailing
    = 5 * 7 * 13 * 9 * 2 * 14,041 = 114,995,790
    
    Total: ~131 million candidates
    """
    generate_repeated_spite()
    generate_repeated_filler_spite()

if __name__ == "__main__":
    main()
