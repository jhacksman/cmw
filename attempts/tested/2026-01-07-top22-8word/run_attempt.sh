#!/bin/bash
# Run top 22 eight-word phrases attempt against Bitcoin wallet hash
# ~52.7M candidates - runs in ~3.3 minutes at 270k H/s

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use hash.txt from tested folder
HASH_FILE="${SCRIPT_DIR}/../tested/2026-01-06-8word-dumbest/hash.txt"

if [ ! -f "$HASH_FILE" ]; then
    echo "Error: hash.txt not found at $HASH_FILE"
    echo "Please copy hash.txt to this directory or update the path"
    exit 1
fi

echo "=== Top 22 Eight-Word Phrases Attempt ==="
echo "Based on Dean's exact quotes from Telegram"
echo ""
echo "Phrases: 44 (22 patterns x password/passphrase)"
echo "All phrases are exactly 8 words"
echo "Word separators: spaces OR periods (consistent throughout)"
echo "Trailing: 0-6 chars from 1234!@#$"
echo ""
echo "Estimated candidates: ~52.7 million"
echo "Estimated runtime at 270k H/s: ~3.3 minutes"
echo ""

# Check for hashcat
if ! command -v hashcat &> /dev/null; then
    echo "Error: hashcat not found. Please install hashcat first."
    exit 1
fi

echo "Running: python3 generate_top22.py | hashcat -m 11300 -a 0 -w 3 -O $HASH_FILE"
echo ""

python3 "$SCRIPT_DIR/generate_top22.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"

echo ""
echo "=== Attempt Complete ==="
