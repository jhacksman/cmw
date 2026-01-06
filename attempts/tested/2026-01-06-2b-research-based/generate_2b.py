#!/usr/bin/env python3
"""
Crack My Wallet - 2-3 Billion Password Generator (Research-Based)

This script generates approximately 2-3 billion passphrase candidates focusing on
patterns identified from comprehensive research of pierce403's GitHub, blog, and
social media that were NOT fully covered in the previous 10B attempt.

Target: ~2,500,000,000 candidates

KEY GAPS FROM PREVIOUS 10B ATTEMPT:
1. "X is/are hard" pattern - Dean's signature phrase NOT systematically covered
2. Potato-specific patterns - Confirmed significant (emoji in Mastodon display name)
3. Blog-derived phrases from 2011 - "just for kicks", "dead simple", etc.
4. Expletive patterns - "damn", "shit", "fuck", "crap"
5. Vim typos - "!wq" endings
6. "derp-de-doo" and similar patterns
7. Specific 2011 memes as standalone/combined

Evidence from Dean (px):
- Signal: "Spaces. Maybe periods." for separators
- Signal: "4-7 words" (more than his usual 3-4)
- Signal: Trailing chars "1, 3, maybe 6" - !, ?, ~, `
- Signal: Leetspeak "p455, p@$$" - @ for a, $ for s, NEVER 7 for r
- Telegram: "I definitely set my password to the weakest possible thing I could out of spite"
- Telegram: "I think it was something like 16 characters"

Optimized for DGX Spark (GB10 Grace Blackwell):
- Streaming output (no memory-hungry deduplication)
- Deterministic ordering for reproducibility

Usage:
    python generate_2b.py > wordlist.txt
    python generate_2b.py --estimate
    python generate_2b.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
"""

import argparse
import itertools
import sys
from typing import Iterator, List

# ============================================================================
# PRIORITY 1: "X IS/ARE HARD" PATTERN (Dean's signature) - MASSIVELY EXPANDED
# ============================================================================

HARD_SUBJECTS = [
    "tables", "spelling", "datatypes", "numbers", "markdown", "flask", "typing",
    "copypasta", "grammar", "USB", "plex", "git", "vim", "emacs", "linux",
    "passphrases", "passwords", "passphrase", "password", "security", "crypto",
    "bitcoin", "encryption", "keys", "wallets", "secrets", "credentials",
    "authentication", "logins", "accounts", "tokens", "hashes", "salts",
    "computers", "programming", "coding", "hacking", "debugging", "testing",
    "javascript", "python", "ruby", "perl", "php", "java", "golang", "rust",
    "databases", "sql", "postgres", "mysql", "mongodb", "redis", "networking",
    "memory", "pointers", "threads", "async", "callbacks", "promises",
    "css", "html", "json", "xml", "yaml", "regex", "unicode", "encoding",
    "time", "dates", "timezones", "floating point", "rounding", "math",
    "life", "everything", "things", "stuff", "work", "money", "adulting",
    "relationships", "communication", "decisions", "choices", "planning",
    "mornings", "mondays", "meetings", "emails", "deadlines", "projects",
]

STUPID_SUBJECTS = [
    "javascript", "CSP", "postgres", "modal stuff", "this", "that", "everything",
    "passphrases", "passwords", "passphrase", "password", "security", "crypto",
    "bitcoin", "encryption", "wallets", "computers", "programming", "life",
    "internet explorer", "windows", "flash", "java applets", "activeX",
    "captchas", "cookies", "popups", "ads", "spam", "phishing",
    "meetings", "emails", "bureaucracy", "paperwork", "forms", "taxes",
]

HARD_ADJECTIVES = ["hard", "difficult", "tough", "tricky", "complicated", "complex",
                   "confusing", "frustrating", "annoying", "painful", "tedious"]
STUPID_ADJECTIVES = ["stupid", "dumb", "dumber", "idiotic", "moronic", "asinine",
                     "ridiculous", "absurd", "insane", "crazy", "bonkers", "nuts"]

INTENSIFIERS = ["", "really", "very", "so", "super", "extremely", "incredibly",
                "fucking", "freaking", "damn", "bloody", "hella", "mad", "wicked"]

def generate_x_is_hard() -> Iterator[str]:
    verbs = ["is", "are", "was", "were", "aint"]
    for subject in HARD_SUBJECTS:
        for verb in verbs:
            for adj in HARD_ADJECTIVES[:8]:
                yield f"{subject} {verb} {adj}"
                for intens in INTENSIFIERS[1:7]:
                    yield f"{subject} {verb} {intens} {adj}"
    for subject in STUPID_SUBJECTS:
        for verb in verbs:
            for adj in STUPID_ADJECTIVES[:8]:
                yield f"{subject} {verb} {adj}"
                for intens in INTENSIFIERS[1:7]:
                    yield f"{subject} {verb} {intens} {adj}"
    prefixes = ["this", "my", "the", "a", "your", "one"]
    for prefix in prefixes:
        for subject in ["passphrase", "password", "thing", "stuff", "code"]:
            for verb in ["is", "was", "aint"]:
                for adj in HARD_ADJECTIVES[:8] + STUPID_ADJECTIVES[:8]:
                    yield f"{prefix} {subject} {verb} {adj}"
                    for intens in INTENSIFIERS[1:6]:
                        yield f"{prefix} {subject} {verb} {intens} {adj}"

# ============================================================================
# PRIORITY 2: POTATO PATTERNS
# ============================================================================

POTATO_BASES = [
    "potato", "potatoes", "tater", "taters", "spud", "spuds",
    "potato potato", "potato potato potato", "tater tater", "spud spud",
    "i am a potato", "im a potato", "i am potato", "im potato",
    "this is potato", "potato passphrase", "potato password",
    "derpy potato", "stupid potato", "dumb potato", "silly potato",
    "potato is life", "potato is love", "all hail potato", "praise potato",
    "potato derp", "derp potato derp", "potato lulz", "lulz potato",
    "hot potato", "couch potato", "small potato", "big potato",
    "potato salad", "baked potato", "mashed potato", "french fries",
    "potato quality", "potato pc", "potato computer", "potato server",
    "such potato", "much potato", "very potato", "wow potato",
    "potato gonna potate", "haters gonna hate potatoes gonna potate",
]

def generate_potato_patterns() -> Iterator[str]:
    yield from POTATO_BASES
    for base in POTATO_BASES:
        for num in ["1", "2", "3", "11", "69", "420", "2011", "123", "1234"]:
            yield f"{base}{num}"
            yield f"{base} {num}"
            yield f"{num}{base}"
    for count in range(3, 30):
        yield "pot" + "a" * count + "to"
        yield "potat" + "o" * count
        yield "p" + "o" * count + "tato"

# ============================================================================
# PRIORITY 3: 2011 BLOG-DERIVED PHRASES
# ============================================================================

BLOG_PHRASES_2011 = [
    "just for kicks", "just for fun", "just for lulz", "just for the lulz",
    "just for giggles", "just for shits and giggles", "for shits and giggles",
    "dead simple", "dead easy", "dead obvious", "brain dead simple",
    "shoot your foot off", "shoot yourself in the foot", "footgun",
    "write some damn code", "write some code", "just write code",
    "shut up and code", "less talk more code", "code monkey",
    "oh no", "oh no oh no", "oh noes", "oh nooo", "oh noooo",
    "oh shit", "oh crap", "oh fuck", "oh damn", "oh hell",
    "shitposting on reddit", "shitposting", "shitpost", "quality shitpost",
    "shut up thats why", "shut up", "because shut up", "thats why",
    "if its stupid and it works", "if it works its not stupid",
    "stupid but it works", "it works so shut up", "works for me",
    "pain in the ass", "pain in my ass", "what a pain", "such a pain",
    "the ever loving crap", "ever loving crap", "beat the crap out of",
    "yolo", "hashtag yolo", "yolo swag", "swag", "yeet", "no ragrets",
    "hold my beer", "watch this", "here goes nothing", "fuck it",
    "whatever works", "good enough", "ship it", "done is better than perfect",
]

def generate_blog_phrases() -> Iterator[str]:
    yield from BLOG_PHRASES_2011
    for phrase in BLOG_PHRASES_2011:
        yield f"{phrase} passphrase"
        yield f"{phrase} password"
        yield f"my {phrase}"
        yield f"this is {phrase}"

# ============================================================================
# PRIORITY 4: EXPLETIVE PATTERNS
# ============================================================================

EXPLETIVES = ["damn", "shit", "fuck", "crap", "ass", "hell", "bloody", "frickin", "freaking"]

EXPLETIVE_PHRASES = [
    "damn passphrase", "damn password", "damn it", "god damn", "god damn it",
    "damn this passphrase", "this damn passphrase", "damn stupid passphrase",
    "damn this password", "this damn password", "damn stupid password",
    "shit passphrase", "shit password", "this is shit", "what a shit passphrase",
    "shitty passphrase", "shitty password", "piece of shit", "total shit",
    "holy shit", "no shit", "bullshit", "horseshit", "dipshit",
    "fuck this passphrase", "fuck this password", "fuck it", "fuck this",
    "fucking passphrase", "fucking password", "what the fuck", "wtf",
    "fuck off", "fuck you", "fuck me", "fuck my life", "fml",
    "crap passphrase", "crap password", "this is crap", "what crap",
    "crappy passphrase", "crappy password", "load of crap", "pile of crap",
    "ass passphrase", "ass password", "dumbass", "jackass", "smartass",
    "pain in the ass", "kick ass", "badass", "half assed",
    "holy shit", "holy crap", "holy fuck", "what the hell",
    "oh shit", "oh crap", "oh fuck", "oh hell", "oh damn",
    "for fucks sake", "for gods sake", "for crying out loud",
]

def generate_expletive_patterns() -> Iterator[str]:
    yield from EXPLETIVE_PHRASES
    for exp in EXPLETIVES:
        for adj in ["bad", "dumb", "stupid", "weak", "terrible", "awful", "shitty"]:
            yield f"{exp} {adj} passphrase"
            yield f"{exp} {adj} password"
            yield f"this {exp} {adj} passphrase"
            yield f"this {exp} {adj} password"
            yield f"my {exp} {adj} passphrase"
            yield f"what a {exp} {adj} passphrase"

# ============================================================================
# PRIORITY 5: VIM TYPOS
# ============================================================================

VIM_SUFFIXES = ["!wq", ":wq", "!wq!", ":wq!", "wq", "!q", ":q", ":q!",
                ":w", ":x", "ZZ", "ZQ", ":wq!!", "!wq!!", ":wqa", ":qa"]

def generate_vim_typo_patterns() -> Iterator[str]:
    bases = [
        "first commit", "initial commit", "first password", "my passphrase",
        "this is my passphrase", "bad passphrase", "dumb passphrase",
        "stupid passphrase", "weak passphrase", "test", "testing",
        "this is a test", "hello world", "foo bar", "asdf", "qwerty",
        "password", "passphrase", "secret", "login", "admin",
        "this passphrase", "my password", "the password", "a password",
    ]
    for base in bases:
        for suffix in VIM_SUFFIXES:
            yield f"{base}{suffix}"
            yield f"{base} {suffix}"
            yield f"{base}{suffix}!"
            yield f"{base}{suffix}!!"

# ============================================================================
# PRIORITY 6: DERP PATTERNS
# ============================================================================

DERP_PATTERNS = [
    "derp", "derpy", "derp derp", "derp derp derp", "derp derp derp derp",
    "derp de doo", "derp de derp", "derpy derp", "derp a derp",
    "heh derp", "lol derp", "derp lol", "derpy doo", "derpity derp",
    "the derp de doo", "derp de doo who", "derpy derpy derp",
    "herp derp", "herp a derp", "herp de derp", "herpaderp",
    "derp passphrase", "derpy passphrase", "derp password", "derpy password",
    "this is derpy", "this is so derpy", "derpy as fuck", "derpy as hell",
    "derp de doo passphrase", "derpy doo passphrase", "herpaderp passphrase",
    "durr", "durr hurr", "hurr durr", "durr durr durr",
]

def generate_derp_patterns() -> Iterator[str]:
    yield from DERP_PATTERNS
    for count in range(3, 25):
        yield "d" + "e" * count + "rp"
        yield "derp" + "y" * count
        yield "h" + "e" * count + "rp"
        yield "d" + "u" * count + "rr"

# ============================================================================
# PRIORITY 7: 2011 MEMES
# ============================================================================

MEME_2011 = [
    "lulz", "for the lulz", "for lulz", "lulzy", "lulz passphrase",
    "lulz password", "this is lulz", "so lulz", "much lulz", "many lulz",
    "i did it for the lulz", "all for the lulz", "lulz were had",
    "rofl", "roflmao", "roflcopter", "rofl passphrase", "rofl password",
    "roflwaffle", "roflcake", "roflstomp",
    "lol", "lolol", "lololol", "lolololol", "lol passphrase", "lol password",
    "lol wut", "lol what", "lol nope", "lol no", "lol yes", "lol ok",
    "lolwut", "lawl", "lawlz", "lel", "kek", "topkek",
    "lulz rofl", "rofl lulz", "lol lulz", "derp lulz rofl",
    "potato lulz", "lulz potato", "derp potato lulz", "lulz derp potato",
    "epic fail", "epic win", "fail", "winning", "u mad bro", "u mad",
    "cool story bro", "cool story", "problem", "no problem", "y u no",
    "troll", "trolling", "trollface", "trololo", "trololol",
    "forever alone", "me gusta", "rage face", "fffffffuuuuuuuuuuuu",
    "challenge accepted", "like a boss", "nailed it", "close enough",
    "not bad", "okay face", "true story", "seems legit",
    "one does not simply", "all the things", "x all the things",
    "brace yourselves", "winter is coming", "you shall not pass",
    "its over 9000", "over 9000", "what 9000",
    "arrow to the knee", "i used to", "but then i took",
    "aint nobody got time for that", "nobody got time",
    "do you even lift", "come at me bro", "do you even",
]

def generate_2011_memes() -> Iterator[str]:
    yield from MEME_2011
    for meme in MEME_2011[:40]:
        yield f"{meme} passphrase"
        yield f"{meme} password"

# ============================================================================
# SEPARATORS AND TRAILING PATTERNS - EXPANDED FOR 2-3B
# ============================================================================

SEPARATORS = [" ", ".", "-", "_", ""]

def generate_trailing_patterns() -> List[str]:
    patterns = [""]
    chars = ["!", "?", "~", "`", ".", "*", "#", "@"]
    
    # 1 char
    patterns.extend(chars)
    patterns.extend([str(i) for i in range(10)])
    
    # 2 chars
    for c in chars:
        patterns.append(c * 2)
        for d in [str(i) for i in range(10)]:
            patterns.append(c + d)
            patterns.append(d + c)
    for i in range(10):
        for j in range(10):
            patterns.append(f"{i}{j}")
    
    # 3 chars
    for c in chars:
        patterns.append(c * 3)
    patterns.extend(["111", "123", "321", "000", "420", "666", "777", "888", "999",
                     "!11", "?11", "~11", "`11", "11!", "11?", "!?!", "?!?", "!1!",
                     "abc", "xyz", "qwe", "asd", "zxc"])
    
    # 4 chars
    for c in chars[:5]:
        patterns.append(c * 4)
    patterns.extend(["1234", "4321", "1111", "0000", "2011", "2010", "2012"])
    
    # 5 chars
    for c in chars[:4]:
        patterns.append(c * 5)
    patterns.extend(["12345", "54321", "11111", "00000"])
    
    # 6 chars
    for c in chars[:6]:
        patterns.append(c * 6)
    patterns.extend(["111111", "123456", "654321", "000000", "!!!111", "???111",
                     "qwerty", "asdfgh", "zxcvbn", "abcdef"])
    
    # Year patterns
    patterns.extend(["2011", "2010", "2012", "11", "10", "12"])
    patterns.extend(["2011!", "!2011", "2011!!", "!!2011", "2011!!!", "!!!2011"])
    
    return list(set(patterns))

TRAILING_PATTERNS = generate_trailing_patterns()

# ============================================================================
# LEETSPEAK
# ============================================================================

LEET_CHAR = {
    "a": ["a", "@", "4"],
    "s": ["s", "$", "5"],
    "e": ["e", "3"],
    "i": ["i", "1", "!"],
    "o": ["o", "0"],
    "l": ["l", "1"],
    "t": ["t", "+"],
}

LEET_WORDS = {
    "pass": ["pass", "p455", "p@$$", "p4$$", "p@55", "pa55", "p@ss", "p4ss"],
    "password": ["password", "p455word", "p@$$word", "p4$$word", "p@55word", 
                 "pa55word", "p@ssword", "passw0rd", "p455w0rd", "p@$$w0rd",
                 "p4ssword", "p4ssw0rd", "pa$$word", "pa55w0rd"],
    "passphrase": ["passphrase", "p455phrase", "p@$$phrase", "p4$$phrase",
                   "passphr4se", "p455phr4se", "p@$$phr4se", "p4ssphr4se",
                   "p@ssphr@se", "p455phr@se", "pa55phrase", "pa55phr4se"],
    "bad": ["bad", "b4d", "b@d"],
    "dumb": ["dumb", "d0mb", "durnb"],
    "stupid": ["stupid", "stup1d", "5tupid", "5tup1d", "s+upid"],
    "hard": ["hard", "h4rd", "h@rd"],
    "this": ["this", "th1s", "+his", "+h1s"],
    "is": ["is", "1s", "!s"],
    "are": ["are", "4re", "@re"],
    "shit": ["shit", "sh1t", "$hit", "$h1t"],
    "fuck": ["fuck", "fvck", "f*ck", "phuck"],
    "damn": ["damn", "d4mn", "d@mn"],
}

def leet_variants(word: str) -> Iterator[str]:
    w = word.lower()
    if w in LEET_WORDS:
        yield from LEET_WORDS[w]
    else:
        yield word
        for char, subs in LEET_CHAR.items():
            if char in w:
                for sub in subs[1:]:
                    yield w.replace(char, sub, 1)

def leet_phrase(phrase: str) -> Iterator[str]:
    words = phrase.split()
    if not words:
        yield phrase
        return
    word_variants = [list(leet_variants(w))[:6] for w in words]
    for combo in itertools.product(*word_variants):
        yield " ".join(combo)

# ============================================================================
# CASE VARIATIONS - EXPANDED
# ============================================================================

def case_variants(phrase: str) -> Iterator[str]:
    yield phrase.lower()
    yield phrase.upper()
    yield phrase.title()
    if phrase:
        yield phrase[0].upper() + phrase[1:].lower()
    if len(phrase) <= 50:
        yield "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(phrase))
        yield "".join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(phrase))
    words = phrase.split()
    if len(words) > 1:
        yield words[0].upper() + " " + " ".join(w.lower() for w in words[1:])
        yield " ".join(w.lower() for w in words[:-1]) + " " + words[-1].upper()

# ============================================================================
# COMBINED HIGH-PROBABILITY PATTERNS
# ============================================================================

def generate_combined_high_prob() -> Iterator[str]:
    prefixes = [
        "this is a", "this is my", "this is the", "this is one",
        "i have a", "i made a", "i set a", "heres a", "heres my",
        "i chose a", "i picked a", "i used a", "i created a",
        "what a", "such a", "one", "another", "yet another",
        "this is a really", "this is a very", "this is such a",
        "i have a really", "i made a really", "what a really",
    ]
    adjectives = [
        "bad", "dumb", "stupid", "terrible", "awful", "weak", "simple",
        "derpy", "shitty", "crappy", "lame", "pathetic", "lazy",
        "ridiculous", "idiotic", "moronic", "asinine", "inane",
        "horrible", "atrocious", "abysmal", "dreadful", "appalling",
        "fucking", "goddamn", "damn", "freaking", "bloody",
    ]
    nouns = ["passphrase", "password", "pass", "passwd", "secret", "key", "phrase"]
    
    for prefix in prefixes:
        for adj in adjectives:
            for noun in nouns:
                yield f"{prefix} {adj} {noun}"

# ============================================================================
# MAIN GENERATOR WITH FULL MUTATIONS
# ============================================================================

def apply_all_mutations(base: str, include_leet: bool = True, leet_trail_limit: int = 40) -> Iterator[str]:
    for sep in SEPARATORS:
        sep_phrase = sep.join(base.split())
        for cased in case_variants(sep_phrase):
            for trail in TRAILING_PATTERNS:
                yield cased + trail
            if include_leet:
                for leet in leet_phrase(cased):
                    if leet != cased:
                        for trail in TRAILING_PATTERNS[:leet_trail_limit]:
                            yield leet + trail

def generate_all() -> Iterator[str]:
    # Priority 1: X is/are hard (HIGHEST - Dean's signature)
    for base in generate_x_is_hard():
        yield from apply_all_mutations(base, include_leet=True, leet_trail_limit=50)
    
    # Combined high-probability patterns
    for base in generate_combined_high_prob():
        yield from apply_all_mutations(base, include_leet=True, leet_trail_limit=50)
    
    # Priority 2: Potato (confirmed significant)
    for base in generate_potato_patterns():
        yield from apply_all_mutations(base, include_leet=False)
    
    # Priority 3: Blog phrases (2011 era)
    for base in generate_blog_phrases():
        yield from apply_all_mutations(base, include_leet=True, leet_trail_limit=40)
    
    # Priority 4: Expletives
    for base in generate_expletive_patterns():
        yield from apply_all_mutations(base, include_leet=True, leet_trail_limit=40)
    
    # Priority 5: Vim typos
    for base in generate_vim_typo_patterns():
        yield from apply_all_mutations(base, include_leet=False)
    
    # Priority 6: Derp patterns
    for base in generate_derp_patterns():
        yield from apply_all_mutations(base, include_leet=False)
    
    # Priority 7: 2011 memes
    for base in generate_2011_memes():
        yield from apply_all_mutations(base, include_leet=False)

def estimate_count() -> dict:
    # Count bases
    p1 = sum(1 for _ in generate_x_is_hard())
    combined = sum(1 for _ in generate_combined_high_prob())
    p2 = sum(1 for _ in generate_potato_patterns())
    p3 = sum(1 for _ in generate_blog_phrases())
    p4 = sum(1 for _ in generate_expletive_patterns())
    p5 = sum(1 for _ in generate_vim_typo_patterns())
    p6 = sum(1 for _ in generate_derp_patterns())
    p7 = sum(1 for _ in generate_2011_memes())
    
    seps = len(SEPARATORS)
    cases = 8
    trails = len(TRAILING_PATTERNS)
    leet_factor = 4
    
    p1_total = p1 * seps * cases * trails * (1 + leet_factor * 0.5)
    combined_total = combined * seps * cases * trails * (1 + leet_factor * 0.5)
    p2_total = p2 * seps * cases * trails
    p3_total = p3 * seps * cases * trails * (1 + leet_factor * 0.4)
    p4_total = p4 * seps * cases * trails * (1 + leet_factor * 0.4)
    p5_total = p5 * seps * cases * trails
    p6_total = p6 * seps * cases * trails
    p7_total = p7 * seps * cases * trails
    
    total = p1_total + combined_total + p2_total + p3_total + p4_total + p5_total + p6_total + p7_total
    
    return {
        "priority_1_x_is_hard": int(p1_total),
        "combined_high_prob": int(combined_total),
        "priority_2_potato": int(p2_total),
        "priority_3_blog": int(p3_total),
        "priority_4_expletives": int(p4_total),
        "priority_5_vim": int(p5_total),
        "priority_6_derp": int(p6_total),
        "priority_7_memes": int(p7_total),
        "total": int(total),
        "trailing_patterns": len(TRAILING_PATTERNS),
        "base_counts": {"p1": p1, "combined": combined, "p2": p2, "p3": p3, 
                        "p4": p4, "p5": p5, "p6": p6, "p7": p7}
    }

def main():
    parser = argparse.ArgumentParser(description="Generate ~2-3B research-based candidates")
    parser.add_argument("--estimate", action="store_true", help="Show estimate")
    parser.add_argument("--limit", type=int, help="Limit output")
    
    args = parser.parse_args()
    
    if args.estimate:
        est = estimate_count()
        print(f"Estimated total: {est['total']:,}")
        print(f"  Priority 1 (X is/are hard): {est['priority_1_x_is_hard']:,}")
        print(f"  Combined high-prob: {est['combined_high_prob']:,}")
        print(f"  Priority 2 (Potato): {est['priority_2_potato']:,}")
        print(f"  Priority 3 (Blog phrases): {est['priority_3_blog']:,}")
        print(f"  Priority 4 (Expletives): {est['priority_4_expletives']:,}")
        print(f"  Priority 5 (Vim typos): {est['priority_5_vim']:,}")
        print(f"  Priority 6 (Derp): {est['priority_6_derp']:,}")
        print(f"  Priority 7 (2011 memes): {est['priority_7_memes']:,}")
        print(f"  Trailing patterns: {est['trailing_patterns']}")
        print(f"\nBase phrase counts: {est['base_counts']}")
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
