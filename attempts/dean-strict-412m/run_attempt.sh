#!/bin/bash
# Dean-Strict Password Attempt (~6.7M candidates)
# Based strictly on Dean's confirmed quotes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="${1:-hash.txt}"

echo "=== Dean-Strict Password Attempt ==="
echo "Candidates: ~6.7 million"
echo "Based strictly on Dean's confirmed quotes"
echo ""

# Check if hash file exists
if [ ! -f "$HASH_FILE" ]; then
    echo "Error: Hash file not found: $HASH_FILE"
    echo "Usage: $0 [hash_file]"
    exit 1
fi

echo "Generating candidates and piping to hashcat..."
echo "Hash file: $HASH_FILE"
echo ""

# Run generator and pipe to hashcat
python3 "$SCRIPT_DIR/generate.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"

echo ""
echo "=== Attempt complete ==="
