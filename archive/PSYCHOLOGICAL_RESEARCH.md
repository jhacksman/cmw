# Psychological Research: Password Memory Activation

## Overview

This document outlines the psychological approach to helping Dean Pierce remember his Bitcoin wallet password from December 2011. The strategy combines nostalgia-based memory activation with A/B testing to narrow down the password search space.

## Theoretical Basis

### Memory Activation Through Context Recreation

Research in cognitive psychology suggests that memories are more easily retrieved when the retrieval context matches the encoding context (Encoding Specificity Principle - Tulving & Thomson, 1973). By recreating the mental and emotional context of December 2011, we aim to activate the neural pathways associated with the password creation event.

### Key Contextual Elements

1. **Temporal Context**: CMU Winter Break 2011 (approximately December 15, 2011 - January 10, 2012)
2. **Social Context**: Dean's brother was home for the holidays
3. **Cultural Context**: Occupy Wall Street movement, Bitcoin 0.5.0 release, 2011 memes
4. **Emotional Context**: The "spite password" hypothesis - Dean may have chosen something deliberately dumb

## A/B Test Questions

The following 10 questions are designed to narrow down the password search space based on Dean's likely preferences:

### Question 1: Separators
**Options:**
- A) Spaces ("this is bad")
- B) No separator ("thisisbad")
- C) Periods ("this.is.bad")

**Rationale**: Dean mentioned in Signal chat that spaces feel more natural than concatenated words.

### Question 2: Capitalization
**Options:**
- A) all lowercase
- B) First word capitalized
- C) Title Case Each Word

**Rationale**: Based on Dean's casual writing style in commits and messages.

### Question 3: Trailing Characters
**Options:**
- A) None
- B) Numbers (123, 403, 2011)
- C) Punctuation (!, ?, ~)
- D) Both (123!, 403?)

**Rationale**: Dean confirmed using trailing chars: "1, 3, maybe 6, exclamations or question marks sometimes tildes or back ticks"

### Question 4: Leetspeak Usage
**Options:**
- A) No leetspeak
- B) Light (@ for a, $ for s)
- C) Heavy (p@$$w0rd)

**Rationale**: Dean mentioned "p455, p@$$, and combinations" but never uses 7 for R or | for anything.

### Question 5: Password Theme
**Options:**
- A) "Spite" password (dumb/bad/stupid)
- B) Common phrase
- C) Personal reference
- D) Random words

**Rationale**: The "spite password" hypothesis from Telegram: "something embarrassingly stupid"

### Question 6: Word Count
**Options:**
- A) Short (2-3 words)
- B) Medium (4-5 words)
- C) Long (6-8 words)

**Rationale**: Dean said "more than my usual 3-4 words, maybe 5, 6, or 7"

### Question 7: Character Length Target
**Options:**
- A) Minimum (exactly 10 chars)
- B) Comfortable (12-16 chars)
- C) Long (17+ chars)

**Rationale**: Bitcoin wallet prompted "10 or more characters, or eight or more words"

### Question 8: Potato/Poop References
**Options:**
- A) Likely included
- B) Probably not
- C) Maybe elongated (pooooop)

**Rationale**: Dean's Mastodon uses potato emoji, and "poop" appears in his LUKS password pattern.

### Question 9: "X is hard" Pattern
**Options:**
- A) Sounds like something I'd use
- B) Not my style

**Rationale**: Dean's GitHub commits frequently use "tables are hard", "spelling is hard", etc.

### Question 10: 2011 References
**Options:**
- A) Bitcoin-related
- B) Memes (nyan, derp, lulz)
- C) Events (occupy, etc)
- D) No 2011 references

**Rationale**: Determine if the password contains temporal markers.

## Nostalgia Website Design

### Visual Elements
- Floating headlines from September-December 2011 Occupy movement
- 2011 memes (Nyan Cat, Futurama Fry, etc.)
- Bitcoin wallet encryption dialog mimicking 2011 Bitcoin-Qt

### Audio Elements
- 2011 pop hits (Party Rock Anthem, Rolling in the Deep)
- Hacker culture music (Sandstorm, ytcracker, nerdcore)
- Angry Birds theme

### Interactive Elements
- A/B test questions
- Password guess input (5 fields)
- 2011 browser games (QWOP, Robot Unicorn Attack)

## Timeline Narrative Structure

The floating timeline follows a 4-act narrative structure:

### Act 1: September - The Spark
- September 17: Occupy Wall Street begins
- September 23: Bitcoin 0.4.0 released (wallet encryption introduced)
- "We are the 99%" slogan spreads

### Act 2: October - The Surge
- October 6: Occupy Portland begins (4,000+ march)
- October 9: Occupy spreads to 70+ cities
- October 15: Global Day of Action (900+ cities)

### Act 3: November - The Crackdown
- November 13: Police evict Occupy Portland
- November 15: NYPD raids Zuccotti Park
- November 17: National Day of Action (400 arrested)
- November 21: Bitcoin 0.5.0 released

### Act 4: December - The Ports & Winter Break
- December 12: Occupy the Ports action
- December 17: Kim Jong-il dies
- December 20-January 10: CMU Winter Break (password likely set)
- January 1, 2012: New Year

## Expected Outcomes

By combining the A/B test results with the password guesses entered while in a nostalgic state, we expect to:

1. Narrow the search space from billions to millions of candidates
2. Identify the most likely password patterns
3. Generate a targeted wordlist based on Dean's actual preferences

## Next Steps

1. Deploy the nostalgia website
2. Have Dean (or someone acting as Dean) complete the A/B test
3. Collect the 5 password guesses
4. Analyze results to create a new, targeted password generator
5. Run the generator against the wallet hash
