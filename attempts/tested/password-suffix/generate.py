#!/usr/bin/env python3
"""
Password/Passphrase Suffix Generator

Just the words "password" and "passphrase" with:
- Case variants: lowercase, First cap
- Leet variants: plain, numbers (a->4, s->5), symbols (a->@, s->$)
- Trailing: 0-6 chars from `~!?

~65K candidates
"""

import itertools
from typing import Generator

# Base words
BASE_WORDS = ["password", "passphrase"]

# Trailing chars
TRAILING_CHARS = "`~!?"
MAX_TRAILING = 6


def apply_leet_numbers(text: str) -> str:
    """Apply number-style leet: a->4, s->5"""
    return text.replace("a", "4").replace("A", "4").replace("s", "5").replace("S", "5")


def apply_leet_symbols(text: str) -> str:
    """Apply symbol-style leet: a->@, s->$"""
    return text.replace("a", "@").replace("A", "@").replace("s", "$").replace("S", "$")


def generate_trailing_combinations() -> list:
    """Generate all trailing combinations from 0-6 chars using `~!?"""
    combinations = [""]
    for length in range(1, MAX_TRAILING + 1):
        for combo in itertools.product(TRAILING_CHARS, repeat=length):
            combinations.append("".join(combo))
    return combinations


def generate_all() -> Generator[str, None, None]:
    """Generate all password candidates."""
    trailing_combos = generate_trailing_combinations()
    case_variants = [False, True]  # lowercase, First cap
    leet_variants = [None, "numbers", "symbols"]
    
    for word in BASE_WORDS:
        for first_cap in case_variants:
            if first_cap:
                cased_word = word.capitalize()
            else:
                cased_word = word
            
            for leet in leet_variants:
                if leet == "numbers":
                    leeted_word = apply_leet_numbers(cased_word)
                elif leet == "symbols":
                    leeted_word = apply_leet_symbols(cased_word)
                else:
                    leeted_word = cased_word
                
                for trailing in trailing_combos:
                    yield f"{leeted_word}{trailing}"


def count_candidates() -> int:
    """Calculate total candidate count."""
    trailing_combos = generate_trailing_combinations()
    # words * case * leet * trailing
    return len(BASE_WORDS) * 2 * 3 * len(trailing_combos)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print(f"Total candidates: {count_candidates():,}")
        print(f"Trailing combinations: {len(generate_trailing_combinations())}")
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
