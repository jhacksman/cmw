#!/bin/bash
# generate_spite_passwords.sh
# Generates 10-character "spite passwords" based on Dean's statement:
# "I definitely set my password to the weakest possible thing I could out of spite"
#
# Bitcoin 0.4.0 requirement: "10 or more random characters"
# Dean likely used EXACTLY 10 characters (minimum) in the simplest way possible
#
# This is UNTESTED SEARCH SPACE - everyone focused on multi-word passphrases!

OUTPUT_FILE="spite_passwords_10char.txt"
> "$OUTPUT_FILE"

echo "[*] Generating 10-character spite passwords..."
echo "[*] Theory: Dean used minimum length (10 chars) out of spite"

# ============================================================================
# TIER 1: Ultra-Simple Common Password Patterns (HIGHEST PRIORITY)
# ============================================================================

echo "[+] Tier 1: Common passwords extended to exactly 10 chars..."

# password variations (most common password)
echo "password1!" >> "$OUTPUT_FILE"  # 10 chars
echo "Password1!" >> "$OUTPUT_FILE"  # meets enterprise requirements
echo "password!!" >> "$OUTPUT_FILE"  # 10 chars
echo "password01" >> "$OUTPUT_FILE"  # 10 chars
echo "password10" >> "$OUTPUT_FILE"
echo "password99" >> "$OUTPUT_FILE"
echo "password12" >> "$OUTPUT_FILE"
echo "password!1" >> "$OUTPUT_FILE"
echo "password1?" >> "$OUTPUT_FILE"
echo "password?!" >> "$OUTPUT_FILE"
echo "password@1" >> "$OUTPUT_FILE"
echo "password#1" >> "$OUTPUT_FILE"
echo "PASSWORD1!" >> "$OUTPUT_FILE"  # all caps variant

# p@ssword variations
echo "p@ssword1!" >> "$OUTPUT_FILE"
echo "P@ssword1!" >> "$OUTPUT_FILE"
echo "p@ssword!!" >> "$OUTPUT_FILE"
echo "p@ssw0rd!!" >> "$OUTPUT_FILE"

# passw0rd variations
echo "passw0rd1!" >> "$OUTPUT_FILE"
echo "Passw0rd1!" >> "$OUTPUT_FILE"
echo "passw0rd!!" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 2: Self-Deprecating 10-Character Passwords
# ============================================================================

echo "[+] Tier 2: Self-deprecating passwords (10 chars)..."

# bad variations
echo "badpass123" >> "$OUTPUT_FILE"  # 10 chars
echo "badpass1!!" >> "$OUTPUT_FILE"
echo "badpass!!!" >> "$OUTPUT_FILE"
echo "Badpass1!!" >> "$OUTPUT_FILE"
echo "badpasswd!" >> "$OUTPUT_FILE"
echo "badpwd1234" >> "$OUTPUT_FILE"

# weak variations
echo "weakpass1!" >> "$OUTPUT_FILE"
echo "weakpass!!" >> "$OUTPUT_FILE"
echo "Weakpass1!" >> "$OUTPUT_FILE"
echo "weak12345!" >> "$OUTPUT_FILE"

# dumb variations
echo "dumbpass1!" >> "$OUTPUT_FILE"
echo "dumbpass!!" >> "$OUTPUT_FILE"
echo "Dumbpass1!" >> "$OUTPUT_FILE"

# simple variations
echo "simplepass" >> "$OUTPUT_FILE"  # 10 chars
echo "simple1234" >> "$OUTPUT_FILE"
echo "simple123!" >> "$OUTPUT_FILE"
echo "Simple123!" >> "$OUTPUT_FILE"

# easy variations
echo "easypass12" >> "$OUTPUT_FILE"
echo "easypass1!" >> "$OUTPUT_FILE"
echo "easy123456" >> "$OUTPUT_FILE"

# lazy variations
echo "lazypass1!" >> "$OUTPUT_FILE"
echo "lazypass!!" >> "$OUTPUT_FILE"

# terrible variations
echo "terrible!!" >> "$OUTPUT_FILE"  # 10 chars
echo "terrible1!" >> "$OUTPUT_FILE"
echo "Terrible1!" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 3: 2011 Slang + Padding to 10 Chars
# ============================================================================

echo "[+] Tier 3: 2011 slang passwords (10 chars)..."

# derpy (popular in 2011)
echo "derpy12345" >> "$OUTPUT_FILE"
echo "derpy1234!" >> "$OUTPUT_FILE"
echo "derpypass!" >> "$OUTPUT_FILE"
echo "Derpy1234!" >> "$OUTPUT_FILE"
echo "derp123456" >> "$OUTPUT_FILE"

# lulz variations
echo "lulzpass1!" >> "$OUTPUT_FILE"
echo "lulzpass!!" >> "$OUTPUT_FILE"
echo "lulz123456" >> "$OUTPUT_FILE"

# other 2011 slang
echo "fail123456" >> "$OUTPUT_FILE"
echo "epic123456" >> "$OUTPUT_FILE"
echo "rofl123456" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 4: Keyboard Patterns (VERY COMMON SPITE PASSWORD)
# ============================================================================

echo "[+] Tier 4: Keyboard patterns (10 chars)..."

# Top row
echo "qwertyuiop" >> "$OUTPUT_FILE"  # 10 chars - very common
echo "Qwertyuiop" >> "$OUTPUT_FILE"
echo "QWERTYUIOP" >> "$OUTPUT_FILE"
echo "qwertyuio!" >> "$OUTPUT_FILE"
echo "Qwertyuio1" >> "$OUTPUT_FILE"

# Second row
echo "asdfghjkl;" >> "$OUTPUT_FILE"  # 10 chars
echo "asdfghjkl!" >> "$OUTPUT_FILE"
echo "Asdfghjkl1" >> "$OUTPUT_FILE"

# Number row
echo "1234567890" >> "$OUTPUT_FILE"  # 10 digits
echo "!234567890" >> "$OUTPUT_FILE"
echo "1234567890!" >> "$OUTPUT_FILE"  # 11 chars but close

# Diagonal patterns
echo "1qaz2wsx3e" >> "$OUTPUT_FILE"
echo "!qaz@wsx#e" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 5: Repeated Character Patterns (Dean mentioned "pooooop")
# ============================================================================

echo "[+] Tier 5: Repeated character patterns (10 chars)..."

# All same character
echo "aaaaaaaaaa" >> "$OUTPUT_FILE"  # 10 a's - ultimate spite!
echo "AAAAAAAAAA" >> "$OUTPUT_FILE"
echo "1111111111" >> "$OUTPUT_FILE"  # 10 1's
echo "!!!!!!!!!!" >> "$OUTPUT_FILE"  # 10 !'s

# Variations
echo "aaaaaaaaaa!" >> "$OUTPUT_FILE"  # 11 chars
echo "1111111111!" >> "$OUTPUT_FILE"
echo "aaaaaa1234" >> "$OUTPUT_FILE"  # 10 chars

# Dean's example: "pooooooooooooop"
echo "poooooooop" >> "$OUTPUT_FILE"  # 10 chars
echo "pooooooop!" >> "$OUTPUT_FILE"  # 10 chars

# Other repeated patterns
echo "passworddd" >> "$OUTPUT_FILE"  # password + repeated d
echo "passsssss1" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 6: Ironic/Sarcastic Passwords
# ============================================================================

echo "[+] Tier 6: Ironic spite passwords (10 chars)..."

echo "notasecure" >> "$OUTPUT_FILE"  # 10 chars
echo "notsecure!" >> "$OUTPUT_FILE"
echo "insecure1!" >> "$OUTPUT_FILE"
echo "insecure!!" >> "$OUTPUT_FILE"
echo "Insecure1!" >> "$OUTPUT_FILE"
echo "unsafe1234" >> "$OUTPUT_FILE"
echo "crackable!" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 7: Bitcoin/Defcon/Vegas Context
# ============================================================================

echo "[+] Tier 7: Bitcoin/Defcon/Vegas context (10 chars)..."

echo "bitcoin123" >> "$OUTPUT_FILE"  # 10 chars
echo "bitcoin1!!" >> "$OUTPUT_FILE"
echo "Bitcoin1!!" >> "$OUTPUT_FILE"
echo "btc1234567" >> "$OUTPUT_FILE"
echo "defcon2011" >> "$OUTPUT_FILE"  # 10 chars
echo "defcon19!!" >> "$OUTPUT_FILE"
echo "vegas2011!" >> "$OUTPUT_FILE"
echo "lasvegas11" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 8: Common Corporate Passwords
# ============================================================================

echo "[+] Tier 8: Corporate password patterns (10 chars)..."

echo "Welcome1!!" >> "$OUTPUT_FILE"
echo "Welcome123" >> "$OUTPUT_FILE"  # 10 chars
echo "Admin12345" >> "$OUTPUT_FILE"
echo "Admin1234!" >> "$OUTPUT_FILE"
echo "User123456" >> "$OUTPUT_FILE"
echo "Test123456" >> "$OUTPUT_FILE"
echo "Temp123456" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 9: Extended Common Passwords to 10
# ============================================================================

echo "[+] Tier 9: Common passwords padded to 10..."

echo "letmein123" >> "$OUTPUT_FILE"
echo "letmein!!!" >> "$OUTPUT_FILE"
echo "welcome!!!" >> "$OUTPUT_FILE"
echo "monkey1234" >> "$OUTPUT_FILE"
echo "dragon1234" >> "$OUTPUT_FILE"
echo "master1234" >> "$OUTPUT_FILE"
echo "abc1234567" >> "$OUTPUT_FILE"
echo "trustno1!!" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 10: Number Padding Patterns
# ============================================================================

echo "[+] Tier 10: Number padding to 10 chars..."

# password + 00-99
for i in {0..99}; do
    printf "password%02d\n" $i >> "$OUTPUT_FILE"
done

# badpass + 000-999
for i in {0..999}; do
    printf "badpass%03d\n" $i >> "$OUTPUT_FILE"
done

# simple + 0000-9999
for i in {0..9999}; do
    printf "simple%04d\n" $i >> "$OUTPUT_FILE"
done

# ============================================================================
# TIER 11: Case Variations of High-Priority Patterns
# ============================================================================

echo "[+] Tier 11: Case variations..."

# All lowercase common passwords
for word in password badpass weakpass dumbpass easypass simplepass; do
    # Lowercase + various endings to make 10
    echo "${word}1!" >> "$OUTPUT_FILE"
    echo "${word}!!" >> "$OUTPUT_FILE"
    echo "${word}12" >> "$OUTPUT_FILE"
    echo "${word}01" >> "$OUTPUT_FILE"
    echo "${word}?!" >> "$OUTPUT_FILE"
done

# Capitalized versions
for word in Password Badpass Weakpass Dumbpass Easypass Simplepass; do
    echo "${word}1!" >> "$OUTPUT_FILE"
    echo "${word}!!" >> "$OUTPUT_FILE"
done

# ============================================================================
# TIER 12: Minimal Leet + Padding
# ============================================================================

echo "[+] Tier 12: Minimal leetspeak (10 chars)..."

# p@ssword variants
echo "p@ssword1!" >> "$OUTPUT_FILE"
echo "P@ssword1!" >> "$OUTPUT_FILE"
echo "p@ssw0rd1!" >> "$OUTPUT_FILE"
echo "P@ssw0rd1!" >> "$OUTPUT_FILE"

# b@dp@ss variants
echo "b@dpass123" >> "$OUTPUT_FILE"
echo "b@dp@ss123" >> "$OUTPUT_FILE"

# passw0rd variants
echo "p@ssw0rd!!" >> "$OUTPUT_FILE"
echo "passw0rd1!" >> "$OUTPUT_FILE"

# ============================================================================
# TIER 13: Symbol Suffix Patterns
# ============================================================================

echo "[+] Tier 13: Symbol suffixes (10 chars)..."

# Common base + !!
echo "password!!" >> "$OUTPUT_FILE"
echo "badpass!!!" >> "$OUTPUT_FILE"
echo "simple!!!!" >> "$OUTPUT_FILE"

# Common base + ?
echo "password??" >> "$OUTPUT_FILE"
echo "badpass???" >> "$OUTPUT_FILE"

# Common base + ~
echo "password~~" >> "$OUTPUT_FILE"
echo "badpass~~~" >> "$OUTPUT_FILE"

# ============================================================================
# Summary
# ============================================================================

# Remove duplicates
sort -u "$OUTPUT_FILE" -o "$OUTPUT_FILE"

TOTAL=$(wc -l < "$OUTPUT_FILE")
echo ""
echo "=========================================="
echo "[+] Generated $TOTAL unique 10-character spite passwords"
echo "[+] Output: $OUTPUT_FILE"
echo "=========================================="
echo ""
echo "This wordlist targets the UNTESTED search space:"
echo "  - Dean said: 'weakest possible thing out of spite'"
echo "  - Bitcoin 0.4.0 minimum: 10 characters"
echo "  - Previous tests stopped at 6-9 characters"
echo "  - Everyone assumed multi-word passphrases"
echo ""
echo "Test with:"
echo "  hashcat -m 11300 -a 0 wallet_hash.txt $OUTPUT_FILE"
echo ""
echo "Priority: HIGHEST - This may be THE answer!"
echo "=========================================="
