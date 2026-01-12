#!/bin/bash
# Run the comprehensive spite password attempt
# ~13.1M candidates

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="${1:-hash.txt}"

if [ ! -f "$HASH_FILE" ]; then
    echo "Usage: $0 <hash_file>"
    echo "Example: $0 /path/to/hash.txt"
    exit 1
fi

echo "Starting comprehensive spite password attempt..."
echo "Candidates: ~13.1M"
echo "Estimated runtime: ~49 seconds at 270k H/s"
echo ""

python3 "$SCRIPT_DIR/generate.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
