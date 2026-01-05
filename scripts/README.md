# Passphrase Candidate Generators

This directory contains Python scripts for generating passphrase candidates based on Dean Pierce's (px) hints about his forgotten Bitcoin wallet passphrase.

## Quick Start

```bash
# Generate all candidates (priority order)
python generate_candidates.py > candidates.txt

# Generate specific priority level
python generate_candidates.py --priority 1 > priority1.txt

# Count candidates without outputting
python generate_candidates.py --count

# Run with hashcat
hashcat -m 11300 -a 0 ../hash.txt candidates.txt
```

## Scripts

### generate_candidates.py

Main generator with 6 priority levels based on evidence strength:

| Priority | Description | Candidates |
|----------|-------------|------------|
| 1 | Core phrases with trailing chars | ~40,000 |
| 2 | 2011 era slang variations | ~20,000 |
| 3 | Dean's specific leetspeak | ~50,000 |
| 4 | Elongated/repeated chars | ~2,000 |
| 5 | Extended phrases (5-7 words) | ~5,000 |
| 6 | DEFCON context | ~500 |

**Usage:**
```bash
python generate_candidates.py [--priority N] [--output FILE] [--count]
```

### generate_trailing_combos.py

Systematic trailing character combinations based on Dean's hint about 1, 3, or 6 trailing characters.

**Usage:**
```bash
python generate_trailing_combos.py > trailing.txt
python generate_trailing_combos.py --trailing-only  # Just the suffixes
python generate_trailing_combos.py --custom-base "my phrase"
```

### generate_elongated.py

Elongated/repeated character patterns based on Dean's "pooooooooooooooop" hint.

**Usage:**
```bash
python generate_elongated.py > elongated.txt
python generate_elongated.py --words-only  # Just elongated words
python generate_elongated.py --repeated-only  # Pure repeated patterns
```

## Recommended Attack Order

1. `python generate_candidates.py --priority 1` - Core phrases + trailing
2. `python generate_trailing_combos.py` - Systematic trailing
3. `python generate_candidates.py --priority 3` - Dean's leetspeak
4. `python generate_elongated.py` - Repeated chars
5. `python generate_candidates.py --priority 2` - Era slang
6. `python generate_candidates.py --priority 5` - Extended phrases
7. `python generate_candidates.py --priority 6` - DEFCON context

## Key Constraints (from Dean)

These scripts are built around Dean's confirmed patterns:

- **Separators:** Spaces (most likely), periods (sometimes), dashes (rarely)
- **Trailing:** 1, 3, or 6 chars - !, ?, ~, `
- **Leetspeak:** p455, p@$$, a->@/4, s->$/5
- **NOT used:** 7 for r, pipe character |
- **Theme:** Self-deprecating statement about password weakness

## Hash

```
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
```

## Contributing

If you run these generators and don't find the passphrase, please document:
1. Which scripts/priorities you ran
2. Any additional mutations you applied
3. Hardware used and runtime

Update the `COVERAGE_INDEX.md` file with your attempts.
