#!/bin/bash
#
# Crack My Wallet - 10 Billion Password Attempt Runner
# Combined Hypotheses: Spite Passphrase + Simple Spite
#
# Usage:
#   ./run_attempt.sh --estimate          # Show estimated count
#   ./run_attempt.sh > wordlist.txt      # Generate to file
#   ./run_attempt.sh --limit N           # Generate N candidates
#   ./run_attempt.sh | hashcat ...       # Pipe to hashcat
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="$SCRIPT_DIR/generate_10b.py"

if [[ ! -f "$GENERATOR" ]]; then
    echo "Error: Generator script not found at $GENERATOR" >&2
    exit 1
fi

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required but not found" >&2
    exit 1
fi

# Pass all arguments to the generator
python3 "$GENERATOR" "$@"
