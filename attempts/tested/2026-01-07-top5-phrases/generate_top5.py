#!/usr/bin/env python3
"""
Top 11 Most Likely Phrases Generator (with password + passphrase variants)

Based on Dean's exact quotes and vocabulary from Telegram research.

Word separators: spaces OR periods (consistent throughout)
- Spaces: "this is a very bad password 123"
- Periods: "this.is.a.very.bad.password.123"

Trailing: 0-6 chars from 1234!@#$

~26.4M candidates total - runs in ~1.6 minutes at 270k H/s
"""

from itertools import product

# The 11 most likely base phrase patterns as word lists
# Will be combined with both "password" and "passphrase"
BASE_PATTERNS = [
    # "this is a..." set (5)
    ["this", "is", "a", "very", "bad"],       # Dean's EXACT quote from Telegram
    ["this", "is", "a", "really", "bad"],     # Natural variation
    ["this", "is", "a", "really", "dumb"],    # Uses "dumb" from "dumbest freaking password"
    ["this", "is", "a", "really", "stupid"],  # Uses "stupid" from "embarrassingly stupid"
    ["this", "is", "a", "super", "bad"],      # "Super" is common 2011 slang
    
    # Short set (6)
    ["bad"],                      # Simplest possible
    ["very", "dumb"],             # Combines "very" with "dumb"
    ["really", "bad"],            # Simple 3-word
    ["dumb"],                     # Minimal, from "dumbest" quote
    ["stupid"],                   # Minimal, from "stupid" quote
    ["really", "dumb"],           # Added per user request
]

# Nouns to append
NOUNS = ["password", "passphrase"]

# Word separators (consistent throughout phrase)
WORD_SEPARATORS = [" ", "."]

# Trailing character set: 1234!@#$
TRAILING_CHARS = "1234!@#$"

def generate_trailing_combinations(max_len=6):
    """Generate all trailing combinations from 0 to max_len chars"""
    combinations = [""]  # Empty (no trailing)
    
    for length in range(1, max_len + 1):
        for combo in product(TRAILING_CHARS, repeat=length):
            combinations.append("".join(combo))
    
    return combinations

# Pre-generate trailing combinations (0-6 chars)
# 1 + 8 + 64 + 512 + 4096 + 32768 + 262144 = 299,593 combinations
TRAILING_COMBOS = generate_trailing_combinations(6)

def output_phrase(words, word_sep):
    """Output phrase with all trailing combinations using consistent separator"""
    base_phrase = word_sep.join(words)
    
    # First output with no trailing
    print(base_phrase)
    
    # Then output with each trailing combination (separator before trailing matches word separator)
    for trail in TRAILING_COMBOS[1:]:  # Skip empty
        print(f"{base_phrase}{word_sep}{trail}")

def main():
    """
    Generate top 11 phrases (x2 for password/passphrase) with all trailing combinations
    
    Candidate count:
    - 11 base patterns x 2 nouns = 22 phrases
    - 2 case variants (lowercase + capitalized)
    - 2 word separators (space, period)
    - 299,593 trailing combinations (including no trailing)
    - Total: 22 * 2 * 2 * 299,593 = 26,364,184 candidates
    """
    for pattern in BASE_PATTERNS:
        for noun in NOUNS:
            words = pattern + [noun]
            
            for word_sep in WORD_SEPARATORS:
                # Output lowercase version
                output_phrase(words, word_sep)
                
                # Output capitalized version (first word capitalized)
                words_cap = [words[0].capitalize()] + words[1:]
                output_phrase(words_cap, word_sep)

if __name__ == "__main__":
    main()
