#!/usr/bin/env python3
"""
Generate systematic trailing character combinations.

Based on Dean's hint: "Likely 1, 3, maybe 6, exclamations or question marks 
sometimes tildes or back ticks"

This script generates all combinations of trailing characters for base phrases.
"""

import argparse
import itertools
import sys

# Base phrases (most likely candidates)
BASE_PHRASES = [
    "this is a bad password",
    "this is a bad passphrase",
    "bad password",
    "bad passphrase",
    "this is a dumb password",
    "this is a dumb passphrase",
    "this is a very bad password",
    "this is a really bad password",
    "this is a really dumb passphrase",
    "this.is.a.bad.password",
    "this.is.a.bad.passphrase",
    "bad.password",
    "this.is.a.dumb.password",
]

# Trailing characters Dean mentioned
TRAILING_CHARS = ["!", "?", "~", "`"]

# Numbers Dean might use
TRAILING_NUMBERS = ["1", "3", "6", "123", "111", "123456"]


def generate_trailing_1char():
    """Generate 1-character trailing patterns."""
    for char in TRAILING_CHARS:
        yield char
    for num in ["1", "2", "3"]:
        yield num


def generate_trailing_3char():
    """Generate 3-character trailing patterns."""
    # Repeated single chars
    for char in TRAILING_CHARS:
        yield char * 3
    
    # Number patterns
    yield "123"
    yield "111"
    yield "321"
    
    # Mixed patterns
    for char in TRAILING_CHARS:
        yield char + "1" + char
        yield "1" + char + "1"


def generate_trailing_6char():
    """Generate 6-character trailing patterns."""
    # Repeated single chars
    for char in TRAILING_CHARS:
        yield char * 6
    
    # Number patterns
    yield "123456"
    yield "111111"
    yield "654321"
    
    # Repeated 3-char patterns
    for char in TRAILING_CHARS:
        yield (char * 3) * 2


def generate_all_trailing():
    """Generate all trailing patterns."""
    yield ""  # No trailing
    yield from generate_trailing_1char()
    yield from generate_trailing_3char()
    yield from generate_trailing_6char()


def main():
    parser = argparse.ArgumentParser(
        description="Generate trailing character combinations"
    )
    parser.add_argument(
        "--base-only", action="store_true",
        help="Output only base phrases without trailing"
    )
    parser.add_argument(
        "--trailing-only", action="store_true",
        help="Output only trailing patterns"
    )
    parser.add_argument(
        "--custom-base", type=str,
        help="Use custom base phrase instead of defaults"
    )
    
    args = parser.parse_args()
    
    if args.trailing_only:
        for trailing in generate_all_trailing():
            if trailing:
                print(trailing)
        return
    
    bases = [args.custom_base] if args.custom_base else BASE_PHRASES
    
    if args.base_only:
        for base in bases:
            print(base)
        return
    
    # Generate all combinations
    seen = set()
    for base in bases:
        for trailing in generate_all_trailing():
            candidate = base + trailing
            if candidate not in seen:
                seen.add(candidate)
                print(candidate)


if __name__ == "__main__":
    main()
