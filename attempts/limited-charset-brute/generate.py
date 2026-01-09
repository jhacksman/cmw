#!/usr/bin/env python3
"""
Limited Charset Brute Force Generator

Position-constrained brute force with the following rules:
- P: positions 1-5 only
- b: positions 1-5 only
- d: positions 3-6 and 8-10 only
- 1, 2, 3: positions 1-3 OR last 3 only
- ~`!?: positions 1-3 OR last 3 only
- Last char: must be from ~`!?123 (7 chars)

Base charset (always available): p a s h r e 0 4 5 w o @ $ (13 chars)

For 8 chars: ~8.4B candidates (~8.6 hours at 270k H/s)
"""

import itertools
from typing import Generator, List

# Base chars (always available in any position except last)
BASE_CHARS = "pashre045wo@$"  # 13 chars

# Position-restricted chars
CHAR_P = "P"      # positions 1-5 only
CHAR_B = "b"      # positions 1-5 only
CHAR_D = "d"      # positions 3-6 and 8-10 only
CHARS_123 = "123" # positions 1-3 or last 3 only
CHARS_SYMBOLS = "~`!?"  # positions 1-3 or last 3 only

# Last char options
LAST_CHARS = "~`!?123"  # 7 chars

# Default max length
DEFAULT_MAX_LENGTH = 8


def get_charset_for_position(pos: int, total_length: int) -> str:
    """Get the allowed charset for a given position in a password of given length."""
    
    # Last position is special
    if pos == total_length:
        return LAST_CHARS
    
    # Start with base chars
    charset = BASE_CHARS
    
    # Add P if position 1-5
    if pos <= 5:
        charset += CHAR_P
    
    # Add b if position 1-5
    if pos <= 5:
        charset += CHAR_B
    
    # Add d if position 3-6 or 8-10
    if (3 <= pos <= 6) or (8 <= pos <= 10):
        charset += CHAR_D
    
    # Add 123 if position 1-3 or last 3 (but not last position itself)
    if pos <= 3 or pos >= total_length - 2:
        charset += CHARS_123
    
    # Add ~`!? if position 1-3 or last 3 (but not last position itself)
    if pos <= 3 or pos >= total_length - 2:
        charset += CHARS_SYMBOLS
    
    return charset


def generate_for_length(length: int) -> Generator[str, None, None]:
    """Generate all candidates of a specific length."""
    if length == 0:
        return
    
    # Get charsets for each position
    charsets = [get_charset_for_position(pos, length) for pos in range(1, length + 1)]
    
    # Generate all combinations
    for combo in itertools.product(*charsets):
        yield "".join(combo)


def generate_all(max_length: int = DEFAULT_MAX_LENGTH) -> Generator[str, None, None]:
    """Generate all candidates from length 1 to max_length."""
    for length in range(1, max_length + 1):
        for candidate in generate_for_length(length):
            yield candidate


def count_for_length(length: int) -> int:
    """Count candidates for a specific length."""
    if length == 0:
        return 0
    
    total = 1
    for pos in range(1, length + 1):
        charset = get_charset_for_position(pos, length)
        total *= len(charset)
    return total


def count_all(max_length: int = DEFAULT_MAX_LENGTH) -> int:
    """Count all candidates from length 1 to max_length."""
    return sum(count_for_length(length) for length in range(1, max_length + 1))


if __name__ == "__main__":
    import sys
    
    max_len = DEFAULT_MAX_LENGTH
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--count":
            if len(sys.argv) > 2:
                max_len = int(sys.argv[2])
            print(f"Counting candidates for lengths 1-{max_len}:")
            total = 0
            for length in range(1, max_len + 1):
                count = count_for_length(length)
                total += count
                print(f"  Length {length}: {count:,}")
            print(f"  Total: {total:,}")
            print(f"\nRuntime at 270k H/s: {total / 270000 / 3600:.1f} hours")
            
        elif sys.argv[1] == "--breakdown":
            if len(sys.argv) > 2:
                length = int(sys.argv[2])
            else:
                length = 8
            print(f"Charset breakdown for {length}-char passwords:")
            for pos in range(1, length + 1):
                charset = get_charset_for_position(pos, length)
                print(f"  Position {pos}: {len(charset)} chars: {charset}")
            print(f"\nTotal combinations: {count_for_length(length):,}")
            
        elif sys.argv[1] == "--sample":
            if len(sys.argv) > 2:
                max_len = int(sys.argv[2])
            count = 0
            for candidate in generate_all(max_len):
                print(candidate)
                count += 1
                if count >= 100:
                    break
                    
        elif sys.argv[1].isdigit():
            max_len = int(sys.argv[1])
            for candidate in generate_all(max_len):
                print(candidate)
        else:
            print("Usage:")
            print("  python3 generate.py [max_length]  - Generate all candidates")
            print("  python3 generate.py --count [max_length]  - Count candidates")
            print("  python3 generate.py --breakdown [length]  - Show charset per position")
            print("  python3 generate.py --sample [max_length]  - Show first 100 candidates")
    else:
        for candidate in generate_all(max_len):
            print(candidate)
