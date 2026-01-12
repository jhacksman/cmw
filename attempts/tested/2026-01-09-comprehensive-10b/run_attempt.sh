#!/bin/bash
# Comprehensive 10-Family Generator Runner
# ~7.3B candidates, ~7.6 hours runtime at 270k H/s

# Bitcoin wallet hash
HASH='$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad'

# Create hash file if it doesn't exist
echo "$HASH" > hash.txt

# Check for --count flag
if [ "$1" == "--count" ]; then
    python3 generate.py --count
    exit 0
fi

# Check for --sample flag
if [ "$1" == "--sample" ]; then
    python3 generate.py --sample
    exit 0
fi

# Check for --to-file flag
if [ "$1" == "--to-file" ]; then
    OUTPUT_FILE="${2:-wordlist.txt}"
    echo "[*] Generating candidates to $OUTPUT_FILE..."
    python3 generate.py > "$OUTPUT_FILE"
    echo "[+] Generated $(wc -l < "$OUTPUT_FILE") candidates"
    echo "[*] Run: hashcat -m 11300 -a 0 -w 3 -O hash.txt $OUTPUT_FILE"
    exit 0
fi

# Default: pipe directly to hashcat
echo "[*] Starting comprehensive 10-family attack (~7.3B candidates)"
echo "[*] Estimated runtime: ~7.6 hours at 270k H/s"
echo "[*] 10 hypothesis families + 54,241 trailing patterns"
echo ""
echo "[*] Families:"
echo "    1. Core self-deprecating phrases"
echo "    2. Leetspeak variations"
echo "    3. Number/year infixes"
echo "    4. Emphasis caps & alternatives"
echo "    5. Extended phrase variations"
echo "    6. Phonetic variations & typos"
echo "    7. Keyboard patterns"
echo "    8. Year range 2000-2025"
echo "    9. Case permutations"
echo "    10. Prefix patterns"
echo ""
echo "[*] Progress will be logged to stderr by generator"
echo ""

python3 generate.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

echo ""
echo "[*] Attack complete. Check hashcat output above."
