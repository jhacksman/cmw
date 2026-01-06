#!/usr/bin/env python3
"""
Generator for "dumbest possible" 8-word passphrase patterns.

Based on Telegram deep dive findings:
- Dean's example: "this is a very bad password" (6 words)
- He said "I came up with the dumbest passphrase I could that matched the requirements"
- The advisory was "10 or more characters, OR eight or more words"
- Separators: spaces (most likely), dots (sometimes)
- Trailing chars: !?~`123

If Dean went the 8-word route, he'd pick the absolute dumbest 8-word phrase.
"""

import sys
from itertools import product, combinations_with_replacement

# Separators Dean uses
SEPARATORS = [' ', '.']

# Trailing characters Dean mentioned
TRAILING_CHARS = ['', '!', '?', '~', '`', '1', '2', '3', '!!', '???', '123']

# Case transformation functions
def case_variants(phrase):
    """Generate case variants of a phrase."""
    yield phrase.lower()
    yield phrase.upper()
    yield phrase.title()
    # First word capitalized only
    words = phrase.split()
    if words:
        yield words[0].capitalize() + ' ' + ' '.join(w.lower() for w in words[1:])


def generate_extended_this_is():
    """
    "this is a very bad password" + 2 more words to make 8.
    """
    base = "this is a very bad password"
    extensions = [
        "for real", "I think", "or something", "you know",
        "ha ha", "lol lol", "so dumb", "so stupid",
        "trust me", "believe me", "no really", "for sure",
        "I guess", "I suppose", "oh well", "too bad",
        "right now", "oh no", "my bad", "so bad",
        "very bad", "real bad", "super bad", "mega bad",
        "duh duh", "blah blah", "yada yada", "etc etc",
    ]
    
    for ext in extensions:
        phrase = base + " " + ext
        for sep in SEPARATORS:
            for case_var in case_variants(phrase):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def generate_sentence_8word():
    """
    Complete 8-word sentence-style phrases.
    """
    sentences = [
        "this is the dumbest password I could think",
        "this is the stupidest password I ever made",
        "this is a really really bad password",
        "this is a very very bad password",
        "this is a super duper bad password",
        "this password is really really really bad",
        "I made this password really really dumb",
        "what a dumb password this really is",
        "this is the worst password ever made",
        "I cannot believe how dumb this is",
        "why did I make this so dumb",
        "this is stupid and I hate it",
        "I hate this stupid password so much",
        "this is a bad password for sure",
        "this is not a good password really",
        "password password password password password password password password",
        "bad bad bad bad bad bad bad bad",
        "dumb dumb dumb dumb dumb dumb dumb dumb",
        "this this this this this this this this",
        "poop poop poop poop poop poop poop poop",
    ]
    
    for sentence in sentences:
        for sep in SEPARATORS:
            for case_var in case_variants(sentence):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def generate_repeated_word():
    """
    Single word repeated 8 times.
    """
    words = [
        "bad", "dumb", "stupid", "poop", "potato", "password",
        "pass", "word", "test", "asdf", "qwerty", "derp",
        "lol", "haha", "meh", "blah", "foo", "bar",
        "this", "is", "a", "the", "very", "really",
        "super", "duper", "mega", "ultra", "weak", "duh",
    ]
    
    for word in words:
        phrase = ' '.join([word] * 8)
        for sep in SEPARATORS:
            for case_var in case_variants(phrase):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def generate_mixed_repeated():
    """
    Two words alternating or split (e.g., "bad bad bad bad dumb dumb dumb dumb").
    """
    words = ["bad", "dumb", "stupid", "poop", "password", "pass", "word", "this", "is", "a"]
    
    for w1 in words:
        for w2 in words:
            if w1 != w2:
                # 4 + 4 pattern
                phrase = ' '.join([w1] * 4 + [w2] * 4)
                for sep in SEPARATORS:
                    for case_var in case_variants(phrase):
                        base_phrase = case_var.replace(' ', sep)
                        for trail in TRAILING_CHARS:
                            yield base_phrase + trail
                
                # Alternating pattern
                phrase = ' '.join([w1, w2] * 4)
                for sep in SEPARATORS:
                    for case_var in case_variants(phrase):
                        base_phrase = case_var.replace(' ', sep)
                        for trail in TRAILING_CHARS:
                            yield base_phrase + trail


def generate_dean_style():
    """
    Dean's commit-message style as 8-word phrases.
    """
    phrases = [
        "tables are hard and so is this",
        "spelling is hard and passwords are too",
        "everything is terrible and nothing works right",
        "this is stupid and I hate it",
        "I hate this stupid password so much",
        "why did I make this so dumb",
        "this is the worst password ever made",
        "I cannot believe how dumb this is",
        "passwords are hard and I am dumb",
        "security is hard and this is dumb",
        "encryption is hard and passwords are dumb",
        "this password is dumb and I know",
        "I know this password is really dumb",
        "what a stupid password this really is",
        "this is a really stupid password here",
        "here is a really stupid password lol",
    ]
    
    for phrase in phrases:
        for sep in SEPARATORS:
            for case_var in case_variants(phrase):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def generate_adjective_combos():
    """
    "this is a [adj] [adj] [adj] [adj] password" with various adjectives.
    """
    adjectives = ["bad", "dumb", "stupid", "very", "really", "super", "terrible", "awful", "weak", "lame"]
    
    # Generate all 4-adjective combinations (with repetition)
    for adj_combo in product(adjectives, repeat=4):
        phrase = f"this is a {adj_combo[0]} {adj_combo[1]} {adj_combo[2]} {adj_combo[3]} password"
        for sep in SEPARATORS:
            for case_var in case_variants(phrase):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def generate_number_words():
    """
    Number words as 8-word phrases.
    """
    phrases = [
        "one two three four five six seven eight",
        "eight seven six five four three two one",
        "zero one two three four five six seven",
        "one one one one one one one one",
        "two two two two two two two two",
        "zero zero zero zero zero zero zero zero",
    ]
    
    for phrase in phrases:
        for sep in SEPARATORS:
            for case_var in case_variants(phrase):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def generate_letter_words():
    """
    Letter sequences as 8-word phrases.
    """
    phrases = [
        "a b c d e f g h",
        "q w e r t y u i",
        "a s d f g h j k",
        "z x c v b n m a",
    ]
    
    for phrase in phrases:
        for sep in SEPARATORS:
            for case_var in case_variants(phrase):
                base_phrase = case_var.replace(' ', sep)
                for trail in TRAILING_CHARS:
                    yield base_phrase + trail


def estimate_count():
    """Estimate total candidate count."""
    # Extended this is: 28 extensions * 2 sep * 4 case * 12 trail = 2688
    extended = 28 * 2 * 4 * 12
    
    # Sentence 8-word: 20 sentences * 2 sep * 4 case * 12 trail = 1920
    sentences = 20 * 2 * 4 * 12
    
    # Repeated word: 30 words * 2 sep * 4 case * 12 trail = 2880
    repeated = 30 * 2 * 4 * 12
    
    # Mixed repeated: 10*9*2 patterns * 2 sep * 4 case * 12 trail = 17280
    mixed = 10 * 9 * 2 * 2 * 4 * 12
    
    # Dean style: 16 phrases * 2 sep * 4 case * 12 trail = 1536
    dean = 16 * 2 * 4 * 12
    
    # Adjective combos: 10^4 combos * 2 sep * 4 case * 12 trail = 960000
    adj = 10000 * 2 * 4 * 12
    
    # Number words: 6 * 2 * 4 * 12 = 576
    numbers = 6 * 2 * 4 * 12
    
    # Letter words: 4 * 2 * 4 * 12 = 384
    letters = 4 * 2 * 4 * 12
    
    total = extended + sentences + repeated + mixed + dean + adj + numbers + letters
    return total


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--estimate':
        count = estimate_count()
        print(f"Estimated candidates: {count:,}")
        print(f"That's approximately {count/1e6:.1f}M")
        return
    
    # Generate all patterns in priority order
    
    # 1. Extended "this is a very bad password"
    for phrase in generate_extended_this_is():
        print(phrase)
    
    # 2. Sentence-style 8-word phrases
    for phrase in generate_sentence_8word():
        print(phrase)
    
    # 3. Dean's commit-style phrases
    for phrase in generate_dean_style():
        print(phrase)
    
    # 4. Repeated single word
    for phrase in generate_repeated_word():
        print(phrase)
    
    # 5. Mixed repeated patterns
    for phrase in generate_mixed_repeated():
        print(phrase)
    
    # 6. Number words
    for phrase in generate_number_words():
        print(phrase)
    
    # 7. Letter words
    for phrase in generate_letter_words():
        print(phrase)
    
    # 8. Adjective combinations (largest category)
    for phrase in generate_adjective_combos():
        print(phrase)


if __name__ == '__main__':
    main()
