#!/usr/bin/env python3
"""
Crack My Wallet - 1 Billion Password Generator

This script generates approximately 1 billion passphrase candidates based on
Dean Pierce's (px) hints, prioritized by likelihood.

Target: ~1,000,000,000 candidates
Strategy: Expand the most likely patterns with systematic mutations

Based on Dean's hints:
- It's a PASSPHRASE (multiple words), not a single password
- Likely 4-7 words (more than his usual 3-4)
- Separators: spaces (most likely), periods (sometimes), dashes (rarely)
- Theme: Self-deprecating statement about password weakness
- Leetspeak: a->@,4; s->$,5; pass->p455,p@$$; NEVER 7 for r
- Trailing chars: 1, 3, or 6 characters - !, ?, ~, `

Keyspace calculation:
- Base phrases: ~50 core phrases
- Separators: 4 options (space, period, dash, none)
- Case variations: 4 options (lower, title, upper, sentence)
- Trailing patterns: ~50 options (expanded)
- Leetspeak mutations: ~100 per phrase
- = 50 * 4 * 4 * 50 * 100 = 4,000,000 (base)
- Extended with more adjectives, nouns, prefixes = ~1B

Usage:
    python generate_1b.py > wordlist.txt
    python generate_1b.py --estimate  # Show estimated count
    python generate_1b.py --chunk N   # Generate chunk N of 10
"""

import argparse
import itertools
import sys
from typing import Generator, List, Set

# ============================================================================
# WORD LISTS (Expanded for 1B target)
# ============================================================================

# Core adjectives (highest priority - Dean mentioned these)
CORE_ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak", "simple", "easy",
    "lazy", "embarrassing", "pathetic", "horrible", "worst", "dumbest",
    "stupidest", "lamest", "weakest", "simplest", "easiest", "poorest",
]

# 2011 era slang adjectives
ERA_ADJECTIVES = [
    "derpy", "lulzy", "lame", "crappy", "shitty", "silly", "ridiculous",
    "retarded", "idiotic", "moronic", "asinine", "inane", "absurd",
]

# Extended adjectives
EXTENDED_ADJECTIVES = [
    "poor", "lousy", "useless", "worthless", "pointless", "meaningless",
    "forgettable", "unmemorable", "generic", "basic", "plain", "boring",
    "unoriginal", "uncreative", "uninspired", "thoughtless", "careless",
    "sloppy", "hasty", "rushed", "quick", "fast", "short", "brief",
]

ALL_ADJECTIVES = CORE_ADJECTIVES + ERA_ADJECTIVES + EXTENDED_ADJECTIVES

# Core nouns (highest priority)
CORE_NOUNS = ["password", "passphrase"]

# Extended nouns
EXTENDED_NOUNS = [
    "password", "passphrase", "pass", "passwd", "secret", "key",
    "phrase", "word", "code", "pin", "combo", "combination",
]

# Prefixes (ordered by likelihood)
PREFIXES = [
    "this is a",
    "this is a really",
    "this is a very",
    "this is such a",
    "this is the",
    "this is my",
    "what a",
    "such a",
    "my",
    "a really",
    "a very",
    "really",
    "very",
    "so",
    "such",
    "the",
    "a",
    "",
]

# Intensifiers to insert
INTENSIFIERS = [
    "", "really", "very", "so", "such a", "truly", "absolutely",
    "incredibly", "extremely", "super", "totally", "completely",
]

# Separators (ordered by likelihood based on Dean's hints)
SEPARATORS = [" ", ".", "-", ""]

# ============================================================================
# TRAILING PATTERNS (Expanded based on Dean's "1, 3, or 6 chars" hint)
# ============================================================================

def generate_trailing_patterns() -> List[str]:
    """Generate all trailing patterns based on Dean's hints."""
    patterns = [""]  # No trailing
    
    # Single characters (1 char)
    single_chars = ["!", "?", "~", "`", "1", "2", "3", "0"]
    patterns.extend(single_chars)
    
    # Double characters (2 chars)
    for c in ["!", "?", "~", "`"]:
        patterns.append(c * 2)
    patterns.extend(["12", "11", "01", "00", "!1", "?1", "1!"])
    
    # Triple characters (3 chars)
    for c in ["!", "?", "~", "`"]:
        patterns.append(c * 3)
    patterns.extend(["123", "111", "000", "321", "!@#", "!?!", "?!?"])
    
    # Quad characters (4 chars)
    for c in ["!", "?"]:
        patterns.append(c * 4)
    patterns.extend(["1234", "1111", "0000"])
    
    # Five characters (5 chars)
    for c in ["!", "?"]:
        patterns.append(c * 5)
    patterns.extend(["12345", "11111"])
    
    # Six characters (6 chars - Dean mentioned this)
    for c in ["!", "?", "~", "`"]:
        patterns.append(c * 6)
    patterns.extend(["123456", "111111", "000000", "654321", "!@#$%^"])
    
    # Mixed patterns
    patterns.extend([
        "!!", "??", "~~", "``",
        "!?", "?!", "!~", "~!",
        "!1!", "?1?", "1!1",
        "!!1", "??1", "1!!", "1??",
        "!!!1", "???1", "1!!!", "1???",
    ])
    
    return list(set(patterns))  # Deduplicate

TRAILING_PATTERNS = generate_trailing_patterns()

# ============================================================================
# LEETSPEAK MUTATIONS (Based on Dean's confirmed patterns)
# ============================================================================

# Dean's confirmed substitutions
LEET_CHAR_SUBS = {
    "a": ["a", "@", "4"],
    "s": ["s", "$", "5"],
    "e": ["e", "3"],
    "i": ["i", "1", "!"],
    "o": ["o", "0"],
    # NOT using 7 for anything - Dean said he never does this
}

# Dean's confirmed word substitutions
LEET_WORD_SUBS = {
    "pass": ["pass", "p455", "p@$$", "p4$$", "p@55", "pa55", "p@ss"],
    "password": ["password", "p455word", "p@$$word", "p4$$word", "p@55word", 
                 "pa55word", "p@ssword", "passw0rd", "p455w0rd", "p@$$w0rd"],
    "passphrase": ["passphrase", "p455phrase", "p@$$phrase", "p4$$phrase",
                   "passphr4se", "p455phr4se", "p@$$phr4se"],
    "bad": ["bad", "b4d", "b@d"],
    "dumb": ["dumb", "durnb", "d0mb"],
}


def apply_word_leet(word: str) -> Generator[str, None, None]:
    """Apply leetspeak to a word using Dean's patterns."""
    word_lower = word.lower()
    
    # Check for known word substitutions first
    if word_lower in LEET_WORD_SUBS:
        for sub in LEET_WORD_SUBS[word_lower]:
            yield sub
        return
    
    # Apply character-level substitutions
    yield word  # Original
    
    # Single character substitutions
    for i, char in enumerate(word):
        char_lower = char.lower()
        if char_lower in LEET_CHAR_SUBS:
            for sub in LEET_CHAR_SUBS[char_lower][1:]:  # Skip original
                yield word[:i] + sub + word[i+1:]


def apply_phrase_leet(phrase: str, max_variants: int = 500) -> Generator[str, None, None]:
    """Apply leetspeak to a phrase, limiting variants."""
    words = phrase.split()
    
    # Get leet variants for each word
    word_variants = []
    for word in words:
        variants = list(apply_word_leet(word))[:20]  # More variants per word
        word_variants.append(variants)
    
    # Generate combinations
    count = 0
    for combo in itertools.product(*word_variants):
        yield " ".join(combo)
        count += 1
        if count >= max_variants:
            return


# ============================================================================
# CASE VARIATIONS
# ============================================================================

def apply_case_variations(phrase: str) -> Generator[str, None, None]:
    """Apply case variations to a phrase."""
    yield phrase.lower()
    yield phrase.title()
    yield phrase.upper()
    # Sentence case
    if phrase:
        yield phrase[0].upper() + phrase[1:].lower()
    # First word caps only
    words = phrase.split()
    if len(words) > 1:
        yield words[0].capitalize() + " " + " ".join(w.lower() for w in words[1:])


# ============================================================================
# MAIN GENERATORS
# ============================================================================

def generate_base_phrases() -> Generator[str, None, None]:
    """Generate base phrases without mutations."""
    # Standard patterns with all nouns
    for prefix in PREFIXES:
        for adj in ALL_ADJECTIVES:
            for noun in EXTENDED_NOUNS:
                if prefix:
                    yield f"{prefix} {adj} {noun}"
                else:
                    yield f"{adj} {noun}"
    
    # Extended patterns with intensifiers - full coverage
    for prefix in PREFIXES:
        for intensifier in INTENSIFIERS:
            for adj in ALL_ADJECTIVES:
                for noun in EXTENDED_NOUNS:
                    if prefix and intensifier:
                        yield f"{prefix} {intensifier} {adj} {noun}"
                    elif prefix:
                        yield f"{prefix} {adj} {noun}"
                    elif intensifier:
                        yield f"{intensifier} {adj} {noun}"
    
    # Double adjective patterns
    for prefix in PREFIXES[:10]:
        for adj1 in ALL_ADJECTIVES:
            for adj2 in ALL_ADJECTIVES[:20]:
                if adj1 != adj2:
                    for noun in EXTENDED_NOUNS[:4]:
                        if prefix:
                            yield f"{prefix} {adj1} {adj2} {noun}"
                        else:
                            yield f"{adj1} {adj2} {noun}"


def generate_with_separators(phrase: str) -> Generator[str, None, None]:
    """Generate phrase with different separators."""
    words = phrase.split()
    for sep in SEPARATORS:
        yield sep.join(words)


def generate_all_candidates() -> Generator[str, None, None]:
    """Generate all ~1 billion candidates."""
    seen: Set[str] = set()
    
    for base_phrase in generate_base_phrases():
        # Apply separator variations
        for sep_phrase in generate_with_separators(base_phrase):
            # Apply case variations
            for case_phrase in apply_case_variations(sep_phrase):
                # Apply trailing patterns
                for trailing in TRAILING_PATTERNS:
                    candidate = case_phrase + trailing
                    if candidate not in seen:
                        seen.add(candidate)
                        yield candidate
                
                # Apply leetspeak mutations (limited to hit ~1B target)
                for leet_phrase in apply_phrase_leet(case_phrase, max_variants=10):
                    for trailing in TRAILING_PATTERNS[:20]:  # Limit trailing for leet
                        candidate = leet_phrase + trailing
                        if candidate not in seen:
                            seen.add(candidate)
                            yield candidate
    
    # Add elongated patterns
    yield from generate_elongated_patterns()
    
    # Add repeated word patterns
    yield from generate_repeated_patterns()


def generate_elongated_patterns() -> Generator[str, None, None]:
    """Generate elongated character patterns."""
    elongations = [
        ("bad", "a", range(3, 20)),
        ("dumb", "u", range(3, 15)),
        ("stupid", "u", range(3, 10)),
        ("poop", "o", range(5, 25)),
        ("lame", "a", range(3, 15)),
        ("weak", "e", range(3, 10)),
    ]
    
    for word, char, counts in elongations:
        idx = word.find(char)
        if idx < 0:
            continue
        
        for count in counts:
            elongated = word[:idx] + char * count + word[idx+1:]
            
            # Standalone
            yield elongated
            for trailing in TRAILING_PATTERNS[:10]:
                yield elongated + trailing
            
            # In phrases
            for prefix in ["", "this is ", "this is a ", "so ", "really "]:
                phrase = prefix + elongated
                yield phrase
                for trailing in TRAILING_PATTERNS[:5]:
                    yield phrase + trailing
                
                # With password/passphrase
                for noun in ["password", "passphrase"]:
                    full = f"{phrase} {noun}"
                    yield full
                    for trailing in TRAILING_PATTERNS[:5]:
                        yield full + trailing


def generate_repeated_patterns() -> Generator[str, None, None]:
    """Generate repeated character/word patterns."""
    # Single char repeated
    for char in "abdeiopsu":
        for count in range(10, 35, 5):
            pattern = char * count
            yield pattern
            yield pattern + "123"
            yield pattern + "!"
    
    # Words repeated
    for word in ["bad", "dumb", "poop", "lol", "lulz", "derp"]:
        for count in range(2, 8):
            yield word * count
            yield (word + " ") * count
            yield (word + ".") * count


def estimate_count() -> int:
    """Estimate total candidate count.
    
    Target: ~1 billion candidates
    
    Calculation:
    - Base phrases: ~120,000 (prefixes * adjectives * nouns + intensifiers + double adj)
    - Separators: 4
    - Cases: 5
    - Trailing: 64
    - Leet variants: 50 per phrase
    - Leet trailing: 30
    
    120,000 * 4 * 5 * (64 + 50 * 30) = 120,000 * 4 * 5 * 1564 = ~3.7B (too high)
    
    Adjusted: Use fewer leet variants (10) and trailing (20)
    120,000 * 4 * 5 * (64 + 10 * 20) = 120,000 * 4 * 5 * 264 = ~633M
    
    Add more base phrases to reach ~1B
    """
    base_phrases = len(PREFIXES) * len(ALL_ADJECTIVES) * len(EXTENDED_NOUNS)
    intensifier_phrases = len(PREFIXES) * len(INTENSIFIERS) * len(ALL_ADJECTIVES) * len(EXTENDED_NOUNS)
    double_adj = 10 * len(ALL_ADJECTIVES) * 20 * 4  # prefix * adj1 * adj2 * noun
    total_base = base_phrases + intensifier_phrases + double_adj
    
    separators = len(SEPARATORS)
    cases = 5
    trailing = len(TRAILING_PATTERNS)
    leet_variants = 10  # Reduced to hit ~1B target
    leet_trailing = 20  # Reduced
    
    main_candidates = total_base * separators * cases * (trailing + leet_variants * leet_trailing)
    elongated = 6 * 20 * (1 + 10 + 5 * (1 + 5 + 2 * (1 + 5)))
    repeated = 9 * 5 * 3 + 6 * 6 * 3
    
    return main_candidates + elongated + repeated


def main():
    parser = argparse.ArgumentParser(
        description="Generate ~1 billion passphrase candidates"
    )
    parser.add_argument(
        "--estimate", action="store_true",
        help="Show estimated candidate count"
    )
    parser.add_argument(
        "--chunk", type=int, choices=range(1, 11),
        help="Generate only chunk N of 10 (for parallel processing)"
    )
    parser.add_argument(
        "--limit", type=int,
        help="Limit output to N candidates"
    )
    
    args = parser.parse_args()
    
    if args.estimate:
        est = estimate_count()
        print(f"Estimated candidates: {est:,}")
        print(f"Base phrases: {len(PREFIXES) * len(ALL_ADJECTIVES) * len(CORE_NOUNS):,}")
        print(f"Separators: {len(SEPARATORS)}")
        print(f"Case variations: 5")
        print(f"Trailing patterns: {len(TRAILING_PATTERNS)}")
        return
    
    count = 0
    for candidate in generate_all_candidates():
        if args.chunk:
            # Simple chunking by hash
            if hash(candidate) % 10 != args.chunk - 1:
                continue
        
        print(candidate)
        count += 1
        
        if args.limit and count >= args.limit:
            break
    
    print(f"Generated {count:,} candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
