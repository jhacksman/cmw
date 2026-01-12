#!/bin/bash
# Alternative Leetspeak & Hybrid Patterns Runner
# ~1.78B candidates, ~1.8 hours runtime at 270k H/s
# Intelligent trailing patterns: 1155 (vs 13 original)

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
echo "[*] Starting alternative leetspeak attack (~1.78B candidates)"
echo "[*] Estimated runtime: ~1.8 hours at 270k H/s"
echo "[*] Intelligent trailing patterns: 1155"
echo "[*] Progress will be logged to stderr by generator"
echo ""

python3 generate.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

echo ""
echo "[*] Attack complete. Check hashcat output above."
