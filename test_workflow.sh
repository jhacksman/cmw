#!/bin/bash
# test_workflow.sh
# Control test to verify the password cracking workflow
# This creates a small test case to ensure your setup works before running the real attack

echo "=========================================="
echo "  Crack My Wallet - Workflow Test"
echo "=========================================="
echo ""
echo "This script helps you verify that your password cracking"
echo "setup is working correctly before attempting the real wallet."
echo ""

# Create test hash file
TEST_HASH_FILE="test_hash.txt"
REAL_HASH_FILE="wallet_hash.txt"

# Create the real hash file for reference
cat > "$REAL_HASH_FILE" << 'EOF'
$bitcoin$96$3fa8554bcc7f1adb4dee43327a2680be93112f8c11e9cbff7561038eddf258827dd38c72354695fc70d4a01102d22c48$16$14bff2455913f62c$25000$96$ad32dfdce53d6c1c7beb7c25f6c2a2730dc136201fe2423f57745743a5d78711b25c0c49c05092af9b8af506da74d066$130$04ffc8348b3538d3a865c4c0c359a7b4eefa687f2ecffda0aa763b58143df7d7ee7cbdbd62ce9fe6608e6c959c406cee192e35a4838e4f2f923d417ff09d0fd6ad
EOF

echo "[*] Real wallet hash saved to: $REAL_HASH_FILE"
echo ""

# Create a small test wordlist
TEST_WORDLIST="test_wordlist.txt"
cat > "$TEST_WORDLIST" << 'EOF'
this is a bad password
this is a very bad password
this is a really bad password
bad password
this is a dumb password
this is a derpy password
this.is.a.bad.password
this-is-a-bad-password
thisisabadpassword
this is a bad passphrase
this is a bad password!
this is a bad password!!!
this is a bad password?
this is a bad password1
this is a bad password123
th1s 1s 4 b4d p4ssw0rd
this is a bad p455word
this is a bad p@$$word
EOF

echo "[+] Test wordlist created: $TEST_WORDLIST (18 candidates)"
echo ""

echo "=========================================="
echo "  Testing Instructions"
echo "=========================================="
echo ""
echo "Step 1: Install John the Ripper (if not already installed)"
echo "  Ubuntu/Debian: sudo apt-get install john"
echo "  macOS: brew install john-jumbo"
echo "  Or compile from source: https://github.com/openwall/john"
echo ""
echo "Step 2: Verify John the Ripper supports Bitcoin hashes"
echo "  Run: john --list=formats | grep -i bitcoin"
echo "  You should see 'bitcoin' or 'Bitcoin-qt' in the output"
echo ""
echo "Step 3: Test with the small wordlist (optional warm-up)"
echo "  Run: john --wordlist=$TEST_WORDLIST --format=bitcoin $REAL_HASH_FILE"
echo ""
echo "Step 4: Generate the full password lists"
echo "  Run: ./generate_all_combinations.sh"
echo ""
echo "Step 5: Run John the Ripper on Tier 1 (highest priority)"
echo "  Run: john --wordlist=tier1_base_and_trailing.txt --format=bitcoin $REAL_HASH_FILE"
echo ""
echo "Step 6: If Tier 1 doesn't crack it, try Tier 2"
echo "  Run: john --wordlist=tier2_leetspeak.txt --format=bitcoin $REAL_HASH_FILE"
echo ""
echo "Step 7: If Tier 2 doesn't crack it, try Tier 3"
echo "  Run: john --wordlist=tier3_leetspeak_trailing.txt --format=bitcoin $REAL_HASH_FILE"
echo ""
echo "Step 8: Or run all candidates at once (may take longer)"
echo "  Run: john --wordlist=all_candidates.txt --format=bitcoin $REAL_HASH_FILE"
echo ""
echo "=========================================="
echo "  Alternative: Using Hashcat"
echo "=========================================="
echo ""
echo "If you prefer hashcat (usually faster with GPU):"
echo ""
echo "Step 1: Install hashcat"
echo "  Ubuntu/Debian: sudo apt-get install hashcat"
echo "  macOS: brew install hashcat"
echo ""
echo "Step 2: Run hashcat with mode 11300 (Bitcoin wallet)"
echo "  hashcat -m 11300 -a 0 $REAL_HASH_FILE tier1_base_and_trailing.txt"
echo ""
echo "Step 3: If cracked, the password will be shown"
echo "  hashcat -m 11300 $REAL_HASH_FILE --show"
echo ""
echo "=========================================="
echo "  Files Created"
echo "=========================================="
echo "  - $REAL_HASH_FILE (real wallet hash)"
echo "  - $TEST_WORDLIST (small test wordlist)"
echo ""
echo "When you crack it, tweet the password to @deanpierce!"
echo "=========================================="
