#!/usr/bin/env python3
"""
Hypothesis Family 05: Sarcasm/Irony Patterns (~10B candidates)

Focus: Ironic/sarcastic statements about password security.
Dean's humor suggests he might have used ironic phrases like
"this is a secure password" (when it's not) or "totally safe password".
"""

from typing import Generator

# Sarcastic qualifiers
SARCASTIC_QUALIFIERS = [
    "totally", "completely", "absolutely", "definitely", "obviously",
    "clearly", "surely", "certainly", "undoubtedly", "100 percent",
    "super", "very", "really", "extremely", "incredibly", "amazingly"
]

# Positive adjectives (used ironically)
POSITIVE_ADJECTIVES = [
    "secure", "safe", "strong", "good", "great", "excellent",
    "perfect", "amazing", "awesome", "brilliant", "genius",
    "smart", "clever", "unbreakable", "unhackable", "foolproof",
    "best", "finest", "top notch", "world class", "elite",
    "professional", "military grade", "bank level", "nsa proof"
]

# Connectors
CONNECTORS = ["my", "this", "the", "a", "another", "yet another", "one more", "such a"]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "pw", "passwd", "secret"]

# Ironic patterns
PATTERNS = [
    "{qual} {adj} {core}",                           # totally secure password
    "this is a {qual} {adj} {core}",                 # this is a totally secure password
    "{conn} {core} is {qual} {adj}",                 # my password is totally secure
    "what a {qual} {adj} {core}",                    # what a totally secure password
    "such a {qual} {adj} {core}",                    # such a totally secure password
    "{qual} not a bad {core}",                       # totally not a bad password
    "this {core} is {qual} {adj}",                   # this password is totally secure
    "{conn} {qual} {adj} {core}",                    # my totally secure password
    "i made a {qual} {adj} {core}",                  # i made a totally secure password
    "behold {conn} {qual} {adj} {core}",             # behold my totally secure password
    "look at {conn} {qual} {adj} {core}",            # look at my totally secure password
    "{qual} {adj} {core} here",                      # totally secure password here
    "yes this is {qual} {adj}",                      # yes this is totally secure
    "{qual} {adj} right",                            # totally secure right
    "nothing wrong with {conn} {core}",              # nothing wrong with my password
    "{conn} {core} is {adj} trust me",               # my password is secure trust me
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
        for qual in SARCASTIC_QUALIFIERS:
            for adj in POSITIVE_ADJECTIVES:
                for conn in CONNECTORS:
                    for core in CORE_WORDS:
                        try:
                            phrase = pattern.format(qual=qual, adj=adj, conn=conn, core=core)
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
    base_count = len(PATTERNS) * len(SARCASTIC_QUALIFIERS) * len(POSITIVE_ADJECTIVES) * len(CONNECTORS) * len(CORE_WORDS)
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
