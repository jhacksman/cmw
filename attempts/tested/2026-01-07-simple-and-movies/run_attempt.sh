#!/bin/bash
# Run the simple phrases + movie references attempt
# ~55.1M candidates, ~3.4 minutes at 270k H/s

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="${SCRIPT_DIR}/../tested/2026-01-06-8word-dumbest/hash.txt"

echo "Starting simple phrases + movie references attempt..."
echo "Candidates: ~55.1M"
echo "Estimated time: ~3.4 minutes at 270k H/s"
echo ""

python3 "${SCRIPT_DIR}/generate_simple_and_movies.py" | hashcat -m 11300 -a 0 -w 3 -O "${HASH_FILE}"
