#!/usr/bin/env python3
"""
Passphrase/Password Brute Force with Prefix+Suffix Pattern

Tests "passphrase" and "password" with ALL prefix and suffix combinations
from `~!? characters where prefix_len + suffix_len <= 10.

This includes all 66 unique (prefix, suffix) pairs:
(0,0), (0,1), (1,0), (1,1), (0,2), (2,0), (1,2), (2,1), ... up to (10,0) and (0,10)

With case variants and leet variants (plain, numbers, symbols).

~179M candidates total
"""

import itertools
from typing import Generator, List, Tuple

# Base words
BASE_WORDS = ["passphrase", "password"]

# Prefix/suffix chars
CHARS = "`~!?"
MAX_TOTAL_LENGTH = 10


def apply_leet_numbers(text: str) -> str:
    """Apply number-style leet: a->4, s->5"""
    return text.replace("a", "4").replace("A", "4").replace("s", "5").replace("S", "5")


def apply_leet_symbols(text: str) -> str:
    """Apply symbol-style leet: a->@, s->$"""
    return text.replace("a", "@").replace("A", "@").replace("s", "$").replace("S", "$")


def generate_prefix_suffix_pairs() -> List[Tuple[int, int]]:
    """
    Generate ALL (prefix_len, suffix_len) pairs where prefix + suffix <= MAX_TOTAL_LENGTH.
    This gives 66 unique pairs for MAX_TOTAL_LENGTH=10.
    """
    pairs = []
    for prefix_len in range(MAX_TOTAL_LENGTH + 1):
        for suffix_len in range(MAX_TOTAL_LENGTH + 1 - prefix_len):
            pairs.append((prefix_len, suffix_len))
    return pairs


def generate_strings(length: int) -> Generator[str, None, None]:
    """Generate all strings of given length from CHARS."""
    if length == 0:
        yield ""
    else:
        for combo in itertools.product(CHARS, repeat=length):
            yield "".join(combo)


def generate_all() -> Generator[str, None, None]:
    """Generate all password candidates."""
    pairs = generate_prefix_suffix_pairs()
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
                
                for prefix_len, suffix_len in pairs:
                    for prefix in generate_strings(prefix_len):
                        for suffix in generate_strings(suffix_len):
                            yield f"{prefix}{leeted_word}{suffix}"


def count_candidates() -> int:
    """Calculate total candidate count."""
    pairs = generate_prefix_suffix_pairs()
    
    total_combos = 0
    for prefix_len, suffix_len in pairs:
        prefix_combos = len(CHARS) ** prefix_len if prefix_len > 0 else 1
        suffix_combos = len(CHARS) ** suffix_len if suffix_len > 0 else 1
        total_combos += prefix_combos * suffix_combos
    
    # words * case * leet * prefix/suffix combos
    return len(BASE_WORDS) * 2 * 3 * total_combos


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print(f"Total candidates: {count_candidates():,}")
        pairs = generate_prefix_suffix_pairs()
        print(f"Prefix/suffix pairs: {len(pairs)}")
        print(f"Pairs: {pairs}")
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
