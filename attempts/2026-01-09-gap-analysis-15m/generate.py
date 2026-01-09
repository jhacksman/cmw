#!/usr/bin/env python3
"""
Gap Analysis Combined Generator - 10 Hypothesis Families
~15.2M candidates addressing systematic gaps in tested search space

Execution order:
  Tier 1 (High Priority): Families 1, 3, 2, 4 (~14.9M, ~1.5 min)
  Tier 2 (Medium Priority): Families 5, 7, 6, 8 (~281K, ~1 min)
  Tier 3 (Low Priority): Families 9, 10 (~4K, <1 sec)

Total: ~15.2M candidates, ~3 minutes at 270k H/s
"""

import itertools
import sys
from typing import Generator, List

# Dean's exact trailing pattern: 0, 1, 3, or 6 of SAME char
DEAN_TRAILING = [""] + ["!", "?", "~", "`"] + ["!!!", "???", "~~~", "```"] + ["!!!!!!", "??????", "~~~~~~", "``````"]

# Common data
ADJECTIVES = ["bad", "dumb", "stupid"]
NOUNS = ["password", "passphrase"]


def log_progress(family_num: int, family_name: str):
    """Log progress to stderr"""
    print(f"# Generating Family {family_num}: {family_name}", file=sys.stderr)


# ==================== FAMILY 1: Dash-Separated Phrases (~75K) ====================
def family_1_dash_separated() -> Generator[str, None, None]:
    """Dash-separated multi-word phrases - Dean said 'rarely dashes'"""
    log_progress(1, "Dash-Separated Phrases")

    starters = ["this", "that", "it", "what", "here", "my"]
    connectors = ["is", "was"]
    articles = ["a", "the", "one", "my"]
    intensifiers = ["really", "very", "super"]

    for starter in starters:
        for conn in connectors:
            for art in articles:
                # No intensifier
                for adj in ADJECTIVES:
                    for noun in NOUNS:
                        phrase = f"{starter}-{conn}-{art}-{adj}-{noun}"
                        for trail in DEAN_TRAILING:
                            yield phrase + trail
                            yield phrase.capitalize() + trail

                # 1-3 intensifiers
                for count in range(1, 4):
                    for intens in intensifiers:
                        intens_part = "-".join([intens] * count)
                        for adj in ADJECTIVES:
                            for noun in NOUNS:
                                phrase = f"{starter}-{conn}-{art}-{intens_part}-{adj}-{noun}"
                                for trail in DEAN_TRAILING:
                                    yield phrase + trail
                                    yield phrase.capitalize() + trail


# ==================== FAMILY 3: Leetspeak on Adjectives Only (~14.7M) ====================
def family_3_adjective_leet() -> Generator[str, None, None]:
    """Leetspeak applied to adjectives, not nouns - unexplored pattern"""
    log_progress(3, "Adjective-Only Leetspeak")

    # Adjective leet mappings
    adj_leet = {
        "bad": ["bad", "b@d", "b4d"],
        "dumb": ["dumb", "dum6"],
        "stupid": ["stupid", "5tupid", "$tupid", "stup1d"],
        "shitty": ["shitty", "5hitty", "$hitty", "sh1tty"],
        "crappy": ["crappy", "cr@ppy", "cr4ppy"],
        "awful": ["awful", "@wful", "4wful"]
    }

    # Phrase templates with {adj} placeholder
    templates = [
        ["this", "is", "a", "{adj}", "password"],
        ["this", "is", "a", "{adj}", "passphrase"],
        ["this", "is", "a", "really", "{adj}", "password"],
        ["this", "is", "a", "really", "{adj}", "passphrase"],
        ["this", "is", "a", "very", "{adj}", "password"],
        ["this", "is", "a", "very", "{adj}", "passphrase"],
        ["this", "is", "a", "super", "{adj}", "password"],
        ["this", "is", "a", "super", "{adj}", "passphrase"],
        ["this", "is", "a", "really", "really", "{adj}", "password"],
        ["this", "is", "a", "really", "really", "{adj}", "passphrase"],
        ["this", "is", "a", "very", "very", "{adj}", "password"],
        ["this", "is", "a", "very", "very", "{adj}", "passphrase"],
        ["{adj}", "password"],
        ["{adj}", "passphrase"],
        ["really", "{adj}", "password"],
        ["really", "{adj}", "passphrase"],
        ["very", "{adj}", "password"],
        ["very", "{adj}", "passphrase"],
    ]

    separators = [" ", ".", "-"]
    trailing_chars = "!?~`"
    max_trailing = 6

    # Generate trailing combinations
    trailing_combos = [""]
    for length in range(1, max_trailing + 1):
        for combo in itertools.product(trailing_chars, repeat=length):
            trailing_combos.append("".join(combo))

    for template in templates:
        for adj_base, leet_variants in adj_leet.items():
            for leet_adj in leet_variants:
                # Substitute {adj} with leeted version
                phrase_words = [w.replace("{adj}", leet_adj) for w in template]

                for sep in separators:
                    phrase = sep.join(phrase_words)

                    for trail in trailing_combos:
                        yield phrase + trail
                        yield phrase.capitalize() + trail


# ==================== FAMILY 2: Exact Character Count (~20K) ====================
def family_2_exact_length() -> Generator[str, None, None]:
    """Phrases targeting exactly 16, 20, or 24 characters"""
    log_progress(2, "Exact Character Count (16/20/24)")

    targets = [16, 20, 24]
    adjectives_extended = ["bad", "dumb", "stupid", "awful", "shitty", "crappy", "weak"]
    nouns_extended = ["password", "passphrase", "pass", "passwd"]
    intensifiers = ["", "very ", "really ", "super ", "so ", "pretty "]
    starters = ["", "this is a ", "this is ", "my ", "a "]
    trailing_chars = ["!", "?", "~", "`", "1", "2", "3"]

    for target in targets:
        for starter in starters:
            for intens in intensifiers:
                for adj in adjectives_extended:
                    for noun in nouns_extended:
                        base = f"{starter}{intens}{adj} {noun}".strip()

                        # Try with different trailing lengths
                        for trail_len in range(0, 10):
                            for trail_char in trailing_chars:
                                trail = trail_char * trail_len
                                if len(base + trail) == target:
                                    yield base + trail
                                    yield (base + trail).capitalize()


# ==================== FAMILY 4: Typo Patterns (~58K) ====================
def family_4_typos() -> Generator[str, None, None]:
    """Common typos in password/passphrase"""
    log_progress(4, "Typo Patterns")

    typo_nouns = [
        # password typos
        "passwrod", "passowrd", "paswword", "pasword",
        "passwordd", "passwoord", "passsword",
        # passphrase typos
        "passphrse", "pasphrase", "passphraes",
        "passphrsae", "passphraze", "pasphras", "paspharse"
    ]

    starters = ["", "this is a ", "this is a really ", "this is a very "]
    separators = [" ", ".", "-"]

    for starter in starters:
        for adj in ADJECTIVES:
            for noun in typo_nouns:
                if starter:
                    for sep in separators:
                        phrase = starter.replace(" ", sep) + adj + sep + noun
                        for trail in DEAN_TRAILING:
                            yield phrase + trail
                            yield phrase.capitalize() + trail
                else:
                    for sep in [" ", "."]:
                        phrase = adj + sep + noun
                        for trail in DEAN_TRAILING:
                            yield phrase + trail
                            yield phrase.capitalize() + trail


# ==================== FAMILY 5: Bitcoin/Crypto-Themed (~164K) ====================
def family_5_bitcoin_theme() -> Generator[str, None, None]:
    """Bitcoin/crypto-specific terminology"""
    log_progress(5, "Bitcoin/Crypto Theme")

    crypto_nouns = ["bitcoin", "btc", "wallet", "crypto", "satoshi", "blockchain", "coin"]
    adjectives_extended = ["bad", "dumb", "stupid", "shitty", "weak"]
    intensifiers = ["", "really ", "very ", "super "]
    starters = ["this is a ", "this is my ", "my ", "a ", ""]
    separators = [" ", ".", "-"]

    for starter in starters:
        for intens in intensifiers:
            for adj in adjectives_extended:
                for crypto in crypto_nouns:
                    for noun in NOUNS:
                        if starter:
                            phrase_words = [starter.strip(), intens.strip(), adj, crypto, noun]
                            phrase_words = [w for w in phrase_words if w]

                            for sep in separators:
                                phrase = sep.join(phrase_words)
                                for trail in DEAN_TRAILING:
                                    yield phrase + trail
                                    yield phrase.capitalize() + trail
                        elif not intens:  # Short form only if no starter and no intensifier
                            for sep in [" ", "."]:
                                phrase = f"{adj}{sep}{crypto}{sep}{noun}"
                                for trail in DEAN_TRAILING:
                                    yield phrase + trail
                                    yield phrase.capitalize() + trail


# ==================== FAMILY 7: Profanity-Heavy (~87K) ====================
def family_7_profanity() -> Generator[str, None, None]:
    """Profanity-heavy combinations"""
    log_progress(7, "Profanity-Heavy Variants")

    profanity = ["fucking", "fuckin", "damn", "shit", "ass", "shitty", "crappy"]
    adjectives_extended = ["bad", "dumb", "stupid", "lame"]
    starters = ["this is a ", "this is my ", "my ", "a ", ""]
    separators = [" ", "."]

    for prof in profanity:
        for noun in NOUNS:
            # Pattern 1: "[prof] password"
            for sep in [" ", "."]:
                phrase = f"{prof}{sep}{noun}"
                for trail in DEAN_TRAILING:
                    yield phrase + trail
                    yield phrase.capitalize() + trail

            # Pattern 2: "this is a [prof] [adj] password"
            for starter in ["this is a ", "this is my ", "my "]:
                for adj in adjectives_extended:
                    for sep in separators:
                        phrase_words = [starter.strip(), prof, adj, noun]
                        phrase = sep.join(phrase_words)
                        for trail in DEAN_TRAILING:
                            yield phrase + trail
                            yield phrase.capitalize() + trail


# ==================== FAMILY 6: Inverted Word Order (~14K) ====================
def family_6_inverted() -> Generator[str, None, None]:
    """Inverted/alternative word order"""
    log_progress(6, "Inverted Word Order")

    intensifiers = ["", "really ", "very ", "super "]
    separators = [" ", "."]

    for noun in NOUNS:
        for adj in ADJECTIVES:
            for intens in intensifiers:
                intens_str = intens.strip()

                # Pattern: "password is [intensifier] bad"
                for sep in separators:
                    if intens_str:
                        phrase = f"{noun}{sep}is{sep}{intens_str}{sep}{adj}"
                    else:
                        phrase = f"{noun}{sep}is{sep}{adj}"

                    for trail in DEAN_TRAILING:
                        yield phrase + trail
                        yield phrase.capitalize() + trail

                # Pattern: "password bad [intensifier]" (no verb)
                for sep in separators:
                    if intens_str:
                        phrase = f"{noun}{sep}{adj}{sep}{intens_str}"
                    else:
                        phrase = f"{noun}{sep}{adj}"

                    for trail in DEAN_TRAILING:
                        yield phrase + trail
                        yield phrase.capitalize() + trail


# ==================== FAMILY 8: Mixed Separators (~16K) ====================
def family_8_mixed_separators() -> Generator[str, None, None]:
    """Mixed separator patterns (space + period in same phrase)"""
    log_progress(8, "Mixed Separators")

    intensifiers = ["", "really", "very"]

    for adj in ADJECTIVES:
        for noun in NOUNS:
            for intens in intensifiers:
                if intens:
                    # Pattern 1: "this is a.really.bad.password"
                    phrase1 = f"this is a.{intens}.{adj}.{noun}"
                    # Pattern 2: "this.is.a really bad password"
                    phrase2 = f"this.is.a {intens} {adj} {noun}"
                    # Pattern 3: "this is a really.bad.password"
                    phrase3 = f"this is a {intens}.{adj}.{noun}"
                else:
                    phrase1 = f"this is a.{adj}.{noun}"
                    phrase2 = f"this.is.a {adj} {noun}"
                    phrase3 = f"this is a.{adj}.{noun}"

                for phrase in [phrase1, phrase2, phrase3]:
                    for trail in DEAN_TRAILING:
                        yield phrase + trail
                        yield phrase.capitalize() + trail


# ==================== FAMILY 9: 2011 Meme Culture (~3K) ====================
def family_9_memes() -> Generator[str, None, None]:
    """2011 meme culture phrases"""
    log_progress(9, "2011 Meme Culture")

    memes = [
        "u mad bro", "like a boss", "epic fail", "cool story bro",
        "y u no", "challenge accepted", "not sure if", "one does not simply"
    ]

    for meme in memes:
        for noun in NOUNS:
            # Pattern 1: "[meme] password"
            for sep in [" ", ""]:
                if sep:
                    phrase = f"{meme} {noun}"
                else:
                    phrase = f"{meme}{noun}"

                for trail in DEAN_TRAILING:
                    yield phrase + trail
                    yield phrase.capitalize() + trail

            # Pattern 2: "this password is [meme]"
            phrase = f"this {noun} is {meme}"
            for trail in DEAN_TRAILING:
                yield phrase + trail
                yield phrase.capitalize() + trail


# ==================== FAMILY 10: CamelCase (~1K) ====================
def family_10_camelcase() -> Generator[str, None, None]:
    """CamelCase/PascalCase patterns"""
    log_progress(10, "CamelCase Patterns")

    phrases = [
        ["this", "is", "a", "bad", "password"],
        ["this", "is", "a", "dumb", "password"],
        ["this", "is", "a", "stupid", "password"],
        ["this", "is", "a", "bad", "passphrase"],
        ["this", "is", "a", "dumb", "passphrase"],
        ["this", "is", "a", "stupid", "passphrase"],
        ["this", "is", "a", "really", "bad", "password"],
        ["this", "is", "a", "very", "bad", "password"],
        ["this", "is", "a", "really", "bad", "passphrase"],
        ["this", "is", "a", "very", "bad", "passphrase"],
    ]

    def to_pascal_case(words):
        return "".join(w.capitalize() for w in words)

    def to_camel_case(words):
        return words[0] + "".join(w.capitalize() for w in words[1:])

    for phrase in phrases:
        # Find adjective index for emphasis
        adj_idx = None
        for i, word in enumerate(phrase):
            if word in ["bad", "dumb", "stupid", "really", "very"]:
                adj_idx = i
                break

        # Pascal case
        pascal = to_pascal_case(phrase)
        for trail in DEAN_TRAILING:
            yield pascal + trail

        # Camel case
        camel = to_camel_case(phrase)
        for trail in DEAN_TRAILING:
            yield camel + trail

        # Emphasis case (if adjective found)
        if adj_idx is not None:
            emphasis = "".join(w.upper() if i == adj_idx else w for i, w in enumerate(phrase))
            for trail in DEAN_TRAILING:
                yield emphasis + trail


# ==================== MAIN GENERATOR ====================
def generate_all() -> Generator[str, None, None]:
    """Generate all candidates in priority order"""

    # TIER 1: High Priority (~14.9M candidates)
    print("# TIER 1: High Priority Families", file=sys.stderr)
    yield from family_1_dash_separated()      # ~75K
    yield from family_3_adjective_leet()      # ~14.7M
    yield from family_2_exact_length()        # ~20K
    yield from family_4_typos()               # ~58K

    # TIER 2: Medium Priority (~281K candidates)
    print("# TIER 2: Medium Priority Families", file=sys.stderr)
    yield from family_5_bitcoin_theme()       # ~164K
    yield from family_7_profanity()           # ~87K
    yield from family_6_inverted()            # ~14K
    yield from family_8_mixed_separators()    # ~16K

    # TIER 3: Low Priority (~4K candidates)
    print("# TIER 3: Low Priority Families", file=sys.stderr)
    yield from family_9_memes()               # ~3K
    yield from family_10_camelcase()          # ~1K


# ==================== MAIN ====================
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print("Estimating candidate counts...")
        print("\nTIER 1 (High Priority):")
        print("  Family 1 (Dash-separated):      ~75,000")
        print("  Family 3 (Adjective leet):   ~14,700,000")
        print("  Family 2 (Exact length):        ~20,000")
        print("  Family 4 (Typos):               ~58,000")
        print("  Tier 1 Subtotal:            ~14,853,000")
        print("\nTIER 2 (Medium Priority):")
        print("  Family 5 (Bitcoin theme):      ~164,000")
        print("  Family 7 (Profanity):           ~87,000")
        print("  Family 6 (Inverted):            ~14,000")
        print("  Family 8 (Mixed sep):           ~16,000")
        print("  Tier 2 Subtotal:               ~281,000")
        print("\nTIER 3 (Low Priority):")
        print("  Family 9 (Memes):                ~3,000")
        print("  Family 10 (CamelCase):           ~1,000")
        print("  Tier 3 Subtotal:                 ~4,000")
        print("\n" + "="*50)
        print("TOTAL ESTIMATED:              ~15,138,000")
        print("="*50)
        print("\nRuntime at 270k H/s: ~56 seconds (~1 minute)")
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
