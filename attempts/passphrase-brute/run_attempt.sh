#!/bin/bash
# Passphrase/Password Brute Force with Prefix+Suffix Pattern
# ~142M candidates
# Runtime: ~8.8 minutes at 270k H/s (3x 3090)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -z "$1" ]; then
    echo "Usage: $0 <hash_file>"
    echo "Example: $0 hash.txt"
    exit 1
fi

HASH_FILE="$1"

echo "Starting passphrase-brute attempt..."
echo "Candidates: ~142M"
echo "Estimated runtime: ~8.8 minutes at 270k H/s"
echo ""

python3 "$SCRIPT_DIR/generate.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
