#!/bin/bash
# Run the 10-char "dumbest possible" password attempt
# Estimated: ~727M candidates

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="$SCRIPT_DIR/generate_10char.py"
HASH_FILE="$SCRIPT_DIR/hash.txt"

if [[ "$1" == "--estimate" ]]; then
    python3 "$GENERATOR" --estimate
    exit 0
fi

# Stream directly to hashcat (no intermediate file needed)
python3 "$GENERATOR" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
