#!/bin/bash
# Run spite passphrase attempts against Bitcoin wallet hash
# Based on Dean's A/B test feedback

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HASH_FILE="$SCRIPT_DIR/hash.txt"

echo "=== Spite Passphrase Attempts ==="
echo "Based on Dean's A/B test feedback:"
echo "- Space separators"
echo "- First word capitalized"
echo "- Punctuation trailing"
echo "- Light leetspeak"
echo "- Spite theme"
echo ""

# Check for hashcat
if ! command -v hashcat &> /dev/null; then
    echo "Error: hashcat not found. Please install hashcat first."
    exit 1
fi

# Function to run a generator
run_generator() {
    local script=$1
    local name=$2
    local estimate=$3
    
    echo "Running $name (~$estimate candidates)..."
    echo "Command: python3 $script | hashcat -m 11300 -a 0 -w 3 -O $HASH_FILE"
    echo ""
    
    python3 "$SCRIPT_DIR/$script" | hashcat -m 11300 -a 0 -w 3 -O "$HASH_FILE"
    
    if [ $? -eq 0 ]; then
        echo "Completed $name"
    else
        echo "Error running $name (exit code: $?)"
    fi
    echo ""
}

# Menu
echo "Select which generator to run:"
echo "1. generate_common.py (~100M most likely patterns)"
echo "2. generate_6word.py (~1B 6-word passphrases)"
echo "3. generate_7word.py (~1B 7-word passphrases)"
echo "4. generate_8word.py (~1B 8-word passphrases)"
echo "5. Run all (common first, then 6/7/8 word)"
echo ""
read -p "Enter choice (1-5): " choice

case $choice in
    1)
        run_generator "generate_common.py" "Most Common Patterns" "100M"
        ;;
    2)
        run_generator "generate_6word.py" "6-Word Passphrases" "1B"
        ;;
    3)
        run_generator "generate_7word.py" "7-Word Passphrases" "1B"
        ;;
    4)
        run_generator "generate_8word.py" "8-Word Passphrases" "1B"
        ;;
    5)
        run_generator "generate_common.py" "Most Common Patterns" "100M"
        run_generator "generate_6word.py" "6-Word Passphrases" "1B"
        run_generator "generate_7word.py" "7-Word Passphrases" "1B"
        run_generator "generate_8word.py" "8-Word Passphrases" "1B"
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo "=== Attempt Complete ==="
