#!/usr/bin/env python3
"""
Full-Phrase Leetspeak + Lulz Password Generator

Applies leetspeak to the ENTIRE phrase (not just the noun):
- Numbers style: all a->4, all s->5 (e.g., "thi5 i5 4 b4d p455word")
- Symbols style: all a->@, all s->$ (e.g., "thi$ i$ @ b@d p@$$word")

Plus "lulz" patterns from 2011 Anonymous/LulzSec era.

Trailing: 0-6 chars from !?~` (mixed)
NO digit suffixes.
"""

import itertools
from typing import Generator, List, Tuple

# Spite words
SPITE_WORDS = ["bad", "dumb"]

# Intensifiers
INTENSIFIERS = ["very", "really", "super"]

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


def apply_leet_numbers(text: str) -> str:
    """Apply number-style leet: a->4, s->5"""
    return text.replace("a", "4").replace("A", "4").replace("s", "5").replace("S", "5")


def apply_leet_symbols(text: str) -> str:
    """Apply symbol-style leet: a->@, s->$"""
    return text.replace("a", "@").replace("A", "@").replace("s", "$").replace("S", "$")


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
    for noun in ["password", "passphrase"]:
        # No intensifier
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", spite, noun], "none"))
        
        # Single intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", "is", "a", intensifier, spite, noun], "none"))
        
        # Double intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", "is", "a", intensifier, intensifier, spite, noun], "none"))
        
        # Triple intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", "is", "a", intensifier, intensifier, intensifier, spite, noun], "none"))
        
        # Quad intensifier
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append((["this", "is", "a", intensifier, intensifier, intensifier, intensifier, spite, noun], "none"))
    
    # ===== STRUCTURE 3: "[spite] password/passphrase" (short) =====
    for noun in ["password", "passphrase"]:
        for spite in SPITE_WORDS:
            phrases.append(([spite, noun], "none"))
    
    # ===== STRUCTURE 4: "[intensifier(s)] [spite] password/passphrase" =====
    for noun in ["password", "passphrase"]:
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append(([intensifier, spite, noun], "none"))
        
        for intensifier in INTENSIFIERS:
            for spite in SPITE_WORDS:
                phrases.append(([intensifier, intensifier, spite, noun], "none"))
    
    # ===== STRUCTURE 5: "Enter a passphrase to encrypt your wallet" variants =====
    phrases.append((["enter", "a", "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    for spite in SPITE_WORDS:
        phrases.append((["enter", "a", spite, "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["enter", "a", intensifier, spite, "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    # ===== LULZ PATTERNS (2011 Anonymous/LulzSec era) =====
    # "for the lulz" variants
    phrases.append((["for", "the", "lulz"], "none"))
    phrases.append((["lulz"], "none"))
    phrases.append((["this", "is", "for", "the", "lulz"], "none"))
    phrases.append((["doing", "it", "for", "the", "lulz"], "none"))
    phrases.append((["i", "did", "it", "for", "the", "lulz"], "none"))
    phrases.append((["all", "for", "the", "lulz"], "none"))
    
    # lulz + password/passphrase
    for noun in ["password", "passphrase"]:
        phrases.append((["lulz", noun], "none"))
        phrases.append((["for", "the", "lulz", noun], "none"))
        phrases.append((["this", noun, "is", "for", "the", "lulz"], "none"))
    
    # lulzsec reference
    phrases.append((["lulzsec"], "none"))
    phrases.append((["lulzsec", "password"], "none"))
    phrases.append((["lulzsec", "passphrase"], "none"))
    
    return phrases


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
    # Leet variants: none, numbers (4/5), symbols (@/$)
    leet_variants = [None, "numbers", "symbols"]
    
    for words, noun_type in base_phrases:
        for sep in separators:
            for first_cap in case_variants:
                cased_words = apply_case(words, first_cap)
                phrase = sep.join(cased_words)
                
                for leet in leet_variants:
                    if leet == "numbers":
                        leeted_phrase = apply_leet_numbers(phrase)
                    elif leet == "symbols":
                        leeted_phrase = apply_leet_symbols(phrase)
                    else:
                        leeted_phrase = phrase
                    
                    for trailing in trailing_combos:
                        if trailing:
                            for trail_sep in ["", sep]:
                                yield f"{leeted_phrase}{trail_sep}{trailing}"
                        else:
                            yield leeted_phrase


def count_candidates() -> int:
    """Calculate total candidate count."""
    base_phrases = generate_base_phrases()
    trailing_combos = generate_trailing_combinations()
    trailing_with_sep = 1 + (len(trailing_combos) - 1) * 2
    
    # separators * case * leet_variants * trailing
    total = len(base_phrases) * 2 * 2 * 3 * trailing_with_sep
    
    return total


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print(f"Total candidates: {count_candidates():,}")
        print(f"Base phrases: {len(generate_base_phrases())}")
        print(f"Trailing combinations: {len(generate_trailing_combinations())}")
    elif len(sys.argv) > 1 and sys.argv[1] == "--phrases":
        for words, noun_type in generate_base_phrases():
            print(" ".join(words))
    elif len(sys.argv) > 1 and sys.argv[1] == "--sample":
        count = 0
        for candidate in generate_all():
            print(candidate)
            count += 1
            if count >= 100:
                break
    else:
        for candidate in generate_all():
            print(candidate)
