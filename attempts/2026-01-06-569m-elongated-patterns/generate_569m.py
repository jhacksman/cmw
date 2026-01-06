#!/usr/bin/env python3
"""
Elongated Potato/Poop Pattern Generator
Target: ~569M candidates

Based on Dean's confirmed patterns:
- NO MIXING: All instances of a character use the SAME leetspeak variant
- p: p, P (2 options)
- o: o, O, 0 (3 options)  
- t: t, T (2 options) - Dean confirmed NEVER uses 7
- a: a, A, 4, @ (4 options)
- y: y, Y (2 options)

Words covered:
- potato (p-o-t-a-t-o): elongate o positions
- poop (p-o-o-p): elongate o positions
- poopy (p-o-o-p-y): elongate o positions
- pootato (p-o-o-t-a-t-o): elongate o positions
- poopoo (p-o-o-p-o-o): elongate o positions

Length: 10-20 characters
Trailing: 0-6 characters from !?~`
Leading: "" or "this is a "
"""

import sys
from itertools import product

# Leetspeak mappings (consistent per word - no mixing)
P_VARIANTS = ['p', 'P']
O_VARIANTS = ['o', 'O', '0']
T_VARIANTS = ['t', 'T']
A_VARIANTS = ['a', 'A', '4', '@']
Y_VARIANTS = ['y', 'Y']

# Trailing characters (Dean uses 1, 3, or 6 chars of !?~`)
TRAILING_CHARS = ['!', '?', '~', '`']

# Leading phrases (space separator only per user's rule)
LEADING_PHRASES = ['', 'this is a ']

def generate_trailing():
    """Generate all trailing patterns: none, or 1-6 chars from !?~`"""
    yield ''  # no trailing
    for length in range(1, 7):
        for combo in product(TRAILING_CHARS, repeat=length):
            yield ''.join(combo)

def distribute_os(total_os, num_positions):
    """
    Generate all ways to distribute total_os among num_positions,
    where each position gets at least 1.
    Uses stars and bars algorithm.
    """
    if num_positions == 1:
        yield [total_os]
        return
    
    if num_positions == 2:
        for first in range(1, total_os):
            yield [first, total_os - first]
        return
    
    if num_positions == 3:
        for first in range(1, total_os - 1):
            for second in range(1, total_os - first):
                third = total_os - first - second
                if third >= 1:
                    yield [first, second, third]
        return
    
    if num_positions == 4:
        for first in range(1, total_os - 2):
            for second in range(1, total_os - first - 1):
                for third in range(1, total_os - first - second):
                    fourth = total_os - first - second - third
                    if fourth >= 1:
                        yield [first, second, third, fourth]
        return

def generate_potato(min_len=10, max_len=20):
    """
    Generate potato patterns: p + o(s) + t + a + t + o(s)
    Base: 6 chars, 2 o-positions
    """
    for length in range(min_len, max_len + 1):
        total_os = length - 4  # p, t, a, t = 4 non-o chars
        if total_os < 2:
            continue
        
        for dist in distribute_os(total_os, 2):
            for p in P_VARIANTS:
                for o in O_VARIANTS:
                    for t in T_VARIANTS:
                        for a in A_VARIANTS:
                            word = p + (o * dist[0]) + t + a + t + (o * dist[1])
                            yield word

def generate_poop(min_len=10, max_len=20):
    """
    Generate poop patterns: p + o(s) + o(s) + p
    Base: 4 chars, 2 o-positions
    """
    for length in range(min_len, max_len + 1):
        total_os = length - 2  # p, p = 2 non-o chars
        if total_os < 2:
            continue
        
        for dist in distribute_os(total_os, 2):
            for p in P_VARIANTS:
                for o in O_VARIANTS:
                    word = p + (o * dist[0]) + (o * dist[1]) + p
                    yield word

def generate_poopy(min_len=10, max_len=20):
    """
    Generate poopy patterns: p + o(s) + o(s) + p + y
    Base: 5 chars, 2 o-positions
    """
    for length in range(min_len, max_len + 1):
        total_os = length - 3  # p, p, y = 3 non-o chars
        if total_os < 2:
            continue
        
        for dist in distribute_os(total_os, 2):
            for p in P_VARIANTS:
                for o in O_VARIANTS:
                    for y in Y_VARIANTS:
                        word = p + (o * dist[0]) + (o * dist[1]) + p + y
                        yield word

def generate_pootato(min_len=10, max_len=20):
    """
    Generate pootato patterns: p + o(s) + o(s) + t + a + t + o(s)
    Base: 7 chars, 3 o-positions
    """
    for length in range(min_len, max_len + 1):
        total_os = length - 4  # p, t, a, t = 4 non-o chars
        if total_os < 3:
            continue
        
        for dist in distribute_os(total_os, 3):
            for p in P_VARIANTS:
                for o in O_VARIANTS:
                    for t in T_VARIANTS:
                        for a in A_VARIANTS:
                            word = p + (o * dist[0]) + (o * dist[1]) + t + a + t + (o * dist[2])
                            yield word

def generate_poopoo(min_len=10, max_len=20):
    """
    Generate poopoo patterns: p + o(s) + o(s) + p + o(s) + o(s)
    Base: 6 chars, 4 o-positions
    """
    for length in range(min_len, max_len + 1):
        total_os = length - 2  # p, p = 2 non-o chars
        if total_os < 4:
            continue
        
        for dist in distribute_os(total_os, 4):
            for p in P_VARIANTS:
                for o in O_VARIANTS:
                    word = p + (o * dist[0]) + (o * dist[1]) + p + (o * dist[2]) + (o * dist[3])
                    yield word

def generate_all():
    """Generate all candidates with leading phrases and trailing chars"""
    trailing_patterns = list(generate_trailing())
    
    # Generate base words
    word_generators = [
        generate_potato,
        generate_poop,
        generate_poopy,
        generate_pootato,
        generate_poopoo,
    ]
    
    for gen in word_generators:
        for word in gen():
            for leading in LEADING_PHRASES:
                for trailing in trailing_patterns:
                    yield leading + word + trailing

def estimate_count():
    """Estimate total candidate count"""
    # Base counts (calculated earlier)
    potato = 5280
    poop = 792
    poopy = 1452
    pootato = 26400
    poopoo = 18150
    base_total = potato + poop + poopy + pootato + poopoo
    
    # Trailing: 1 + 4 + 16 + 64 + 256 + 1024 + 4096 = 5461
    trailing = 5461
    
    # Leading: 2 phrases
    leading = 2
    
    return base_total * trailing * leading

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--estimate':
        count = estimate_count()
        print(f"Estimated candidates: {count:,}", file=sys.stderr)
        print(f"That's {count / 1_000_000:.2f}M candidates", file=sys.stderr)
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == '--count':
        count = 0
        for _ in generate_all():
            count += 1
            if count % 10_000_000 == 0:
                print(f"Counted: {count:,}", file=sys.stderr)
        print(f"Total: {count:,}", file=sys.stderr)
        return
    
    # Stream output
    for candidate in generate_all():
        print(candidate)

if __name__ == '__main__':
    main()
