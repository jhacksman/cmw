#!/bin/bash
# generate_all_combinations.sh
# Master script that generates all password combinations
# This runs all generation scripts in sequence and creates final wordlists

set -e  # Exit on error

echo "=========================================="
echo "  Crack My Wallet - Password Generator"
echo "=========================================="
echo ""

# Make scripts executable
chmod +x generate_base_phrases.sh
chmod +x generate_leetspeak_mutations.sh
chmod +x generate_trailing_chars.sh

# Step 1: Generate base phrases
echo "[STEP 1/5] Generating base phrases..."
./generate_base_phrases.sh
echo ""

# Step 2: Apply leetspeak to base phrases
echo "[STEP 2/5] Applying leetspeak mutations to base phrases..."
./generate_leetspeak_mutations.sh base_phrases.txt
echo ""

# Step 3: Add trailing chars to base phrases (no leetspeak)
echo "[STEP 3/5] Adding trailing characters to base phrases..."
./generate_trailing_chars.sh base_phrases.txt
mv phrases_with_trailing.txt base_phrases_with_trailing.txt
echo ""

# Step 4: Add trailing chars to leetspeak mutations
echo "[STEP 4/5] Adding trailing characters to leetspeak mutations..."
./generate_trailing_chars.sh leetspeak_mutations.txt
mv phrases_with_trailing.txt leetspeak_with_trailing.txt
echo ""

# Step 5: Combine all into priority-ordered lists
echo "[STEP 5/5] Creating final wordlists..."

# Create tier-based wordlists for efficient cracking

# TIER 1: Highest priority - base phrases + light mutations
cat base_phrases.txt base_phrases_with_trailing.txt | sort -u > tier1_base_and_trailing.txt
TIER1=$(wc -l < tier1_base_and_trailing.txt)
echo "[+] Tier 1 (base + trailing): $TIER1 candidates -> tier1_base_and_trailing.txt"

# TIER 2: Medium priority - leetspeak without trailing
cp leetspeak_mutations.txt tier2_leetspeak.txt
TIER2=$(wc -l < tier2_leetspeak.txt)
echo "[+] Tier 2 (leetspeak): $TIER2 candidates -> tier2_leetspeak.txt"

# TIER 3: Lower priority - leetspeak with trailing (largest set)
cp leetspeak_with_trailing.txt tier3_leetspeak_trailing.txt
TIER3=$(wc -l < tier3_leetspeak_trailing.txt)
echo "[+] Tier 3 (leetspeak + trailing): $TIER3 candidates -> tier3_leetspeak_trailing.txt"

# Create a single comprehensive wordlist (all candidates)
cat tier1_base_and_trailing.txt tier2_leetspeak.txt tier3_leetspeak_trailing.txt | sort -u > all_candidates.txt
TOTAL=$(wc -l < all_candidates.txt)

echo ""
echo "=========================================="
echo "  Generation Complete!"
echo "=========================================="
echo "Total unique candidates: $TOTAL"
echo ""
echo "Wordlists created:"
echo "  - tier1_base_and_trailing.txt ($TIER1 candidates) - START HERE"
echo "  - tier2_leetspeak.txt ($TIER2 candidates)"
echo "  - tier3_leetspeak_trailing.txt ($TIER3 candidates)"
echo "  - all_candidates.txt ($TOTAL candidates) - All combined"
echo ""
echo "Recommended cracking order:"
echo "  1. Run tier1_base_and_trailing.txt first (most likely)"
echo "  2. Then tier2_leetspeak.txt"
echo "  3. Finally tier3_leetspeak_trailing.txt (largest)"
echo ""
echo "Next steps:"
echo "  See README.md for instructions on running with John the Ripper"
echo "=========================================="
