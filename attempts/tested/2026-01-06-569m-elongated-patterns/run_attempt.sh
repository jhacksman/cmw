#!/bin/bash
# Elongated Potato/Poop Pattern Attempt
# ~569M candidates targeting Dean's "dumbest passphrase" with elongated words
#
# Based on:
# - NO MIXING rule: all instances of a character use the same leetspeak variant
# - Words: potato, poop, poopy, pootato, poopoo (elongated 10-20 chars)
# - Trailing: 0-6 chars from !?~`
# - Leading: "" or "this is a "
#
# Usage:
#   ./run_attempt.sh              # Stream to hashcat
#   ./run_attempt.sh --estimate   # Show candidate count
#   ./run_attempt.sh > wordlist.txt  # Save to file

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="$SCRIPT_DIR/generate_569m.py"
HASH_FILE="$SCRIPT_DIR/hash.txt"

# Check if estimate mode
if [[ "$1" == "--estimate" ]]; then
    python3 "$GENERATOR" --estimate
    exit 0
fi

# Check if hash file exists
if [[ ! -f "$HASH_FILE" ]]; then
    echo "Error: hash.txt not found at $HASH_FILE" >&2
    exit 1
fi

# Check if output is being redirected to a file
if [[ ! -t 1 ]]; then
    # Output is redirected, just generate
    python3 "$GENERATOR"
else
    # Output to terminal, pipe to hashcat
    echo "Starting hashcat with ~569M candidates..." >&2
    echo "Estimated time depends on your GPU speed." >&2
    echo "" >&2
    
    python3 "$GENERATOR" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
fi
