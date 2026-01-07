#!/bin/bash
# Run refined spite passphrase attempt against Bitcoin wallet hash
# ~2.8 billion candidates based on Dean's actual vocabulary

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Use hash.txt from tested folder (or copy one locally)
HASH_FILE="${SCRIPT_DIR}/../tested/2026-01-06-8word-dumbest/hash.txt"

if [ ! -f "$HASH_FILE" ]; then
    echo "Error: hash.txt not found at $HASH_FILE"
    echo "Please copy hash.txt to this directory or update the path"
    exit 1
fi

echo "=== Refined Spite Passphrase Attempt ==="
echo "Based on Dean's actual vocabulary from Telegram, GitHub, and A/B test feedback"
echo ""
echo "Key refinements:"
echo "- Only words Dean actually uses"
echo "- Trailing: 0-4 chars from 1234!@#$ with space/period separator"
echo "- Minimal leetspeak (only on password/passphrase)"
echo ""
echo "Estimated candidates: ~2.8 billion"
echo "Estimated runtime at 120k H/s: ~6.5 hours"
echo ""

# Check for hashcat
if ! command -v hashcat &> /dev/null; then
    echo "Error: hashcat not found. Please install hashcat first."
    exit 1
fi

echo "Running: python3 generate_refined.py | hashcat -m 11300 -a 0 -w 3 -O $HASH_FILE"
echo ""

python3 "$SCRIPT_DIR/generate_refined.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"

echo ""
echo "=== Attempt Complete ==="
