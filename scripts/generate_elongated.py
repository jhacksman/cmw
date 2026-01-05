#!/usr/bin/env python3
"""
Generate elongated/repeated character patterns.

Based on Dean's hint: "I just know it's going to be the dumbest freaking 
password. Like 'pooooooooooooooop' or something."

This script generates variations with repeated characters.
"""

import argparse
import sys

# Words to elongate with their elongatable character
ELONGATABLE_WORDS = {
    "bad": [("a", [3, 5, 7, 10, 15])],
    "dumb": [("u", [3, 5, 7, 10])],
    "stupid": [("u", [3, 5, 7])],
    "poop": [("o", [5, 10, 15, 20])],
    "password": [("s", [3, 5, 7]), ("a", [3, 5])],
    "passphrase": [("s", [3, 5, 7])],
    "lame": [("a", [3, 5, 7, 10])],
    "weak": [("e", [3, 5, 7])],
    "easy": [("a", [3, 5, 7])],
    "simple": [("i", [3, 5])],
    "terrible": [("e", [3, 5])],
    "awful": [("a", [3, 5])],
    "shit": [("i", [3, 5, 7])],
    "crap": [("a", [3, 5, 7])],
    "derpy": [("e", [3, 5])],
}

# Phrase templates
PHRASE_TEMPLATES = [
    "{word}",
    "{word} password",
    "{word} passphrase",
    "this is {word}",
    "this is a {word} password",
    "this is a {word} passphrase",
    "really {word}",
    "so {word}",
    "very {word}",
]

# Trailing patterns
TRAILING = ["", "!", "123", "1", "!!!", "?"]


def elongate_word(word: str, char: str, count: int) -> str:
    """Elongate a word by repeating a character."""
    idx = word.find(char)
    if idx >= 0:
        return word[:idx] + char * count + word[idx+1:]
    return word


def generate_elongated_words():
    """Generate all elongated word variations."""
    for word, elongations in ELONGATABLE_WORDS.items():
        for char, counts in elongations:
            for count in counts:
                elongated = elongate_word(word, char, count)
                yield elongated


def generate_elongated_phrases():
    """Generate phrases with elongated words."""
    for word, elongations in ELONGATABLE_WORDS.items():
        for char, counts in elongations:
            for count in counts:
                elongated = elongate_word(word, char, count)
                
                for template in PHRASE_TEMPLATES:
                    phrase = template.format(word=elongated)
                    
                    for trailing in TRAILING:
                        yield phrase + trailing
                        
                    # Also with periods instead of spaces
                    phrase_dots = phrase.replace(" ", ".")
                    if phrase_dots != phrase:
                        for trailing in TRAILING:
                            yield phrase_dots + trailing


def generate_repeated_patterns():
    """Generate pure repeated character patterns."""
    # Single character repeated
    chars = ["a", "b", "d", "e", "i", "o", "p", "s", "u"]
    for char in chars:
        for count in [10, 15, 20, 25, 30]:
            yield char * count
            yield char * count + "123"
            yield char * count + "!"
    
    # Word repeated
    words = ["bad", "dumb", "poop", "lol", "lulz"]
    for word in words:
        for count in [2, 3, 4, 5]:
            yield word * count
            yield (word + " ") * count
            yield (word + ".") * count


def main():
    parser = argparse.ArgumentParser(
        description="Generate elongated/repeated character patterns"
    )
    parser.add_argument(
        "--words-only", action="store_true",
        help="Output only elongated words, not phrases"
    )
    parser.add_argument(
        "--repeated-only", action="store_true",
        help="Output only pure repeated patterns"
    )
    
    args = parser.parse_args()
    
    seen = set()
    
    if args.words_only:
        for word in generate_elongated_words():
            if word not in seen:
                seen.add(word)
                print(word)
        return
    
    if args.repeated_only:
        for pattern in generate_repeated_patterns():
            if pattern not in seen:
                seen.add(pattern)
                print(pattern)
        return
    
    # Generate all
    for phrase in generate_elongated_phrases():
        if phrase not in seen:
            seen.add(phrase)
            print(phrase)
    
    for pattern in generate_repeated_patterns():
        if pattern not in seen:
            seen.add(pattern)
            print(pattern)


if __name__ == "__main__":
    main()
