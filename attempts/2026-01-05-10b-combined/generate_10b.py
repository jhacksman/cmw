#!/usr/bin/env python3
"""
Crack My Wallet - 10 Billion Password Generator (Combined Hypotheses)

This script generates approximately 10 billion passphrase candidates combining:
1. Spite Passphrase Hypothesis - Short, deliberately weak multi-word phrases
2. Simple Spite Hypothesis - 10-16 char simple patterns (Claude's theory expanded)

Target: ~10,000,000,000 candidates

Evidence from Dean (px):
- Signal: "Spaces. Maybe periods." for separators
- Signal: "4-7 words" (more than his usual 3-4)
- Signal: Trailing chars "1, 3, maybe 6" - !, ?, ~, `
- Signal: Leetspeak "p455, p@$$" - @ for a, $ for s, NEVER 7 for r
- Telegram: "I definitely set my password to the weakest possible thing I could out of spite"
- Telegram: "I think it was something like 16 characters"

Key improvements over previous 600M attempt:
- NO deduplication set (streams directly, hashcat handles dupes)
- Full leetspeak expansion (not limited)
- Shorter phrases (2-5 words) included
- Simple 10-16 char patterns included
- More trailing pattern combinations
- More case variations

Usage:
    python generate_10b.py > wordlist.txt
    python generate_10b.py --estimate
    python generate_10b.py --limit N
"""

import argparse
import itertools
import sys
from typing import Generator, List, Iterator

# ============================================================================
# WORD LISTS - EXPANDED FOR 10B TARGET
# ============================================================================

# Core adjectives (Dean's self-deprecating theme)
CORE_ADJECTIVES = [
    "bad", "dumb", "stupid", "terrible", "awful", "weak", "simple", "easy",
    "lazy", "embarrassing", "pathetic", "horrible", "worst", "dumbest",
    "stupidest", "lamest", "weakest", "simplest", "easiest", "poorest",
    "crappy", "shitty", "silly", "ridiculous", "idiotic", "moronic",
]

# 2011 era slang
ERA_ADJECTIVES = [
    "derpy", "lulzy", "lame", "retarded", "asinine", "inane", "absurd",
    "epic", "fail", "noob", "n00b", "lol", "rofl", "lmao", "potato",
]

# Extended for more coverage
EXTENDED_ADJECTIVES = [
    "poor", "lousy", "useless", "worthless", "pointless", "forgettable",
    "generic", "basic", "plain", "boring", "unoriginal", "thoughtless",
    "careless", "sloppy", "hasty", "rushed", "quick", "short", "common",
    "typical", "ordinary", "standard", "default", "obvious", "predictable",
    "insecure", "unsafe", "vulnerable", "exposed", "open", "public",
    "horrendous", "atrocious", "abysmal", "dreadful", "appalling",
    "mediocre", "subpar", "inferior", "inadequate", "insufficient", "lacking",
    "trash", "garbage", "junk", "crap", "rubbish", "nonsense",
    "random", "arbitrary", "meaningless", "senseless", "brainless", "mindless",
    "foolish", "daft", "dim", "dense", "thick", "slow",
]

ALL_ADJECTIVES = CORE_ADJECTIVES + ERA_ADJECTIVES + EXTENDED_ADJECTIVES

# Nouns - expanded
CORE_NOUNS = ["password", "passphrase"]
EXTENDED_NOUNS = [
    "password", "passphrase", "pass", "passwd", "secret", "key", "phrase",
    "word", "code", "pin", "combo", "combination", "login", "credential",
    "security", "encryption", "wallet", "bitcoin", "btc", "crypto",
]

# Verbs for phrase construction
VERBS = ["is", "was", "made", "chose", "picked", "used", "created", "set", "have", "had"]

# Prefixes for multi-word phrases - significantly expanded
SHORT_PREFIXES = [
    "", "a", "my", "the", "so", "very", "really", "such a", "what a",
    "one", "another", "yet another", "just a", "only a", "merely a",
    "its", "its a", "its my", "its the", "thats a", "thats my",
]
MEDIUM_PREFIXES = [
    "this is a", "this is my", "this is the", "this is such a",
    "this is a really", "this is a very", "what a", "such a",
    "here is a", "here is my", "here is the", "i have a",
    "i made a", "i chose a", "i picked a", "i used a",
    "i set a", "i created a", "i need a", "i want a",
    "this was a", "this was my", "that is a", "that is my",
    "that was a", "that was my", "it is a", "it is my",
    "heres a", "heres my", "theres a", "theres my",
]
LONG_PREFIXES = [
    "this is a really", "this is a very", "this is such a",
    "this is the most", "this is probably the", "i have a really",
    "this is one really", "this is my really", "this is my very",
    "i made a really", "i chose a really", "i picked a really",
    "this is probably a", "this is definitely a", "this is certainly a",
    "i definitely made a", "i probably made a", "i certainly made a",
    "this was probably a", "this was definitely a", "that was probably a",
]

# Intensifiers - expanded
INTENSIFIERS = [
    "", "really", "very", "so", "super", "totally", "extremely", "incredibly",
    "absolutely", "completely", "utterly", "truly", "genuinely", "seriously",
    "ridiculously", "stupidly", "insanely", "terribly", "horribly", "awfully",
    "pretty", "quite", "fairly", "rather", "somewhat", "kind of", "sort of",
]

# Separators
SEPARATORS = [" ", ".", "-", "_", ""]

# ============================================================================
# TRAILING PATTERNS - MASSIVELY EXPANDED (~250 patterns)
# ============================================================================

def generate_trailing_patterns() -> List[str]:
    """Generate comprehensive trailing patterns."""
    patterns = [""]
    chars = ["!", "?", "~", "`", ".", "*", "#", "@"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # 1 char
    patterns.extend(chars)
    patterns.extend(digits)
    
    # 2 chars - all combinations of special chars
    for c1 in chars[:5]:
        for c2 in chars[:5]:
            patterns.append(c1 + c2)
    # Digit pairs
    for d1 in digits[:5]:
        for d2 in digits[:5]:
            patterns.append(d1 + d2)
    # Mixed
    for c in chars[:5]:
        for d in digits[:5]:
            patterns.append(c + d)
            patterns.append(d + c)
    
    # 3 chars (Dean mentioned)
    for c in chars[:5]:
        patterns.append(c * 3)
    patterns.extend(["123", "111", "000", "321", "!@#", "!?!", "?!?", "!1!", "?1?"])
    patterns.extend(["abc", "xyz", "qwe", "asd", "zxc"])
    for c in chars[:5]:
        patterns.append(c + "11")
        patterns.append("11" + c)
        patterns.append(c + "1" + c)
    
    # 4 chars
    for c in chars[:4]:
        patterns.append(c * 4)
    patterns.extend(["1234", "1111", "0000", "4321", "!!11", "??11", "!!!!"])
    
    # 5 chars
    for c in chars[:3]:
        patterns.append(c * 5)
    patterns.extend(["12345", "11111", "00000", "54321"])
    
    # 6 chars (Dean mentioned)
    for c in chars[:5]:
        patterns.append(c * 6)
    patterns.extend([
        "123456", "111111", "000000", "654321", "!@#$%^", "!!!111", "???111",
        "abcdef", "qwerty", "asdfgh", "zxcvbn",
    ])
    
    # Year patterns (2011 era)
    patterns.extend(["2011", "2010", "2012", "11", "10", "12"])
    patterns.extend(["2011!", "2011!!", "!2011", "!!2011"])
    
    # Common endings
    patterns.extend([
        "01", "02", "03", "69", "42", "13", "07", "77", "99",
        "001", "007", "123", "321", "666", "777", "888", "999",
    ])
    
    return list(set(patterns))

TRAILING_PATTERNS = generate_trailing_patterns()

# ============================================================================
# LEETSPEAK - FULL EXPANSION
# ============================================================================

LEET_CHAR = {
    "a": ["a", "@", "4"],
    "s": ["s", "$", "5"],
    "e": ["e", "3"],
    "i": ["i", "1", "!"],
    "o": ["o", "0"],
    "l": ["l", "1"],
    "t": ["t", "7"],
    # NOT using 7 for r - Dean confirmed never
}

LEET_WORDS = {
    "pass": ["pass", "p455", "p@$$", "p4$$", "p@55", "pa55", "p@ss", "p4ss"],
    "password": [
        "password", "p455word", "p@$$word", "p4$$word", "p@55word", 
        "pa55word", "p@ssword", "passw0rd", "p455w0rd", "p@$$w0rd",
        "p4ssword", "p4ssw0rd", "p@55w0rd", "pa$$word", "pa55w0rd",
    ],
    "passphrase": [
        "passphrase", "p455phrase", "p@$$phrase", "p4$$phrase",
        "passphr4se", "p455phr4se", "p@$$phr4se", "p4ssphr4se",
        "p@ssphr@se", "p455phr@se", "pa55phrase", "pa55phr4se",
    ],
    "bad": ["bad", "b4d", "b@d"],
    "dumb": ["dumb", "d0mb", "durnb"],
    "stupid": ["stupid", "stup1d", "5tupid", "5tup1d", "s7upid"],
    "weak": ["weak", "we4k", "w34k", "w3@k"],
    "easy": ["easy", "e4sy", "3asy", "34sy", "e@sy"],
    "simple": ["simple", "s1mple", "5imple", "51mple", "s!mple"],
    "lame": ["lame", "l4me", "l@me", "1ame"],
    "this": ["this", "th1s", "7his", "7h1s"],
    "is": ["is", "1s", "!s"],
}


def leet_word(word: str) -> Iterator[str]:
    """Generate all leetspeak variants of a word."""
    w = word.lower()
    if w in LEET_WORDS:
        yield from LEET_WORDS[w]
        return
    
    yield word
    
    # Character substitutions
    positions = [(i, LEET_CHAR[c.lower()]) for i, c in enumerate(word) if c.lower() in LEET_CHAR]
    
    if not positions:
        return
    
    # Generate combinations of substitutions (up to 4 positions for more coverage)
    for r in range(1, min(5, len(positions) + 1)):
        for combo in itertools.combinations(range(len(positions)), r):
            indices = [positions[i] for i in combo]
            for subs in itertools.product(*[p[1][1:] for p in indices]):
                result = list(word)
                for (idx, _), sub in zip(indices, subs):
                    result[idx] = sub
                yield "".join(result)


def leet_phrase(phrase: str, sep: str = " ") -> Iterator[str]:
    """Generate leetspeak variants of a phrase."""
    words = phrase.split()
    if not words:
        yield phrase
        return
    
    # Get variants for each word
    word_variants = [list(leet_word(w)) for w in words]
    
    # Limit combinations to target ~10B total (was 12, now 3 to reduce by ~22x)
    max_variants_per_word = 3
    word_variants = [v[:max_variants_per_word] for v in word_variants]
    
    # Generate combinations
    for combo in itertools.product(*word_variants):
        yield sep.join(combo)


# ============================================================================
# CASE VARIATIONS - EXPANDED (~10 variations)
# ============================================================================

def case_variants(phrase: str) -> Iterator[str]:
    """Generate case variations."""
    yield phrase.lower()
    yield phrase.upper()
    yield phrase.title()
    
    # Sentence case
    if phrase:
        yield phrase[0].upper() + phrase[1:].lower()
    
    # First word caps
    words = phrase.split()
    if len(words) > 1:
        yield words[0].upper() + " " + " ".join(w.lower() for w in words[1:])
        yield words[0].lower() + " " + " ".join(w.title() for w in words[1:])
    
    # Alternating case
    if len(phrase) <= 30:
        yield "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(phrase))
        yield "".join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(phrase))
    
    # Last word caps
    if len(words) > 1:
        yield " ".join(w.lower() for w in words[:-1]) + " " + words[-1].upper()


# ============================================================================
# HYPOTHESIS 1: SPITE PASSPHRASE (Multi-word)
# ============================================================================

def generate_short_phrases() -> Iterator[str]:
    """Generate 2-3 word phrases."""
    # Pattern: [adj] [noun]
    for adj in ALL_ADJECTIVES:
        for noun in EXTENDED_NOUNS:
            yield f"{adj} {noun}"
    
    # Pattern: [prefix] [adj] [noun]
    for prefix in SHORT_PREFIXES:
        for adj in ALL_ADJECTIVES:
            for noun in CORE_NOUNS:
                if prefix:
                    yield f"{prefix} {adj} {noun}"
    
    # Pattern: [adj] [adj] [noun]
    for adj1 in CORE_ADJECTIVES[:20]:
        for adj2 in CORE_ADJECTIVES[:20]:
            if adj1 != adj2:
                for noun in CORE_NOUNS:
                    yield f"{adj1} {adj2} {noun}"


def generate_medium_phrases() -> Iterator[str]:
    """Generate 4-5 word phrases."""
    # Pattern: [prefix] [adj] [noun]
    for prefix in MEDIUM_PREFIXES:
        for adj in ALL_ADJECTIVES:
            for noun in EXTENDED_NOUNS:
                yield f"{prefix} {adj} {noun}"
    
    # Pattern: [prefix] [intensifier] [adj] [noun]
    for prefix in SHORT_PREFIXES[:12]:
        for intensifier in INTENSIFIERS[:15]:
            for adj in CORE_ADJECTIVES:
                for noun in CORE_NOUNS:
                    if prefix and intensifier:
                        yield f"{prefix} {intensifier} {adj} {noun}"
    
    # Pattern: [prefix] [adj] [adj] [noun]
    for prefix in SHORT_PREFIXES[:10]:
        for adj1 in CORE_ADJECTIVES[:15]:
            for adj2 in CORE_ADJECTIVES[:15]:
                if adj1 != adj2 and prefix:
                    for noun in CORE_NOUNS:
                        yield f"{prefix} {adj1} {adj2} {noun}"


def generate_long_phrases() -> Iterator[str]:
    """Generate 5-7 word phrases."""
    for prefix in LONG_PREFIXES:
        for adj in ALL_ADJECTIVES:
            for noun in EXTENDED_NOUNS:
                yield f"{prefix} {adj} {noun}"
    
    # Double adjective with long prefix
    for prefix in MEDIUM_PREFIXES[:15]:
        for adj1 in CORE_ADJECTIVES[:18]:
            for adj2 in CORE_ADJECTIVES[:18]:
                if adj1 != adj2:
                    for noun in CORE_NOUNS:
                        yield f"{prefix} {adj1} {adj2} {noun}"
    
    # Triple adjective
    for prefix in SHORT_PREFIXES[:8]:
        for adj1 in CORE_ADJECTIVES[:10]:
            for adj2 in CORE_ADJECTIVES[:10]:
                for adj3 in CORE_ADJECTIVES[:10]:
                    if len(set([adj1, adj2, adj3])) == 3 and prefix:
                        for noun in CORE_NOUNS:
                            yield f"{prefix} {adj1} {adj2} {adj3} {noun}"


def generate_passphrase_candidates() -> Iterator[str]:
    """Generate all passphrase candidates with mutations."""
    phrase_generators = [
        generate_short_phrases,
        generate_medium_phrases,
        generate_long_phrases,
    ]
    
    for gen in phrase_generators:
        for base in gen():
            # Separator variations
            words = base.split()
            for sep in SEPARATORS:
                sep_phrase = sep.join(words)
                
                # Case variations
                for cased in case_variants(sep_phrase):
                    # Trailing patterns
                    for trail in TRAILING_PATTERNS:
                        yield cased + trail
                    
                    # Leetspeak + trailing
                    for leet in leet_phrase(cased, sep):
                        for trail in TRAILING_PATTERNS:
                            yield leet + trail


# ============================================================================
# HYPOTHESIS 2: SIMPLE SPITE (10-16 char patterns)
# ============================================================================

def generate_simple_spite() -> Iterator[str]:
    """Generate simple 10-16 character spite passwords."""
    
    # Common passwords extended to 10+ chars
    common_bases = [
        "password", "passphrase", "badpass", "dumbpass", "weakpass",
        "easypass", "simplepass", "lazypass", "mypass", "thepass",
        "letmein", "welcome", "admin", "master", "monkey", "dragon",
        "qwerty", "abc123", "iloveyou", "trustno1", "bitcoin", "wallet",
        "secret", "login", "access", "enter", "open", "unlock",
    ]
    
    # Padding patterns to reach 10+ chars
    padding = [
        "1", "12", "123", "1234", "12345", "123456",
        "!", "!!", "!!!", "!!!!", "!!!!!", "!!!!!!",
        "?", "??", "???", "????", "?????", "??????",
        "1!", "!1", "11", "00", "01", "10",
        "111", "000", "1!1", "!1!", "123!", "!123",
        "2011", "2010", "2012", "11!", "10!", "12!",
    ]
    
    for base in common_bases:
        for pad in padding:
            candidate = base + pad
            if 10 <= len(candidate) <= 20:
                yield candidate
                yield candidate.title()
                yield candidate.upper()
        
        # Leetspeak variants
        for leet in leet_word(base):
            for pad in padding[:20]:
                candidate = leet + pad
                if 10 <= len(candidate) <= 20:
                    yield candidate
    
    # Keyboard patterns (10+ chars)
    keyboard = [
        "qwertyuiop", "asdfghjkl;", "zxcvbnm,./",
        "1234567890", "0987654321",
        "qwerty1234", "asdfgh1234", "zxcvbn1234",
        "1qaz2wsx3e", "!qaz@wsx#e",
        "qazwsxedcr", "plmoknijbu",
        "qwertyuio", "asdfghjkl", "zxcvbnm",
    ]
    for k in keyboard:
        yield k
        for trail in TRAILING_PATTERNS[:40]:
            if 10 <= len(k + trail) <= 20:
                yield k + trail
    
    # Repeated characters (10+ chars)
    for c in "abcdefghijklmnopqrstuvwxyz0123456789!?":
        for length in [10, 11, 12, 13, 14, 15, 16]:
            yield c * length
    
    # Self-deprecating short forms
    spite_bases = [
        "badpassword", "dumbpassword", "weakpassword", "easypassword",
        "stupidpass", "simplepass", "lazypassword", "worstpassword",
        "badpasswor", "dumbpasswo", "weakpasswo", "mypassword",
        "thepassword", "apassword", "password123", "passphrase1",
    ]
    for base in spite_bases:
        yield base
        for trail in TRAILING_PATTERNS[:30]:
            yield base + trail
        for leet in leet_word(base):
            yield leet
            for trail in TRAILING_PATTERNS[:15]:
                yield leet + trail
    
    # Number sequences
    for start in range(10):
        seq = "".join(str((start + i) % 10) for i in range(10))
        yield seq
        for trail in TRAILING_PATTERNS[:15]:
            yield seq + trail
        # Longer sequences
        for length in [11, 12, 13, 14, 15, 16]:
            long_seq = "".join(str((start + i) % 10) for i in range(length))
            yield long_seq


# ============================================================================
# ELONGATED PATTERNS
# ============================================================================

def generate_elongated() -> Iterator[str]:
    """Generate elongated character patterns."""
    elongations = [
        ("bad", "a", range(3, 40)),
        ("dumb", "u", range(3, 35)),
        ("stupid", "u", range(3, 30)),
        ("poop", "o", range(5, 45)),
        ("lame", "a", range(3, 35)),
        ("weak", "e", range(3, 30)),
        ("derp", "e", range(3, 30)),
        ("fail", "a", range(3, 30)),
        ("noob", "o", range(3, 35)),
        ("lol", "o", range(3, 40)),
    ]
    
    for word, char, counts in elongations:
        idx = word.find(char)
        if idx < 0:
            continue
        
        for count in counts:
            elongated = word[:idx] + char * count + word[idx+1:]
            yield elongated
            
            for trail in TRAILING_PATTERNS[:25]:
                yield elongated + trail
            
            for prefix in ["", "this is ", "this is a ", "so ", "really ", "my ", "a ", "the ", "such a "]:
                phrase = prefix + elongated
                yield phrase
                for trail in TRAILING_PATTERNS[:20]:
                    yield phrase + trail
                
                for noun in CORE_NOUNS:
                    full = f"{phrase} {noun}"
                    yield full
                    for trail in TRAILING_PATTERNS[:20]:
                        yield full + trail


# ============================================================================
# MAIN GENERATOR
# ============================================================================

def generate_all() -> Iterator[str]:
    """Generate all ~10 billion candidates."""
    # Hypothesis 1: Spite passphrases (bulk of candidates)
    yield from generate_passphrase_candidates()
    
    # Hypothesis 2: Simple spite patterns
    yield from generate_simple_spite()
    
    # Elongated patterns
    yield from generate_elongated()


def estimate_count() -> dict:
    """Estimate total candidates."""
    # Count base phrases
    short = len(ALL_ADJECTIVES) * len(EXTENDED_NOUNS)
    short += len([p for p in SHORT_PREFIXES if p]) * len(ALL_ADJECTIVES) * len(CORE_NOUNS)
    short += 20 * 19 * len(CORE_NOUNS)  # adj adj noun
    
    medium = len(MEDIUM_PREFIXES) * len(ALL_ADJECTIVES) * len(EXTENDED_NOUNS)
    medium += 12 * 15 * len(CORE_ADJECTIVES) * len(CORE_NOUNS)  # prefix intensifier adj noun
    medium += 10 * 15 * 14 * len(CORE_NOUNS)  # prefix adj adj noun
    
    long_p = len(LONG_PREFIXES) * len(ALL_ADJECTIVES) * len(EXTENDED_NOUNS)
    long_p += 15 * 18 * 17 * len(CORE_NOUNS)  # double adj
    long_p += 8 * 10 * 9 * 8 * len(CORE_NOUNS)  # triple adj
    
    total_phrases = short + medium + long_p
    
    # Mutations per phrase
    seps = len(SEPARATORS)
    cases = 10  # case_variants generates ~10
    trails = len(TRAILING_PATTERNS)
    leet_factor = 6  # Average leet variants per phrase (3^n combinations, limited to 3 per word)
    
    passphrase_total = total_phrases * seps * cases * trails * (1 + leet_factor)
    
    # Simple spite estimate
    simple = 28 * 42 * 3 + 15 * 40 + 38 * 7 + 16 * (1 + 30 + 15 * 16) + 10 * (1 + 15 + 6)
    
    # Elongated estimate
    elongated = 10 * 35 * (1 + 25 + 9 * (1 + 20 + 2 * (1 + 20)))
    
    return {
        "phrases": total_phrases,
        "passphrase_candidates": passphrase_total,
        "simple_spite": simple,
        "elongated": elongated,
        "total": passphrase_total + simple + elongated,
        "trailing_patterns": len(TRAILING_PATTERNS),
        "adjectives": len(ALL_ADJECTIVES),
        "nouns": len(EXTENDED_NOUNS),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate ~10B passphrase candidates")
    parser.add_argument("--estimate", action="store_true", help="Show estimate")
    parser.add_argument("--limit", type=int, help="Limit output")
    
    args = parser.parse_args()
    
    if args.estimate:
        est = estimate_count()
        print(f"Estimated total: {est['total']:,}")
        print(f"  Base phrases: {est['phrases']:,}")
        print(f"  Passphrase candidates: {est['passphrase_candidates']:,}")
        print(f"  Simple spite: {est['simple_spite']:,}")
        print(f"  Elongated: {est['elongated']:,}")
        print(f"  Trailing patterns: {est['trailing_patterns']}")
        print(f"  Adjectives: {est['adjectives']}")
        print(f"  Nouns: {est['nouns']}")
        return
    
    count = 0
    limit = args.limit or float("inf")
    
    for candidate in generate_all():
        print(candidate)
        count += 1
        if count >= limit:
            break
    
    print(f"Generated {count:,} candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
