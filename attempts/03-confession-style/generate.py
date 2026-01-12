#!/usr/bin/env python3
"""
Hypothesis Family 03: Confession Style Patterns (~10B candidates)

Focus: Self-deprecating confessions about making a bad password.
Dean's humor suggests he might have used confessional phrases like
"i admit my password is bad" or "i confess this is stupid".
"""

from typing import Generator

# Confession starters
CONFESSION_STARTERS = [
    "i admit", "i confess", "i know", "i realize", "i understand",
    "yes", "ok", "okay", "fine", "alright", "sure", "yep", "yeah",
    "its true", "honestly", "truthfully", "seriously", "really",
    "look", "listen", "hey", "well", "so", "anyway"
]

# Middle connectors
CONNECTORS = [
    "my", "this", "the", "that", "a", "another", "yet another"
]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "pw", "passwd", "secret", "key"]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "shitty", "lame",
    "pathetic", "horrible", "ridiculous", "embarrassing",
    "useless", "worthless", "idiotic", "moronic", "insecure"
]

# Confession patterns
PATTERNS = [
    "{starter} {conn} {core} is {adj}",              # i admit my password is bad
    "{starter} i made a {adj} {core}",               # i confess i made a bad password
    "{starter} i chose a {adj} {core}",              # i know i chose a dumb password
    "{starter} i have a {adj} {core}",               # yes i have a bad password
    "{starter} {conn} {core} sucks",                 # ok my password sucks
    "{starter} {conn} {core} is {adj} as hell",      # fine my password is bad as hell
    "{starter} this is a {adj} {core}",              # i admit this is a bad password
    "{starter} i picked a {adj} {core}",             # i confess i picked a dumb password
    "{starter} its a {adj} {core}",                  # ok its a bad password
    "i made a {adj} {core} {starter}",               # i made a bad password ok
    "{conn} {core} is {adj} {starter}",              # my password is bad ok
    "so {starter} {conn} {core} is {adj}",           # so yes my password is bad
    "{starter} so {conn} {core} is {adj}",           # ok so my password is bad
    "{starter} {conn} {adj} {core}",                 # fine my bad password
    "just {starter} {conn} {core} is {adj}",         # just admit my password is bad
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
        for starter in CONFESSION_STARTERS:
            for conn in CONNECTORS:
                for core in CORE_WORDS:
                    for adj in ADJECTIVES:
                        try:
                            phrase = pattern.format(starter=starter, conn=conn, core=core, adj=adj)
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
    base_count = len(PATTERNS) * len(CONFESSION_STARTERS) * len(CONNECTORS) * len(CORE_WORDS) * len(ADJECTIVES)
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
