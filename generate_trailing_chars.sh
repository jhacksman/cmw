#!/bin/bash
# generate_trailing_chars.sh
# Adds trailing characters to phrases based on Dean's patterns
# Dean mentioned: "Likely 1, 3, or maybe 6 characters - exclamations, question marks, tildes, backticks"
# Input: Any phrase file (base_phrases.txt or leetspeak_mutations.txt)
# Output: phrases_with_trailing.txt

INPUT_FILE="${1:-base_phrases.txt}"
OUTPUT_FILE="phrases_with_trailing.txt"

if [ ! -f "$INPUT_FILE" ]; then
    echo "[!] Error: Input file $INPUT_FILE not found"
    exit 1
fi

> "$OUTPUT_FILE"  # Clear file

echo "[*] Adding trailing characters to $INPUT_FILE..."

# Dean's trailing patterns:
# - 1, 3, or maybe 6 characters
# - Exclamations (!)
# - Question marks (?)
# - Tildes (~)
# - Backticks (`)
# Also numbers: 1, 123

TRAILING_PATTERNS=(
    # Single character (most common)
    "!"
    "?"
    "~"
    "\`"
    "1"

    # Three characters (common)
    "!!!"
    "???"
    "~~~"
    "123"
    "111"
    "!?!"
    "!~!"

    # Six characters (maybe)
    "!!!!!!"
    "123456"
    "111111"
    "!?!?!?"
    "~~~~~~"

    # Mixed patterns
    "!1"
    "?1"
    "!11"
    "!23"
)

# Function to add trailing patterns
add_trailing() {
    local phrase="$1"

    # Output original (no trailing)
    echo "$phrase"

    # Add each trailing pattern
    for trail in "${TRAILING_PATTERNS[@]}"; do
        echo "${phrase}${trail}"
    done
}

# Process each phrase
while IFS= read -r phrase; do
    add_trailing "$phrase" >> "$OUTPUT_FILE"
done < "$INPUT_FILE"

# Remove duplicates and sort
sort -u "$OUTPUT_FILE" -o "$OUTPUT_FILE"

TOTAL=$(wc -l < "$OUTPUT_FILE")
echo "[+] Generated $TOTAL phrases with trailing chars -> $OUTPUT_FILE"
