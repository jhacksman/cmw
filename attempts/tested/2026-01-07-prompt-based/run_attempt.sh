#!/bin/bash
# Run the prompt-based password attempt
# ~72M candidates, ~4.4 minutes at 270k H/s

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="${SCRIPT_DIR}/../tested/2026-01-06-8word-dumbest/hash.txt"

echo "Starting prompt-based password attempt..."
echo "Candidates: ~72M"
echo "Estimated time: ~4.4 minutes at 270k H/s"
echo ""

python3 "${SCRIPT_DIR}/generate_prompt_based.py" | hashcat -m 11300 -a 0 -w 3 -O "${HASH_FILE}"
