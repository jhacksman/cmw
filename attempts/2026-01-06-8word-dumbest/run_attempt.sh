#!/bin/bash
# Run the 8-word dumbest passphrase attempt against the Bitcoin wallet hash
#
# Usage:
#   ./run_attempt.sh              # Pipe directly to hashcat
#   ./run_attempt.sh --estimate   # Show estimated candidate count
#
# This script generates ~1M candidates targeting 8-word "dumbest possible"
# passphrase patterns based on Dean's hints from Telegram.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="$SCRIPT_DIR/generate_8word.py"
HASH_FILE="$SCRIPT_DIR/hash.txt"

if [[ "$1" == "--estimate" ]]; then
    python3 "$GENERATOR" --estimate
    exit 0
fi

python3 "$GENERATOR" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
