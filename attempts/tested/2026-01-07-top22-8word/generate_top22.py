#!/usr/bin/env python3
"""
Top 22 Eight-Word Phrases Generator (with password + passphrase variants)

Based on Dean's exact quotes and vocabulary from Telegram research.
All phrases are exactly 8 words, prioritized by likelihood.

Word separators: spaces OR periods (consistent throughout)
Trailing: 0-6 chars from 1234!@#$

~52.7M candidates total
"""

from itertools import product

# Top 22 eight-word phrase patterns (prioritized by likelihood)
# All patterns are exactly 8 words when combined with noun
# Format: list of 7 words (noun added separately)
BASE_PATTERNS = [
    # Tier 1: Most likely - based on Dean's exact "this is a very bad password" quote
    # Extended with repeated fillers to reach 8 words
    ["this", "is", "a", "really", "really", "really", "bad"],       # 1. Most natural extension
    ["this", "is", "a", "very", "very", "very", "bad"],             # 2. His exact word "very" repeated
    ["this", "is", "a", "really", "really", "really", "dumb"],      # 3. "dumb" from "dumbest freaking"
    ["this", "is", "a", "really", "really", "really", "stupid"],    # 4. "stupid" from "embarrassingly stupid"
    ["this", "is", "a", "super", "super", "super", "bad"],          # 5. "super" common 2011 slang
    
    # Tier 2: Variations with different spite words
    ["this", "is", "a", "very", "very", "very", "dumb"],            # 6.
    ["this", "is", "a", "very", "very", "very", "stupid"],          # 7.
    ["this", "is", "a", "super", "super", "super", "dumb"],         # 8.
    ["this", "is", "a", "super", "super", "super", "stupid"],       # 9.
    ["this", "is", "a", "really", "really", "bad", "bad"],          # 10. Double spite word
    ["this", "is", "a", "very", "very", "bad", "bad"],              # 11.
    
    # Tier 3: Different starters
    ["this", "was", "a", "really", "really", "really", "bad"],      # 12. "was" instead of "is"
    ["that", "is", "a", "really", "really", "really", "bad"],       # 13. "that" starter
    ["it", "is", "a", "really", "really", "really", "bad"],         # 14. "it" starter
    ["this", "is", "my", "really", "really", "really", "bad"],      # 15. "my" instead of "a"
    ["this", "is", "one", "really", "really", "really", "bad"],     # 16. "one" instead of "a"
    
    # Tier 4: Mixed fillers
    ["this", "is", "a", "really", "really", "very", "bad"],         # 17.
    ["this", "is", "a", "really", "very", "very", "bad"],           # 18.
    ["this", "is", "a", "super", "really", "really", "bad"],        # 19.
    ["this", "is", "a", "damn", "damn", "damn", "bad"],             # 20. "damn" filler
    ["this", "is", "a", "freaking", "freaking", "freaking", "bad"], # 21. "freaking" from his quote
    ["this", "is", "a", "pretty", "pretty", "pretty", "bad"],       # 22. "pretty" common filler
]

# Nouns to append (makes it 8 words total)
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
    Generate top 22 eight-word phrases (x2 for password/passphrase) with all trailing combinations
    
    Candidate count:
    - 22 base patterns x 2 nouns = 44 phrases
    - 2 case variants (lowercase + capitalized)
    - 2 word separators (space, period)
    - 299,593 trailing combinations (including no trailing)
    - Total: 44 * 2 * 2 * 299,593 = 52,728,368 candidates
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
