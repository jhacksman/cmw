# Crack My Wallet (CMW)

A collaborative effort to crack Dean Pierce's (px) Bitcoin wallet passphrase. This repository contains all known information, previous attempts, and methodology for continuing the challenge.

## The Challenge

Dean Pierce forgot the passphrase to his Bitcoin wallet containing approximately 25 BTC. He is offering a 5 BTC bounty to anyone who can crack it. The wallet was encrypted using Bitcoin Core 0.4.0+ (released September 2011).

## Technical Specifications

### Hash (for hashcat -m 11300)

```
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
```

### Wallet Addresses

- https://blockchain.info/address/14PEUoKuRB9Q7yfS94cRXh2XugsrBxbxAo
- https://blockchain.info/address/189AfNrrK4a25SKtkwjdF2TZfXmnGt4PcZ

### Wallet Details

- Amount in wallet: ~25 BTC spread across ~20 addresses
- Single master key encrypts all addresses
- Wallet format: Bitcoin Core wallet.dat
- Encryption version: Bitcoin Core 0.4.0+ (released 2011-09-27)
- BDB version: 4.8 (upgraded from 4.7)

## Critical Insights from Dean (px)

These insights come directly from Dean Pierce's conversations in the Telegram group and should be treated as authoritative.

### Passphrase Format

1. **It's a PASSPHRASE, not a password** - The Bitcoin 0.4.0 encryption prompt said "Enter the new passphrase" and suggested "8 or more words"

2. **Word count**: Dean typically uses 3-4 words, but this passphrase has MORE words than his usual (likely 4-7 words)

3. **Word separators**: "Usually spaces, sometimes dots, rarely dashes, don't think I've ever used underscores" (April 2025)

4. **Self-deprecating theme**: The passphrase is likely a self-deprecating statement about the password's weakness. Examples Dean mentioned:
   - "this is a bad password"
   - "bad password"
   - "this is a very bad password"
   - "this is a really dumb passphrase"
   - Something "embarrassingly stupid"
   - Possibly using the word "derpy" (popular slang circa 2011)

5. **Length**: Probably around 20 characters (Bitcoin-Qt minimum was ~16 characters)

6. **Character set**: Likely lowercase with spaces/periods between words. May include:
   - 1337ifications (letter substitutions)
   - Whitespace converted to punctuation
   - Capitalizations
   - Trailing garbage

7. **Leetspeak patterns** (from Dean): 
   - `a` -> `@`, `4`
   - `s` -> `$`, `5`
   - `pass` -> `p455`, `p@$$`
   - `R` -> `|2` (maybe, but rare)
   - **NOT used**: `7` for `r` (never), pipe character `|` in passwords (never)

8. **Trailing characters** (from Dean): Likely 1, 3, or maybe 6 characters at the end - exclamations (!), question marks (?), tildes (~), or backticks (`)

9. **NOT relevant**: Game of Thrones references (Dean didn't watch until season 4, ~2014)

### Timeline Context

- **DEFCON 19**: August 4-7, 2011 (Las Vegas) - Dean was there
- **Bitcoin 0.4.0 release**: September 27, 2011 - First version with wallet encryption
- **Wallet encryption**: Happened after Sept 2011, possibly while "hanging out with his brother"
- **Last successful use**: Throughout 2012, forgot it towards end of 2013
- **Era slang**: derpy, lulz, rofl, potato were popular around this time

### Dean's Confidence Level

- "99% sure that if it ever cracks it's going to be something embarrassingly stupid"
- "I just know it's going to be the dumbest freaking password. Like 'pooooooooooooooop' or something"
- Solar Designer (famous password cracker) spent about a month on it without success

## What Has Been Tried

### By Dean (from crackmywallet.org)

- `?d 1-9` - All combinations of digits up to 9 characters
- `?l 1-7` - All combinations of lowercase chars up to 7 characters
- `?a 1-6` - All combinations of all ASCII up to 6 characters
- `rockyou.txt + best64 / d3ad0ne / dive`
- `weakpass2a + best64`

### Previous Attempts (archive/attempt-1/)

The `archive/attempt-1/` directory contains wallet encryption testing scripts that were used to verify the bitcoin2john hash extraction process. These scripts tested wallet creation and encryption across Bitcoin versions 0.3.21 through 0.5.1 to ensure the hash format is correct.

### Community Efforts

- Multiple people with GPU rigs have attempted cracking
- Solar Designer spent approximately one month on it
- Various combinatorics generators have been built
- Hashtopolis distributed cracking has been discussed

## ⚡ RECOMMENDED APPROACH (Research-Backed)

**After extensive research into password cracking methodologies**, we've identified more efficient approaches than pre-generating massive wordlists.

### 📚 Read These First

1. **[RESEARCH_ANALYSIS.md](RESEARCH_ANALYSIS.md)** - Academic research & industry best practices
2. **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Step-by-step cracking guide

### 🎯 Priority Methods (10-100x more efficient)

| Method | Tool | Efficiency | Time |
|--------|------|------------|------|
| **1. Token Lists** | BTCRecover | Highest (purpose-built) | Hours-Days |
| **2. Rules-Based** | Hashcat + custom rules | Very High | Hours |
| **3. PRINCE** | princeprocessor | High | Hours-Days |
| **4. Hybrid** | Hashcat -a 6/7 | High | Minutes-Hours |

### 🚀 Quick Start (Recommended)

```bash
# Method 1: BTCRecover (if you have wallet.dat)
git clone https://github.com/gurnec/btcrecover.git
cd btcrecover
pip install -r requirements.txt
python3 btcrecover.py --wallet wallet.dat --tokenlist ../btcrecover_tokens.txt --max-tokens 7 --enable-gpu

# Method 2: Hashcat with custom rules (hash-only)
hashcat -m 11300 -a 0 wallet_hash.txt base_phrases_curated.txt -r hashcat_rules/dean_patterns.rule

# Method 3: PRINCE processor (multi-word combinations)
git clone https://github.com/hashcat/princeprocessor.git
cd princeprocessor && make
./princeprocessor --elem-cnt-min=4 --elem-cnt-max=7 < ../prince_words.txt | hashcat -m 11300 ../wallet_hash.txt
```

See **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** for complete instructions.

### 📁 Research-Backed Files

| File | Purpose | Size |
|------|---------|------|
| `btcrecover_tokens.txt` | Token list for BTCRecover | 2 KB |
| `hashcat_rules/dean_patterns.rule` | Custom hashcat rules (Dean's patterns) | 15 KB |
| `prince_words.txt` | Single words for PRINCE combinations | 500 B |
| `base_phrases_curated.txt` | High-priority base phrases | 2 KB |

**Total: ~20 KB** (vs 500MB-5GB for pre-generated wordlists)

---

## Repository Structure

```
cmw/
├── README.md                           # This file
├── RESEARCH_ANALYSIS.md                # 🆕 Academic research & methodology analysis
├── IMPLEMENTATION_GUIDE.md             # 🆕 Step-by-step cracking guide
├── METHODOLOGY.md                      # Original methodology notes
├── btcrecover_tokens.txt               # 🆕 Token list for BTCRecover
├── base_phrases_curated.txt            # 🆕 Curated high-priority phrases
├── prince_words.txt                    # 🆕 Words for PRINCE processor
├── hashcat_rules/
│   └── dean_patterns.rule              # 🆕 Custom hashcat rules
├── generate_base_phrases.sh            # Generates base passphrase combinations
├── generate_leetspeak_mutations.sh     # Applies leetspeak transformations
├── generate_trailing_chars.sh          # Adds trailing characters (!?~` etc)
├── generate_all_combinations.sh        # Master script - runs all generators
├── test_workflow.sh                    # Control test & workflow instructions
├── archive/
│   ├── attempt-1/                      # Previous cracking attempt files
│   │   ├── README.md                   # Original crackmywallet.org README
│   │   ├── *.sh                        # Wallet testing scripts
│   │   └── ...                         # Bitcoin version test environments
│   ├── telegram/                       # Telegram chat history
│   │   ├── result.json                 # Full chat export
│   │   ├── photos/                     # Shared images
│   │   └── files/                      # Shared files
│   └── signal-chat-with-px.md          # Signal conversation with Dean
```

## Alternative: Pre-Generated Wordlists (Less Efficient)

**Note:** The scripts below generate large pre-computed wordlists. While comprehensive, they are **less efficient** than the research-backed approaches above. Consider using BTCRecover, hashcat rules, or PRINCE instead.

This repository includes automated scripts to generate password candidates based on all the intelligence gathered about Dean's passphrase habits.

### Step-by-Step Workflow

#### 1. Generate Password Lists

Run the master script to generate all password candidates:

```bash
chmod +x generate_all_combinations.sh
./generate_all_combinations.sh
```

This will create three tier-based wordlists:
- **tier1_base_and_trailing.txt** - Highest priority candidates (start here)
- **tier2_leetspeak.txt** - Medium priority with leetspeak mutations
- **tier3_leetspeak_trailing.txt** - Lower priority (largest set)
- **all_candidates.txt** - All candidates combined

#### 2. Crack with John the Ripper

**Install John the Ripper** (if needed):
```bash
# Ubuntu/Debian
sudo apt-get install john

# macOS
brew install john-jumbo
```

**Run the attack** (try tier 1 first):
```bash
# Create the hash file
cat > wallet_hash.txt << 'EOF'
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
EOF

# Run John the Ripper on tier 1
john --wordlist=tier1_base_and_trailing.txt --format=bitcoin wallet_hash.txt

# If tier 1 doesn't work, try tier 2
john --wordlist=tier2_leetspeak.txt --format=bitcoin wallet_hash.txt

# If tier 2 doesn't work, try tier 3
john --wordlist=tier3_leetspeak_trailing.txt --format=bitcoin wallet_hash.txt
```

#### 3. Alternative: Crack with Hashcat (GPU-accelerated)

Hashcat is typically faster if you have a GPU:

```bash
# Install hashcat
sudo apt-get install hashcat  # Ubuntu/Debian
brew install hashcat          # macOS

# Run hashcat with mode 11300 (Bitcoin wallet)
hashcat -m 11300 -a 0 wallet_hash.txt tier1_base_and_trailing.txt

# Check if cracked
hashcat -m 11300 wallet_hash.txt --show
```

#### 4. Test Your Setup (Optional)

Run the test workflow script to verify everything is configured correctly:

```bash
chmod +x test_workflow.sh
./test_workflow.sh
```

This creates test files and shows detailed instructions for both John the Ripper and Hashcat.

### Understanding the Scripts

- **generate_base_phrases.sh** - Creates base phrases like "this is a bad password" with variations in:
  - Prefixes (this is a, this is a really, etc.)
  - Adjectives (bad, dumb, derpy, etc.)
  - Nouns (password, passphrase, pass, etc.)
  - Separators (spaces, periods, dashes)
  - Capitalization (lowercase, Title Case, First letter caps)

- **generate_leetspeak_mutations.sh** - Applies Dean's known leetspeak patterns:
  - `pass` → `p455`, `p@$$`
  - `a` → `@`, `4`
  - `s` → `$`, `5`
  - `e` → `3`
  - `i` → `1`
  - `o` → `0`
  - Multiple combinations of the above

- **generate_trailing_chars.sh** - Adds trailing characters Dean mentioned:
  - Single chars: `!`, `?`, `~`, `` ` ``, `1`
  - Three chars: `!!!`, `???`, `123`, `!?!`, etc.
  - Six chars: `!!!!!!`, `123456`, etc.

### What If You Crack It?

Tweet the password to [@deanpierce](https://twitter.com/deanpierce) to claim the 5 BTC bounty!

## How to Contribute

### For Humans

1. Generate passphrase candidates based on the hints above
2. Run hashcat with `-m 11300` against the hash
3. If you crack it, tweet the password to [@deanpierce](https://twitter.com/deanpierce)
4. Document your search space in a writeup (Dean offers partial bounty for documented attempts)

### For AI/Bots

See the prompt below for instructions on how to approach this challenge.

## Resources

- **Website**: https://crackmywallet.org/
- **Telegram**: https://t.me/CryptoRescue
- **Twitter**: https://twitter.com/deanpierce
- **Hashtag**: #crackmywallet
- **Hashcat mode**: 11300 (Bitcoin wallet)
- **Dean's bip39brute tool**: https://github.com/pierce403/bip39brute

---

## Prompt for AI Assistants / Chatbots

```
You are tasked with helping crack a Bitcoin wallet passphrase. Here is what you need to know:

OBJECTIVE: Generate candidate passphrases for a Bitcoin wallet encrypted in late 2011.

KEY CONSTRAINTS:
- It's a PASSPHRASE (multiple words), not a single password
- Likely 4-7 words (more than the owner's usual 3-4)
- Words separated by SPACES (most likely) or PERIODS (sometimes) or DASHES (rarely)
- Theme: Self-deprecating statement about password weakness
- Era: Late 2011, DEFCON 19 timeframe
- Slang of the era: derpy, lulz, rofl, potato, dumb, bad

LIKELY PATTERNS:
- "this is a [adjective] [password/passphrase]"
- "this is a really [adjective] [password/passphrase]"
- "this is a very [adjective] [password/passphrase]"
- "[adjective] [password/passphrase]"
- Variations with 1337speak, capitalization, trailing characters

ADJECTIVES TO TRY:
- bad, dumb, stupid, terrible, awful, weak, simple, easy, lazy
- derpy, lulzy, lame, crappy, shitty, silly, ridiculous
- embarrassing, pathetic, horrible, worst

NOUNS TO TRY:
- password, passphrase, pass, passwd, secret, key

MUTATIONS TO APPLY:
1. Case variations (all lower, Title Case, UPPER)
2. 1337speak (a->4, e->3, i->1, o->0, s->5, t->7)
3. Separator variations (space, period, dash, none)
4. Trailing characters (!, 1, 123, etc.)
5. Word order permutations

WHAT HAS BEEN EXHAUSTED:
- All digits up to 9 characters
- All lowercase up to 7 characters
- All ASCII up to 6 characters
- rockyou.txt with common rules
- weakpass2a with best64

YOUR TASK:
Generate novel passphrase candidates that haven't been tried, focusing on:
1. Multi-word self-deprecating phrases
2. 2011-era internet slang
3. Variations of "this is a bad password" theme
4. Combinations with spaces/periods between words

Output format: One passphrase per line, ready for hashcat input.
```

---

## Contact

- **Wallet Owner**: Dean Pierce ([@deanpierce](https://twitter.com/deanpierce))
- **Prize**: 5 BTC for cracking, partial bounty for documented search space coverage
- **Claim Method**: Tweet the password to @deanpierce

## License

This repository is for educational and collaborative purposes. The wallet and bounty belong to Dean Pierce.
