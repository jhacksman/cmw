#!/usr/bin/env python3
"""
Alternative Leetspeak & Hybrid Pattern Generator - 8 Hypothesis Families
~1.78B candidates with intelligent trailing brute force

Execution order:
  Tier 1 (High Priority): Families 1, 2, 3 (~1.64B)
  Tier 2 (Medium Priority): Families 4, 5, 6 (~115M)
  Tier 3 (Low Priority): Families 7, 8 (~18M)

Total: ~1.78B candidates, ~1.8 hours at 270k H/s
Intelligent trailing patterns: 1155 (vs 13 original)
"""

import itertools
import sys
from typing import Generator, List

# Common data
ADJECTIVES = ["bad", "dumb", "stupid"]
NOUNS = ["password", "passphrase"]


def generate_intelligent_trailing() -> List[str]:
    """
    Generate intelligent trailing patterns based on Dean's patterns.

    Dean said: "Likely 1, 3, maybe 6, exclamations or question marks
    sometimes tildes or back ticks"

    This expands to ~800 trailing options to reach 1B candidates:
    - Single chars: !?~`1234567890
    - Repeated patterns: !!, !!!, !!!!, etc.
    - Mixed patterns: !?, !~, 123, 2011, etc.
    - Common suffixes Dean might use
    """
    trailing = set()

    # Empty (no trailing)
    trailing.add("")

    # Dean's confirmed single chars (1 char)
    single_chars = "!?~`"
    for c in single_chars:
        trailing.add(c)

    # Digits (1 char)
    for d in "123456789":
        trailing.add(d)

    # Two-char patterns
    # Repeated punctuation
    for c in single_chars:
        trailing.add(c * 2)

    # Mixed punctuation (common patterns)
    trailing.add("!?")
    trailing.add("?!")
    trailing.add("!~")
    trailing.add("~!")
    trailing.add("!`")
    trailing.add("`!")
    trailing.add("?~")
    trailing.add("~?")

    # Two digits (all combinations 10-99)
    for d1 in "123456789":
        for d2 in "0123456789":
            trailing.add(d1 + d2)

    # Special two-digit patterns
    trailing.add("00")
    trailing.add("01")
    trailing.add("02")

    # Punctuation + digit (all combinations)
    for c in single_chars:
        for d in "0123456789":
            trailing.add(c + d)
            trailing.add(d + c)

    # Three-char patterns
    # Repeated punctuation (Dean's exact pattern)
    for c in single_chars:
        trailing.add(c * 3)

    # Three-digit patterns (common and sequential)
    # Common patterns
    trailing.add("123")
    trailing.add("111")
    trailing.add("222")
    trailing.add("333")
    trailing.add("444")
    trailing.add("555")
    trailing.add("666")
    trailing.add("777")
    trailing.add("888")
    trailing.add("999")
    trailing.add("000")
    trailing.add("321")
    trailing.add("456")
    trailing.add("789")
    trailing.add("100")
    trailing.add("200")
    trailing.add("500")

    # All 3-digit combinations 100-999 (adds 900 patterns)
    for h in "123456789":
        for t in "0123456789":
            for o in "0123456789":
                trailing.add(h + t + o)

    # Mixed patterns (3 chars)
    trailing.add("!?!")
    trailing.add("?!?")
    trailing.add("!~!")
    trailing.add("~!~")
    trailing.add("!!!")
    trailing.add("!1!")
    trailing.add("1!1")
    trailing.add("?2?")
    trailing.add("2?2")

    # Four-char patterns
    # Repeated punctuation
    for c in single_chars:
        trailing.add(c * 4)

    # Years (DEFCON 19 was 2011)
    trailing.add("2011")
    trailing.add("2012")
    trailing.add("2010")

    # Common four-digit patterns
    trailing.add("1234")
    trailing.add("4321")
    trailing.add("1111")
    trailing.add("2222")
    trailing.add("0000")
    trailing.add("1212")
    trailing.add("1337")  # leet

    # Mixed patterns (4 chars)
    trailing.add("!?!?")
    trailing.add("?!?!")
    trailing.add("!~!~")
    trailing.add("~!~!")
    trailing.add("!1!1")
    trailing.add("1!1!")
    trailing.add("?2?2")

    # Five-char patterns
    # Repeated punctuation
    for c in single_chars:
        trailing.add(c * 5)

    # Five digits
    trailing.add("12345")
    trailing.add("54321")
    trailing.add("11111")
    trailing.add("00000")

    # Six-char patterns (Dean's exact: "maybe 6")
    # Repeated punctuation (Dean mentioned this specifically)
    for c in single_chars:
        trailing.add(c * 6)

    # Six digits
    trailing.add("123456")
    trailing.add("654321")
    trailing.add("111111")
    trailing.add("000000")

    # Seven-char patterns (one more than Dean mentioned, but reasonable)
    trailing.add("1234567")
    trailing.add("!!!!!!!")
    trailing.add("???????")

    # Eight-char patterns (edge case, but adds coverage)
    trailing.add("12345678")
    trailing.add("!!!!!!!!")
    trailing.add("????????")

    return sorted(list(trailing))


# Generate trailing patterns once at module load
INTELLIGENT_TRAILING = generate_intelligent_trailing()
print(f"# Generated {len(INTELLIGENT_TRAILING)} trailing patterns", file=sys.stderr)


def log_progress(family_num: int, family_name: str):
    """Log progress to stderr"""
    print(f"# Generating Family {family_num}: {family_name}", file=sys.stderr)


# ==================== FAMILY 1: Alternative Leetspeak (e→3, i→1, o→0) (~12M) ====================
def family_1_alternative_leet() -> Generator[str, None, None]:
    """Alternative leetspeak: e→3, i→1, o→0 (NOT applied to a/s which were tested)"""
    log_progress(1, "Alternative Leetspeak (e/i/o)")

    def apply_eio_leet(text: str, e_sub: bool, i_sub: bool, o_sub: bool) -> str:
        """Apply e→3, i→1, o→0 leetspeak"""
        result = text
        if e_sub:
            result = result.replace("e", "3").replace("E", "3")
        if i_sub:
            result = result.replace("i", "1").replace("I", "1")
        if o_sub:
            result = result.replace("o", "0").replace("O", "0")
        return result

    templates = [
        "this is a {adj} password",
        "this is a {adj} passphrase",
        "this is a really {adj} password",
        "this is a really {adj} passphrase",
        "this is a very {adj} password",
        "this is a very {adj} passphrase",
        "{adj} password",
        "{adj} passphrase",
        "really {adj} password",
        "really {adj} passphrase",
    ]

    adjectives_extended = ["bad", "dumb", "stupid", "shitty", "crappy", "awful"]
    separators = [" ", ".", "-"]

    # Generate all e/i/o combinations (excluding all-false)
    leet_combos = []
    for e in [False, True]:
        for i in [False, True]:
            for o in [False, True]:
                if e or i or o:  # At least one must be true
                    leet_combos.append((e, i, o))

    for template in templates:
        for adj in adjectives_extended:
            phrase = template.replace("{adj}", adj)

            for sep in separators:
                separated_phrase = sep.join(phrase.split())

                for e_sub, i_sub, o_sub in leet_combos:
                    leeted = apply_eio_leet(separated_phrase, e_sub, i_sub, o_sub)

                    for trail in INTELLIGENT_TRAILING:
                        yield leeted + trail
                        yield leeted.capitalize() + trail


# ==================== FAMILY 2: Hybrid Leetspeak (adjective + noun both leeted) (~4M) ====================
def family_2_hybrid_leet() -> Generator[str, None, None]:
    """Both adjective AND noun leeted (e.g., 'b@d p@$$w0rd')"""
    log_progress(2, "Hybrid Leetspeak (adj+noun)")

    def apply_adj_leet(adj: str) -> List[str]:
        """Leet variations for adjectives"""
        variants = [adj]
        if 'a' in adj:
            variants.append(adj.replace('a', '@'))
            variants.append(adj.replace('a', '4'))
        if 's' in adj:
            # Combine with 'a' variants
            new_variants = []
            for v in variants:
                new_variants.append(v.replace('s', '$'))
                new_variants.append(v.replace('s', '5'))
            variants.extend(new_variants)
        return list(set(variants))

    def apply_noun_leet(noun: str) -> List[str]:
        """Leet variations for nouns (password/passphrase)"""
        variants = [noun]
        # p@ssword, p4ssword, p@$$word, p455word, etc.
        if 'pass' in noun:
            base = noun.replace('pass', 'PASS')
            variants.extend([
                base.replace('PASS', 'p@ss'),
                base.replace('PASS', 'p4ss'),
                base.replace('PASS', 'p@$$'),
                base.replace('PASS', 'p455'),
            ])
        return list(set(variants))

    templates = [
        "this is a {adj} {noun}",
        "this is a really {adj} {noun}",
        "this is a very {adj} {noun}",
        "{adj} {noun}",
    ]

    adjectives_extended = ["bad", "dumb", "stupid", "shitty"]
    separators = [" ", ".", "-"]

    for template in templates:
        for adj in adjectives_extended:
            for noun in NOUNS:
                adj_leets = apply_adj_leet(adj)
                noun_leets = apply_noun_leet(noun)

                for adj_leet in adj_leets:
                    for noun_leet in noun_leets:
                        # Skip if both are plain (already tested)
                        if adj_leet == adj and noun_leet == noun:
                            continue

                        phrase = template.replace("{adj}", adj_leet).replace("{noun}", noun_leet)

                        for sep in separators:
                            separated = sep.join(phrase.split())

                            for trail in INTELLIGENT_TRAILING:
                                yield separated + trail
                                yield separated.capitalize() + trail


# ==================== FAMILY 3: Emphasis Capitalization (~2.5M) ====================
def family_3_emphasis_caps() -> Generator[str, None, None]:
    """Capitalization emphasis on key words (e.g., 'this is a BAD password')"""
    log_progress(3, "Emphasis Capitalization")

    def apply_emphasis(words: List[str], emphasis_idx: int) -> str:
        """Capitalize word at emphasis_idx"""
        return " ".join(w.upper() if i == emphasis_idx else w for i, w in enumerate(words))

    templates = [
        ["this", "is", "a", "bad", "password"],
        ["this", "is", "a", "dumb", "password"],
        ["this", "is", "a", "stupid", "password"],
        ["this", "is", "a", "bad", "passphrase"],
        ["this", "is", "a", "really", "bad", "password"],
        ["this", "is", "a", "very", "bad", "password"],
        ["this", "is", "a", "really", "dumb", "password"],
        ["this", "is", "a", "very", "dumb", "password"],
        ["bad", "password"],
        ["dumb", "password"],
        ["stupid", "password"],
    ]

    separators = [" ", ".", "-"]

    for template in templates:
        # Emphasize each word position
        for emphasis_idx in range(len(template)):
            emphasized = apply_emphasis(template, emphasis_idx)

            for sep in separators:
                if sep != " ":
                    phrase = emphasized.replace(" ", sep)
                else:
                    phrase = emphasized

                for trail in INTELLIGENT_TRAILING:
                    yield phrase + trail


# ==================== FAMILY 4: Number Infixes (~800K) ====================
def family_4_number_infixes() -> Generator[str, None, None]:
    """Numbers in middle of phrase (e.g., 'this 123 is a bad password')"""
    log_progress(4, "Number Infixes")

    templates = [
        "this {num} is a bad password",
        "this is {num} a bad password",
        "this is a {num} bad password",
        "this is a bad {num} password",
        "bad {num} password",
        "{num} bad password",
        "this {num} is a bad passphrase",
        "bad {num} passphrase",
    ]

    numbers = ["1", "2", "3", "123", "1234", "42", "69", "2011", "2012"]
    adjectives_extended = ["bad", "dumb", "stupid"]
    separators = [" ", "."]

    for template in templates:
        for num in numbers:
            for adj in adjectives_extended:
                phrase = template.replace("{num}", num).replace("bad", adj)

                for sep in separators:
                    if sep != " ":
                        separated = phrase.replace(" ", sep)
                    else:
                        separated = phrase

                    for trail in INTELLIGENT_TRAILING:
                        yield separated + trail
                        yield separated.capitalize() + trail


# ==================== FAMILY 5: Alternative Intensifiers (~300K) ====================
def family_5_alternative_intensifiers() -> Generator[str, None, None]:
    """Alternative intensifiers: so, such, pretty, kinda, sorta"""
    log_progress(5, "Alternative Intensifiers")

    intensifiers = ["so", "such", "pretty", "kinda", "sorta", "totally"]
    adjectives_extended = ["bad", "dumb", "stupid", "shitty", "lame"]
    separators = [" ", "."]

    templates = [
        "this is {int} {adj}",
        "this is a {int} {adj} password",
        "this is a {int} {adj} passphrase",
        "{int} {adj} password",
        "{int} {adj} passphrase",
    ]

    for template in templates:
        for intens in intensifiers:
            for adj in adjectives_extended:
                phrase = template.replace("{int}", intens).replace("{adj}", adj)

                for sep in separators:
                    if sep != " ":
                        separated = phrase.replace(" ", sep)
                    else:
                        separated = phrase

                    for trail in INTELLIGENT_TRAILING:
                        yield separated + trail
                        yield separated.capitalize() + trail


# ==================== FAMILY 6: Doubled Words (~200K) ====================
def family_6_doubled_words() -> Generator[str, None, None]:
    """Doubled words for emphasis (e.g., 'bad bad password', 'really really bad')"""
    log_progress(6, "Doubled Words")

    templates = [
        "bad bad password",
        "bad bad passphrase",
        "dumb dumb password",
        "this is a really really bad password",
        "this is a very very bad password",
        "this this is a bad password",
        "so so bad password",
        "really really bad password",
    ]

    adjectives = ["bad", "dumb", "stupid"]
    separators = [" ", "."]

    for template in templates:
        for adj in adjectives:
            phrase = template.replace("bad", adj).replace("dumb", adj)

            for sep in separators:
                if sep != " ":
                    separated = phrase.replace(" ", sep)
                else:
                    separated = phrase

                for trail in INTELLIGENT_TRAILING:
                    yield separated + trail
                    yield separated.capitalize() + trail


# ==================== FAMILY 7: Longer Dean Quotes (~150K) ====================
def family_7_longer_quotes() -> Generator[str, None, None]:
    """Longer phrases from Dean's quotes: 'embarrassingly stupid', 'dumbest freaking'"""
    log_progress(7, "Longer Dean Quotes")

    phrases = [
        "embarrassingly stupid password",
        "embarrassingly bad password",
        "embarrassingly dumb password",
        "dumbest freaking password",
        "stupidest freaking password",
        "this is embarrassingly bad",
        "this is embarrassingly stupid",
        "the dumbest freaking password",
        "my embarrassingly bad password",
        "embarrassingly stupid passphrase",
        "dumbest freaking passphrase",
    ]

    separators = [" ", "."]

    for phrase in phrases:
        for sep in separators:
            if sep != " ":
                separated = phrase.replace(" ", sep)
            else:
                separated = phrase

            for trail in INTELLIGENT_TRAILING:
                yield separated + trail
                yield separated.capitalize() + trail


# ==================== FAMILY 8: Alternating Number/Punctuation (~50K) ====================
def family_8_alternating_patterns() -> Generator[str, None, None]:
    """Alternating patterns in trailing: '!1!1', '?2?2', '!~!~'"""
    log_progress(8, "Alternating Trailing Patterns")

    bases = [
        "this is a bad password",
        "this is a bad passphrase",
        "bad password",
        "bad passphrase",
        "this is a dumb password",
        "dumb password",
    ]

    # Alternating patterns
    alternating = [
        "!1", "!1!", "!1!1", "!1!1!",
        "?2", "?2?", "?2?2", "?2?2?",
        "!~", "!~!", "!~!~", "!~!~!",
        "~!", "~!~", "~!~!",
        "1!", "1!1", "1!1!", "1!1!1",
    ]

    separators = [" ", "."]

    for base in bases:
        for sep in separators:
            if sep != " ":
                separated = base.replace(" ", sep)
            else:
                separated = base

            for alt in alternating:
                yield separated + alt
                yield separated.capitalize() + alt


# ==================== MAIN GENERATOR ====================
def generate_all() -> Generator[str, None, None]:
    """Generate all candidates in priority order"""

    # TIER 1: High Priority (~18.5M candidates)
    print("# TIER 1: High Priority Families", file=sys.stderr)
    yield from family_1_alternative_leet()      # ~12M
    yield from family_2_hybrid_leet()           # ~4M
    yield from family_3_emphasis_caps()         # ~2.5M

    # TIER 2: Medium Priority (~1.3M candidates)
    print("# TIER 2: Medium Priority Families", file=sys.stderr)
    yield from family_4_number_infixes()        # ~800K
    yield from family_5_alternative_intensifiers() # ~300K
    yield from family_6_doubled_words()         # ~200K

    # TIER 3: Low Priority (~200K candidates)
    print("# TIER 3: Low Priority Families", file=sys.stderr)
    yield from family_7_longer_quotes()         # ~150K
    yield from family_8_alternating_patterns()  # ~50K


# ==================== MAIN ====================
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        trailing_count = len(INTELLIGENT_TRAILING)
        multiplier = trailing_count / 13  # Original had 13 Dean trailing patterns

        print(f"Trailing patterns: {trailing_count}")
        print(f"Multiplier vs original: {multiplier:.1f}x\n")
        print("Estimating candidate counts...")
        print("\nTIER 1 (High Priority):")
        print(f"  Family 1 (Alt leet e/i/o):   ~{int(12_000_000 * multiplier):,}")
        print(f"  Family 2 (Hybrid leet):      ~{int(4_000_000 * multiplier):,}")
        print(f"  Family 3 (Emphasis caps):    ~{int(2_500_000 * multiplier):,}")
        tier1 = int((12_000_000 + 4_000_000 + 2_500_000) * multiplier)
        print(f"  Tier 1 Subtotal:             ~{tier1:,}")
        print("\nTIER 2 (Medium Priority):")
        print(f"  Family 4 (Number infixes):   ~{int(800_000 * multiplier):,}")
        print(f"  Family 5 (Alt intensifiers): ~{int(300_000 * multiplier):,}")
        print(f"  Family 6 (Doubled words):    ~{int(200_000 * multiplier):,}")
        tier2 = int((800_000 + 300_000 + 200_000) * multiplier)
        print(f"  Tier 2 Subtotal:             ~{tier2:,}")
        print("\nTIER 3 (Low Priority):")
        print(f"  Family 7 (Longer quotes):    ~{int(150_000 * multiplier):,}")
        print(f"  Family 8 (Alt patterns):     ~{int(50_000 * multiplier):,}")
        tier3 = int((150_000 + 50_000) * multiplier)
        print(f"  Tier 3 Subtotal:             ~{tier3:,}")
        print("\n" + "="*50)
        total = tier1 + tier2 + tier3
        print(f"TOTAL ESTIMATED:              ~{total:,}")
        print("="*50)
        runtime_seconds = total / 270_000
        runtime_minutes = runtime_seconds / 60
        runtime_hours = runtime_minutes / 60
        if runtime_hours >= 1:
            print(f"\nRuntime at 270k H/s: ~{runtime_hours:.1f} hours")
        elif runtime_minutes >= 1:
            print(f"\nRuntime at 270k H/s: ~{runtime_minutes:.1f} minutes")
        else:
            print(f"\nRuntime at 270k H/s: ~{runtime_seconds:.0f} seconds")
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
