#!/bin/bash
#
# Crack My Wallet - 2-3B Research-Based Attempt Runner
#
# This script runs the password generator and pipes to hashcat.
# Optimized for DGX Spark (GB10 Grace Blackwell) with unified memory.
#
# Usage:
#   ./run_attempt.sh                    # Run with hashcat
#   ./run_attempt.sh --estimate         # Show candidate count estimate
#   ./run_attempt.sh --to-file FILE     # Save wordlist to file
#   ./run_attempt.sh --help             # Show this help
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="$SCRIPT_DIR/generate_2b.py"
HASH_FILE="$SCRIPT_DIR/hash.txt"

# Check if generator exists
if [[ ! -f "$GENERATOR" ]]; then
    echo "Error: Generator script not found at $GENERATOR"
    exit 1
fi

# Check if hash file exists
if [[ ! -f "$HASH_FILE" ]]; then
    echo "Error: Hash file not found at $HASH_FILE"
    exit 1
fi

# Parse arguments
case "${1:-}" in
    --estimate)
        echo "Estimating candidate count..."
        python3 "$GENERATOR" --estimate
        exit 0
        ;;
    --to-file)
        if [[ -z "${2:-}" ]]; then
            echo "Error: --to-file requires a filename"
            exit 1
        fi
        echo "Generating wordlist to $2..."
        python3 "$GENERATOR" > "$2"
        echo "Done. Wordlist saved to $2"
        exit 0
        ;;
    --help|-h)
        echo "Crack My Wallet - 2-3B Research-Based Attempt Runner"
        echo ""
        echo "Usage:"
        echo "  ./run_attempt.sh                    # Run with hashcat"
        echo "  ./run_attempt.sh --estimate         # Show candidate count estimate"
        echo "  ./run_attempt.sh --to-file FILE     # Save wordlist to file"
        echo "  ./run_attempt.sh --help             # Show this help"
        echo ""
        echo "This attempt targets ~2.2 billion candidates based on:"
        echo "  - 'X is/are hard' pattern (Dean's signature phrase)"
        echo "  - Potato patterns (confirmed significant from Mastodon)"
        echo "  - 2011 blog-derived phrases"
        echo "  - Expletive patterns"
        echo "  - Vim typos (!wq endings)"
        echo "  - Derp patterns"
        echo "  - 2011 memes"
        exit 0
        ;;
esac

# Run with hashcat
# -m 11300: Bitcoin/Litecoin wallet.dat
# -a 0: Dictionary attack (wordlist)
# -w 3: Workload profile high (best for dedicated cracking)
# -O: Optimized kernels (faster)
# --status: Show status updates
# --status-timer=60: Update every 60 seconds

echo "Starting hashcat with ~2.2B research-based candidates..."
echo "Hash file: $HASH_FILE"
echo ""

python3 "$GENERATOR" | hashcat -m 11300 -a 0 -w 3 -O --status --status-timer=60 "$HASH_FILE"
