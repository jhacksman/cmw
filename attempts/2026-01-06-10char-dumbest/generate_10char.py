#!/usr/bin/env python3
"""
Generator for "dumbest possible" 10-character patterns.

Based on Telegram deep dive findings:
- Dean was GUIDED (not forced) by "10 or more characters, or 8 or more words"
- He tried to set "the dumbest passphrase I could that matched the requirements"
- His LUKS password was "poop123"
- He said "pooooooooooooooop" as an example
- He uses words like "bad", "dumb", "stupid"
- Separators: spaces (most likely), dots (sometimes)

Target: ~500M candidates focused on exactly 10-12 character patterns.

NO MIXING RULE: All instances of a character type use the same leetspeak variant.
"""

import sys
from itertools import product

# Leetspeak variants (no mixing - pick one variant for all instances)
P_VARIANTS = ['p', 'P']
O_VARIANTS = ['o', 'O', '0']
T_VARIANTS = ['t', 'T']
A_VARIANTS = ['a', 'A', '4', '@']
Y_VARIANTS = ['y', 'Y']

# Trailing characters Dean mentioned
TRAILING_CHARS = ['!', '?', '~', '`', '1', '2', '3']

# Digits
DIGITS = '0123456789'


def generate_poop_with_digits():
    """
    poop + digits to make 10-12 chars.
    poop = 4 chars, so need 6-8 digits.
    """
    for p in P_VARIANTS:
        for o in O_VARIANTS:
            poop = p + o + o + p
            # 6 digits = 10 chars total
            for d in range(1000000):
                yield poop + str(d).zfill(6)
            # 7 digits = 11 chars total
            for d in range(10000000):
                yield poop + str(d).zfill(7)
            # 8 digits = 12 chars total
            for d in range(100000000):
                yield poop + str(d).zfill(8)


def generate_poop_with_mixed_trailing():
    """
    poop + digits + special chars to make 10 chars.
    """
    for p in P_VARIANTS:
        for o in O_VARIANTS:
            poop = p + o + o + p
            # 5 digits + 1 special = 10 chars
            for d in range(100000):
                for t in TRAILING_CHARS:
                    yield poop + str(d).zfill(5) + t
            # 4 digits + 2 special = 10 chars
            for d in range(10000):
                for t1 in TRAILING_CHARS:
                    for t2 in TRAILING_CHARS:
                        yield poop + str(d).zfill(4) + t1 + t2


def generate_potato_with_digits():
    """
    potato + digits to make 10-12 chars.
    potato = 6 chars, so need 4-6 digits.
    """
    for p in P_VARIANTS:
        for o in O_VARIANTS:
            for t in T_VARIANTS:
                for a in A_VARIANTS:
                    potato = p + o + t + a + t + o
                    # 4 digits = 10 chars
                    for d in range(10000):
                        yield potato + str(d).zfill(4)
                    # 5 digits = 11 chars
                    for d in range(100000):
                        yield potato + str(d).zfill(5)
                    # 6 digits = 12 chars
                    for d in range(1000000):
                        yield potato + str(d).zfill(6)


def generate_elongated_poop(min_len=10, max_len=15):
    """
    Elongated poop: p + o's + p with variable o count.
    Since all o's are the same (no mixing), we just need p + (o * n) + p
    """
    for length in range(min_len, max_len + 1):
        num_os = length - 2  # p at start and end
        if num_os < 2:
            continue
        for p in P_VARIANTS:
            for o in O_VARIANTS:
                yield p + (o * num_os) + p


def generate_elongated_potato(min_len=10, max_len=15):
    """
    Elongated potato: p + o(s) + t + a(s) + t + o(s).
    Base: p-o-t-a-t-o = 6 chars.
    """
    for length in range(min_len, max_len + 1):
        extra = length - 6
        if extra < 0:
            continue
        # Distribute extra chars among o1, a, o2 (each gets at least 1)
        for o1_extra in range(extra + 1):
            for a_extra in range(extra - o1_extra + 1):
                o2_extra = extra - o1_extra - a_extra
                for p in P_VARIANTS:
                    for o in O_VARIANTS:
                        for t in T_VARIANTS:
                            for a in A_VARIANTS:
                                word = p + (o * (1 + o1_extra)) + t + (a * (1 + a_extra)) + t + (o * (1 + o2_extra))
                                if len(word) == length:
                                    yield word


def generate_elongated_poopy(min_len=10, max_len=15):
    """
    Elongated poopy: p + o's + p + y.
    Base: p-o-o-p-y = 5 chars.
    Since all o's are the same (no mixing), we just need p + (o * n) + p + y
    """
    for length in range(min_len, max_len + 1):
        num_os = length - 3  # p, p, y = 3 non-o chars
        if num_os < 2:
            continue
        for p in P_VARIANTS:
            for o in O_VARIANTS:
                for y in Y_VARIANTS:
                    yield p + (o * num_os) + p + y


def generate_bad_password_phrases():
    """
    Phrases like "bad password", "dumb password", etc.
    With space or dot separators, case variations, and trailing chars.
    """
    adjectives = ['bad', 'dumb', 'stupid']
    nouns = ['password', 'passwd', 'passwrd', 'pass', 'pwd']
    separators = [' ', '.', '']
    
    for adj in adjectives:
        for noun in nouns:
            for sep in separators:
                base = adj + sep + noun
                # Case variations
                cases = [
                    base.lower(),
                    base.title(),
                    base.upper(),
                    base.lower().replace(adj, adj.title()),
                ]
                for case_var in cases:
                    # No trailing
                    yield case_var
                    # 1-3 trailing digits
                    for d in range(1000):
                        yield case_var + str(d)
                    # 1-3 trailing special
                    for t1 in TRAILING_CHARS:
                        yield case_var + t1
                        for t2 in TRAILING_CHARS:
                            yield case_var + t1 + t2


def generate_this_is_patterns():
    """
    "this is a bad password" style patterns, truncated/modified.
    """
    bases = [
        'thisisabad',
        'thisisadumb', 
        'thisisstupid',
        'this is bad',
        'this is dumb',
        'this.is.bad',
        'this.is.dumb',
        'thisisabadpassword',
        'thisisadumbpassword',
    ]
    
    for base in bases:
        cases = [base.lower(), base.title(), base.upper()]
        for case_var in cases:
            yield case_var
            # With trailing
            for d in range(100):
                yield case_var + str(d)
            for t in TRAILING_CHARS:
                yield case_var + t


def generate_keyboard_patterns():
    """
    Keyboard patterns like qwertyuiop (exactly 10 chars).
    """
    patterns = [
        'qwertyuiop',  # 10 chars
        'asdfghjkl;',  # 10 chars
        '1234567890',  # 10 chars
        '0987654321',  # 10 chars
        'qazwsxedcr',  # 10 chars
        'qwerty1234',  # 10 chars
        'asdf123456',  # 10 chars
        'zxcvbnm,./',  # 10 chars
    ]
    
    for pattern in patterns:
        yield pattern
        yield pattern.upper()
        yield pattern.title() if pattern.isalpha() else pattern
        # Reversed
        yield pattern[::-1]
        yield pattern[::-1].upper()


def generate_password_variants():
    """
    "password" + digits to make 10-12 chars.
    password = 8 chars.
    """
    bases = ['password', 'Password', 'PASSWORD', 'passphrase', 'Passphrase', 'PASSPHRASE']
    
    for base in bases:
        yield base
        # password + 2 digits = 10 chars
        if len(base) == 8:
            for d in range(100):
                yield base + str(d).zfill(2)
            for d in range(1000):
                yield base + str(d).zfill(3)
            for d in range(10000):
                yield base + str(d).zfill(4)
        # passphrase is already 10 chars
        elif len(base) == 10:
            yield base
            for d in range(100):
                yield base + str(d)


def generate_simple_repeated():
    """
    Single character repeated 10 times.
    """
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    for c in chars:
        yield c * 10
        yield c * 11
        yield c * 12


def estimate_count():
    """Estimate total candidate count."""
    # poop + 6 digits: 6 variants * 1M = 6M
    # poop + 7 digits: 6 variants * 10M = 60M
    # poop + 8 digits: 6 variants * 100M = 600M
    poop_digits = 6 * (1000000 + 10000000 + 100000000)
    
    # poop + 5 digits + 1 special: 6 * 100k * 7 = 4.2M
    # poop + 4 digits + 2 special: 6 * 10k * 49 = 2.94M
    poop_mixed = 6 * 100000 * 7 + 6 * 10000 * 49
    
    # potato + 4-6 digits: 48 variants * (10k + 100k + 1M) = 53.3M
    potato_digits = 48 * (10000 + 100000 + 1000000)
    
    # Elongated patterns: ~3k
    elongated = 3000
    
    # Phrases: ~200k
    phrases = 200000
    
    # Keyboard: ~100
    keyboard = 100
    
    # Password variants: ~50k
    password = 50000
    
    # Repeated: ~200
    repeated = 200
    
    total = poop_digits + poop_mixed + potato_digits + elongated + phrases + keyboard + password + repeated
    return total


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--estimate':
        count = estimate_count()
        print(f"Estimated candidates: {count:,}")
        print(f"That's approximately {count/1e6:.1f}M or {count/1e9:.2f}B")
        return
    
    # Generate all patterns
    # Priority order based on evidence strength
    
    # 1. Elongated patterns (Dean's explicit example)
    for word in generate_elongated_poop():
        print(word)
    for word in generate_elongated_potato():
        print(word)
    for word in generate_elongated_poopy():
        print(word)
    
    # 2. Bad password phrases (Dean's explicit example)
    for word in generate_bad_password_phrases():
        print(word)
    
    # 3. "This is" patterns
    for word in generate_this_is_patterns():
        print(word)
    
    # 4. Keyboard patterns
    for word in generate_keyboard_patterns():
        print(word)
    
    # 5. Password variants
    for word in generate_password_variants():
        print(word)
    
    # 6. Simple repeated
    for word in generate_simple_repeated():
        print(word)
    
    # 7. Poop + mixed trailing (smaller set)
    for word in generate_poop_with_mixed_trailing():
        print(word)
    
    # 8. Poop + digits (largest set - 666M)
    for word in generate_poop_with_digits():
        print(word)
    
    # 9. Potato + digits (53M)
    for word in generate_potato_with_digits():
        print(word)


if __name__ == '__main__':
    main()
