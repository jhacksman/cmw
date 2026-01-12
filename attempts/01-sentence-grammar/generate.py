#!/usr/bin/env python3
"""
Hypothesis Family 01: Sentence Grammar Patterns (~10B candidates)

Focus: Grammatically complete sentences with subject-verb-object structure
that haven't been covered by previous "this is a [adj] [noun]" patterns.

Key insight: Dean might have used complete sentences like:
- "i made a bad password"
- "my password is bad"
- "i forgot my password"
- "this password sucks"

These are DIFFERENT from "this is a bad password" patterns already tested.
"""

import itertools
from typing import Generator

# Subject pronouns
SUBJECTS = ["i", "my", "the", "this", "that", "what a", "such a", "another", "yet another", "one more"]

# Verbs (past and present)
VERBS = [
    "made", "created", "chose", "picked", "set", "used", "have", "got",
    "forgot", "lost", "need", "want", "hate", "love", "like", "remember",
    "typed", "entered", "wrote", "saved", "picked", "selected", "thought of"
]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak", "simple",
    "easy", "lazy", "crappy", "shitty", "lame", "pathetic", "horrible"
]

# Nouns
NOUNS = ["password", "passphrase", "pass", "key", "secret", "pw", "passwd", "phrase"]

# Sentence patterns (subject + verb + object variations)
PATTERNS = [
    "{subj} {verb} a {adj} {noun}",           # i made a bad password
    "{subj} {verb} the {adj} {noun}",         # i chose the dumb password
    "{subj} {noun} is {adj}",                 # my password is bad
    "{subj} {noun} was {adj}",                # the password was stupid
    "{subj} {adj} {noun}",                    # my bad password
    "{noun} {verb} {adj}",                    # password is bad
    "what a {adj} {noun}",                    # what a bad password
    "such a {adj} {noun}",                    # such a dumb password
    "so {adj} {noun}",                        # so bad password
    "{verb} {adj} {noun}",                    # forgot bad password
    "i {verb} my {adj} {noun}",               # i forgot my bad password
    "i {verb} this {adj} {noun}",             # i made this bad password
    "this {noun} is so {adj}",                # this password is so bad
    "my {noun} is really {adj}",              # my password is really bad
    "i have a {adj} {noun}",                  # i have a bad password
    "i need a {adj} {noun}",                  # i need a bad password (ironic)
    "why is my {noun} so {adj}",              # why is my password so bad
    "cant remember my {adj} {noun}",          # cant remember my bad password
    "i always {verb} {adj} {noun}s",          # i always make bad passwords
    "{adj} {noun} again",                     # bad password again
]

# Separators
SEPARATORS = [" ", ".", ""]

# Case variants
def case_variants(phrase):
    yield phrase.lower()
    yield phrase.title()
    yield phrase.lower().capitalize()

# Trailing patterns (0-3 chars for ~10B)
TRAILING_CHARS = "0123456789!?~`"

def generate_trailing():
    yield ""
    # 1 char
    for c in TRAILING_CHARS:
        yield c
    # 2 chars
    for c1 in TRAILING_CHARS:
        for c2 in TRAILING_CHARS:
            yield c1 + c2
    # 3 chars
    for c1 in TRAILING_CHARS:
        for c2 in TRAILING_CHARS:
            for c3 in TRAILING_CHARS:
                yield c1 + c2 + c3

def generate_base_phrases():
    """Generate all base phrase patterns"""
    for pattern in PATTERNS:
        for subj in SUBJECTS:
            for verb in VERBS:
                for adj in ADJECTIVES:
                    for noun in NOUNS:
                        try:
                            phrase = pattern.format(subj=subj, verb=verb, adj=adj, noun=noun)
                            yield phrase
                        except KeyError:
                            # Pattern doesn't use all variables
                            pass
        
        # Also try patterns with just some variables
        for adj in ADJECTIVES:
            for noun in NOUNS:
                try:
                    phrase = pattern.format(subj="i", verb="made", adj=adj, noun=noun)
                    yield phrase
                except KeyError:
                    pass

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
    # Base patterns
    base_count = len(PATTERNS) * len(SUBJECTS) * len(VERBS) * len(ADJECTIVES) * len(NOUNS)
    # Separators
    sep_count = len(SEPARATORS)
    # Case variants
    case_count = 3
    # Trailing: 1 + 14 + 196 + 2744 = 2955
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
