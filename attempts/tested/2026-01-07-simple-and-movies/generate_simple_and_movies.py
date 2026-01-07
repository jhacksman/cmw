#!/usr/bin/env python3
"""
Generate password candidates for:
1. Simple "this is a passphrase/password" (no pejorative) + 0-6 trailing
2. Sneakers (1992) and Hackers (1995) movie references + 0-6 trailing

Trailing: 0-6 chars from 1234!@#$
Separators: spaces OR periods (consistent throughout)
Case: lowercase and first-word capitalized
"""

import itertools

# Simple phrases (no pejorative)
SIMPLE_PHRASES = [
    ["this", "is", "a", "passphrase"],
    ["this", "is", "a", "password"],
    ["this", "is", "my", "passphrase"],
    ["this", "is", "my", "password"],
]

# Sneakers (1992) movie references
SNEAKERS_PHRASES = [
    ["my", "voice", "is", "my", "passport"],                          # Classic line
    ["my", "voice", "is", "my", "passport", "verify", "me"],          # Full quote
    ["no", "more", "secrets"],                                         # Key phrase
    ["its", "all", "just", "electrons"],                              # Cosmo quote
    ["too", "many", "secrets"],                                        # Anagram of "setec astronomy"
]

# Hackers (1995) movie references
HACKERS_PHRASES = [
    ["hack", "the", "planet"],                                         # Tagline
    ["mess", "with", "the", "best", "die", "like", "the", "rest"],    # Zero Cool
    ["the", "pool", "on", "the", "roof", "must", "have", "a", "leak"], # Social engineering
    ["zero", "cool"],                                                  # Dade's handle
    ["crash", "override"],                                             # Dade's new handle
    ["acid", "burn"],                                                  # Kate's handle
    ["cereal", "killer"],                                              # Character handle
    ["lord", "nikon"],                                                 # Character handle
    ["phantom", "phreak"],                                             # Character handle
    ["type", "cookie", "you", "idiot"],                               # Famous line
]

# Common passwords mentioned in Hackers movie
HACKERS_PASSWORDS = [
    ["love"],
    ["sex"],
    ["secret"],
    ["god"],
]

# All phrases combined
ALL_PHRASES = SIMPLE_PHRASES + SNEAKERS_PHRASES + HACKERS_PHRASES + HACKERS_PASSWORDS

# Separators (consistent throughout phrase)
WORD_SEPARATORS = [" ", "."]

# Trailing characters
TRAILING_CHARS = "1234!@#$"
MAX_TRAILING = 6

def generate_trailing_combinations():
    """Generate all trailing combinations from 0-6 chars."""
    combinations = [""]  # Empty (no trailing)
    for length in range(1, MAX_TRAILING + 1):
        for combo in itertools.product(TRAILING_CHARS, repeat=length):
            combinations.append("".join(combo))
    return combinations

def capitalize_first(phrase):
    """Capitalize first word only."""
    if not phrase:
        return phrase
    return phrase[0].upper() + phrase[1:]

def main():
    trailing_combos = generate_trailing_combinations()
    
    for phrase_words in ALL_PHRASES:
        for sep in WORD_SEPARATORS:
            # Build base phrase with separator
            base_phrase = sep.join(phrase_words)
            
            # Case variants
            case_variants = [
                base_phrase.lower(),
                capitalize_first(base_phrase.lower()),
            ]
            
            for phrase in case_variants:
                for trailing in trailing_combos:
                    if trailing:
                        # Add trailing with same separator style
                        if sep == " ":
                            print(f"{phrase} {trailing}")
                            print(f"{phrase}{trailing}")  # Also try no space before trailing
                        else:
                            print(f"{phrase}{sep}{trailing}")
                            print(f"{phrase}{trailing}")  # Also try no separator before trailing
                    else:
                        print(phrase)

if __name__ == "__main__":
    main()
