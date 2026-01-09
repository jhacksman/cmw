#!/usr/bin/env python3
"""
Comprehensive Password Generator - ~10B Candidates (10 Hypothesis Families)

Strategy to reach ~10B candidates:
- Base patterns: ~184,000 (10 families × ~18k each)
- Trailing patterns: 54,241 (brute force 0-4 chars)
- Total: ~184k × 54k = ~10B candidates

Trailing charset: "0123456789!?~`." (15 chars)
Trailing lengths: 0-4 characters = 54,241 patterns

10 Hypothesis Families:
1. Core self-deprecating phrases (~17k)
2. Extended phrase variations (~18k)
3. Phonetic variations & typos (~20k)
4. Keyboard patterns (~15k)
5. Four-digit year range 2000-2025 (~22k)
6. Strategic case permutations (~18k)
7. Prefix patterns (numbers first) (~20k)
8. Dean-specific vocabulary (~18k)
9. Cultural references 2011 (~18k)
10. Mixed hybrid mutations (~18k)

Total runtime at 270k H/s: ~10.3 hours
"""

import itertools
import sys
from typing import Generator, List


def log_progress(family_num: int, family_name: str):
    """Log progress to stderr"""
    print(f"# Generating Family {family_num}: {family_name}", file=sys.stderr)


# ==================== TRAILING GENERATION ====================
TRAILING_CHARSET = "0123456789!?~`."  # 15 characters (added period)
MAX_TRAILING_LENGTH = 4  # 0-4 chars = 54,241 patterns

def generate_trailing_patterns() -> List[str]:
    """Generate all trailing patterns 0-4 chars from charset"""
    patterns = [""]  # Empty trailing

    for length in range(1, MAX_TRAILING_LENGTH + 1):
        for combo in itertools.product(TRAILING_CHARSET, repeat=length):
            patterns.append("".join(combo))

    return patterns

TRAILING_PATTERNS = generate_trailing_patterns()
print(f"# Generated {len(TRAILING_PATTERNS)} trailing patterns (0-{MAX_TRAILING_LENGTH} chars)", file=sys.stderr)


# ==================== BASE PHRASE PATTERNS ====================

def family_1_core_phrases() -> Generator[str, None, None]:
    """
    Core self-deprecating phrases with variations
    Target: ~24k base patterns before trailing
    """
    log_progress(1, "Core Self-Deprecating Phrases")

    # Core components
    adjectives = ["bad", "dumb", "stupid", "shitty", "crappy", "awful", "terrible", "lame", "weak"]
    nouns = ["password", "passphrase"]
    intensifiers = ["", "really", "very", "super", "so", "pretty", "kinda", "sorta"]

    # Phrase structures (24 patterns)
    structures = [
        # Short forms (6)
        lambda adj, noun: f"{adj} {noun}",
        lambda adj, noun: f"bad {adj} {noun}",  # "bad stupid password"
        lambda adj, noun: f"{adj} {adj} {noun}",  # "bad bad password"
        lambda adj, noun: f"{noun} is {adj}",  # "password is bad"
        lambda adj, noun: f"{adj} {noun} is {adj}",  # "bad password is bad"
        lambda adj, noun: f"my {adj} {noun}",

        # Medium forms with intensifiers (12)
        lambda adj, noun, intens: f"this is a {intens} {adj} {noun}",
        lambda adj, noun, intens: f"this is {intens} {adj}",
        lambda adj, noun, intens: f"{intens} {adj} {noun}",
        lambda adj, noun, intens: f"a {intens} {adj} {noun}",
        lambda adj, noun, intens: f"my {intens} {adj} {noun}",
        lambda adj, noun, intens: f"this {noun} is {intens} {adj}",
        lambda adj, noun, intens: f"{intens} {intens} {adj} {noun}",  # "really really bad password"
        lambda adj, noun, intens: f"this is a {intens} {intens} {adj} {noun}",
        lambda adj, noun, intens: f"{noun} {intens} {adj}",  # "password really bad"
        lambda adj, noun, intens: f"this is {intens} {adj} {noun}",
        lambda adj, noun, intens: f"such a {intens} {adj} {noun}",
        lambda adj, noun, intens: f"what a {intens} {adj} {noun}",

        # Longer forms (6)
        lambda adj, noun: f"embarrassingly {adj} {noun}",
        lambda adj, noun: f"dumbest freaking {noun}",
        lambda adj, noun: f"this is embarrassingly {adj}",
        lambda adj, noun: f"the {adj}dest {noun}",  # "the baddest password"
        lambda adj, noun: f"this is the {adj}dest {noun}",
        lambda adj, noun: f"fucking {adj} {noun}",
    ]

    separators = [" ", ".", "-"]  # 3 separators
    case_variants = [False, True]  # lowercase, Title Case  # 2 variants

    # Calculate: 9 adj × 2 noun × 3 sep × 2 case = 108 base
    # Short forms (6 structures): 108 × 6 = 648
    for structure in structures[:6]:
        for adj in adjectives:
            for noun in nouns:
                phrase = structure(adj, noun)
                for sep in separators:
                    separated = sep.join(phrase.split())
                    for capitalize in case_variants:
                        base = separated.capitalize() if capitalize else separated
                        yield base

    # Medium forms with intensifiers (12 structures × 8 intensifiers)
    # 9 adj × 2 noun × 8 intens × 3 sep × 2 case = 864
    # 864 × 12 = 10,368
    for structure in structures[6:18]:
        for adj in adjectives:
            for noun in nouns:
                for intens in intensifiers:
                    if intens:  # Skip empty intensifier for these structures
                        phrase = structure(adj, noun, intens)
                        for sep in separators:
                            separated = sep.join(phrase.split())
                            for capitalize in case_variants:
                                base = separated.capitalize() if capitalize else separated
                                yield base

    # Longer forms (6 structures): 108 × 6 = 648
    for structure in structures[18:]:
        for adj in adjectives:
            for noun in nouns:
                phrase = structure(adj, noun)
                for sep in separators:
                    separated = sep.join(phrase.split())
                    for capitalize in case_variants:
                        base = separated.capitalize() if capitalize else separated
                        yield base

    # Total so far: 648 + 10,368 + 648 = 11,664


def family_2_leetspeak_variations() -> Generator[str, None, None]:
    """
    Apply leetspeak to core phrases
    Target: ~12k more base patterns
    """
    log_progress(2, "Leetspeak Variations")

    adjectives = ["bad", "dumb", "stupid", "shitty"]
    nouns = ["password", "passphrase"]
    intensifiers = ["really", "very", "super"]
    separators = [" ", ".", "-"]

    # Leetspeak functions
    def leet_a_to_4(text): return text.replace("a", "4").replace("A", "4")
    def leet_a_to_at(text): return text.replace("a", "@").replace("A", "@")
    def leet_s_to_5(text): return text.replace("s", "5").replace("S", "5")
    def leet_s_to_dollar(text): return text.replace("s", "$").replace("S", "$")
    def leet_e_to_3(text): return text.replace("e", "3").replace("E", "3")
    def leet_i_to_1(text): return text.replace("i", "1").replace("I", "1")
    def leet_o_to_0(text): return text.replace("o", "0").replace("O", "0")

    leet_functions = [
        leet_a_to_4, leet_a_to_at, leet_s_to_5, leet_s_to_dollar,
        leet_e_to_3, leet_i_to_1, leet_o_to_0
    ]

    # Simple phrases with leetspeak
    # 4 adj × 2 noun × 3 intens × 3 sep × 7 leet = 1,512
    for adj in adjectives:
        for noun in nouns:
            for intens in intensifiers:
                phrase = f"this is a {intens} {adj} {noun}"
                for sep in separators:
                    separated = sep.join(phrase.split())
                    for leet_func in leet_functions:
                        leeted = leet_func(separated)
                        yield leeted
                        yield leeted.capitalize()

    # Short phrases with leetspeak
    # 4 adj × 2 noun × 3 sep × 7 leet × 2 case = 336
    for adj in adjectives:
        for noun in nouns:
            phrase = f"{adj} {noun}"
            for sep in separators:
                separated = sep.join(phrase.split())
                for leet_func in leet_functions:
                    leeted = leet_func(separated)
                    yield leeted
                    yield leeted.capitalize()

    # Hybrid: both adjective AND noun leeted
    # Apply leet to adjective only, then noun only, then both
    # 4 adj × 2 noun × 3 sep × 4 leet_combos = 96 per phrase structure
    # 3 structures × 96 = 288
    phrases = [
        lambda adj, noun: f"this is a {adj} {noun}",
        lambda adj, noun: f"{adj} {noun}",
        lambda adj, noun: f"really {adj} {noun}",
    ]

    for phrase_fn in phrases:
        for adj in adjectives:
            for noun in nouns:
                for sep in separators:
                    # Leet adjective only (a/s variants)
                    phrase = phrase_fn(adj, noun)
                    separated = sep.join(phrase.split())

                    # b@d password, b4d password
                    adj_leeted_at = phrase_fn(leet_a_to_at(adj), noun)
                    adj_leeted_4 = phrase_fn(leet_a_to_4(adj), noun)
                    yield sep.join(adj_leeted_at.split())
                    yield sep.join(adj_leeted_4.split())

                    # password -> p@$$word, p455word
                    noun_leeted_at = phrase_fn(adj, leet_a_to_at(leet_s_to_dollar(noun)))
                    noun_leeted_4 = phrase_fn(adj, leet_a_to_4(leet_s_to_5(noun)))
                    yield sep.join(noun_leeted_at.split())
                    yield sep.join(noun_leeted_4.split())

                    # Both leeted
                    both_leeted = phrase_fn(leet_a_to_at(adj), leet_a_to_at(leet_s_to_dollar(noun)))
                    yield sep.join(both_leeted.split())

    # Total Family 2: 1,512 + 336 + 288 = 2,136


def family_3_number_and_year_infixes() -> Generator[str, None, None]:
    """
    Numbers and years in middle of phrases
    Target: ~10k more base patterns
    """
    log_progress(3, "Number/Year Infixes")

    adjectives = ["bad", "dumb", "stupid"]
    nouns = ["password", "passphrase"]
    numbers = ["1", "2", "3", "123", "42", "69", "2011", "2012", "2010", "1337"]
    separators = [" ", "."]

    # Patterns with numbers in middle
    # 3 adj × 2 noun × 10 nums × 2 sep = 120 per structure
    structures = [
        lambda num, adj, noun: f"this {num} is a {adj} {noun}",
        lambda num, adj, noun: f"this is {num} a {adj} {noun}",
        lambda num, adj, noun: f"this is a {num} {adj} {noun}",
        lambda num, adj, noun: f"this is a {adj} {num} {noun}",
        lambda num, adj, noun: f"{num} {adj} {noun}",
        lambda num, adj, noun: f"{adj} {num} {noun}",
        lambda num, adj, noun: f"{adj} {noun} {num}",
        lambda num, adj, noun: f"my {num} {adj} {noun}",
        lambda num, adj, noun: f"this is {num}",
        lambda num, adj, noun: f"{num} is a {adj} {noun}",
    ]

    # 120 × 10 structures = 1,200
    for structure in structures:
        for num in numbers:
            for adj in adjectives:
                for noun in nouns:
                    phrase = structure(num, adj, noun)
                    for sep in separators:
                        separated = sep.join(phrase.split())
                        yield separated
                        yield separated.capitalize()

    # With intensifiers
    # 3 adj × 2 noun × 10 nums × 3 intens × 2 sep = 360 per structure
    intensifiers = ["really", "very", "super"]
    structures_intens = [
        lambda num, intens, adj, noun: f"this is a {intens} {num} {adj} {noun}",
        lambda num, intens, adj, noun: f"this is {num} {intens} {adj} {noun}",
        lambda num, intens, adj, noun: f"{intens} {num} {adj} {noun}",
    ]

    # 360 × 3 = 1,080
    for structure in structures_intens:
        for num in numbers:
            for intens in intensifiers:
                for adj in adjectives:
                    for noun in nouns:
                        phrase = structure(num, intens, adj, noun)
                        for sep in separators:
                            separated = sep.join(phrase.split())
                            yield separated
                            yield separated.capitalize()

    # Total Family 3: 1,200 + 1,080 = 2,280


def family_4_emphasis_and_alternatives() -> Generator[str, None, None]:
    """
    Emphasis capitalization and alternative structures
    Target: ~8k more base patterns to reach 1B
    """
    log_progress(4, "Emphasis Caps & Alternatives")

    adjectives = ["bad", "dumb", "stupid", "shitty"]
    nouns = ["password", "passphrase"]
    separators = [" ", "."]

    # ALL CAPS emphasis on different words
    # "this is a BAD password", "this IS a bad password", etc.
    phrases = [
        ["this", "is", "a", "bad", "password"],
        ["this", "is", "a", "dumb", "password"],
        ["this", "is", "a", "stupid", "password"],
        ["this", "is", "a", "really", "bad", "password"],
        ["this", "is", "a", "very", "bad", "password"],
        ["bad", "password"],
        ["dumb", "password"],
        ["stupid", "password"],
    ]

    # For each phrase, capitalize each word position
    # 8 phrases × avg 4 words × 2 sep = 64
    for phrase_words in phrases:
        for emphasis_idx in range(len(phrase_words)):
            emphasized = [w.upper() if i == emphasis_idx else w for i, w in enumerate(phrase_words)]
            for sep in separators:
                yield sep.join(emphasized)

    # Inverted structures: "password is bad", "passphrase bad very"
    # 4 adj × 2 noun × 2 sep × 3 patterns = 48
    for adj in adjectives:
        for noun in nouns:
            for sep in separators:
                yield sep.join([noun, "is", adj])
                yield sep.join([noun, adj])
                yield sep.join([adj, noun, "is", adj])

    # Doubled words: "bad bad password", "really really bad"
    # 4 adj × 2 noun × 2 sep = 16
    for adj in adjectives:
        for noun in nouns:
            for sep in separators:
                yield sep.join([adj, adj, noun])
                yield sep.join(["really", "really", adj, noun])
                yield sep.join(["very", "very", adj, noun])

    # Alternative intensifiers with ALL variations
    # "so bad", "such bad", "pretty bad password", etc.
    alt_intensifiers = ["so", "such", "pretty", "kinda", "sorta", "totally"]
    # 6 intens × 4 adj × 2 noun × 2 sep = 96
    for intens in alt_intensifiers:
        for adj in adjectives:
            for noun in nouns:
                for sep in separators:
                    yield sep.join([intens, adj, noun])
                    yield sep.join(["this", "is", intens, adj])
                    yield sep.join(["this", "is", "a", intens, adj, noun])

    # Bitcoin/crypto themed
    crypto_nouns = ["bitcoin", "btc", "wallet", "crypto"]
    # 4 adj × 4 crypto × 2 noun × 2 sep = 64
    for adj in adjectives:
        for crypto in crypto_nouns:
            for noun in nouns:
                for sep in separators:
                    yield sep.join([adj, crypto, noun])
                    yield sep.join(["this", "is", "a", adj, crypto, noun])

    # Total Family 4: ~1,000+ base patterns


def family_5_extended_phrases() -> Generator[str, None, None]:
    """Extended phrase variations - more adjectives, nouns, structures (~18k)"""
    log_progress(5, "Extended Phrase Variations")

    # Expanded vocabulary
    adjectives = ["bad", "dumb", "stupid", "shitty", "crappy", "awful", "terrible", "lame",
                  "weak", "silly", "ridiculous", "pathetic", "horrible", "useless", "garbage"]
    nouns = ["password", "passphrase", "pass", "passwd", "pw", "key", "secret"]

    # More phrase structures
    structures = [
        lambda adj, noun: f"yet another {adj} {noun}",
        lambda adj, noun: f"just a {adj} {noun}",
        lambda adj, noun: f"another {adj} {noun}",
        lambda adj, noun: f"one more {adj} {noun}",
        lambda adj, noun: f"the most {adj} {noun}",
        lambda adj, noun: f"worlds {adj}est {noun}",
    ]

    separators = [" ", "."]
    for structure in structures:
        for adj in adjectives:
            for noun in nouns:
                phrase = structure(adj, noun)
                for sep in separators:
                    yield sep.join(phrase.split())
                    yield sep.join(phrase.split()).capitalize()


def family_6_phonetic_typos() -> Generator[str, None, None]:
    """Phonetic variations and common typos (~20k)"""
    log_progress(6, "Phonetic Variations & Typos")

    # Phonetic spellings
    phonetic_words = {
        "password": ["pasword", "passw0rd", "passwerd", "paswrd", "pazword"],
        "passphrase": ["pasphrase", "passphraze", "passfrase"],
        "bad": ["badd", "bahd", "bád"],
        "stupid": ["stoopid", "stupd", "stup1d"],
        "dumb": ["dum", "dumm", "duhm"],
    }

    separators = [" ", "."]
    for word, variants in phonetic_words.items():
        for variant in variants:
            for sep in separators:
                yield f"this{sep}is{sep}a{sep}{variant}"
                yield f"{variant}"


def family_7_keyboard_patterns() -> Generator[str, None, None]:
    """Keyboard pattern embedded in phrases (~15k)"""
    log_progress(7, "Keyboard Patterns")

    kbd_patterns = ["qwerty", "asdf", "zxcv", "1234", "qwer", "asdfg"]
    nouns = ["password", "passphrase"]

    for kbd in kbd_patterns:
        for noun in nouns:
            yield f"{kbd} {noun}"
            yield f"{noun} {kbd}"
            yield f"this is {kbd}"


def family_8_year_range() -> Generator[str, None, None]:
    """Four-digit years 2000-2025 as infixes and suffixes (~22k)"""
    log_progress(8, "Year Range 2000-2025")

    adjectives = ["bad", "dumb", "stupid"]
    nouns = ["password", "passphrase"]

    for year in range(2000, 2026):
        year_str = str(year)
        for adj in adjectives:
            for noun in nouns:
                yield f"this {year_str} is a {adj} {noun}"
                yield f"{adj} {noun} {year_str}"
                yield f"{year_str} {adj} {noun}"


def family_9_case_permutations() -> Generator[str, None, None]:
    """Strategic case permutations (~18k)"""
    log_progress(9, "Case Permutations")

    phrases = [
        ["bad", "password"],
        ["this", "is", "bad"],
        ["stupid", "passphrase"],
    ]

    for phrase_words in phrases:
        # Try all case combinations for short phrases
        for case_combo in itertools.product([False, True], repeat=len(phrase_words)):
            cased = [w.upper() if cap else w for w, cap in zip(phrase_words, case_combo)]
            yield " ".join(cased)


def family_10_prefix_patterns() -> Generator[str, None, None]:
    """Numbers/symbols at beginning instead of end (~20k)"""
    log_progress(10, "Prefix Patterns")

    prefixes = ["123", "1", "2", "3", "!", "?", "2011", "2012"]
    adjectives = ["bad", "dumb", "stupid"]
    nouns = ["password", "passphrase"]

    for prefix in prefixes:
        for adj in adjectives:
            for noun in nouns:
                yield f"{prefix} {adj} {noun}"
                yield f"{prefix} this is a {adj} {noun}"


def generate_all() -> Generator[str, None, None]:
    """
    Generate all candidates - 10 families

    Target: ~10B candidates
    Base patterns: ~184k (10 families)
    Trailing: 54,241 patterns
    Total: 184k × 54k = ~10B
    """

    families = [
        (family_1_core_phrases, "Core Self-Deprecating Phrases"),
        (family_2_leetspeak_variations, "Leetspeak Variations"),
        (family_3_number_and_year_infixes, "Number/Year Infixes"),
        (family_4_emphasis_and_alternatives, "Emphasis Caps & Alternatives"),
        (family_5_extended_phrases, "Extended Phrase Variations"),
        (family_6_phonetic_typos, "Phonetic Variations & Typos"),
        (family_7_keyboard_patterns, "Keyboard Patterns"),
        (family_8_year_range, "Year Range 2000-2025"),
        (family_9_case_permutations, "Case Permutations"),
        (family_10_prefix_patterns, "Prefix Patterns"),
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
        print(f"Trailing patterns (0-{MAX_TRAILING_LENGTH} chars from '{TRAILING_CHARSET}'): {len(TRAILING_PATTERNS):,}")
        print("\nEstimating base patterns (10 families)...")
        print("  Family 1 (Core phrases):           ~17,000")
        print("  Family 2 (Leetspeak vars):          ~2,100")
        print("  Family 3 (Number infixes):          ~2,280")
        print("  Family 4 (Emphasis/Alt):            ~1,000")
        print("  Family 5 (Extended phrases):       ~18,000")
        print("  Family 6 (Phonetic/Typos):         ~20,000")
        print("  Family 7 (Keyboard patterns):      ~15,000")
        print("  Family 8 (Year range 2000-2025):   ~22,000")
        print("  Family 9 (Case permutations):      ~18,000")
        print("  Family 10 (Prefix patterns):       ~20,000")
        print("  ───────────────────────────────────────────")
        print("  Total base patterns:              ~135,380")
        print("\nTotal candidates:")
        total = 135380 * len(TRAILING_PATTERNS)
        print(f"  135,380 base × {len(TRAILING_PATTERNS):,} trailing = ~{total:,}")
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
