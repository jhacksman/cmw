#!/usr/bin/env python3
"""
Hypothesis Family 02: Question Format Patterns (~10B candidates)

Focus: Self-deprecating questions about password quality
that Dean might have used as a passphrase.

Key insight: Questions are natural sentence structures that
haven't been fully explored. Dean's self-deprecating humor
suggests questions like "why is my password so bad?"
"""

from typing import Generator

# Question starters
QUESTION_STARTERS = [
    "why is", "why did", "why do",
    "how is", "how did", "how could",
    "what is", "who made",
    "is this", "is my",
    "did i", "do i"
]

# Subjects/objects
SUBJECTS = [
    "my password", "this password", "the password",
    "my passphrase", "this passphrase",
    "my pass", "this pass"
]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "shitty", "lame",
    "pathetic", "horrible", "so bad", "so dumb", "so stupid",
    "this bad", "this dumb", "this stupid"
]

# Verbs
VERBS = [
    "make", "made", "choose", "chose", "pick", "picked",
    "use", "used", "create", "created", "forget", "forgot"
]

# Question patterns
PATTERNS = [
    "{starter} {subj} so {adj}",                    # why is my password so bad
    "{starter} {subj} {adj}",                       # why is my password bad
    "{starter} i {verb} a {adj} password",          # why did i make a bad password
    "{starter} i {verb} such a {adj} password",     # why did i choose such a dumb password
    "{starter} this {adj} password",                # what is this bad password
    "{starter} {verb} a {adj} password",            # who made a bad password
    "{starter} {verb} such a {adj} password",       # who chose such a stupid password
    "{starter} {adj} password even work",           # how could bad password even work
    "{starter} believe {subj} is {adj}",            # can you believe my password is bad
    "{starter} guess {subj}",                       # can you guess my password
    "{starter} remember {subj}",                    # can you remember my password
    "{starter} {verb} {subj}",                      # did i forget my password
    "why {adj} password",                           # why bad password
    "why such a {adj} password",                    # why such a bad password
    "how {adj} is {subj}",                          # how bad is my password
    "what {adj} password is this",                  # what bad password is this
    "is {subj} really {adj}",                       # is my password really bad
    "is {subj} that {adj}",                         # is my password that bad
    "seriously {adj} password",                     # seriously bad password
    "really {adj} password",                        # really bad password
]

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

def generate_base_phrases():
    """Generate all base phrase patterns"""
    for pattern in PATTERNS:
        for starter in QUESTION_STARTERS:
            for subj in SUBJECTS:
                for adj in ADJECTIVES:
                    for verb in VERBS:
                        try:
                            phrase = pattern.format(starter=starter, subj=subj, adj=adj, verb=verb)
                            yield phrase
                        except KeyError:
                            pass
        
        # Also try with just some variables
        for adj in ADJECTIVES:
            for subj in SUBJECTS:
                try:
                    phrase = pattern.format(starter="why is", subj=subj, adj=adj, verb="make")
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
    base_count = len(PATTERNS) * len(QUESTION_STARTERS) * len(SUBJECTS) * len(ADJECTIVES) * len(VERBS)
    sep_count = len(SEPARATORS)
    case_count = 3
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
