#!/usr/bin/env python3
"""
Hypothesis Family 08: Repeated Words Patterns (~10B candidates)

Focus: Phrases with repeated words or emphasis through repetition.
Dean might have used patterns like "bad bad password" or
"password password password" for emphasis or humor.
"""

from typing import Generator

# Words to repeat
REPEAT_WORDS = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "really", "very",
    "so", "such", "my", "this", "the", "a", "another",
    "yet", "more", "super", "ultra", "mega", "extra",
    "totally", "completely", "absolutely", "seriously",
    "honestly", "truly", "damn", "freaking", "fucking"
]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "secret", "pw", "passwd", "key"]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "shitty", "lame",
    "pathetic", "horrible", "ridiculous", "embarrassing",
    "useless", "worthless", "idiotic", "moronic"
]

# Repetition patterns
PATTERNS = [
    "{word} {word} {core}",                          # bad bad password
    "{word} {word} {word} {core}",                   # bad bad bad password
    "{adj} {adj} {core}",                            # stupid stupid password
    "{core} {core}",                                 # password password
    "{core} {core} {core}",                          # password password password
    "this is a {adj} {adj} {core}",                  # this is a bad bad password
    "my {adj} {adj} {core}",                         # my bad bad password
    "{word} {adj} {word} {core}",                    # really bad really password
    "so {adj} so {adj} {core}",                      # so bad so bad password
    "very {adj} very {adj} {core}",                  # very bad very bad password
    "{adj} {core} {adj} {core}",                     # bad password bad password
    "i made a {adj} {adj} {core}",                   # i made a bad bad password
    "what a {adj} {adj} {core}",                     # what a bad bad password
    "such a {adj} {adj} {core}",                     # such a bad bad password
    "{word} {word} {adj} {core}",                    # really really bad password
    "{adj} {word} {word} {core}",                    # bad really really password
    "{word} {word} {word} {adj} {core}",             # really really really bad password
    "{adj} {adj} {adj} {core}",                      # bad bad bad password
    "this {core} is {adj} {adj}",                    # this password is bad bad
    "my {core} is {adj} {adj}",                      # my password is bad bad
    "{word} {word} this {core}",                     # really really this password
    "{adj} {word} {adj} {core}",                     # bad really bad password
    "i {word} {word} made a {adj} {core}",           # i really really made a bad password
    "{word} {adj} {adj} {core}",                     # really bad bad password
    "{adj} {adj} {word} {core}",                     # bad bad really password
    "the {adj} {adj} {core}",                        # the bad bad password
    "a {adj} {adj} {core}",                          # a bad bad password
    "another {adj} {adj} {core}",                    # another bad bad password
    "{word} {core} {word} {core}",                   # my password my password
    "i have a {adj} {adj} {core}",                   # i have a bad bad password
    "i chose a {adj} {adj} {core}",                  # i chose a bad bad password
    "why is my {core} so {adj} {adj}",               # why is my password so bad bad
    "{word} {word} {word} {word} {core}",            # really really really really password
    "{adj} {adj} {adj} {adj} {core}",                # bad bad bad bad password
    "this is {word} {word} {adj} {core}",            # this is really really bad password
    "i {word} made a {adj} {adj} {core}",            # i really made a bad bad password
    "{word} this is a {adj} {core}",                 # really this is a bad password
    "ok {word} {word} {adj} {core}",                 # ok really really bad password
    "yes {word} {word} {adj} {core}",                # yes really really bad password
    "its a {adj} {adj} {core}",                      # its a bad bad password
    "just a {adj} {adj} {core}",                     # just a bad bad password
    "only a {adj} {adj} {core}",                     # only a bad bad password
    "{word} {word} {core} {core}",                   # really really password password
    "{adj} {core} {core}",                           # bad password password
    "{core} {adj} {core}",                           # password bad password
    "{word} {adj} {core} {core}",                    # really bad password password
    "i {word} {word} {word} made {adj} {core}",      # i really really really made bad password
    "{word} {word} i made a {adj} {core}",           # really really i made a bad password
    "oh {word} {word} {adj} {core}",                 # oh really really bad password
    "wow {word} {word} {adj} {core}",                # wow really really bad password
    "damn {word} {word} {adj} {core}",               # damn really really bad password
    "shit {word} {word} {adj} {core}",               # shit really really bad password
    "crap {word} {word} {adj} {core}",               # crap really really bad password
    "ugh {word} {word} {adj} {core}",                # ugh really really bad password
    "omg {word} {word} {adj} {core}",                # omg really really bad password
    "lol {word} {word} {adj} {core}",                # lol really really bad password
    "wtf {word} {word} {adj} {core}",                # wtf really really bad password
    "fml {word} {word} {adj} {core}",                # fml really really bad password
    "{word} {word} {adj} {adj} {core}",              # really really bad bad password
    "{adj} {word} {word} {adj} {core}",              # bad really really bad password
    "{word} {adj} {word} {adj} {core}",              # really bad really bad password
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
        for word in REPEAT_WORDS:
            for core in CORE_WORDS:
                for adj in ADJECTIVES:
                    try:
                        phrase = pattern.format(word=word, core=core, adj=adj)
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
    base_count = len(PATTERNS) * len(REPEAT_WORDS) * len(CORE_WORDS) * len(ADJECTIVES)
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
