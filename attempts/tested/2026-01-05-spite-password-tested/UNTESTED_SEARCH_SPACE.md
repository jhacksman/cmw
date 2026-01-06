# UNTESTED SEARCH SPACE ANALYSIS
## Critical Discovery from Telegram Archive

**Date of Analysis:** 2026-01-05

## KEY FINDING: "Weakest Possible Thing Out of Spite"

From telegram archive, Dean (px) stated:

> "I set the password *right* after they added the feature. I think it was something like 16 characters. I don't think they were doing phrases like that yet. **I definitely set my password to the weakest possible thing I could out of spite.** I should definitely go back and check the git history to see exactly what the requirements were."

## Bitcoin 0.4.0 Password Requirements (from source code)

From `archive/attempt-1/bitcoin-v0.4.0/src/ui.cpp`:

```cpp
strWalletPass = wxGetPasswordFromUser(
    _("Enter the new passphrase to the wallet.\n
      Please use a passphrase of 10 or more random characters,
      or eight or more words."),
    _("Passphrase")).ToStdString();
```

**Requirements:**
- **Option 1:** 10 or more random characters
- **Option 2:** 8 or more words

**NO ENFORCED COMPLEXITY** - no requirement for uppercase, numbers, or special characters!

## The "Spite Password" Theory

If Dean set it to the "weakest possible thing" out of spite:
- He would use **EXACTLY 10 characters** (minimum)
- He would use **simple/common characters** (not random)
- He would make it **memorable but stupid**
- It would **spite the recommendation** of "random characters"

## What Has Actually Been Tested

From README.md (Dean's confirmed tests):
- `?d 1-9` - All digits up to 9 characters ❌ **ONLY 9 CHARS, PASSWORD IS 10+**
- `?l 1-7` - All lowercase up to 7 characters ❌ **ONLY 7 CHARS, PASSWORD IS 10+**
- `?a 1-6` - All ASCII up to 6 characters ❌ **ONLY 6 CHARS, PASSWORD IS 10+**
- `rockyou.txt + best64 / d3ad0ne / dive` ✓ (but may have missed simple patterns)
- `weakpass2a + best64` ✓

**CRITICAL GAP:** 10-character simple passwords have NOT been exhaustively tested!

## Untested Search Spaces

### 1. Simple 10-Character Patterns (HIGHEST PRIORITY)

Dean said "weakest possible thing" - likely means:

**Pattern A: Repeated Simple Words**
```
badpassword  (11 chars - close)
badpasswor   (10 chars - truncated)
dumbpasswo   (10 chars)
password10   (10 chars - password + minimal suffix)
password1!   (10 chars)
passw0rd!!   (10 chars - minimal leet + suffix)
p@ssword!!   (10 chars)
Password1!   (10 chars - meets "complex" checkbox)
Password!!   (10 chars)
```

**Pattern B: Self-Deprecating 10-char**
```
badpass123   (10 chars)
dumbpass1!   (10 chars)
weakpass!!   (10 chars)
simplepass   (10 chars)
easypass12   (10 chars)
lazypass!!   (10 chars)
derpy12345   (10 chars - 2011 slang)
lulzpass!!   (10 chars)
```

**Pattern C: Spite Patterns**
```
aaaaaaaaaa   (10 a's - ultimate spite)
1234567890   (10 digits)
qwertyuiop   (keyboard row)
asdfghjkl;   (keyboard row with semicolon)
password!!   (10 chars - literal)
notasecure   (10 chars - ironic)
insecure10   (10 chars)
```

**Pattern D: Common + Minimal Requirement Met**
```
password1!   (common + number + special)
Password1!   (common + caps + number + special)
Welcome1!    (very common corporate password)
Admin12345   (10 chars)
```

### 2. Keyboard Patterns (10+ chars)

```
qwertyuiop
asdfghjkl
zxcvbnm123
1qaz2wsx3e
!qaz@wsx#e
```

### 3. Repeated Character Patterns

Dean mentioned "pooooooooooooooop" as example of stupid password:

```
aaaaaaaaaa   (10 a's)
1111111111   (10 1's)
aaaaaaaaaa!  (10 a's + !)
passworddd   (10 chars - password with repeated d)
poooooooop   (10 o's between p's)
```

### 4. Number Padding Patterns

```
password01
password02
password03
...
password99
badpass001
badpass123
```

### 5. Common Passwords Extended to 10

```
letmein!!!
welcome!!!
monkey1234
dragon1234
master1234
```

### 6. Defcon/Vegas/2011 Context (10 chars)

```
defcon2011
defcon19!!
vegas2011!
lasvegas11
bitcoin!11
btc2011!!!
```

### 7. "Bad" Variations (10 chars exactly)

```
reallybad!
verybad!!!
sobad12345
toobad!!!!
badstuff!!
```

## What About Multi-Word Passphrases?

Dean said:
- "I don't think they were doing phrases like that yet"
- "I think it was something like 16 characters"
- Set to "weakest possible thing"

**Analysis:**
- Minimum for 8-word phrase would be ~15+ chars ("a a a a a a a a")
- Dean misremembered as 16 chars (close to 8-word minimum)
- BUT he said "weakest possible" which suggests 10-char minimum, not 8-word minimum
- More likely: **10-character simple password**

## Recommendations for New Wordlist

### Tier 1: 10-Character Spite Patterns (UNTESTED!)
- All lowercase common words + padding to 10
- password + numbers/symbols to reach 10
- Keyboard patterns (10 chars)
- Repeated characters (10 chars)
- Common passwords extended to exactly 10

### Tier 2: 11-15 Character Simple Patterns
- badpassword (11)
- dumbpassword (12)
- simplepassword (14)
- Common words + minimal padding

### Tier 3: Minimal Complexity Met
- Password1! (meets typical enterprise requirements)
- Welcome123! (corporate standard)
- Simple word + 1 cap + 1 number + 1 symbol

### Tier 4: Multi-Word (if 10-char fails)
- Two short words (5+5 = 10)
- Three short words with spaces (3+3+3 = 9 + spaces = 11)

## Why This Hasn't Been Tested

1. **Everyone assumed multi-word passphrase** based on Bitcoin prompt "8 or more words"
2. **Brute force stopped at 9 chars** (digits), 7 chars (lowercase), 6 chars (all ASCII)
3. **10-character simple patterns** fall in the gap between:
   - Too long for brute force (10^10 = 10 billion for digits)
   - Too simple for wordlist assumptions (everyone targeted complex passphrases)
4. **Rockyou.txt** has many 10+ char passwords, but:
   - Rules may not have generated exact 10-char variants
   - May have missed specific "spite" patterns

## Attack Strategy

### Method 1: Generate Exact 10-Character Candidates
```bash
# Simple patterns
echo "password1!" > 10char_spite.txt
echo "Password1!" >> 10char_spite.txt
echo "badpass123" >> 10char_spite.txt
# ... (generate all variations)

hashcat -m 11300 -a 0 hash.txt 10char_spite.txt
```

### Method 2: Mask Attack for 10-15 Characters
```bash
# 10 lowercase
hashcat -m 11300 -a 3 hash.txt ?l?l?l?l?l?l?l?l?l?l

# 10 lowercase + digits/symbols at end
hashcat -m 11300 -a 3 hash.txt ?l?l?l?l?l?l?l?l?d?d
hashcat -m 11300 -a 3 hash.txt ?l?l?l?l?l?l?l?l?s?s

# Common password patterns
hashcat -m 11300 -a 3 hash.txt password?d?s
hashcat -m 11300 -a 3 hash.txt Password?d?s
```

### Method 3: Hybrid (Common Words + Padding)
```bash
# Create base words
echo "password" > base_10char.txt
echo "badpass" >> base_10char.txt
echo "simple" >> base_10char.txt

# Hybrid attack with masks to reach 10 chars
hashcat -m 11300 -a 6 hash.txt base_10char.txt ?d?d
hashcat -m 11300 -a 6 hash.txt base_10char.txt ?d?s
```

## Estimated Search Space

### 10 lowercase chars:
- Keyspace: 26^10 = 141 trillion
- With GPU (100 GH/s): ~400 hours
- **FEASIBLE if narrowed to patterns**

### 10 chars (lowercase + common symbols):
- Keyspace: Much smaller if using patterns
- Dictionary of spite patterns: ~10,000 candidates
- **VERY FEASIBLE**

## Conclusion

The most likely untested space is **10-character "spite passwords"** that meet the minimum requirement but are deliberately weak:

1. password1!
2. Password1!
3. badpass123
4. qwertyuiop
5. aaaaaaaaaa
6. 1234567890

This theory is supported by:
- Dean's explicit statement: "weakest possible thing out of spite"
- Bitcoin 0.4.0 requirement: "10 or more random characters"
- Dean's misremembering as "16 characters" (close to 8-word minimum)
- Gap in tested keyspace (stopped at 6-9 characters)

**Recommended Action:** Generate and test 10-character spite password wordlist BEFORE continuing with multi-word passphrases.
