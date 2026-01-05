#!/usr/bin/env python3
"""
Fast untested gap generator (<= 1B candidates per list)
Based on what Dean tested vs. untested search spaces
"""

import string
import itertools
from pathlib import Path

# ASCII charset (95 printable chars)
ASCII_CHARS = string.printable.strip()
DIGITS = string.digits
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
COMMON_SYMBOLS = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'

def generate_gap(base, suffix_chars, suffix_length, output_file):
    """Generate base + suffix combinations"""
    print(f"[*] Generating: '{base}' + {suffix_length} chars from charset ({len(suffix_chars)} chars)")
    print(f"    Keyspace: {len(suffix_chars)}^{suffix_length} = {len(suffix_chars)**suffix_length:,}")

    count = 0
    with open(output_file, 'w') as f:
        for combo in itertools.product(suffix_chars, repeat=suffix_length):
            f.write(f"{base}{''.join(combo)}\n")
            count += 1
            if count % 1000000 == 0:
                print(f"    Generated {count:,}...")

    print(f"[+] Complete: {count:,} → {output_file}")
    return count

def main():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║    Fast Untested Gap Generator (<= 1B Per List)              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    print("Dean tested:")
    print("  - Digits: 1-9 chars")
    print("  - Lowercase: 1-7 chars")
    print("  - All ASCII: 1-6 chars")
    print()
    print("Generating UNTESTED patterns...")
    print()

    gaps = []

    # GAP 1: password + 2 chars (limited charset for speed)
    gaps.append({
        'base': 'password',
        'suffix_chars': DIGITS + LOWERCASE + '!@#$',
        'suffix_length': 2,
        'output': 'gap1_password_plus2.txt'
    })

    # GAP 2: Password + 2 chars (capital P)
    gaps.append({
        'base': 'Password',
        'suffix_chars': DIGITS + '!@#$',
        'suffix_length': 2,
        'output': 'gap2_Password_plus2.txt'
    })

    # GAP 3: password + 1 digit + 1 symbol (common pattern)
    print("[GAP 3] password + 1 digit + 1 symbol (100 combos)")
    count = 0
    with open('gap3_password_d_s.txt', 'w') as f:
        for d in DIGITS:
            for s in '!@#$%^&*':
                f.write(f"password{d}{s}\n")
                count += 1
    print(f"[+] Complete: {count:,} → gap3_password_d_s.txt")

    # GAP 4: Password + 1 digit + 1 symbol (Password1!)
    print("[GAP 4] Password + 1 digit + 1 symbol (80 combos)")
    count = 0
    with open('gap4_Password_d_s.txt', 'w') as f:
        for d in DIGITS:
            for s in '!@#$%^&*':
                f.write(f"Password{d}{s}\n")
                count += 1
    print(f"[+] Complete: {count:,} → gap4_Password_d_s.txt")

    # GAP 5: qwertyuiop (10 chars - exact keyboard row)
    print("[GAP 5] qwertyuiop variations (single password)")
    with open('gap5_qwertyuiop.txt', 'w') as f:
        f.write("qwertyuiop\n")
        f.write("Qwertyuiop\n")
        f.write("QWERTYUIOP\n")
    print(f"[+] Complete: 3 → gap5_qwertyuiop.txt")

    # GAP 6: qwertyui + 2 chars (8 char keyboard + 2)
    gaps.append({
        'base': 'qwertyui',
        'suffix_chars': DIGITS + LOWERCASE[:10] + '!@#$',
        'suffix_length': 2,
        'output': 'gap6_qwertyui_plus2.txt'
    })

    # GAP 7: asdfghjkl; (10 chars - exact keyboard row)
    print("[GAP 7] asdfghjkl; variations")
    with open('gap7_asdfghjkl.txt', 'w') as f:
        f.write("asdfghjkl;\n")
        f.write("asdfghjkl!\n")
        f.write("asdfghjkl1\n")
        f.write("Asdfghjkl;\n")
    print(f"[+] Complete: 4 → gap7_asdfghjkl.txt")

    # GAP 8: 1234567890 (10 digits - exact)
    print("[GAP 8] 1234567890 (sequential digits)")
    with open('gap8_1234567890.txt', 'w') as f:
        f.write("1234567890\n")
        f.write("0987654321\n")  # reverse
    print(f"[+] Complete: 2 → gap8_1234567890.txt")

    # GAP 9: aaaaaaaaaa and variants (repeated chars - 10 chars)
    print("[GAP 9] Repeated 10 chars (a-z, 0-9)")
    count = 0
    with open('gap9_repeated10.txt', 'w') as f:
        for char in LOWERCASE + DIGITS:
            f.write(f"{char * 10}\n")
            count += 1
    print(f"[+] Complete: {count:,} → gap9_repeated10.txt")

    # GAP 10: badpass + 3 chars (limited for < 1B)
    gaps.append({
        'base': 'badpass',
        'suffix_chars': DIGITS + '!@#',
        'suffix_length': 3,
        'output': 'gap10_badpass_plus3.txt'
    })

    # GAP 11: welcome + 3 chars
    gaps.append({
        'base': 'welcome',
        'suffix_chars': DIGITS + '!@#',
        'suffix_length': 3,
        'output': 'gap11_welcome_plus3.txt'
    })

    # GAP 12: Welcome + 3 chars
    gaps.append({
        'base': 'Welcome',
        'suffix_chars': DIGITS + '!@#',
        'suffix_length': 3,
        'output': 'gap12_Welcome_plus3.txt'
    })

    # GAP 13: p@ssword + 1-2 chars (Dean's leet pattern)
    gaps.append({
        'base': 'p@ssword',
        'suffix_chars': DIGITS + '!@#$',
        'suffix_length': 1,
        'output': 'gap13_p@ssword_plus1.txt'
    })

    gaps.append({
        'base': 'p@ssword',
        'suffix_chars': DIGITS + '!@',
        'suffix_length': 2,
        'output': 'gap14_p@ssword_plus2.txt'
    })

    # GAP 15: p@ssw0rd + 1-2 chars (double leet)
    gaps.append({
        'base': 'p@ssw0rd',
        'suffix_chars': DIGITS + '!@#$',
        'suffix_length': 1,
        'output': 'gap15_p@ssw0rd_plus1.txt'
    })

    gaps.append({
        'base': 'p@ssw0rd',
        'suffix_chars': DIGITS + '!@',
        'suffix_length': 2,
        'output': 'gap16_p@ssw0rd_plus2.txt'
    })

    # Generate all gaps
    total = 0
    for gap in gaps:
        total += generate_gap(
            gap['base'],
            gap['suffix_chars'],
            gap['suffix_length'],
            gap['output']
        )
        print()

    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                    Generation Complete                        ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    print(f"Total candidates: {total:,}")
    print()
    print("Test with hashcat:")
    print("  for file in gap*.txt; do")
    print("    hashcat -m 11300 -a 0 -w 3 -O -D 2 hash.txt $file")
    print("  done")
    print()
    print("Or combine all:")
    print("  cat gap*.txt > all_untested_gaps.txt")
    print("  sort -u all_untested_gaps.txt -o all_untested_gaps_unique.txt")
    print("  hashcat -m 11300 -a 0 -w 3 -O -D 2 hash.txt all_untested_gaps_unique.txt")

if __name__ == "__main__":
    main()
