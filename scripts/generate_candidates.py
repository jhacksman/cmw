#!/usr/bin/env python3
"""
Crack My Wallet - Passphrase Candidate Generator

This script generates passphrase candidates based on Dean Pierce's (px) hints
about his forgotten Bitcoin wallet passphrase.

Key constraints from Dean:
- It's a PASSPHRASE (multiple words), not a single password
- Likely 4-7 words (more than his usual 3-4)
- Separators: spaces (most likely), periods (sometimes), dashes (rarely)
- Theme: Self-deprecating statement about password weakness
- Leetspeak: a->@,4; s->$,5; pass->p455,p@$$; NEVER 7 for r
- Trailing chars: 1, 3, or 6 characters - !, ?, ~, `
- Era: Late 2011, DEFCON 19 timeframe

Usage:
    python generate_candidates.py [--priority N] [--output FILE] [--count]
    
    --priority N: Generate only priority level N (1-6)
    --output FILE: Write to file instead of stdout
    --count: Just count candidates, don't output them
"""

import argparse
import itertools
import sys
from typing import Generator, Set

# Core adjectives (most likely based on Dean's hints)
CORE_ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak", 
    "simple", "easy", "lazy", "embarrassing", "pathetic"
]

# 2011 era slang adjectives
ERA_ADJECTIVES = [
    "derpy", "lulzy", "lame", "crappy", "shitty", "silly",
    "ridiculous", "horrible", "worst", "dumbest"
]

# All adjectives combined
ALL_ADJECTIVES = CORE_ADJECTIVES + ERA_ADJECTIVES

# Core nouns
CORE_NOUNS = ["password", "passphrase"]

# Extended nouns
EXTENDED_NOUNS = ["password", "passphrase", "pass", "passwd", "secret", "key"]

# Separators (ordered by likelihood based on Dean's hints)
SEPARATORS = [" ", ".", "-", ""]

# Trailing patterns (1, 3, or 6 chars as Dean mentioned)
TRAILING_PATTERNS = [
    "",  # No trailing
    # 1 character
    "!", "?", "~", "`", "1",
    # 3 characters
    "!!!", "???", "~~~", "```", "123", "111",
    # 6 characters
    "!!!!!!", "??????", "~~~~~~", "``````", "123456", "111111",
]

# Leetspeak substitutions (Dean's confirmed patterns)
LEET_SUBSTITUTIONS = {
    "a": ["a", "@", "4"],
    "s": ["s", "$", "5"],
    "e": ["e", "3"],
    "i": ["i", "1"],
    "o": ["o", "0"],
}

# Special word substitutions (Dean confirmed p455, p@$$)
WORD_SUBSTITUTIONS = {
    "pass": ["pass", "p455", "p@$$", "p4$$", "p@55"],
    "password": ["password", "p455word", "p@$$word", "p4$$word", "p@55word"],
    "passphrase": ["passphrase", "p455phrase", "p@$$phrase"],
}


def apply_leet(word: str, level: int = 1) -> Generator[str, None, None]:
    """Apply leetspeak substitutions to a word.
    
    level 1: Only Dean's confirmed substitutions (a, s)
    level 2: Extended substitutions (a, s, e, i, o)
    """
    if level == 0:
        yield word
        return
    
    # Check for special word substitutions first
    word_lower = word.lower()
    if word_lower in WORD_SUBSTITUTIONS:
        for sub in WORD_SUBSTITUTIONS[word_lower]:
            yield sub
        return
    
    # Apply character-level substitutions
    chars_options = []
    for char in word:
        char_lower = char.lower()
        if level >= 1 and char_lower in ["a", "s"]:
            chars_options.append(LEET_SUBSTITUTIONS[char_lower])
        elif level >= 2 and char_lower in LEET_SUBSTITUTIONS:
            chars_options.append(LEET_SUBSTITUTIONS[char_lower])
        else:
            chars_options.append([char])
    
    # Generate all combinations (limit to avoid explosion)
    count = 0
    for combo in itertools.product(*chars_options):
        yield "".join(combo)
        count += 1
        if count > 100:  # Limit per word
            break


def apply_case_variations(phrase: str) -> Generator[str, None, None]:
    """Apply case variations to a phrase."""
    yield phrase.lower()
    yield phrase.title()
    yield phrase.upper()
    # Sentence case (first letter caps)
    if phrase:
        yield phrase[0].upper() + phrase[1:].lower()


def generate_priority_1() -> Generator[str, None, None]:
    """Priority 1: Core phrase variations with spaces.
    
    Focus on the exact patterns Dean mentioned:
    - "this is a bad password"
    - "bad password"
    - "this is a very bad password"
    - "this is a really dumb passphrase"
    """
    prefixes = [
        "this is a",
        "this is a really",
        "this is a very",
        "this is such a",
        "what a",
        "such a",
        "my",
        "a really",
        "a very",
        "",
    ]
    
    for prefix in prefixes:
        for adj in CORE_ADJECTIVES:
            for noun in CORE_NOUNS:
                for sep in [" ", "."]:  # Most likely separators
                    if prefix:
                        phrase = f"{prefix}{sep}{adj}{sep}{noun}"
                    else:
                        phrase = f"{adj}{sep}{noun}"
                    
                    # Apply case variations
                    for case_var in apply_case_variations(phrase):
                        # Apply trailing patterns
                        for trailing in TRAILING_PATTERNS:
                            yield case_var + trailing


def generate_priority_2() -> Generator[str, None, None]:
    """Priority 2: 2011 era slang variations.
    
    Incorporate slang that was popular in 2011:
    derpy, lulzy, lame, etc.
    """
    prefixes = [
        "this is a",
        "this is a really",
        "this is such a",
        "such a",
        "",
    ]
    
    for prefix in prefixes:
        for adj in ERA_ADJECTIVES:
            for noun in CORE_NOUNS:
                for sep in [" ", "."]:
                    if prefix:
                        phrase = f"{prefix}{sep}{adj}{sep}{noun}"
                    else:
                        phrase = f"{adj}{sep}{noun}"
                    
                    for case_var in apply_case_variations(phrase):
                        for trailing in TRAILING_PATTERNS:
                            yield case_var + trailing


def generate_priority_3() -> Generator[str, None, None]:
    """Priority 3: Leetspeak mutations.
    
    Apply Dean's confirmed leetspeak patterns:
    - p455, p@$$
    - a->@,4; s->$,5
    """
    base_phrases = [
        "this is a bad password",
        "this is a bad passphrase",
        "bad password",
        "bad passphrase",
        "this is a dumb password",
        "this is a very bad password",
        "this is a really bad password",
        "this is a really dumb passphrase",
    ]
    
    for phrase in base_phrases:
        words = phrase.split()
        
        # Apply leet to each word
        word_options = []
        for word in words:
            word_options.append(list(apply_leet(word, level=1)))
        
        # Generate combinations (limit to avoid explosion)
        count = 0
        for combo in itertools.product(*word_options):
            for sep in [" ", ".", ""]:
                leet_phrase = sep.join(combo)
                for trailing in TRAILING_PATTERNS[:7]:  # Limit trailing
                    yield leet_phrase + trailing
                    count += 1
                    if count > 50000:
                        return


def generate_priority_4() -> Generator[str, None, None]:
    """Priority 4: Repeated character patterns.
    
    Based on Dean's "pooooooooooooooop" example.
    """
    # Elongated words
    elongations = [
        ("bad", "a", [3, 5, 7, 10]),  # baaad, baaaad, etc.
        ("dumb", "u", [3, 5, 7]),
        ("stupid", "u", [3, 5]),
        ("poop", "o", [5, 10, 15]),
        ("password", "s", [3, 5]),
        ("lame", "a", [3, 5, 7]),
    ]
    
    for word, char, counts in elongations:
        for count in counts:
            # Find the character position and elongate
            idx = word.find(char)
            if idx >= 0:
                elongated = word[:idx] + char * count + word[idx+1:]
                yield elongated
                yield elongated + "123"
                yield elongated + "!"
                
                # In phrase context
                for prefix in ["this is a ", "this is ", ""]:
                    yield prefix + elongated
                    yield prefix + elongated + " password"


def generate_priority_5() -> Generator[str, None, None]:
    """Priority 5: Extended phrase patterns (5-7 words).
    
    Longer phrases that fit the "more words than usual" hint.
    """
    templates = [
        "this is a really really {adj} {noun}",
        "this is a very very {adj} {noun}",
        "this is the {adj}est {noun} ever",
        "i have a really {adj} {noun}",
        "my {noun} is really {adj}",
        "what a really {adj} {noun} this is",
        "this {noun} is so {adj}",
        "such a {adj} {adj} {noun}",
    ]
    
    for template in templates:
        for adj in CORE_ADJECTIVES[:5]:  # Limit adjectives
            for noun in CORE_NOUNS:
                phrase = template.format(adj=adj, noun=noun)
                for sep in [" ", "."]:
                    phrase_sep = phrase.replace(" ", sep)
                    yield phrase_sep
                    yield phrase_sep + "!"
                    yield phrase_sep + "123"


def generate_priority_6() -> Generator[str, None, None]:
    """Priority 6: DEFCON and hacker culture context.
    
    Phrases that might relate to DEFCON 19 or hacker culture.
    """
    defcon_phrases = [
        "defcon password",
        "defcon passphrase",
        "my defcon password",
        "this is my defcon password",
        "hacker password",
        "vegas password",
        "conference password",
        "defcon 19 password",
        "defcon19password",
        "dc19 password",
        "dc19password",
    ]
    
    for phrase in defcon_phrases:
        yield phrase
        yield phrase.replace(" ", ".")
        yield phrase.replace(" ", "")
        yield phrase + "!"
        yield phrase + "123"
        for case_var in apply_case_variations(phrase):
            yield case_var


def generate_all(priority: int = None) -> Generator[str, None, None]:
    """Generate all candidates, optionally filtered by priority."""
    generators = {
        1: generate_priority_1,
        2: generate_priority_2,
        3: generate_priority_3,
        4: generate_priority_4,
        5: generate_priority_5,
        6: generate_priority_6,
    }
    
    if priority:
        if priority in generators:
            yield from generators[priority]()
    else:
        for p in sorted(generators.keys()):
            yield from generators[p]()


def deduplicate(generator: Generator[str, None, None]) -> Generator[str, None, None]:
    """Remove duplicates while preserving order."""
    seen: Set[str] = set()
    for item in generator:
        if item not in seen:
            seen.add(item)
            yield item


def main():
    parser = argparse.ArgumentParser(
        description="Generate passphrase candidates for crackmywallet.org"
    )
    parser.add_argument(
        "--priority", "-p", type=int, choices=[1, 2, 3, 4, 5, 6],
        help="Generate only priority level N"
    )
    parser.add_argument(
        "--output", "-o", type=str,
        help="Write to file instead of stdout"
    )
    parser.add_argument(
        "--count", "-c", action="store_true",
        help="Just count candidates, don't output them"
    )
    parser.add_argument(
        "--no-dedup", action="store_true",
        help="Don't deduplicate (faster but may have duplicates)"
    )
    
    args = parser.parse_args()
    
    # Generate candidates
    generator = generate_all(args.priority)
    
    if not args.no_dedup:
        generator = deduplicate(generator)
    
    if args.count:
        count = sum(1 for _ in generator)
        print(f"Total candidates: {count:,}")
        return
    
    # Output
    if args.output:
        with open(args.output, "w") as f:
            for candidate in generator:
                f.write(candidate + "\n")
        print(f"Wrote candidates to {args.output}", file=sys.stderr)
    else:
        for candidate in generator:
            print(candidate)


if __name__ == "__main__":
    main()
