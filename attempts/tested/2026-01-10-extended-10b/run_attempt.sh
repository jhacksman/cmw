#!/bin/bash
# Extended 10-Family Generator Runner
# ~10B candidates (NEW untested areas), ~10.3 hours runtime at 270k H/s

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
echo "[*] Starting extended 10-family attack (~10B candidates)"
echo "[*] Estimated runtime: ~10.3 hours at 270k H/s"
echo "[*] 10 NEW hypothesis families (completely untested areas)"
echo ""
echo "[*] NEW Families:"
echo "    1. Full year brute 0000-9999"
echo "    2. Symbol-heavy patterns"
echo "    3. Exact length optimization"
echo "    4. Extended phonetic variations"
echo "    5. Dean-specific vocabulary"
echo "    6. DEFCON/Portland 2011 culture"
echo "    7. Bidirectional prefix+suffix"
echo "    8. Full leetspeak coverage (t→7 l→1)"
echo "    9. Multi-word case patterns"
echo "    10. Irony/spite META patterns"
echo ""
echo "[*] Progress will be logged to stderr by generator"
echo ""

python3 generate.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt

echo ""
echo "[*] Attack complete. Check hashcat output above."
