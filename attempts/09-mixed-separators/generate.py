#!/usr/bin/env python3
"""
Hypothesis Family 09: Mixed Separators Patterns (~10B candidates)

Focus: Phrases with mixed separator styles (spaces, periods, dashes, underscores).
Dean might have used inconsistent separators like "this.is a_bad-password"
or other mixed separator patterns.
"""

from typing import Generator
import itertools

# Base words
WORDS = [
    "this", "is", "a", "my", "the", "bad", "dumb", "stupid",
    "terrible", "awful", "weak", "simple", "easy", "lazy",
    "crappy", "password", "passphrase", "pass", "secret"
]

# Adjectives
ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak",
    "simple", "easy", "lazy", "crappy", "shitty", "lame",
    "pathetic", "horrible", "ridiculous", "embarrassing",
    "useless", "worthless", "idiotic", "moronic"
]

# Core words
CORE_WORDS = ["password", "passphrase", "pass", "secret", "pw", "passwd", "key", "phrase"]

# Separators to mix
SEPARATORS = [" ", ".", "-", "_", ""]

# Phrase templates (with {sep1}, {sep2}, {sep3} placeholders)
TEMPLATES = [
    "this{sep1}is{sep2}a{sep3}{adj}{sep1}{core}",
    "this{sep1}is{sep2}{adj}{sep3}{core}",
    "my{sep1}{adj}{sep2}{core}",
    "{adj}{sep1}{core}",
    "i{sep1}made{sep2}a{sep3}{adj}{sep1}{core}",
    "i{sep1}chose{sep2}a{sep3}{adj}{sep1}{core}",
    "what{sep1}a{sep2}{adj}{sep3}{core}",
    "such{sep1}a{sep2}{adj}{sep3}{core}",
    "really{sep1}{adj}{sep2}{core}",
    "very{sep1}{adj}{sep2}{core}",
    "so{sep1}{adj}{sep2}{core}",
    "the{sep1}{adj}{sep2}{core}",
    "a{sep1}{adj}{sep2}{core}",
    "another{sep1}{adj}{sep2}{core}",
    "{adj}{sep1}{adj}{sep2}{core}",
    "my{sep1}{core}{sep2}is{sep3}{adj}",
    "this{sep1}{core}{sep2}is{sep3}{adj}",
    "the{sep1}{core}{sep2}is{sep3}{adj}",
    "i{sep1}have{sep2}a{sep3}{adj}{sep1}{core}",
    "sorry{sep1}{adj}{sep2}{core}",
    "i{sep1}forgot{sep2}my{sep3}{adj}{sep1}{core}",
    "i{sep1}need{sep2}a{sep3}{adj}{sep1}{core}",
    "i{sep1}want{sep2}a{sep3}{adj}{sep1}{core}",
    "i{sep1}hate{sep2}my{sep3}{adj}{sep1}{core}",
    "why{sep1}is{sep2}my{sep3}{core}{sep1}{adj}",
    "how{sep1}is{sep2}my{sep3}{core}{sep1}{adj}",
    "cant{sep1}remember{sep2}my{sep3}{adj}{sep1}{core}",
    "forgot{sep1}my{sep2}{adj}{sep3}{core}",
    "lost{sep1}my{sep2}{adj}{sep3}{core}",
    "oops{sep1}{adj}{sep2}{core}",
    "damn{sep1}{adj}{sep2}{core}",
    "crap{sep1}{adj}{sep2}{core}",
    "shit{sep1}{adj}{sep2}{core}",
    "ugh{sep1}{adj}{sep2}{core}",
    "ok{sep1}{adj}{sep2}{core}",
    "fine{sep1}{adj}{sep2}{core}",
    "yes{sep1}{adj}{sep2}{core}",
    "no{sep1}{adj}{sep2}{core}",
    "just{sep1}a{sep2}{adj}{sep3}{core}",
    "only{sep1}a{sep2}{adj}{sep3}{core}",
    "its{sep1}a{sep2}{adj}{sep3}{core}",
    "thats{sep1}a{sep2}{adj}{sep3}{core}",
    "heres{sep1}a{sep2}{adj}{sep3}{core}",
    "one{sep1}more{sep2}{adj}{sep3}{core}",
    "yet{sep1}another{sep2}{adj}{sep3}{core}",
    "totally{sep1}{adj}{sep2}{core}",
    "completely{sep1}{adj}{sep2}{core}",
    "absolutely{sep1}{adj}{sep2}{core}",
    "seriously{sep1}{adj}{sep2}{core}",
    "honestly{sep1}{adj}{sep2}{core}",
    "truly{sep1}{adj}{sep2}{core}",
    "super{sep1}{adj}{sep2}{core}",
    "ultra{sep1}{adj}{sep2}{core}",
    "mega{sep1}{adj}{sep2}{core}",
    "extra{sep1}{adj}{sep2}{core}",
]

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
    """Generate all base phrase patterns with mixed separators"""
    for template in TEMPLATES:
        for adj in ADJECTIVES:
            for core in CORE_WORDS:
                # Generate all combinations of 3 separators
                for sep1, sep2, sep3 in itertools.product(SEPARATORS, repeat=3):
                    try:
                        phrase = template.format(sep1=sep1, sep2=sep2, sep3=sep3, adj=adj, core=core)
                        yield phrase
                    except KeyError:
                        pass

def generate_all() -> Generator[str, None, None]:
    """Generate all candidates"""
    trailing_list = list(generate_trailing())
    
    seen = set()
    for base in generate_base_phrases():
        for case_phrase in case_variants(base):
            for trailing in trailing_list:
                candidate = case_phrase + trailing
                if candidate not in seen:
                    seen.add(candidate)
                    yield candidate

def count_candidates():
    """Estimate candidate count"""
    base_count = len(TEMPLATES) * len(ADJECTIVES) * len(CORE_WORDS) * (len(SEPARATORS) ** 3)
    case_count = 3
    trailing_count = 1 + 14 + 14**2 + 14**3
    
    total = base_count * case_count * trailing_count
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
