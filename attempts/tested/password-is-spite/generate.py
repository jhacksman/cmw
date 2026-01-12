#!/usr/bin/env python3
"""
"This password/passphrase is [intensifier] [brute-spite]" Structure Generator

Brute forces the spite slot with 1-5 lowercase chars (22 letters, excluding jqxzv).

Pattern: "this password is really [BRUTE 1-5 chars]"

Dean's exact trailing pattern:
- 0, 1, 3, or 6 of the SAME char from !?~`
- No mixed trailing like "!?~"

Intensifiers: very, really, super (single, double, triple, quad)
Nouns: password, passphrase (+ leet variants)

Target: ~5.6B candidates
"""

import itertools
from typing import Generator, List, Tuple

# Brute force charset: 21 lowercase letters (excluding j, q, x, z, v)
BRUTE_CHARS = "abcdefghiklmnoprstuwy"  # 21 chars (no j, q, x, z, v)

# Brute force lengths: 1-5 chars
BRUTE_LENGTHS = [1, 2, 3, 4, 5]

# Dean-confirmed intensifiers
INTENSIFIERS = ["very", "really", "super"]

# Dean-confirmed nouns with leetspeak variants (no mixing)
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

# Dean's exact trailing chars
TRAILING_CHARS = ["!", "?", "~", "`"]

# Dean's exact trailing lengths: 0, 1, 3, or 6 (same char repeated)
TRAILING_LENGTHS = [0, 1, 3, 6]


def generate_trailing_combinations() -> List[str]:
    """
    Generate Dean's exact trailing pattern:
    - Empty (no trailing)
    - 1 char: !, ?, ~, `
    - 3 chars: !!!, ???, ~~~, ```
    - 6 chars: !!!!!!, ??????, ~~~~~~, ``````
    """
    combinations = [""]  # Empty (no trailing)
    for char in TRAILING_CHARS:
        for length in TRAILING_LENGTHS:
            if length > 0:
                combinations.append(char * length)
    return combinations


def generate_brute_spite() -> Generator[str, None, None]:
    """Generate all brute force spite words (1-5 chars from 22 letters)."""
    for length in BRUTE_LENGTHS:
        for combo in itertools.product(BRUTE_CHARS, repeat=length):
            yield "".join(combo)


def count_brute_spite() -> int:
    """Count total brute force spite combinations."""
    total = 0
    for length in BRUTE_LENGTHS:
        total += len(BRUTE_CHARS) ** length
    return total


def generate_phrase_templates() -> List[Tuple[List[str], str, int]]:
    """
    Generate phrase templates with placeholder for brute spite.
    Returns list of (word_list_before_spite, noun_base, intensifier_count).
    The spite word will be appended at the end.
    """
    templates = []
    
    for noun_base in ["password", "passphrase"]:
        # No intensifier: "this password is [SPITE]"
        templates.append((["this", noun_base, "is"], noun_base, 0))
        
        # Single intensifier: "this password is really [SPITE]"
        for intensifier in INTENSIFIERS:
            templates.append((["this", noun_base, "is", intensifier], noun_base, 1))
        
        # Double intensifier: "this password is really really [SPITE]"
        for intensifier in INTENSIFIERS:
            templates.append((["this", noun_base, "is", intensifier, intensifier], noun_base, 2))
        
        # Triple intensifier: "this password is really really really [SPITE]"
        for intensifier in INTENSIFIERS:
            templates.append((["this", noun_base, "is", intensifier, intensifier, intensifier], noun_base, 3))
        
        # Quad intensifier: "this password is really really really really [SPITE]"
        for intensifier in INTENSIFIERS:
            templates.append((["this", noun_base, "is", intensifier, intensifier, intensifier, intensifier], noun_base, 4))
    
    return templates


def get_noun_variants(noun_base: str) -> List[str]:
    """Get the appropriate noun variants based on base noun."""
    if noun_base == "password":
        return PASSWORD_VARIANTS
    elif noun_base == "passphrase":
        return PASSPHRASE_VARIANTS
    return [noun_base]


def apply_case(words: List[str], first_cap: bool) -> List[str]:
    """Apply case variant to word list."""
    if first_cap and words:
        return [words[0].capitalize()] + words[1:]
    return words


def generate_all() -> Generator[str, None, None]:
    """Generate all password candidates."""
    templates = generate_phrase_templates()
    trailing_combos = generate_trailing_combinations()
    
    # Separators: space and period
    separators = [" ", "."]
    
    # Case variants: lowercase and First cap
    case_variants = [False, True]
    
    for template_words, noun_base, _ in templates:
        noun_variants = get_noun_variants(noun_base)
        
        for noun in noun_variants:
            # Replace the noun_base in template with the leet variant
            leet_template = [noun if w == noun_base else w for w in template_words]
            
            for sep in separators:
                for first_cap in case_variants:
                    cased_template = apply_case(leet_template, first_cap)
                    template_str = sep.join(cased_template)
                    
                    # Now iterate through all brute spite words
                    for spite in generate_brute_spite():
                        phrase = f"{template_str}{sep}{spite}"
                        
                        for trailing in trailing_combos:
                            if trailing:
                                # Trailing separator matches word separator
                                for trail_sep in ["", sep]:
                                    yield f"{phrase}{trail_sep}{trailing}"
                            else:
                                # No trailing
                                yield phrase


def count_candidates() -> int:
    """Calculate total candidate count."""
    templates = generate_phrase_templates()
    trailing_combos = generate_trailing_combinations()
    brute_count = count_brute_spite()
    
    # Count trailing with separators
    # No trailing: 1
    # With trailing: (len(trailing_combos) - 1) * 2 (none or matching separator)
    trailing_with_sep = 1 + (len(trailing_combos) - 1) * 2
    
    total = 0
    for template_words, noun_base, _ in templates:
        noun_count = len(get_noun_variants(noun_base))
        # separators * case * nouns * brute_spite * trailing
        total += 2 * 2 * noun_count * brute_count * trailing_with_sep
    
    return total


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        brute_count = count_brute_spite()
        templates = generate_phrase_templates()
        trailing_combos = generate_trailing_combinations()
        
        print(f"Brute spite combinations: {brute_count:,}")
        print(f"Phrase templates: {len(templates)}")
        print(f"Trailing combinations: {len(trailing_combos)}")
        print(f"Total candidates: {count_candidates():,}")
    else:
        for candidate in generate_all():
            print(candidate)
