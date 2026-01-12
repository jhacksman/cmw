#!/usr/bin/env python3
"""
Hypothesis Family 06: Hacker Slang Patterns (~10B candidates)

Focus: 2011-era hacker/internet slang that Dean might have used.
This includes terms like "derp", "herp", "lulz", "rofl", "potato",
"poop", and other meme-era vocabulary combined with password themes.
"""

from typing import Generator

# 2011-era slang words
SLANG_WORDS = [
    "derp", "herp", "derpy", "herpy", "derpina", "herpderp",
    "lulz", "lol", "rofl", "lmao", "lmfao", "roflmao",
    "potato", "potatoes", "potatoe", "tater", "spud",
    "poop", "poopy", "poo", "crap", "crappy",
    "fail", "epic fail", "failboat", "failure",
    "win", "epic win", "ftw", "winning",
    "noob", "n00b", "newb", "newbie", "scrub",
    "pwn", "pwned", "owned", "rekt", "wrecked"
]

# Password-related words
PASSWORD_WORDS = ["password", "passphrase", "pass", "pw", "passwd", "secret"]

# Connectors
CONNECTORS = [
    "is", "was", "my", "this", "the", "a", "such", "very", "so", "much"
]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "shitty", "lame"
]

# Slang patterns
PATTERNS = [
    "{slang} {core}",                                # derp password
    "{core} {slang}",                                # password derp
    "{slang} {adj} {core}",                          # derp bad password
    "{adj} {slang} {core}",                          # bad derp password
    "{conn} {slang} {core}",                         # my derp password
    "{conn} {core} is {slang}",                      # my password is derp
    "this {core} is {slang}",                        # this password is derp
    "{slang} {slang} {core}",                        # derp derp password
    "such {slang} {core}",                           # such derp password
    "very {slang} {core}",                           # very derp password
    "so {slang} {core}",                             # so derp password
    "much {slang} {core}",                           # much derp password
    "{slang} is {conn} {core}",                      # derp is my password
    "i {slang} at {core}s",                          # i fail at passwords
    "{core} {slang} {slang}",                        # password derp herp
    "{slang} {conn} {adj} {core}",                   # derp my bad password
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
        for slang in SLANG_WORDS:
            for core in PASSWORD_WORDS:
                for conn in CONNECTORS:
                    for adj in ADJECTIVES:
                        try:
                            phrase = pattern.format(slang=slang, core=core, conn=conn, adj=adj)
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
    base_count = len(PATTERNS) * len(SLANG_WORDS) * len(PASSWORD_WORDS) * len(CONNECTORS) * len(ADJECTIVES)
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
