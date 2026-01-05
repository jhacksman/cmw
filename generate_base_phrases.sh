#!/bin/bash
# generate_base_phrases.sh
# Generates base passphrase candidates based on Dean Pierce's hints
# Output: base_phrases.txt

OUTPUT_FILE="base_phrases.txt"
> "$OUTPUT_FILE"  # Clear file

# Arrays of components based on Dean's hints
PREFIXES=(
    "this is a"
    "this is a really"
    "this is a very"
    "this is such a"
    "this is the"
    "what a"
    "such a"
    "my"
    "a really"
    "a very"
    "i have a"
    "i made a"
    ""  # Empty for just "adjective noun" patterns
)

ADJECTIVES=(
    "bad"
    "dumb"
    "stupid"
    "terrible"
    "awful"
    "weak"
    "simple"
    "easy"
    "lazy"
    "derpy"          # 2011 era slang - HIGH PRIORITY
    "lulzy"
    "lame"
    "crappy"
    "shitty"
    "silly"
    "ridiculous"
    "embarrassing"
    "pathetic"
    "horrible"
    "worst"
    "terrible"
    "lulz"
    "derpish"
    "derped"
)

NOUNS=(
    "password"
    "passphrase"
    "pass"
    "passwd"
    "secret"
    "key"
)

SEPARATORS=(
    " "    # Space - MOST LIKELY
    "."    # Period - sometimes
    "-"    # Dash - rarely
)

echo "[*] Generating base phrases..."

# Generate all combinations
for prefix in "${PREFIXES[@]}"; do
    for adj in "${ADJECTIVES[@]}"; do
        for noun in "${NOUNS[@]}"; do
            for sep in "${SEPARATORS[@]}"; do
                if [ -z "$prefix" ]; then
                    # No prefix, just "adjective noun"
                    phrase="${adj}${sep}${noun}"
                else
                    # With prefix
                    phrase="${prefix}${sep}${adj}${sep}${noun}"
                fi

                # Output lowercase version
                echo "$phrase" | tr '[:upper:]' '[:lower:]' >> "$OUTPUT_FILE"

                # Output Title Case version
                echo "$phrase" | sed 's/\b\(.\)/\u\1/g' >> "$OUTPUT_FILE"

                # Output first letter caps only
                first_letter=$(echo "$phrase" | cut -c1 | tr '[:lower:]' '[:upper:]')
                rest=$(echo "$phrase" | cut -c2-)
                echo "${first_letter}${rest}" >> "$OUTPUT_FILE"
            done
        done
    done
done

# Add some specific high-priority phrases Dean mentioned
echo "this is a bad password" >> "$OUTPUT_FILE"
echo "bad password" >> "$OUTPUT_FILE"
echo "this is a very bad password" >> "$OUTPUT_FILE"
echo "this is a really dumb passphrase" >> "$OUTPUT_FILE"
echo "this is a bad passphrase" >> "$OUTPUT_FILE"

# Add repeated character patterns (Dean mentioned "pooooooooooooooop")
echo "baaaaaad password" >> "$OUTPUT_FILE"
echo "duuuuumb password" >> "$OUTPUT_FILE"
echo "this is baaaaaad" >> "$OUTPUT_FILE"
echo "sooooo bad" >> "$OUTPUT_FILE"
echo "soooooo bad password" >> "$OUTPUT_FILE"
echo "really baaaaaad password" >> "$OUTPUT_FILE"

# Remove duplicates and sort
sort -u "$OUTPUT_FILE" -o "$OUTPUT_FILE"

TOTAL=$(wc -l < "$OUTPUT_FILE")
echo "[+] Generated $TOTAL base phrases -> $OUTPUT_FILE"
