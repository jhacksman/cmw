#!/bin/bash
# generate_leetspeak_mutations.sh
# Applies leetspeak transformations based on Dean's specific patterns
# Input: base_phrases.txt
# Output: leetspeak_mutations.txt

INPUT_FILE="${1:-base_phrases.txt}"
OUTPUT_FILE="leetspeak_mutations.txt"

if [ ! -f "$INPUT_FILE" ]; then
    echo "[!] Error: Input file $INPUT_FILE not found"
    echo "[!] Run generate_base_phrases.sh first"
    exit 1
fi

> "$OUTPUT_FILE"  # Clear file

echo "[*] Applying leetspeak mutations to $INPUT_FILE..."

# Function to apply leetspeak transformations
apply_leet() {
    local phrase="$1"

    # Output original
    echo "$phrase"

    # Dean's confirmed patterns:
    # - a -> @ or 4
    # - s -> $ or 5
    # - pass -> p455, p@$$
    # - e -> 3
    # - i -> 1 or !
    # - o -> 0
    # - NOT: 7 for r (Dean never uses this)
    # - NOT: | pipe character (Dean never uses this)

    # Light mutations (most likely)
    echo "$phrase" | sed 's/pass/p455/g'                    # pass -> p455
    echo "$phrase" | sed 's/pass/p@$$/g'                    # pass -> p@$$
    echo "$phrase" | sed 's/Pass/P455/g'                    # Pass -> P455
    echo "$phrase" | sed 's/Pass/P@$$/g'                    # Pass -> P@$$

    # Single character substitutions
    echo "$phrase" | sed 's/a/@/g'                          # a -> @
    echo "$phrase" | sed 's/a/4/g'                          # a -> 4
    echo "$phrase" | sed 's/s/$/g'                          # s -> $
    echo "$phrase" | sed 's/s/5/g'                          # s -> 5
    echo "$phrase" | sed 's/e/3/g'                          # e -> 3
    echo "$phrase" | sed 's/i/1/g'                          # i -> 1
    echo "$phrase" | sed 's/o/0/g'                          # o -> 0

    # Combo mutations - pass variations with other chars
    echo "$phrase" | sed 's/pass/p455/g; s/a/@/g'           # p455 + @ for other a's
    echo "$phrase" | sed 's/pass/p@$$/g; s/s/5/g'           # p@$$ + 5 for other s's
    echo "$phrase" | sed 's/pass/p455/g; s/e/3/g'           # p455 + e->3
    echo "$phrase" | sed 's/pass/p@$$/g; s/a/4/g'           # p@$$ + a->4

    # Medium mutations (moderate likelihood)
    echo "$phrase" | sed 's/a/@/g; s/s/$/g'                 # a->@ and s->$
    echo "$phrase" | sed 's/a/4/g; s/s/5/g'                 # a->4 and s->5
    echo "$phrase" | sed 's/a/@/g; s/s/5/g'                 # a->@ and s->5
    echo "$phrase" | sed 's/a/4/g; s/s/$/g'                 # a->4 and s->$

    # With additional common substitutions
    echo "$phrase" | sed 's/a/@/g; s/s/$/g; s/e/3/g'        # @, $, 3
    echo "$phrase" | sed 's/a/4/g; s/s/5/g; s/e/3/g'        # 4, 5, 3
    echo "$phrase" | sed 's/a/@/g; s/s/$/g; s/i/1/g'        # @, $, 1
    echo "$phrase" | sed 's/a/4/g; s/s/5/g; s/o/0/g'        # 4, 5, 0

    # Heavier mutations (less likely but possible)
    echo "$phrase" | sed 's/a/@/g; s/s/$/g; s/e/3/g; s/i/1/g'       # @, $, 3, 1
    echo "$phrase" | sed 's/a/4/g; s/s/5/g; s/e/3/g; s/o/0/g'       # 4, 5, 3, 0
    echo "$phrase" | sed 's/a/@/g; s/s/$/g; s/e/3/g; s/i/1/g; s/o/0/g'  # All common

    # Capital letter at start with leetspeak
    local first_upper=$(echo "$phrase" | sed 's/^\(.\)/\U\1/')
    echo "$first_upper" | sed 's/pass/p455/g'
    echo "$first_upper" | sed 's/pass/p@$$/g'
    echo "$first_upper" | sed 's/a/@/g; s/s/$/g'
}

# Process each base phrase
while IFS= read -r phrase; do
    apply_leet "$phrase" >> "$OUTPUT_FILE"
done < "$INPUT_FILE"

# Remove duplicates and sort
sort -u "$OUTPUT_FILE" -o "$OUTPUT_FILE"

TOTAL=$(wc -l < "$OUTPUT_FILE")
echo "[+] Generated $TOTAL leetspeak mutations -> $OUTPUT_FILE"
