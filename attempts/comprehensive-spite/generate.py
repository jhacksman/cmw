#!/usr/bin/env python3
"""
Comprehensive Spite Password Generator

Combines all untried structures:
1. "this password/passphrase is [intensifier(s)] [spite]" (new structure)
2. "this is a [intensifier(s)] [spite] password/passphrase" (with triple/quad)
3. "[spite] password/passphrase" (short)
4. "Enter a passphrase..." variants

Intensifiers: very, really, super (single, double, triple, quad)
Spite: bad, dumb
Trailing: 0-6 chars from !?~` (mixed, for more coverage)
"""

import itertools
from typing import Generator, List, Tuple

# Spite words
SPITE_WORDS = ["bad", "dumb"]

# Intensifiers
INTENSIFIERS = ["very", "really", "super"]

# Nouns with leetspeak variants (no mixing)
PASSWORD_VARIANTS = [
    "password",
    "p@$$word",
    "p455word",
]

PASSPHRASE_VARIANTS = [
    "passphrase",
    "p@$$phr@$e",
    "p455phr45e",
]

# Trailing chars
TRAILING_CHARS = "!?~`"
MAX_TRAILING = 6


def generate_trailing_combinations() -> List[str]:
    """Generate all trailing combinations from 0-6 chars using !?~`"""
    combinations = [""]
    for length in range(1, MAX_TRAILING + 1):
        for combo in itertools.product(TRAILING_CHARS, repeat=length):
            combinations.append("".join(combo))
    return combinations


def generate_base_phrases() -> List[Tuple[List[str], str]]:
    """
    Generate all base phrases.
    Returns list of (word_list, noun_type) where noun_type is 'password', 'passphrase', or 'none'
    """
    phrases = []
    
    # ===== STRUCTURE 1: "this password/passphrase is [intensifier(s)] [spite]" =====
    for noun_base in ["password", "passphrase"]:
        # No intensifier
        for spite in SPITE_WORDS:
            phrases.append((["this", noun_base, "is", spite], "none"))
        
        # Single intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", noun_base, "is", intensifier, spite], "none"))
        
        # Double intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", noun_base, "is", intensifier, intensifier, spite], "none"))
        
        # Triple intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", noun_base, "is", intensifier, intensifier, intensifier, spite], "none"))
        
        # Quad intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", noun_base, "is", intensifier, intensifier, intensifier, intensifier, spite], "none"))
    
    # ===== STRUCTURE 2: "this is a [intensifier(s)] [spite] password/passphrase" =====
    # No intensifier
    for spite in SPITE_WORDS:
        phrases.append((["this", "is", "a", spite], "password"))
        phrases.append((["this", "is", "a", spite], "passphrase"))
    
    # Single intensifier
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", intensifier, spite], "password"))
            phrases.append((["this", "is", "a", intensifier, spite], "passphrase"))
    
    # Double intensifier
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", intensifier, intensifier, spite], "password"))
            phrases.append((["this", "is", "a", intensifier, intensifier, spite], "passphrase"))
    
    # Triple intensifier
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", intensifier, intensifier, intensifier, spite], "password"))
            phrases.append((["this", "is", "a", intensifier, intensifier, intensifier, spite], "passphrase"))
    
    # Quad intensifier
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", intensifier, intensifier, intensifier, intensifier, spite], "password"))
            phrases.append((["this", "is", "a", intensifier, intensifier, intensifier, intensifier, spite], "passphrase"))
    
    # ===== STRUCTURE 3: "[spite] password/passphrase" (short) =====
    for spite in SPITE_WORDS:
        phrases.append(([spite], "password"))
        phrases.append(([spite], "passphrase"))
    
    # ===== STRUCTURE 4: "[intensifier(s)] [spite] password/passphrase" =====
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append(([intensifier, spite], "password"))
            phrases.append(([intensifier, spite], "passphrase"))
    
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append(([intensifier, intensifier, spite], "password"))
            phrases.append(([intensifier, intensifier, spite], "passphrase"))
    
    # ===== STRUCTURE 5: "Enter a passphrase to encrypt your wallet" variants =====
    phrases.append((["enter", "a", "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    for spite in SPITE_WORDS:
        phrases.append((["enter", "a", spite, "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["enter", "a", intensifier, spite, "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    return phrases


def get_noun_variants(noun_type: str) -> List[str]:
    """Get the appropriate noun variants based on type."""
    if noun_type == "password":
        return PASSWORD_VARIANTS
    elif noun_type == "passphrase":
        return PASSPHRASE_VARIANTS
    else:
        return [""]


def apply_case(words: List[str], first_cap: bool) -> List[str]:
    """Apply case variant to word list."""
    if first_cap and words:
        return [words[0].capitalize()] + words[1:]
    return words


def generate_all() -> Generator[str, None, None]:
    """Generate all password candidates."""
    base_phrases = generate_base_phrases()
    trailing_combos = generate_trailing_combinations()
    separators = [" ", "."]
    case_variants = [False, True]
    
    for words, noun_type in base_phrases:
        noun_variants = get_noun_variants(noun_type)
        
        for noun in noun_variants:
            for sep in separators:
                for first_cap in case_variants:
                    if noun:
                        full_words = words + [noun]
                    else:
                        full_words = words
                    
                    cased_words = apply_case(full_words, first_cap)
                    phrase = sep.join(cased_words)
                    
                    for trailing in trailing_combos:
                        if trailing:
                            for trail_sep in ["", sep]:
                                yield f"{phrase}{trail_sep}{trailing}"
                        else:
                            yield phrase


def count_candidates() -> int:
    """Calculate total candidate count."""
    base_phrases = generate_base_phrases()
    trailing_combos = generate_trailing_combinations()
    trailing_with_sep = 1 + (len(trailing_combos) - 1) * 2
    
    total = 0
    for words, noun_type in base_phrases:
        noun_count = len(get_noun_variants(noun_type))
        if noun_count == 0:
            noun_count = 1
        total += 2 * 2 * noun_count * trailing_with_sep
    
    return total


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print(f"Total candidates: {count_candidates():,}")
        print(f"Base phrases: {len(generate_base_phrases())}")
        print(f"Trailing combinations: {len(generate_trailing_combinations())}")
    else:
        for candidate in generate_all():
            print(candidate)
