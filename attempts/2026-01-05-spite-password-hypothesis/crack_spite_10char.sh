#!/bin/bash
# crack_spite_10char.sh
# Comprehensive 10-character password attack script
# Generates BILLIONS of candidates via mask attacks

HASH_FILE="hash.txt"

if [ ! -f "$HASH_FILE" ]; then
    echo "[!] Error: $HASH_FILE not found"
    echo "[!] Create it first with the bitcoin hash"
    exit 1
fi

# Hashcat optimized flags
HC_FLAGS="-m 11300 -a 3 -w 3 -O -D 2"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         10-Character Spite Password Mask Attack              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Based on: Dean said 'weakest possible thing out of spite'"
echo "Requirement: 10 characters minimum (Bitcoin 0.4.0)"
echo "Testing gap: Dean tested up to 9 chars max"
echo ""
echo "This will take DAYS to WEEKS depending on GPU"
echo ""

# ============================================================================
# PHASE 1: Pure Character Classes (10 chars)
# ============================================================================

echo "[PHASE 1] Pure character class attacks (10 chars)"
echo "------------------------------------------------"

# 10 lowercase (26^10 = 141 trillion)
echo "[*] Attack: 10 lowercase letters"
echo "    Keyspace: 141,167,095,653,376 (141 trillion)"
echo "    Examples: aaaaaaaaaa, password**, qwertyuiop"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?l?l'
fi

# 10 digits (10^10 = 10 billion) - FASTEST
echo "[*] Attack: 10 digits"
echo "    Keyspace: 10,000,000,000 (10 billion)"
echo "    Examples: 1234567890, 0000000000, 1111111111"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?d?d?d?d?d?d?d?d?d?d'
fi

# 10 uppercase (26^10 = 141 trillion)
echo "[*] Attack: 10 uppercase letters"
echo "    Keyspace: 141,167,095,653,376 (141 trillion)"
echo "    Examples: AAAAAAAAAA, PASSWORD**, QWERTYUIOP"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?u?u?u?u?u?u?u?u?u?u'
fi

# ============================================================================
# PHASE 2: Mixed Character Classes (10 chars) - HIGHEST PROBABILITY
# ============================================================================

echo ""
echo "[PHASE 2] Mixed character attacks (10 chars) - SPITE PATTERNS"
echo "------------------------------------------------------------"

# 8 lowercase + 2 digits (common pattern)
echo "[*] Attack: 8 lowercase + 2 digits at end"
echo "    Keyspace: ~2 trillion"
echo "    Examples: password01, password12, badpass99"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?d?d'
fi

# 1 uppercase + 8 lowercase + 1 digit (Password1 pattern)
echo "[*] Attack: Capital + 8 lowercase + 1 digit"
echo "    Keyspace: ~1 trillion"
echo "    Examples: Password1, Badpass1, Welcome1"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?u?l?l?l?l?l?l?l?l?d'
fi

# 8 lowercase + 1 digit + 1 symbol (password1! pattern)
echo "[*] Attack: 8 lowercase + 1 digit + 1 symbol"
echo "    Keyspace: ~2 trillion"
echo "    Examples: password1!, badpass1!, welcome1!"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?d?s'
fi

# 1 uppercase + 7 lowercase + 1 digit + 1 symbol (Password1! pattern)
echo "[*] Attack: Capital + 7 lowercase + 1 digit + 1 symbol"
echo "    Keyspace: ~500 billion"
echo "    Examples: Password1!, Welcome1!, Badpass1!"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?u?l?l?l?l?l?l?l?d?s'
fi

# 8 lowercase + 2 symbols
echo "[*] Attack: 8 lowercase + 2 symbols at end"
echo "    Keyspace: ~1 trillion"
echo "    Examples: password!!, password!?, badpass!!"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?s?s'
fi

# 9 lowercase + 1 digit
echo "[*] Attack: 9 lowercase + 1 digit at end"
echo "    Keyspace: ~1 trillion"
echo "    Examples: password1, badpass1, welcome1"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?l?d'
fi

# 9 lowercase + 1 symbol
echo "[*] Attack: 9 lowercase + 1 symbol at end"
echo "    Keyspace: ~1 trillion"
echo "    Examples: password!, badpass!, welcome!"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?l?s'
fi

# ============================================================================
# PHASE 3: Keyboard Pattern Attacks
# ============================================================================

echo ""
echo "[PHASE 3] Keyboard pattern brute force"
echo "--------------------------------------"

# Custom charset for keyboard rows
echo "[*] Attack: Keyboard row patterns (qwerty, asdfgh, etc.)"
echo "    Using custom charset: qwertyuiopasdfghjklzxcvbnm"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Top row
    hashcat $HC_FLAGS $HASH_FILE -1 qwertyuiop '?1?1?1?1?1?1?1?1?1?1'
    # Middle row
    hashcat $HC_FLAGS $HASH_FILE -1 asdfghjkl '?1?1?1?1?1?1?1?1?1?1'
    # Combined
    hashcat $HC_FLAGS $HASH_FILE -1 qwertyuiopasdfghjklzxcvbnm '?1?1?1?1?1?1?1?1?1?1'
fi

# ============================================================================
# PHASE 4: Repeated Character Patterns
# ============================================================================

echo ""
echo "[PHASE 4] Repeated character attacks (Dean mentioned 'pooooop')"
echo "---------------------------------------------------------------"

# All same character (26 lowercase + 26 uppercase + 10 digits = 62 total)
echo "[*] Attack: Same character repeated 10 times"
echo "    Keyspace: 62 (very fast)"
echo "    Examples: aaaaaaaaaa, 1111111111, AAAAAAAAAA"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Generate file with all repeated chars
    cat > repeated_10char.txt << 'CHARS'
aaaaaaaaaa
bbbbbbbbbb
cccccccccc
dddddddddd
eeeeeeeeee
ffffffffff
gggggggggg
hhhhhhhhhh
iiiiiiiiii
jjjjjjjjjj
kkkkkkkkkk
llllllllll
mmmmmmmmmm
nnnnnnnnnn
oooooooooo
pppppppppp
qqqqqqqqqq
rrrrrrrrrr
ssssssssss
tttttttttt
uuuuuuuuuu
vvvvvvvvvv
wwwwwwwwww
xxxxxxxxxx
yyyyyyyyyy
zzzzzzzzzz
AAAAAAAAAA
BBBBBBBBBB
CCCCCCCCCC
DDDDDDDDDD
EEEEEEEEEE
FFFFFFFFFF
GGGGGGGGGG
HHHHHHHHHH
IIIIIIIIII
JJJJJJJJJJ
KKKKKKKKKK
LLLLLLLLLL
MMMMMMMMMM
NNNNNNNNNN
OOOOOOOOOO
PPPPPPPPPP
QQQQQQQQQQ
RRRRRRRRRR
SSSSSSSSSS
TTTTTTTTTT
UUUUUUUUUU
VVVVVVVVVV
WWWWWWWWWW
XXXXXXXXXX
YYYYYYYYYY
ZZZZZZZZZZ
0000000000
1111111111
2222222222
3333333333
4444444444
5555555555
6666666666
7777777777
8888888888
9999999999
!!!!!!!!!!
@@@@@@@@@@
##########
$$$$$$$$$$
%%%%%%%%%%
^^^^^^^^^^
&&&&&&&&&&
**********
CHARS
    hashcat -m 11300 -a 0 -w 3 -O -D 2 $HASH_FILE repeated_10char.txt
fi

# ============================================================================
# PHASE 5: Extended Attacks (11-15 chars if 10 fails)
# ============================================================================

echo ""
echo "[PHASE 5] Extended length attacks (11-15 chars)"
echo "-----------------------------------------------"
echo "[!] Only run these if 10-char attacks fail"
echo ""

# 11 lowercase
echo "[*] Attack: 11 lowercase letters"
echo "    Keyspace: 3.67 quadrillion (VERY LONG)"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?l?l?l'
fi

# 10 lowercase + 1 digit
echo "[*] Attack: 10 lowercase + 1 digit"
echo "    Keyspace: ~1.4 quadrillion"
read -p "    Run this? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    hashcat $HC_FLAGS $HASH_FILE '?l?l?l?l?l?l?l?l?l?l?d'
fi

# ============================================================================
# PHASE 6: Show Cracked Password
# ============================================================================

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                   CHECK FOR CRACKED PASSWORD                 ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
hashcat -m 11300 $HASH_FILE --show

echo ""
echo "Attack complete. If password was found, it's shown above."
echo "If successful, tweet it to @deanpierce for 5 BTC bounty!"
