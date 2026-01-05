# Implementation Guide: Research-Backed Bitcoin Wallet Cracking

**Based on:** Independent research into password cracking methodologies (see RESEARCH_ANALYSIS.md)

**Recommendation:** Use specialized tools (BTCRecover, PRINCE) and dynamic generation (hashcat rules) instead of pre-generated wordlists.

---

## Quick Reference: Priority Order

| Priority | Method | Expected Time | Success Probability |
|----------|--------|---------------|---------------------|
| **1** | BTCRecover with token list | Hours - Days | HIGH (purpose-built) |
| **2** | Hashcat + custom rules | Hours | MEDIUM-HIGH |
| **3** | PRINCE processor | Hours - Days | MEDIUM |
| **4** | Hybrid attacks | Hours | MEDIUM |
| **5** | Markov chains | Days | LOW-MEDIUM |

---

## Method 1: BTCRecover (HIGHEST PRIORITY)

### Why This First?

- **Purpose-built** for Bitcoin wallet recovery with partial knowledge
- **GPU-accelerated** (100x faster than CPU)
- **Handles token combinations** dynamically
- Real-world success: ~50% recovery rate when partial info known

### Setup

```bash
# Install BTCRecover
git clone https://github.com/gurnec/btcrecover.git
cd btcrecover

# Install dependencies
pip3 install -r requirements.txt

# Verify GPU support (optional but recommended)
python3 btcrecover.py --help | grep -i gpu
```

### Get the Wallet File

You need Dean's actual `wallet.dat` file. The hash alone won't work with BTCRecover.

If you only have the hash:
- BTCRecover can't use it directly
- Skip to Method 2 (Hashcat)

If you have the wallet.dat:
```bash
# Copy wallet file to btcrecover directory
cp /path/to/wallet.dat ./wallet.dat
```

### Run BTCRecover

```bash
# Basic run with our token list
python3 btcrecover.py \
    --wallet wallet.dat \
    --tokenlist ../btcrecover_tokens.txt \
    --max-tokens 7 \
    --enable-gpu

# With more aggressive options
python3 btcrecover.py \
    --wallet wallet.dat \
    --tokenlist ../btcrecover_tokens.txt \
    --max-tokens 7 \
    --typos 2 \
    --typos-case \
    --typos-swap \
    --delimiter-space \
    --enable-gpu \
    --threads 8
```

### BTCRecover Options Explained

- `--max-tokens 7`: Dean mentioned 4-7 words
- `--typos 2`: Allow up to 2 typos/variations
- `--typos-case`: Try case variations
- `--typos-swap`: Try swapping adjacent characters
- `--delimiter-space`: Use space as separator (Dean's primary)
- `--enable-gpu`: Use GPU acceleration
- `--threads 8`: Use 8 CPU threads

### Expected Runtime

- With GPU: Hours to a few days
- Without GPU: Days to weeks
- Depends on token combinations

---

## Method 2: Hashcat with Custom Rules

### Why This?

- **More efficient** than pre-generated wordlists
- **Tiny storage** (rules are ~50KB, not 5GB)
- **GPU-accelerated**
- **Flexible** for iteration

### Setup

```bash
# Install hashcat (if not already installed)
sudo apt-get install hashcat  # Ubuntu/Debian
brew install hashcat          # macOS

# Or download from hashcat.net
```

### Prepare Hash File

```bash
# Create hash file (already done in test_workflow.sh)
cat > wallet_hash.txt << 'EOF'
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
EOF
```

### Run with Custom Rules

```bash
# Tier 1: Curated base phrases + custom rules
hashcat -m 11300 -a 0 wallet_hash.txt base_phrases_curated.txt -r hashcat_rules/dean_patterns.rule

# Check if cracked
hashcat -m 11300 wallet_hash.txt --show

# Tier 2: Use existing base_phrases.txt (from generate_base_phrases.sh) + rules
hashcat -m 11300 -a 0 wallet_hash.txt base_phrases.txt -r hashcat_rules/dean_patterns.rule

# Tier 3: With hashcat's built-in rules
hashcat -m 11300 -a 0 wallet_hash.txt base_phrases_curated.txt -r /usr/share/hashcat/rules/best64.rule
```

### Performance Tuning

```bash
# Use workload profile 3 (high performance, may make system unresponsive)
hashcat -m 11300 -a 0 -w 3 wallet_hash.txt base_phrases_curated.txt -r hashcat_rules/dean_patterns.rule

# Use all GPUs
hashcat -m 11300 -a 0 -d 1,2,3 wallet_hash.txt base_phrases_curated.txt -r hashcat_rules/dean_patterns.rule

# Benchmark first
hashcat -m 11300 -b
```

### Expected Runtime

- Curated wordlist (50 phrases) + rules: Minutes to hours
- Full base_phrases.txt (15K) + rules: Hours to days
- Depends on GPU (RTX 4090 vs integrated graphics = 100x difference)

---

## Method 3: PRINCE Processor

### Why This?

- **Designed for passphrases** (multi-word combinations)
- Successfully cracked 24-char, 5-word passphrase "in a few hours"
- **Dynamic generation** from single wordlist

### Setup

```bash
# Download princeprocessor
git clone https://github.com/hashcat/princeprocessor.git
cd princeprocessor
make

# Or download binary from releases
```

### Run PRINCE

```bash
# Generate candidates with 4-7 word combinations, pipe to hashcat
./princeprocessor \
    --elem-cnt-min=4 \
    --elem-cnt-max=7 \
    < ../prince_words.txt | \
hashcat -m 11300 ../wallet_hash.txt

# Save candidates to file first (for analysis)
./princeprocessor \
    --elem-cnt-min=4 \
    --elem-cnt-max=7 \
    < ../prince_words.txt \
    > prince_candidates.txt

# Then run hashcat
hashcat -m 11300 wallet_hash.txt prince_candidates.txt
```

### PRINCE Options

- `--elem-cnt-min=4`: Minimum 4 words (Dean said 4-7)
- `--elem-cnt-max=7`: Maximum 7 words
- Default separator: space (perfect for Dean's hints)

### Expected Output

With 44 words in prince_words.txt:
- 4-word combinations: ~3.5 million
- 5-word combinations: ~130 million
- 6-word combinations: ~4.8 billion
- 7-word combinations: ~176 billion

**Recommendation:** Start with 4-5 words, then escalate if needed.

### Expected Runtime

- 4-word combos (3.5M): Minutes to hours
- 5-word combos (130M): Hours to days
- 6-word combos (4.8B): Days to weeks
- 7-word combos (176B): Weeks to months (unless high-end GPU cluster)

---

## Method 4: Hybrid Attacks

### Why This?

- **Efficient for trailing patterns**
- No need to pre-generate every combination
- Dynamically appends/prepends to each candidate

### Run Hybrid Attacks

```bash
# Append single trailing characters (Dean's pattern: 1 char)
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '!'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '?'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '~'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '`'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '1'

# Append triple trailing characters (Dean's pattern: 3 chars)
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '!!!'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '???'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '123'

# Append digit masks (Dean's pattern: 1, 3, or 6 digits)
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '?d'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '?d?d?d'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '?d?d?d?d?d?d'

# Prepend (less likely for Dean, but comprehensive)
hashcat -m 11300 -a 7 wallet_hash.txt '!' base_phrases_curated.txt
```

### Mask Syntax

- `?d`: Single digit (0-9)
- `?l`: Single lowercase letter (a-z)
- `?u`: Single uppercase letter (A-Z)
- `?s`: Single special character
- `?a`: Single character (any)

### Expected Runtime

- Single character append (50 phrases): Seconds to minutes
- Triple character append: Minutes
- Digit masks: Minutes to hours

---

## Method 5: Combinator Attack

### Why This?

- Combines two wordlists
- Good for multi-word phrases when word order is unknown

### Run Combinator

```bash
# Create word lists
cat > words1.txt << 'EOF'
this is a
this is a very
this is a really
this is such a
what a
EOF

cat > words2.txt << 'EOF'
bad password
dumb password
derpy password
terrible passphrase
EOF

# Run combinator
hashcat -m 11300 -a 1 wallet_hash.txt words1.txt words2.txt

# With rules on right side
hashcat -m 11300 -a 1 wallet_hash.txt words1.txt words2.txt -k hashcat_rules/dean_patterns.rule
```

---

## Method 6: Markov Chains (Advanced)

### When to Use

- If Methods 1-5 fail
- Have time to train on Dean's patterns
- Want statistically probable candidates

### Setup

```bash
# Download statsprocessor
git clone https://github.com/hashcat/statsprocessor.git
cd statsprocessor
make
```

### Generate Training Data

Create a file with Dean's known password patterns and similar passwords:

```bash
cat > training_data.txt << 'EOF'
this is a bad password
this is a dumb password
this is a terrible password
bad password
dumb passphrase
[...add hundreds of similar patterns...]
EOF
```

### Train and Generate

```bash
# Generate stats file
./hcstatgen training_data.txt stats.hcstat

# Generate candidates
./statsprocessor stats.hcstat --pw-min=15 --pw-max=35 | hashcat -m 11300 wallet_hash.txt
```

---

## Monitoring & Progress

### Check Hashcat Progress

While hashcat is running:
- Press `s`: Show status
- Press `p`: Pause
- Press `r`: Resume
- Press `q`: Quit (save progress)

### Save Session

```bash
# Run with session name (allows resume)
hashcat -m 11300 -a 0 --session=dean_wallet wallet_hash.txt wordlist.txt -r rules.rule

# Resume if interrupted
hashcat -m 11300 --session=dean_wallet --restore
```

### Benchmark Your GPU

```bash
# Test hashcat performance on your hardware
hashcat -m 11300 -b

# Example output:
# Speed.#1.........:   150.0 kH/s (RTX 3080)
# Speed.#1.........:    15.0 kH/s (integrated graphics)
```

---

## Success Indicators

### If You Crack It

```bash
# Check for cracked password
hashcat -m 11300 wallet_hash.txt --show

# Output will be:
# $bitcoin$...:PASSWORD_HERE
```

### Then What?

1. **Tweet the password** to [@deanpierce](https://twitter.com/deanpierce)
2. **Claim 5 BTC bounty**
3. **Document your approach** for partial bounty consideration
4. **Share with the community** (optional)

---

## Troubleshooting

### "Out of memory" errors

- Reduce `--elem-cnt-max` in PRINCE
- Use smaller wordlists
- Close other applications
- Add swap space

### "Not enough compute units" (GPU)

- BTCRecover/Hashcat didn't detect GPU
- Install GPU drivers (NVIDIA CUDA, AMD ROCm)
- Use `--force` flag (not recommended but sometimes works)

### Very slow performance

- Check if running on CPU instead of GPU
- Use `hashcat -I` to list devices
- Specify device: `hashcat -d 1` (use GPU #1)

### hashcat says "Exhausted"

- All candidates were tried, none matched
- Try next method
- Refine wordlist/rules based on new insights

---

## Priority Workflow (Recommended)

```bash
# Day 1: Try BTCRecover (if you have wallet.dat)
python3 btcrecover.py --wallet wallet.dat --tokenlist btcrecover_tokens.txt --max-tokens 7 --enable-gpu

# Day 2: Hashcat with curated wordlist + custom rules
hashcat -m 11300 -a 0 wallet_hash.txt base_phrases_curated.txt -r hashcat_rules/dean_patterns.rule

# Day 3: Hybrid attacks (trailing characters)
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '!'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '!!!'
hashcat -m 11300 -a 6 wallet_hash.txt base_phrases_curated.txt '?d?d?d'

# Day 4: PRINCE processor (4-5 words first)
./princeprocessor --elem-cnt-min=4 --elem-cnt-max=5 < prince_words.txt | hashcat -m 11300 wallet_hash.txt

# Day 5: Extended base wordlist + rules
hashcat -m 11300 -a 0 wallet_hash.txt base_phrases.txt -r hashcat_rules/dean_patterns.rule

# Week 2: PRINCE with 6 words (if needed)
./princeprocessor --elem-cnt-min=6 --elem-cnt-max=6 < prince_words.txt | hashcat -m 11300 wallet_hash.txt

# Week 3+: Markov chains or ML approaches
```

---

## Files Created for This Strategy

| File | Purpose | Size |
|------|---------|------|
| `btcrecover_tokens.txt` | Token list for BTCRecover | ~2 KB |
| `hashcat_rules/dean_patterns.rule` | Custom hashcat rules | ~15 KB |
| `prince_words.txt` | Words for PRINCE combinations | ~500 B |
| `base_phrases_curated.txt` | Curated high-priority phrases | ~2 KB |
| `wallet_hash.txt` | Bitcoin wallet hash | ~400 B |

**Total:** ~20 KB (vs 500MB-5GB for pre-generated wordlists)

---

## Why This Approach is Better

### Old Approach (Pre-generation)
- ❌ Generate millions of passwords to disk
- ❌ Huge files (GB of storage)
- ❌ Slow I/O reading from disk
- ❌ Hard to iterate/modify
- ❌ Not using specialized tools

### New Approach (Research-backed)
- ✅ Dynamic generation on-the-fly
- ✅ Tiny files (KB not GB)
- ✅ GPU-accelerated everywhere
- ✅ Easy to modify rules/tokens
- ✅ Using purpose-built tools (BTCRecover, PRINCE)
- ✅ Following industry best practices
- ✅ Based on academic research + real-world success stories

---

## Next Steps

1. **Read RESEARCH_ANALYSIS.md** for the full academic/industry backing
2. **Start with Method 1** (BTCRecover) if you have wallet.dat
3. **Fall back to Method 2** (Hashcat + rules) if hash-only
4. **Iterate based on results** - refine wordlists and rules
5. **Document your attempts** for partial bounty consideration

**Good luck cracking Dean's wallet!** 🔓₿
