#!/bin/bash
# Generate passwords matching Dean Pierce's documented communication style
# Based on profile analysis of GitHub commits, docs, and writing patterns
# Priority: lowercase, minimal, ironic, self-deprecating

OUTPUT_FILE="dean_style_passwords.txt"

echo "Generating passwords matching Dean Pierce's writing style..."
echo "Analysis: lowercase commits, self-deprecating humor, minimal effort, 2011 culture"
echo ""

# Clear output file
> "$OUTPUT_FILE"

#####################################
# TIER 1: Keyboard Patterns (Lowercase)
# Dean's style: minimal effort, literal mockery
# 10 chars exactly (Bitcoin minimum)
#####################################
echo "# TIER 1: Lowercase keyboard patterns (pure spite)" >> "$OUTPUT_FILE"
echo "qwertyuiop" >> "$OUTPUT_FILE"
echo "asdfghjkl;" >> "$OUTPUT_FILE"
echo "zxcvbnm,./" >> "$OUTPUT_FILE"
echo "qwerty1234" >> "$OUTPUT_FILE"
echo "asdfgh1234" >> "$OUTPUT_FILE"
echo "zxcvbn1234" >> "$OUTPUT_FILE"

# Variations without symbols
echo "asdfghjkla" >> "$OUTPUT_FILE"
echo "qwertyuiop1" >> "$OUTPUT_FILE"
echo "qwertyuiop!" >> "$OUTPUT_FILE"

#####################################
# TIER 2: Lowercase "password" + minimal
# Dean's style: literal mockery of requirements
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 2: Lowercase 'password' variants (literal mockery)" >> "$OUTPUT_FILE"
echo "password1!" >> "$OUTPUT_FILE"
echo "password!!" >> "$OUTPUT_FILE"
echo "password12" >> "$OUTPUT_FILE"
echo "password123" >> "$OUTPUT_FILE"
echo "password01" >> "$OUTPUT_FILE"
echo "password00" >> "$OUTPUT_FILE"
echo "password??" >> "$OUTPUT_FILE"
echo "password!?" >> "$OUTPUT_FILE"
echo "password~" >> "$OUTPUT_FILE"

#####################################
# TIER 3: Self-deprecating (lowercase)
# Dean's commits: "fixing dumbness"
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 3: Self-deprecating lowercase (matches 'fixing dumbness' style)" >> "$OUTPUT_FILE"
echo "badpasswd1" >> "$OUTPUT_FILE"
echo "badpasswd!" >> "$OUTPUT_FILE"
echo "weakpass12" >> "$OUTPUT_FILE"
echo "weakpass!!" >> "$OUTPUT_FILE"
echo "dumbpass12" >> "$OUTPUT_FILE"
echo "dumbpass!!" >> "$OUTPUT_FILE"
echo "mypassword" >> "$OUTPUT_FILE"
echo "badpass123" >> "$OUTPUT_FILE"
echo "weakpwd123" >> "$OUTPUT_FILE"

#####################################
# TIER 4: Repeated chars (ultimate laziness)
# Dean's style: minimal effort spite
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 4: Repeated characters (ultimate minimal effort)" >> "$OUTPUT_FILE"
echo "aaaaaaaaaa" >> "$OUTPUT_FILE"
echo "1111111111" >> "$OUTPUT_FILE"
echo "0000000000" >> "$OUTPUT_FILE"
echo "1234567890" >> "$OUTPUT_FILE"
echo "0987654321" >> "$OUTPUT_FILE"

#####################################
# TIER 5: Dean's "derp" culture
# Multiple repos use "derp"
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 5: Dean's 'derp' variants (used in multiple repos)" >> "$OUTPUT_FILE"
echo "derp123456" >> "$OUTPUT_FILE"
echo "derpderp12" >> "$OUTPUT_FILE"
echo "derp12345!" >> "$OUTPUT_FILE"
echo "derpderp!!" >> "$OUTPUT_FILE"

#####################################
# TIER 6: 2011 internet slang (lowercase)
# Dean's keyhunter from 2013, wallet from 2011
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 6: 2011-era internet slang (lowercase)" >> "$OUTPUT_FILE"
echo "yolo123456" >> "$OUTPUT_FILE"
echo "fail123456" >> "$OUTPUT_FILE"
echo "epic123456" >> "$OUTPUT_FILE"
echo "lulz123456" >> "$OUTPUT_FILE"

#####################################
# TIER 7: Ironic Bitcoin context
# Dean is Bitcoin researcher who "forgot" password
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 7: Ironic Bitcoin context" >> "$OUTPUT_FILE"
echo "bitcoin123" >> "$OUTPUT_FILE"
echo "btc1234567" >> "$OUTPUT_FILE"
echo "bitcoin!!" >> "$OUTPUT_FILE"
echo "satoshi123" >> "$OUTPUT_FILE"

#####################################
# TIER 8: Common + minimal (lowercase)
# Classic bad passwords, 10 chars
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 8: Common bad passwords (lowercase + minimal)" >> "$OUTPUT_FILE"
echo "letmein123" >> "$OUTPUT_FILE"
echo "welcome123" >> "$OUTPUT_FILE"
echo "admin12345" >> "$OUTPUT_FILE"
echo "login12345" >> "$OUTPUT_FILE"
echo "test123456" >> "$OUTPUT_FILE"

#####################################
# TIER 9: "yay" variants
# Dean uses "yay" in keyhunter docs
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 9: 'yay' variants (Dean uses this in docs)" >> "$OUTPUT_FILE"
echo "yay1234567" >> "$OUTPUT_FILE"
echo "yayyayyay1" >> "$OUTPUT_FILE"

#####################################
# TIER 10: Lowercase variants with trailing symbols
# Dean might add minimal symbols at end
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 10: Lowercase + trailing symbols" >> "$OUTPUT_FILE"
echo "qwerty1234!" >> "$OUTPUT_FILE"
echo "qwerty1234?" >> "$OUTPUT_FILE"
echo "password1234" >> "$OUTPUT_FILE"
echo "password1!!" >> "$OUTPUT_FILE"

#####################################
# TIER 11: LESS LIKELY - Capitalized variants
# Only if lowercase fails
# Dean's commits are lowercase, but worth trying
#####################################
echo "" >> "$OUTPUT_FILE"
echo "# TIER 11: LESS LIKELY - Capitalized variants (inconsistent with commit style)" >> "$OUTPUT_FILE"
echo "Password1!" >> "$OUTPUT_FILE"
echo "Password!!" >> "$OUTPUT_FILE"
echo "Qwertyuiop" >> "$OUTPUT_FILE"
echo "Badpasswd1" >> "$OUTPUT_FILE"
echo "Weakpass12" >> "$OUTPUT_FILE"

# Count and report
COUNT=$(wc -l < "$OUTPUT_FILE" | tr -d ' ')
echo ""
echo "Generated $COUNT password candidates in $OUTPUT_FILE"
echo ""
echo "Testing order priority:"
echo "1. Lowercase keyboard patterns (qwertyuiop, asdfghjkl;)"
echo "2. Lowercase 'password' + minimal (password1!, password!!)"
echo "3. Self-deprecating lowercase (badpasswd1, dumbpass12)"
echo "4. Repeated characters (aaaaaaaaaa, 1111111111)"
echo "5. Dean's 'derp' culture (derp123456)"
echo ""
echo "Run with: hashcat -m 11300 -a 0 -w 3 -O -D 2 hash.txt $OUTPUT_FILE"
