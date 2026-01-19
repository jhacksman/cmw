#!/usr/bin/env python3
"""
Hypothesis Family 07: Minimal Leet Patterns (~10B candidates)

Focus: Phrases with only 1-2 leet substitutions, not full leet.
Dean confirmed a→@ and s→$ but might have only applied them
selectively rather than to every occurrence.
"""

from typing import Generator

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy"
]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "secret"]

# Subjects
SUBJECTS = ["i", "my", "this", "the", "a"]

# Verbs
VERBS = ["made", "chose", "picked", "created", "used"]

# Patterns to generate base phrases
PHRASE_PATTERNS = [
    "this is a {adj} {core}",
    "{subj} {core} is {adj}",
    "{adj} {core}",
    "{subj} {verb} a {adj} {core}",
    "what a {adj} {core}",
    "such a {adj} {core}",
    "really {adj} {core}",
    "{core} is {adj}",
    "this {core} is {adj}",
    "{subj} {adj} {core}",
]

def generate_base_phrases():
    """Generate all base phrase patterns"""
    for pattern in PHRASE_PATTERNS:
        for adj in ADJECTIVES:
            for core in CORE_WORDS:
                for subj in SUBJECTS:
                    for verb in VERBS:
                        try:
                            phrase = pattern.format(adj=adj, core=core, subj=subj, verb=verb)
                            yield phrase
                        except KeyError:
                            pass

# Leet substitution pairs (only apply 1-2 at a time)
LEET_SUBS = [
    ("a", "@"),
    ("a", "4"),
    ("s", "$"),
    ("s", "5"),
    ("e", "3"),
    ("i", "1"),
    ("o", "0"),
]

def apply_single_leet(phrase, sub_from, sub_to):
    """Apply leet substitution to first occurrence only"""
    return phrase.replace(sub_from, sub_to, 1)

def apply_all_leet(phrase, sub_from, sub_to):
    """Apply leet substitution to all occurrences"""
    return phrase.replace(sub_from, sub_to)

def generate_leet_variants(phrase):
    """Generate variants with 0, 1, or 2 leet substitutions"""
    yield phrase  # No leet
    
    # Single substitution (first occurrence)
    for sub_from, sub_to in LEET_SUBS:
        if sub_from in phrase:
            yield apply_single_leet(phrase, sub_from, sub_to)
    
    # Single substitution (all occurrences)
    for sub_from, sub_to in LEET_SUBS:
        if sub_from in phrase:
            yield apply_all_leet(phrase, sub_from, sub_to)
    
    # Double substitution (two different subs)
    for i, (sub1_from, sub1_to) in enumerate(LEET_SUBS):
        for sub2_from, sub2_to in LEET_SUBS[i+1:]:
            if sub1_from in phrase and sub2_from in phrase:
                variant = apply_all_leet(phrase, sub1_from, sub1_to)
                variant = apply_all_leet(variant, sub2_from, sub2_to)
                yield variant

# Separators
SEPARATORS = [" ", ".", ""]

# Case variants
def case_variants(phrase):
    yield phrase.lower()
    yield phrase.title()
    yield phrase.lower().capitalize()

# Trailing patterns (0-3 chars)
TRAILING_CHARS = "0123456789!?~`"

def generate_trailing():
    yield ""
    for c in TRAILING_CHARS:
        yield c
    for c1 in TRAILING_CHARS:
        for c2 in TRAILING_CHARS:
            yield c1 + c2
    for c1 in TRAILING_CHARS:
        for c2 in TRAILING_CHARS:
            for c3 in TRAILING_CHARS:
                yield c1 + c2 + c3

def generate_all() -> Generator[str, None, None]:
    """Generate all candidates"""
    trailing_list = list(generate_trailing())
    
    seen = set()
    for base in generate_base_phrases():
        for leet_variant in generate_leet_variants(base):
            for sep in SEPARATORS:
                phrase = leet_variant.replace(" ", sep) if sep != " " else leet_variant
                for case_phrase in case_variants(phrase):
                    for trailing in trailing_list:
                        candidate = case_phrase + trailing
                        if candidate not in seen:
                            seen.add(candidate)
                            yield candidate

def count_candidates():
    """Estimate candidate count"""
    # Rough estimate: base phrases * leet variants * separators * case * trailing
    base_count = len(PHRASE_PATTERNS) * len(ADJECTIVES) * len(CORE_WORDS) * len(SUBJECTS) * len(VERBS)
    leet_variants = 1 + len(LEET_SUBS) * 2 + (len(LEET_SUBS) * (len(LEET_SUBS) - 1) // 2)
    sep_count = len(SEPARATORS)
    case_count = 3
    trailing_count = 1 + 14 + 14**2 + 14**3
    
    total = base_count * leet_variants * sep_count * case_count * trailing_count
    return total

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        count = count_candidates()
        print(f"Estimated candidates: {count:,}")
        print(f"Runtime at 270k H/s: {count / 270000 / 3600:.1f} hours")
    elif len(sys.argv) > 1 and sys.argv[1] == "--sample":
        for i, candidate in enumerate(generate_all()):
            print(candidate)
            if i >= 99:
                break
    else:
        for candidate in generate_all():
            print(candidate)
