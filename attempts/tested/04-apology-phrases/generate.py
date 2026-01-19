#!/usr/bin/env python3
"""
Hypothesis Family 04: Apology Phrases (~10B candidates)

Focus: Apologetic phrases about password quality.
Dean's self-deprecating humor suggests he might have used
apologetic phrases like "sorry for the bad password" or
"my apologies for this stupid password".
"""

from typing import Generator

# Apology starters
APOLOGY_STARTERS = [
    "sorry", "sorry for", "sorry about", "im sorry", "im sorry for",
    "apologies", "my apologies", "apologies for", "sincere apologies",
    "forgive me", "forgive me for", "pardon", "pardon me", "excuse me",
    "my bad", "oops", "whoops", "ugh", "damn", "crap", "shit",
    "i apologize", "i apologize for", "please forgive", "please excuse"
]

# Connectors
CONNECTORS = [
    "my", "this", "the", "such a", "another", "yet another"
]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "pw", "passwd", "secret"]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "shitty", "lame",
    "pathetic", "horrible", "ridiculous", "embarrassing",
    "useless", "worthless", "idiotic", "moronic", "insecure"
]

# Apology patterns
PATTERNS = [
    "{starter} {conn} {adj} {core}",                 # sorry my bad password
    "{starter} {conn} {core} is {adj}",              # sorry my password is bad
    "{starter} the {adj} {core}",                    # sorry for the bad password
    "{starter} making a {adj} {core}",               # sorry for making a bad password
    "{starter} choosing a {adj} {core}",             # apologies for choosing a dumb password
    "{starter} using a {adj} {core}",                # sorry for using a weak password
    "{starter} i made a {adj} {core}",               # sorry i made a bad password
    "{starter} i chose a {adj} {core}",              # my bad i chose a dumb password
    "{starter} i have a {adj} {core}",               # oops i have a bad password
    "{starter} {adj} {core}",                        # sorry bad password
    "{conn} {core} is {adj} {starter}",              # my password is bad sorry
    "i know {conn} {core} is {adj} {starter}",       # i know my password is bad sorry
    "{starter} but {conn} {core} is {adj}",          # sorry but my password is bad
    "{starter} {conn} {core} sucks",                 # sorry my password sucks
    "{starter} this {adj} {core}",                   # my bad this stupid password
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
        for starter in APOLOGY_STARTERS:
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
    base_count = len(PATTERNS) * len(APOLOGY_STARTERS) * len(CONNECTORS) * len(CORE_WORDS) * len(ADJECTIVES)
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
