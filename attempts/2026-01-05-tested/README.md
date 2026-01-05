# Crack My Wallet - 2026-01-05 Attempt

**Status**: UNTRIED  
**Estimated Candidates**: ~1.08 billion  
**Priority**: Based on Dean Pierce's (px) confirmed hints

## Overview

This attempt generates approximately 1 billion passphrase candidates based on the priority analysis from Dean's hints about his passphrase characteristics.

## Key Patterns Covered

Based on Dean's confirmed hints:

1. **Passphrase structure**: Multiple words (4-7), not a single password
2. **Separators**: Spaces (most likely), periods, dashes, or none
3. **Theme**: Self-deprecating statements about password weakness
4. **Trailing characters**: 1, 3, or 6 chars - !, ?, ~, `
5. **Leetspeak**: a->@,4; s->$,5; pass->p455,p@$$; NEVER 7 for r
6. **Era context**: 2011 slang (derpy, lulz, etc.)

## Files

- `generate_1b.py` - Python generator script (~1.08B candidates)
- `run_attempt.sh` - Shell wrapper for easy execution

## Usage

### Estimate candidate count
```bash
./run_attempt.sh --estimate
```

### Generate all candidates to file
```bash
./run_attempt.sh > wordlist.txt
```

### Pipe directly to hashcat
```bash
./run_attempt.sh | hashcat -m 11300 -a 0 hash.txt
```

### Generate limited sample (for testing)
```bash
./run_attempt.sh --limit 1000
```

### Parallel processing (10 chunks)
```bash
# Run in parallel on multiple machines
./run_attempt.sh --chunk 1 > chunk1.txt &
./run_attempt.sh --chunk 2 > chunk2.txt &
# ... etc
```

## Keyspace Breakdown

| Component | Count | Notes |
|-----------|-------|-------|
| Base phrases | ~120,000 | prefixes + adjectives + nouns + intensifiers |
| Separators | 4 | space, period, dash, none |
| Case variations | 5 | lower, title, upper, sentence, first-word |
| Trailing patterns | 64 | 1-6 char combinations |
| Leet variants | 10 | per phrase |
| Leet trailing | 20 | per leet variant |

Total: ~1,085,876,043 candidates

## Hash Information

```
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
```

Hashcat mode: 11300 (Bitcoin/Litecoin wallet.dat)
