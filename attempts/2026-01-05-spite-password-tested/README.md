# Spite Password Hypothesis - Attempt

**Date:** 2026-01-05
**Status:** Ready to Test
**Priority:** HIGHEST (untested search space)

## Hypothesis

Dean said he set the password to the "**weakest possible thing out of spite**" - not a complex multi-word passphrase.

Bitcoin 0.4.0 minimum requirement: **10 characters**

Everyone tested up to 6-9 characters and assumed multi-word passphrases. **Nobody tested simple 10-character spite passwords.**

## Files in This Attempt

### Documentation
- **SUMMARY_FOR_HUMAN.md** - Quick overview (start here)
- **UNTESTED_SEARCH_SPACE.md** - Full telegram archive analysis
- **NEW_ATTACK_STRATEGY.md** - Complete 5-phase attack plan

### Wordlists (Ready to Use)
- **spite_passwords_10char.txt** - 11,241 targeted 10-char passwords
- **base_phrases_curated.txt** - 50 high-priority base phrases
- **btcrecover_tokens.txt** - Token list for BTCRecover
- **prince_words.txt** - Words for PRINCE processor

### Generation Scripts
- **generate_spite_passwords.sh** - Generates the spite password list

### Rules
- **hashcat_rules/dean_patterns.rule** - Custom hashcat rules

## Quick Test

```bash
cd attempts/spite-password-hypothesis

# Test with hashcat
hashcat -m 11300 -a 0 ../../wallet_hash.txt spite_passwords_10char.txt

# Or with John the Ripper
john --wordlist=spite_passwords_10char.txt --format=bitcoin ../../wallet_hash.txt
```

## Top Candidates

1. `password1!` - Most common + minimal compliance
2. `Password1!` - Meets enterprise requirements
3. `qwertyuiop` - Classic keyboard spite pattern
4. `1234567890` - Sequential numbers
5. `aaaaaaaaaa` - Ultimate mockery

## Why This Works

- Dean's quote: "weakest possible thing out of spite"
- Bitcoin 0.4.0 minimum: 10 characters (verified in source)
- Testing gap: brute force stopped at 6-9 characters
- Spite password psychology: predictable patterns

See SUMMARY_FOR_HUMAN.md for full details.
