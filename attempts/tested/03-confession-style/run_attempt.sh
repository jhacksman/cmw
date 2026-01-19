#!/bin/bash
# Run confession style password attempt against Bitcoin wallet
# Estimated candidates: ~9.8B
# Runtime at 270k H/s: ~10 hours

if [ -z "$1" ]; then
    echo "Usage: ./run_attempt.sh <hash_file>"
    exit 1
fi

HASH_FILE="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_DIR/generate.py" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
