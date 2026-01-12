#!/bin/bash
# Limited Charset Brute Force - Position-constrained password generator
# ~9B candidates for 1-8 chars (~9.3 hours at 270k H/s)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="${1:-hash.txt}"

if [ ! -f "$HASH_FILE" ]; then
    echo "Usage: $0 <hash_file>"
    echo "Example: $0 /path/to/hash.txt"
    exit 1
fi

echo "Generating limited charset brute force candidates..."
echo "Position constraints:"
echo "  - P: positions 1-5 only"
echo "  - b: positions 1-5 only"
echo "  - d: positions 3-6 and 8-10 only"
echo "  - 1,2,3: positions 1-3 or last 3 only"
echo "  - ~\`!?: positions 1-3 or last 3 only"
echo "  - Last char: ~\`!?123"
echo ""
echo "Estimated: ~9B candidates (~9.3 hours at 270k H/s)"
echo ""

python3 "$SCRIPT_DIR/generate.py" 8 | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
