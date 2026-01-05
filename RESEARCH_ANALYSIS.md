# Research-Backed Analysis: Password Cracking Strategy for CMW

**Date:** 2026-01-05
**Analysis:** Independent research on optimal methodologies for Dean Pierce's Bitcoin wallet recovery

---

## Executive Summary

After comprehensive research into password cracking methodologies, the current approach (both Claude's bash scripts and Devin's Python scripts) is **suboptimal**. Pre-generating massive wordlists is less efficient than using:

1. **BTCRecover** with token lists (designed specifically for this use case)
2. **Hashcat rules** instead of pre-generated mutations
3. **PRINCE algorithm** for dynamic word combinations
4. **Hybrid attacks** for trailing character patterns

**Recommendation:** Shift from pre-generation to dynamic rule-based generation.

---

## Research Findings

### 1. Bitcoin Wallet Recovery Best Practices

**Source:** [BTCRecover Documentation](https://btcrecover.readthedocs.io/en/latest/TUTORIAL/)

**Key Finding:** BTCRecover is specifically designed for Bitcoin wallet recovery where you know *parts* of the password. It uses:
- Token lists (word/pattern fragments)
- Dynamic combination generation
- GPU acceleration (100x performance improvement)
- Pattern-based recovery for known structures

**Success Rate:** ~50% when user remembers partial information ([Crypto Recovery Services](https://cryptorecovers.com/blog/bitcoin-core-password-recovery-how-to-recover-your-wallet/))

**Implication:** We have extensive information about Dean's patterns - BTCRecover is purpose-built for exactly this scenario.

---

### 2. Rules vs Pre-Generated Wordlists

**Source:** [Hashcat Wiki - Rule-based Attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack)

**Key Finding:** Rule-based attacks are described as "the most flexible, accurate and efficient attack" because:
- **Storage:** Rules are tiny compared to pre-generated wordlists
- **Performance:** With small/medium wordlists, rules are "practically free" ([4ARMED Blog](https://www.4armed.com/blog/hashcat-rule-based-attack/))
- **Flexibility:** One rule set can generate millions of variations from a small base wordlist
- **Targeted Attacks:** "Opting for a targeted more efficient ruleset over increasingly large dictionaries can yield better results" ([Password Village](https://passwordvillage.org/adv.html))

**Current Approach Problem:**
- My scripts: Generate ~15K base phrases, potentially millions with mutations → large files, slow I/O
- Devin's scripts: Generate ~100K pre-computed candidates
- Both miss the efficiency of dynamic rule application

**Better Approach:**
- Small base wordlist (500-1000 core phrases)
- Custom hashcat rules that encode Dean's patterns
- Let hashcat generate candidates on-the-fly

---

### 3. PRINCE Algorithm for Passphrases

**Source:** [Hashcat Princeprocessor](https://github.com/hashcat/princeprocessor)

**Key Finding:** PRINCE (PRobability INfinite Chained Elements) is specifically designed for passphrase cracking:
- Intelligently combines words from a single wordlist
- Builds "chains" of combined words
- Successfully cracked 24-character alphabetic passphrase (5 words) "in a few hours" ([Purple Rain Attack](https://www.netmux.com/blog/purple-rain-attack))
- More efficient than pre-generating all combinations

**Dean's Passphrase:** 4-7 words with self-deprecating theme
- Perfect use case for PRINCE
- Feed it: ["this", "is", "a", "bad", "dumb", "derpy", "password", "passphrase", etc.]
- Let PRINCE generate: "this is a bad password", "this is a derpy passphrase", etc.

**Efficiency:** Dynamic generation >> pre-generated wordlists for multi-word phrases

---

### 4. Hybrid Attacks for Trailing Characters

**Source:** [Hashcat Hybrid Attack](https://hashcat.net/wiki/doku.php?id=hybrid_attack)

**Key Finding:** Hybrid attacks combine wordlists with masks:
- `-a 6`: Append mask to each word (e.g., `password?d?d?d`)
- `-a 7`: Prepend mask to each word

**Dean's Patterns:** Trailing characters (1, 3, or 6 chars: `!`, `?`, `~`, `` ` ``, digits)

**Current Approach:**
- Generate every word + every trailing combination = exponential explosion
- Example: 1000 base phrases × 30 trailing patterns = 30,000 candidates

**Better Approach:**
```bash
# Hybrid attack: base phrases + mask for trailing
hashcat -m 11300 -a 6 hash.txt base_phrases.txt ?d?d?d
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '!?!?!?'
```

This generates combinations dynamically without storing them.

---

### 5. Markov Chains vs Wordlists

**Source:** [Hashcat Statsprocessor](https://github.com/hashcat/statsprocessor)

**Key Finding:** Markov chains generate statistically probable passwords based on training data:
- Train on Dean's known password patterns (from hints)
- Generate candidates based on character-position probability
- More efficient for longer passwords where traditional brute-force is impractical

**Applicability:** Medium - useful if wordlist/rules/PRINCE don't work, but requires training data

---

### 6. Academic Research (2023-2024)

**Source:** [PMC Systematic Review on Password Guessing](https://pmc.ncbi.nlm.nih.gov/articles/PMC10528539/)

**Key Finding:** Cutting-edge approaches use machine learning:
- **PassBERT Framework:** Bi-directional Transformer for targeted password guessing
- **Multi-credential analysis:** Leverages patterns across multiple leaked passwords
- **Targeted attacks** outperform generic dictionary attacks when partial information is known

**Implication:** For a high-value target like Dean's wallet, could explore ML-based generation if traditional methods fail.

---

### 7. Success Stories & What Actually Worked

**Source:** [Cointelegraph - Crypto Password Recovery](https://cointelegraph.com/news/lost-your-crypto-password-or-seed-phrase-here-s-what-actually-works-in-2025)

**Real-world successes:**

1. **Electrum Wallet (2014):** User created custom Ruby script with hand-picked tokens → cracked in seconds
   - **Method:** Token combinations (similar to BTCRecover approach)

2. **$300K Bitcoin Recovery:** Used cryptanalytic techniques + Nvidia GPUs
   - **Method:** Targeted attack with remembered patterns + GPU acceleration

3. **Wallet Recovery Services:** 50% success rate when partial info known
   - **Method:** "Quality of information" is key - detailed hints → higher success

**Common Thread:** All successes used *targeted* approaches based on known patterns, NOT generic wordlists.

---

## Critical Assessment of Current Approach

### What We're Doing Right ✅

1. **Targeting Dean's specific patterns** (self-deprecating phrases, leetspeak)
2. **Incorporating timeline context** (2011 slang like "derpy")
3. **Tier-based prioritization** (highest probability first)
4. **Comprehensive coverage** of separator variations

### What We're Doing Wrong ❌

1. **Pre-generating everything** instead of using dynamic rules
   - Wastes disk space
   - Slower I/O than on-the-fly generation
   - Less flexible for iteration

2. **Not using specialized tools**
   - BTCRecover is purpose-built for this exact scenario
   - We're reinventing the wheel

3. **Combinatorial explosion**
   - Generating every base phrase × every mutation × every trailing pattern
   - Creates redundant/unlikely candidates

4. **No GPU optimization**
   - Current approach doesn't leverage GPU acceleration
   - Hashcat/BTCRecover with GPU = 100x faster

5. **Not using PRINCE for word combinations**
   - Would be more efficient for multi-word passphrases
   - Generates statistically likely combinations dynamically

---

## Recommended Strategy (Research-Backed)

### Phase 1: BTCRecover with Token List (HIGHEST PRIORITY)

**Why:** Purpose-built for Bitcoin wallet recovery with partial knowledge.

**Implementation:**
```
Create token list file:
this
is
a
very
really
bad
dumb
derpy
lulzy
password
passphrase
pass
```

**BTCRecover features to use:**
- Token combinations with `--max-tokens 7` (Dean mentioned 4-7 words)
- Typo simulation for variations
- Custom separators (space, period, dash)
- GPU acceleration
- Pattern matching for trailing chars

**Advantage:** Specifically designed for this use case, GPU-accelerated, flexible.

---

### Phase 2: Hashcat with Custom Rules

**Why:** More efficient than pre-generated wordlists.

**Implementation:**

1. **Create minimal base wordlist** (500-1000 core phrases):
```
this is a bad password
this is a dumb password
this is a derpy password
bad password
dumb passphrase
[etc.]
```

2. **Create custom rule file** encoding Dean's patterns:
```
# leetspeak.rule
:
# pass -> p455
so0ss/pass/p455/
# pass -> p@$$
so0ss/pass/p@$$/
# a -> @
sa@
# a -> 4
sa4
# s -> $
ss$
# Combined
so0ss/pass/p455/ sa@ ss$
[etc.]
```

3. **Run with rules:**
```bash
hashcat -m 11300 -a 0 hash.txt base_phrases.txt -r leetspeak.rule
```

**Advantage:** Tiny wordlist + rules = millions of candidates generated on-the-fly.

---

### Phase 3: PRINCE for Word Combinations

**Why:** Optimal for multi-word passphrases.

**Implementation:**
```bash
# Create word list
echo -e "this\nis\na\nvery\nreally\nbad\ndumb\nderpy\npassword\npassphrase" > words.txt

# Generate combinations with princeprocessor
./princeprocessor --elem-cnt-min=4 --elem-cnt-max=7 < words.txt | hashcat -m 11300 hash.txt
```

**Advantage:** Generates "this is a bad password" style combinations dynamically.

---

### Phase 4: Hybrid Attacks for Trailing Characters

**Why:** Efficient for suffix patterns.

**Implementation:**
```bash
# Append single trailing chars
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '!'
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '?'
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '~'

# Append triple trailing
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '!!!'
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '???'

# Append digits
hashcat -m 11300 -a 6 hash.txt base_phrases.txt '?d?d?d'
```

**Advantage:** No need to pre-generate every combination.

---

### Phase 5: Loopback & Incremental

**Why:** Refine successful patterns.

**Implementation:**
```bash
# Use cracked passwords as input for new attempts (loopback)
hashcat -m 11300 hash.txt --loopback

# Incremental mode in JtR
john --incremental=Alnum --format=bitcoin hash.txt
```

---

## Estimated Efficiency Gains

| Approach | Estimated Candidates | Disk Space | Generation Time | Cracking Speed |
|----------|---------------------|------------|-----------------|----------------|
| **Current (pre-gen)** | ~1-10 million | ~500MB - 5GB | ~30-60 min | Slow (I/O bound) |
| **BTCRecover tokens** | Generated dynamically | ~1KB | Instant | Fast (GPU) |
| **Hashcat + rules** | ~100K base × rules | ~10MB | Instant | Very Fast (GPU) |
| **PRINCE processor** | Generated dynamically | ~5KB | Instant | Fast (GPU) |
| **Hybrid attacks** | Generated dynamically | ~1MB | Instant | Very Fast (GPU) |

**Result:** 50-500x less disk usage, instant generation, 10-100x faster cracking with GPU.

---

## Recommended Action Plan

### Immediate (Next Steps)

1. **Install BTCRecover**
   ```bash
   git clone https://github.com/gurnec/btcrecover.git
   cd btcrecover
   pip install -r requirements.txt
   ```

2. **Create token list** with Dean's known patterns
   - Core words: this, is, a, very, really, bad, dumb, derpy, lulzy, password, passphrase, pass
   - Special patterns: p455, p@$$
   - Trailing: !, ?, ~, `, 123

3. **Run BTCRecover with GPU**
   ```bash
   python btcrecover.py --wallet wallet.dat --tokenlist tokens.txt --enable-gpu --max-tokens 7
   ```

### Short-term (If BTCRecover doesn't work)

4. **Create minimal base wordlist** (500 phrases)
5. **Write custom hashcat rules** for Dean's leetspeak patterns
6. **Test with PRINCE processor** for word combinations
7. **Run hybrid attacks** for trailing characters

### Long-term (If standard methods fail)

8. **Train Markov chains** on Dean's pattern hints
9. **Explore ML-based approaches** (PassBERT, if worth the investment)
10. **Distribute across multiple GPUs** (Hashtopolis)

---

## Conclusion

**Current approach (both Claude and Devin):** Reinventing the wheel with pre-generation.

**Research-backed approach:** Use specialized tools (BTCRecover, PRINCE) + dynamic generation (hashcat rules, hybrid attacks).

**Expected outcome:** 10-100x faster, more comprehensive coverage, less disk usage.

**Confidence level:** HIGH - backed by academic research, industry best practices, and real-world success stories.

---

## Sources

1. [BTCRecover Documentation](https://btcrecover.readthedocs.io/en/latest/TUTORIAL/)
2. [Hashcat Rule-based Attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack)
3. [Hashcat Princeprocessor](https://github.com/hashcat/princeprocessor)
4. [Hashcat Hybrid Attack](https://hashcat.net/wiki/doku.php?id=hybrid_attack)
5. [Bitcoin Wallet Password Cracking Guide](https://bitcoininsiderz.com/cracking-bitcoin-wallet-passwords/)
6. [Passphrase Wordlist Project](https://github.com/initstring/passphrase-wordlist)
7. [Statsprocessor (Markov Chains)](https://github.com/hashcat/statsprocessor)
8. [PMC Systematic Review on Password Guessing](https://pmc.ncbi.nlm.nih.gov/articles/PMC10528539/)
9. [Crypto Password Recovery Success Stories](https://cointelegraph.com/news/lost-your-crypto-password-or-seed-phrase-here-s-what-actually-works-in-2025)
10. [Purple Rain Attack - PRINCE Algorithm](https://www.netmux.com/blog/purple-rain-attack)
11. [Hashcat Attack Strategies](https://www.onlinehashcrack.com/guides/password-recovery/hybrid-attack-strategies-combine-rules-for-success.php)
12. [Crypto Wallet Recovery Best Practices](https://cryptorecovers.com/blog/bitcoin-core-password-recovery-how-to-recover-your-wallet/)
