#!/usr/bin/env python3
"""
Generate password candidates based on the Bitcoin wallet encryption prompt text.

The hypothesis is that Dean may have typed something based on the prompt he saw:
"Enter a passphrase to encrypt your wallet."

Base phrases: 14 variations with different pejoratives
Separators: spaces, periods, no separator
Trailing period: with/without
Case: lowercase, First-word-capitalized
Trailing: 0-6 chars from 1234!@#$
"""

import itertools

# Pejoratives to insert (including empty for original prompt)
PEJORATIVES = [
    "",        # Original: "Enter a passphrase to encrypt your wallet"
    "bad",
    "dumb", 
    "stupid",
    "shitty",
    "shit",
    "poop",
    "poopy",
    "potato",
    "p0t4t0",  # Leetspeak variant
    "crappy",
    "awful",
    "weak",
    "derp",
    "derpy",
]

# Base phrase structure: "Enter a [PEJORATIVE] passphrase to encrypt your wallet"
def build_phrase_words(pejorative):
    """Build the phrase as a list of words."""
    if pejorative:
        return ["enter", "a", pejorative, "passphrase", "to", "encrypt", "your", "wallet"]
    else:
        return ["enter", "a", "passphrase", "to", "encrypt", "your", "wallet"]

# Separators
WORD_SEPARATORS = [" ", ".", ""]  # spaces, periods, no separator

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
    """Capitalize first letter only."""
    if not phrase:
        return phrase
    return phrase[0].upper() + phrase[1:]

def main():
    trailing_combos = generate_trailing_combinations()
    
    for pejorative in PEJORATIVES:
        phrase_words = build_phrase_words(pejorative)
        
        for sep in WORD_SEPARATORS:
            # Build base phrase with separator
            base_phrase = sep.join(phrase_words)
            
            # Case variants
            case_variants = [
                base_phrase.lower(),
                capitalize_first(base_phrase.lower()),
            ]
            
            for phrase in case_variants:
                # Trailing period options (with and without)
                period_variants = [phrase, phrase + "."] if sep != "." else [phrase]
                
                for phrase_with_period in period_variants:
                    for trailing in trailing_combos:
                        if trailing:
                            # For space-separated, try both with and without space before trailing
                            if sep == " ":
                                print(f"{phrase_with_period}{trailing}")
                                print(f"{phrase_with_period} {trailing}")
                            elif sep == ".":
                                print(f"{phrase_with_period}{trailing}")
                                print(f"{phrase_with_period}.{trailing}")
                            else:
                                # No separator - just append trailing
                                print(f"{phrase_with_period}{trailing}")
                        else:
                            print(phrase_with_period)

if __name__ == "__main__":
    main()
