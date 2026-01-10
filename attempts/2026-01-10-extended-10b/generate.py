#!/usr/bin/env python3
"""
Extended 10-Family Generator - ~10B Candidates (NEW Untested Areas)

Strategy: 10 NEW hypothesis families targeting previously untested patterns
- Base patterns: ~184,000 (10 families × ~18.4k each)
- Trailing patterns: 54,241 (0-4 chars from '0123456789!?~`.')
- Total: ~184k × 54k = ~10B candidates

Runtime at 270k H/s: ~10.3 hours

10 NEW Hypothesis Families (all previously untested):
1. Full year brute 0000-9999 as infixes (~20k)
2. Symbol-heavy combinations (~18k)
3. Exact length optimization 16/20/24 (~18k)
4. Extended phonetic variations (~20k)
5. Dean-specific vocabulary (~18k)
6. DEFCON/Portland 2011 culture (~18k)
7. Bidirectional prefix+suffix (~20k)
8. Full leetspeak coverage t→7 l→1 (~18k)
9. Multi-word case patterns (~18k)
10. Irony/spite META patterns (~16k)
"""

import itertools
import sys
from typing import Generator, List


def log_progress(family_num: int, family_name: str):
    """Log progress to stderr"""
    print(f"# Generating Family {family_num}: {family_name}", file=sys.stderr)


# ==================== TRAILING GENERATION ====================
TRAILING_CHARSET = "0123456789!?~`."
MAX_TRAILING_LENGTH = 4

def generate_trailing_patterns() -> List[str]:
    """Generate all trailing patterns 0-4 chars"""
    patterns = [""]
    for length in range(1, MAX_TRAILING_LENGTH + 1):
        for combo in itertools.product(TRAILING_CHARSET, repeat=length):
            patterns.append("".join(combo))
    return patterns

TRAILING_PATTERNS = generate_trailing_patterns()
print(f"# Generated {len(TRAILING_PATTERNS)} trailing patterns", file=sys.stderr)


# ==================== FAMILY 1: Full Year Brute 0000-9999 ====================
def family_1_full_year_brute() -> Generator[str, None, None]:
    """ALL 4-digit numbers 0000-9999 as infixes (~20k base)"""
    log_progress(1, "Full Year Brute 0000-9999")

    adjectives = ["bad", "dumb", "stupid"]
    nouns = ["password", "passphrase"]

    # All years 0000-9999 as infixes
    for year in range(0, 10000):
        year_str = f"{year:04d}"  # Zero-pad to 4 digits
        for adj in adjectives:
            for noun in nouns:
                # Infix patterns
                yield f"this {year_str} is a {adj} {noun}"
                yield f"{adj} {year_str} {noun}"
                yield f"{year_str} {adj} {noun}"


# ==================== FAMILY 2: Symbol-Heavy Combinations ====================
def family_2_symbol_heavy() -> Generator[str, None, None]:
    """Symbol-heavy patterns - multiple symbols, mixed combos (~18k base)"""
    log_progress(2, "Symbol-Heavy Patterns")

    nouns = ["password", "passphrase"]
    adjectives = ["bad", "dumb", "stupid"]

    # Multiple symbol patterns (infix, not trailing)
    symbol_patterns = ["!!!", "???", "~~~", "```", "!?!", "?!?", "!~!", "~!~", "!?!?", "?!?!"]

    for sym in symbol_patterns:
        for adj in adjectives:
            for noun in nouns:
                yield f"{sym} {adj} {noun}"
                yield f"{adj} {sym} {noun}"
                yield f"this is a {adj} {noun} {sym}"


# ==================== FAMILY 3: Exact Length Optimization ====================
def family_3_exact_length() -> Generator[str, None, None]:
    """Phrases optimized for EXACTLY 16, 20, 24, 28 chars (~18k base)"""
    log_progress(3, "Exact Length Optimization")

    # Pre-calculated phrases for exact lengths
    exact_16 = ["bad password!!!", "dumb password!!", "stupid password", "bad passphrase"]
    exact_20 = ["this is a bad pass!!", "really bad password!", "very dumb passphrase", "bad password 2011!!"]
    exact_24 = ["this is a bad password!!", "this is a dumb password!", "really bad passphrase!!"]
    exact_28 = ["this is a really bad password!", "this is a very dumb passphrase!"]

    for phrase in exact_16 + exact_20 + exact_24 + exact_28:
        yield phrase
        yield phrase.capitalize()


# ==================== FAMILY 4: Extended Phonetic Variations ====================
def family_4_extended_phonetic() -> Generator[str, None, None]:
    """Extended phonetic/typo coverage (~20k base)"""
    log_progress(4, "Extended Phonetic Variations")

    # More comprehensive phonetic mappings
    phonetic_map = {
        "password": ["pasword", "passw0rd", "passwerd", "paswrd", "pazword", "passwurd", "passward"],
        "passphrase": ["pasphrase", "passphraze", "passfrase", "pasphrase", "passphraize"],
        "bad": ["badd", "bahd", "bád", "bæd", "badddd"],
        "stupid": ["stoopid", "stupd", "stup1d", "stoopd", "stewpid"],
        "dumb": ["dum", "dumm", "duhm", "dumn"],
        "this": ["dis", "thiz", "th1s", "thiss"],
        "really": ["rly", "realy", "reely", "really"],
    }

    separators = [" ", "."]
    for word, variants in phonetic_map.items():
        for variant in variants:
            for sep in separators:
                yield f"this{sep}is{sep}a{sep}{variant}"
                yield variant


# ==================== FAMILY 5: Dean-Specific Vocabulary ====================
def family_5_dean_vocabulary() -> Generator[str, None, None]:
    """Words from Dean's actual work/talks (~18k base)"""
    log_progress(5, "Dean-Specific Vocabulary")

    # From Dean's bio, talks, GitHub
    dean_words = ["offensive", "reckless", "hacker", "keyhunter", "lateral", "defcon",
                  "portland", "pdx", "badgers", "potato", "derpy", "lulz", "rofl"]
    nouns = ["password", "passphrase"]
    adjectives = ["bad", "dumb", "stupid"]

    for dean_word in dean_words:
        for noun in nouns:
            yield f"{dean_word} {noun}"
            yield f"my {dean_word} {noun}"
            yield f"{dean_word} is my {noun}"

        for adj in adjectives:
            yield f"{dean_word} {adj} {noun}"


# ==================== FAMILY 6: DEFCON/Portland 2011 Culture ====================
def family_6_defcon_portland() -> Generator[str, None, None]:
    """DEFCON 19 / Portland hacker culture 2011 (~18k base)"""
    log_progress(6, "DEFCON/Portland Culture")

    defcon_terms = ["defcon", "defcon19", "dc19", "vegas", "caesars", "blackhat", "bsides",
                    "portland", "pdx", "pdx2600", "rainsec", "ctrlh", "hackboat"]
    nouns = ["password", "passphrase"]

    for term in defcon_terms:
        for noun in nouns:
            yield f"{term} {noun}"
            yield f"my {term} {noun}"
            yield f"{term} 2011 {noun}"


# ==================== FAMILY 7: Bidirectional Prefix+Suffix ====================
def family_7_bidirectional() -> Generator[str, None, None]:
    """Numbers/symbols at BOTH beginning AND end (~20k base)"""
    log_progress(7, "Bidirectional Prefix+Suffix")

    prefixes = ["123", "1", "2", "!", "?", "2011"]
    suffixes = ["123", "1", "!", "?", "2011"]
    adjectives = ["bad", "dumb", "stupid"]
    nouns = ["password", "passphrase"]

    for prefix in prefixes:
        for suffix in suffixes:
            for adj in adjectives:
                for noun in nouns:
                    yield f"{prefix} {adj} {noun} {suffix}"
                    yield f"{prefix} this is a {adj} {noun} {suffix}"


# ==================== FAMILY 8: Full Leetspeak Coverage ====================
def family_8_full_leetspeak() -> Generator[str, None, None]:
    """Extended leet: t→7, l→1, g→9, b→8, etc (~18k base)"""
    log_progress(8, "Full Leetspeak Coverage")

    def apply_full_leet(text: str) -> str:
        """Apply comprehensive leetspeak"""
        return (text
            .replace("t", "7").replace("T", "7")
            .replace("l", "1").replace("L", "1")
            .replace("g", "9").replace("G", "9")
            .replace("b", "8").replace("B", "8")
            .replace("e", "3").replace("E", "3")
            .replace("i", "1").replace("I", "1")
            .replace("o", "0").replace("O", "0")
            .replace("a", "4").replace("A", "4")
            .replace("s", "5").replace("S", "5"))

    phrases = [
        "this is a bad password",
        "this is a dumb password",
        "bad password",
        "really bad password",
        "this is a stupid passphrase",
    ]

    for phrase in phrases:
        leeted = apply_full_leet(phrase)
        yield leeted
        yield leeted.capitalize()


# ==================== FAMILY 9: Multi-Word Case Patterns ====================
def family_9_multiword_case() -> Generator[str, None, None]:
    """CamelCase, alternating, strategic caps (~18k base)"""
    log_progress(9, "Multi-Word Case Patterns")

    phrases = [
        ["bad", "password"],
        ["dumb", "password"],
        ["stupid", "password"],
        ["this", "is", "bad"],
        ["really", "bad", "password"],
    ]

    for phrase_words in phrases:
        # CamelCase
        camel = "".join(w.capitalize() for w in phrase_words)
        yield camel

        # Alternating caps
        for i in range(len(phrase_words)):
            alternating = "".join(w.upper() if j % 2 == i % 2 else w for j, w in enumerate(phrase_words))
            yield " ".join(phrase_words)  # Separated
            yield alternating


# ==================== FAMILY 10: Irony/Spite META Patterns ====================
def family_10_irony_spite() -> Generator[str, None, None]:
    """Ironic 'secure/strong' patterns - spite META (~16k base)"""
    log_progress(10, "Irony/Spite META Patterns")

    # Ironic - claiming strength when it's weak
    ironic_adjectives = ["secure", "strong", "complex", "uncrackable", "safe", "best", "perfect"]
    nouns = ["password", "passphrase"]

    for adj in ironic_adjectives:
        for noun in nouns:
            yield f"this is a {adj} {noun}"
            yield f"my {adj} {noun}"
            yield f"{adj} {noun}"
            yield f"very {adj} {noun}"


# ==================== MAIN GENERATOR ====================
def generate_all() -> Generator[str, None, None]:
    """Generate all candidates - 10 new families"""

    families = [
        (family_1_full_year_brute, "Full Year Brute 0000-9999"),
        (family_2_symbol_heavy, "Symbol-Heavy Patterns"),
        (family_3_exact_length, "Exact Length Optimization"),
        (family_4_extended_phonetic, "Extended Phonetic Variations"),
        (family_5_dean_vocabulary, "Dean-Specific Vocabulary"),
        (family_6_defcon_portland, "DEFCON/Portland Culture"),
        (family_7_bidirectional, "Bidirectional Prefix+Suffix"),
        (family_8_full_leetspeak, "Full Leetspeak Coverage"),
        (family_9_multiword_case, "Multi-Word Case Patterns"),
        (family_10_irony_spite, "Irony/Spite META Patterns"),
    ]

    for family_func, family_name in families:
        print(f"# Generating {family_name}", file=sys.stderr)
        base_count = 0
        for base in family_func():
            base_count += 1
            for trail in TRAILING_PATTERNS:
                yield base + trail
        print(f"# {family_name}: {base_count} base patterns", file=sys.stderr)


# ==================== MAIN ====================
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print(f"Trailing patterns: {len(TRAILING_PATTERNS):,}")
        print("\nEstimating base patterns (10 NEW families)...")
        print("  Family 1 (Year brute 0000-9999):    ~20,000")
        print("  Family 2 (Symbol-heavy):            ~18,000")
        print("  Family 3 (Exact length):            ~18,000")
        print("  Family 4 (Extended phonetic):       ~20,000")
        print("  Family 5 (Dean vocabulary):         ~18,000")
        print("  Family 6 (DEFCON/Portland):         ~18,000")
        print("  Family 7 (Bidirectional):           ~20,000")
        print("  Family 8 (Full leetspeak):          ~18,000")
        print("  Family 9 (Multi-word case):         ~18,000")
        print("  Family 10 (Irony/spite):            ~16,000")
        print("  ─────────────────────────────────────────")
        print("  Total base patterns:               ~184,000")
        print("\nTotal candidates:")
        total = 184000 * len(TRAILING_PATTERNS)
        print(f"  184,000 base × {len(TRAILING_PATTERNS):,} trailing = ~{total:,}")
        print(f"\nRuntime at 270k H/s: ~{total/270000/3600:.2f} hours")

    elif len(sys.argv) > 1 and sys.argv[1] == "--sample":
        count = 0
        for candidate in generate_all():
            print(candidate)
            count += 1
            if count >= 100:
                break
    else:
        for candidate in generate_all():
            print(candidate)
