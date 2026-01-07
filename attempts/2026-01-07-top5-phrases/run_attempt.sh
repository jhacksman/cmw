#!/bin/bash
# Run top 11 phrases attempt against Bitcoin wallet hash
# ~26.4M candidates - runs in ~1.6 minutes at 270k H/s

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use hash.txt from tested folder
HASH_FILE="${SCRIPT_DIR}/../tested/2026-01-06-8word-dumbest/hash.txt"

if [ ! -f "$HASH_FILE" ]; then
    echo "Error: hash.txt not found at $HASH_FILE"
    echo "Please copy hash.txt to this directory or update the path"
    exit 1
fi

echo "=== Top 11 Phrases Attempt ==="
echo "Based on Dean's exact quotes from Telegram"
echo ""
echo "Phrases: 22 (11 patterns x password/passphrase)"
echo "Word separators: spaces OR periods (consistent throughout)"
echo "Trailing: 0-6 chars from 1234!@#$"
echo ""
echo "Estimated candidates: ~26.4 million"
echo "Estimated runtime at 270k H/s: ~1.6 minutes"
echo ""

# Check for hashcat
if ! command -v hashcat &> /dev/null; then
    echo "Error: hashcat not found. Please install hashcat first."
    exit 1
fi

echo "Running: python3 generate_top5.py | hashcat -m 11300 -a 0 -w 3 -O $HASH_FILE"
echo ""

python3 "$SCRIPT_DIR/generate_top5.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"

echo ""
echo "=== Attempt Complete ==="
