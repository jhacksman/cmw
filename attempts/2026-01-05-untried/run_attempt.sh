#!/bin/bash
#
# Crack My Wallet - 2026-01-05 Attempt
# 
# This script generates ~1 billion passphrase candidates based on Dean Pierce's
# hints and pipes them to hashcat for cracking.
#
# Usage:
#   ./run_attempt.sh                    # Generate candidates to stdout
#   ./run_attempt.sh > wordlist.txt     # Save to file
#   ./run_attempt.sh | hashcat ...      # Pipe directly to hashcat
#
# Options:
#   --estimate    Show estimated candidate count
#   --limit N     Generate only N candidates (for testing)
#   --chunk N     Generate chunk N of 10 (for parallel processing)
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="$SCRIPT_DIR/generate_1b.py"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required but not found" >&2
    exit 1
fi

# Check if generator exists
if [ ! -f "$GENERATOR" ]; then
    echo "Error: Generator script not found at $GENERATOR" >&2
    exit 1
fi

# Pass all arguments to the Python generator
python3 "$GENERATOR" "$@"
