#!/bin/bash
# Run the password-is-spite brute force attempt
# ~33.4B candidates, ~34 hours at 270k H/s

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="${1:-hash.txt}"

if [ ! -f "$HASH_FILE" ]; then
    echo "Usage: $0 <hash_file>"
    echo "Example: $0 /path/to/hash.txt"
    exit 1
fi

echo "Starting password-is-spite brute force attempt..."
echo "Candidates: ~33.4B"
echo "Estimated runtime: ~34 hours at 270k H/s"
echo ""

python3 "$SCRIPT_DIR/generate.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
