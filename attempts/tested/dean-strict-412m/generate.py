#!/usr/bin/env python3
"""
Dean-Strict Password Generator (~412M candidates)

Based STRICTLY on Dean's confirmed quotes:
- Separators: "Spaces. Maybe periods." 
- Trailing: "Likely 1, 3, maybe 6, exclamations or question marks sometimes tildes or back ticks"
- Leetspeak: "I've leetified pass as p455, p@$$" and "@ for a and $ for s"
- Example: "this is a very bad password"
- Alternatives: "also 'dumb'", "really really stupid"

Rules:
- No mixing leetspeak within words (all @ or all 4, not mixed)
- Trailing chars: !?~` only (0-6 chars)
- Separators: spaces or periods (consistent throughout)
- Case: lowercase and First cap
- Trailing separator matches word separator (space phrases get space, period phrases get period)
"""

import itertools
from typing import Generator, List, Tuple

# Dean-confirmed spite words
SPITE_WORDS = ["bad", "dumb", "stupid"]

# Dean-confirmed intensifiers
INTENSIFIERS = ["very", "really"]

# Dean-confirmed nouns with leetspeak variants (no mixing - all @ or all 4)
PASSWORD_VARIANTS = [
    "password",
    "p@$$word",   # all a->@, all s->$
    "p455word",   # all a->4, all s->5
]

PASSPHRASE_VARIANTS = [
    "passphrase",
    "p@$$phr@$e",  # all a->@, all s->$
    "p455phr45e",  # all a->4, all s->5
]

# All noun variants
NOUN_VARIANTS = PASSWORD_VARIANTS + PASSPHRASE_VARIANTS

# Dean-confirmed trailing chars
TRAILING_CHARS = "!?~`"

# Trailing lengths 0-6
MAX_TRAILING = 6


def generate_base_phrases() -> List[Tuple[List[str], str]]:
    """
    Generate all 70 base phrases as word lists with their noun type.
    Returns list of (word_list, noun_type) where noun_type is 'password' or 'passphrase'
    """
    phrases = []
    
    # Set 1: "this is a [spite] password/passphrase" (no intensifier)
    for spite in SPITE_WORDS:
        phrases.append((["this", "is", "a", spite], "password"))
        phrases.append((["this", "is", "a", spite], "passphrase"))
    
    # Set 1b: "this is a [intensifier] [spite] password/passphrase" (single intensifier)
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", intensifier, spite], "password"))
            phrases.append((["this", "is", "a", intensifier, spite], "passphrase"))
    
    # Set 1c: "this is a [double intensifier] [spite] password/passphrase"
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["this", "is", "a", intensifier, intensifier, spite], "password"))
            phrases.append((["this", "is", "a", intensifier, intensifier, spite], "passphrase"))
    
    # Set 2: "[spite] password/passphrase" (short, no intensifier)
    for spite in SPITE_WORDS:
        phrases.append(([spite], "password"))
        phrases.append(([spite], "passphrase"))
    
    # Set 2b: "[double intensifier] [spite] password/passphrase"
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append(([intensifier, intensifier, spite], "password"))
            phrases.append(([intensifier, intensifier, spite], "passphrase"))
    
    # Set 3: "Enter a passphrase to encrypt your wallet" (original prompt, 7 words)
    phrases.append((["enter", "a", "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    # Set 3b: "Enter a [spite] passphrase to encrypt your wallet" (8 words)
    for spite in SPITE_WORDS:
        phrases.append((["enter", "a", spite, "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    # Set 3c: "Enter a [intensifier] [spite] passphrase to encrypt your wallet" (9 words)
    for intensifier in INTENSIFIERS:
        for spite in SPITE_WORDS:
            phrases.append((["enter", "a", intensifier, spite, "passphrase", "to", "encrypt", "your", "wallet"], "none"))
    
    return phrases


def generate_trailing_combinations() -> List[str]:
    """Generate all trailing combinations from 0-6 chars using !?~`"""
    combinations = [""]  # Empty (no trailing)
    for length in range(1, MAX_TRAILING + 1):
        for combo in itertools.product(TRAILING_CHARS, repeat=length):
            combinations.append("".join(combo))
    return combinations


def apply_case(words: List[str], first_cap: bool) -> List[str]:
    """Apply case variant to word list."""
    if first_cap and words:
        return [words[0].capitalize()] + words[1:]
    return words


def get_noun_variants(noun_type: str) -> List[str]:
    """Get the appropriate noun variants based on type."""
    if noun_type == "password":
        return PASSWORD_VARIANTS
    elif noun_type == "passphrase":
        return PASSPHRASE_VARIANTS
    else:
        return [""]  # No noun to append (prompt-based phrases already have passphrase)


def generate_all() -> Generator[str, None, None]:
    """Generate all ~412M password candidates."""
    base_phrases = generate_base_phrases()
    trailing_combos = generate_trailing_combinations()
    
    # Separators: space and period
    separators = [" ", "."]
    
    # Case variants: lowercase and First cap
    case_variants = [False, True]
    
    for words, noun_type in base_phrases:
        noun_variants = get_noun_variants(noun_type)
        
        for noun in noun_variants:
            for sep in separators:
                for first_cap in case_variants:
                    # Build the phrase
                    if noun:
                        full_words = words + [noun]
                    else:
                        full_words = words
                    
                    cased_words = apply_case(full_words, first_cap)
                    phrase = sep.join(cased_words)
                    
                    for trailing in trailing_combos:
                        if trailing:
                            # Trailing separator matches word separator
                            # (space phrases get space, period phrases get period, or none)
                            for trail_sep in ["", sep]:
                                yield f"{phrase}{trail_sep}{trailing}"
                        else:
                            # No trailing
                            yield phrase


def count_candidates() -> int:
    """Calculate total candidate count."""
    base_phrases = generate_base_phrases()
    trailing_combos = generate_trailing_combinations()
    
    # Count trailing with separators
    # No trailing: 1
    # With trailing: (len(trailing_combos) - 1) * 2 (none or matching separator)
    trailing_with_sep = 1 + (len(trailing_combos) - 1) * 2
    
    total = 0
    for words, noun_type in base_phrases:
        noun_count = len(get_noun_variants(noun_type))
        if noun_count == 0:
            noun_count = 1
        # separators * case * nouns * trailing
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
