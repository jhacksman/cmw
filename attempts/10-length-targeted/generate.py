#!/usr/bin/env python3
"""
Hypothesis Family 10: Length-Targeted Patterns (~10B candidates)

Focus: Phrases specifically targeting the ~20 character length hint.
Dean said the password is approximately 20 characters, so this
generates phrases that are close to that length with variations.
"""

from typing import Generator

# Subjects
SUBJECTS = ["i", "my", "this", "the", "a", "another", "yet another", "one more"]

# Verbs
VERBS = ["made", "chose", "picked", "created", "used", "have", "forgot"]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy"
]

# Intensifiers
INTENSIFIERS = ["really", "very", "so", "such a", "totally", "completely", "absolutely"]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "secret", "pw", "passwd"]

# Phrase patterns
PHRASE_PATTERNS = [
    "{adj} {core}",
    "{subj} {adj} {core}",
    "{subj} {core} is {adj}",
    "{subj} {verb} a {adj} {core}",
    "this is a {adj} {core}",
    "this is {adj} {core}",
    "what a {adj} {core}",
    "such a {adj} {core}",
    "{intens} {adj} {core}",
    "{subj} {intens} {adj} {core}",
    "{subj} {verb} a {intens} {adj} {core}",
    "this is a {intens} {adj} {core}",
    "why is {subj} {core} so {adj}",
    "how is {subj} {core} so {adj}",
    "{subj} {core} is {intens} {adj}",
    "sorry {adj} {core}",
    "oops {adj} {core}",
    "damn {adj} {core}",
    "crap {adj} {core}",
    "ugh {adj} {core}",
]

def generate_base_phrases():
    """Generate all base phrase patterns"""
    for pattern in PHRASE_PATTERNS:
        for subj in SUBJECTS:
            for verb in VERBS:
                for adj in ADJECTIVES:
                    for intens in INTENSIFIERS:
                        for core in CORE_WORDS:
                            try:
                                phrase = pattern.format(subj=subj, verb=verb, adj=adj, intens=intens, core=core)
                                yield phrase
                            except KeyError:
                                pass

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
        for sep in SEPARATORS:
            phrase = base.replace(" ", sep) if sep != " " else base
            for case_phrase in case_variants(phrase):
                for trailing in trailing_list:
                    candidate = case_phrase + trailing
                    if candidate not in seen:
                        seen.add(candidate)
                        yield candidate

def count_candidates():
    """Estimate candidate count"""
    base_count = len(PHRASE_PATTERNS) * len(SUBJECTS) * len(VERBS) * len(ADJECTIVES) * len(INTENSIFIERS) * len(CORE_WORDS)
    sep_count = len(SEPARATORS)
    case_count = 3
    # 0-3 chars: 1 + 14 + 196 + 2744 = 2955
    trailing_count = 1 + 14 + 14**2 + 14**3
    
    total = base_count * sep_count * case_count * trailing_count
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
