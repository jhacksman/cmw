#!/bin/bash
# gen_untested_gaps.sh
# Generates wordlists for UNTESTED search spaces (<= 1B candidates each)
# Based on what Dean actually tested vs. what's missing

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║       Untested Gap Generator (<= 1 Billion Per List)         ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Dean tested:"
echo "  - Digits: 1-9 chars"
echo "  - Lowercase: 1-7 chars"
echo "  - All ASCII: 1-6 chars"
echo "  - rockyou.txt + rules"
echo ""
echo "This generates UNTESTED patterns based on spite password theory"
echo ""

# ============================================================================
# GAP 1: password + 2 chars (9,025 combos)
# ============================================================================

echo "[GAP 1] Generating: 'password' + 2 ASCII chars (9,025 combos)"
OUTPUT="gap1_password_plus2.txt"
> "$OUTPUT"

base="password"
for c1 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+' '[' ']' '{' '}' '|' '\' ';' ':' "'" '"' '<' '>' ',' '.' '?' '/' '`' '~'; do
    for c2 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+' '[' ']' '{' '}' '|' '\' ';' ':' "'" '"' '<' '>' ',' '.' '?' '/' '`' '~'; do
        echo "${base}${c1}${c2}" >> "$OUTPUT"
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 2: Password + 2 chars (9,025 combos) - Capital P
# ============================================================================

echo "[GAP 2] Generating: 'Password' + 2 ASCII chars (9,025 combos)"
OUTPUT="gap2_Password_plus2.txt"
> "$OUTPUT"

base="Password"
for c1 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+' '[' ']' '{' '}' '|' '\' ';' ':' "'" '"' '<' '>' ',' '.' '?' '/' '`' '~'; do
    for c2 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+' '[' ']' '{' '}' '|' '\' ';' ':' "'" '"' '<' '>' ',' '.' '?' '/' '`' '~'; do
        echo "${base}${c1}${c2}" >> "$OUTPUT"
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 3: badpass + 2 chars (9,025 combos)
# ============================================================================

echo "[GAP 3] Generating: 'badpass' + 2 ASCII chars (9,025 combos)"
OUTPUT="gap3_badpass_plus2.txt"
> "$OUTPUT"

base="badpass"
for c1 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+'; do
    for c2 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+'; do
        echo "${base}${c1}${c2}" >> "$OUTPUT"
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 4: qwertyui + 2 chars (8 char keyboard pattern + 2)
# ============================================================================

echo "[GAP 4] Generating: 'qwertyui' + 2 ASCII chars (9,025 combos)"
OUTPUT="gap4_qwertyui_plus2.txt"
> "$OUTPUT"

base="qwertyui"
for c1 in {0..9} {a..z} '!' '@' '#' '$'; do
    for c2 in {0..9} {a..z} '!' '@' '#' '$'; do
        echo "${base}${c1}${c2}" >> "$OUTPUT"
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 5: Repeated chars + 2 (aaaaaaa + 2 chars)
# ============================================================================

echo "[GAP 5] Generating: Repeated 7 chars + 2 ASCII (Dean mentioned 'pooooop')"
OUTPUT="gap5_repeated7_plus2.txt"
> "$OUTPUT"

for char in {a..z} {0..9}; do
    base=$(printf '%s' "$char" | head -c1)
    base="${base}${base}${base}${base}${base}${base}${base}"  # 7 of same char
    for c1 in {0..9} {a..z} '!' '@' '#'; do
        for c2 in {0..9} {a..z} '!' '@' '#'; do
            echo "${base}${c1}${c2}" >> "$OUTPUT"
        done
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 6: p@ssword + 1 char (leetspeak 8-char + 1)
# ============================================================================

echo "[GAP 6] Generating: 'p@ssword' + 1 ASCII char (Dean's leet pattern)"
OUTPUT="gap6_p@ssword_plus1.txt"
> "$OUTPUT"

base="p@ssword"
for c1 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '-' '_' '=' '+'; do
    echo "${base}${c1}" >> "$OUTPUT"
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 7: p@ssw0rd + 1 char (double leet)
# ============================================================================

echo "[GAP 7] Generating: 'p@ssw0rd' + 1 ASCII char"
OUTPUT="gap7_p@ssw0rd_plus1.txt"
> "$OUTPUT"

base="p@ssw0rd"
for c1 in {0..9} {a..z} {A..Z} '!' '@' '#' '$' '%' '^' '&' '*'; do
    echo "${base}${c1}" >> "$OUTPUT"
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 8: welcome + 2 chars (common corporate password)
# ============================================================================

echo "[GAP 8] Generating: 'welcome' + 2 ASCII chars"
OUTPUT="gap8_welcome_plus2.txt"
> "$OUTPUT"

base="welcome"
for c1 in {0..9} {A..Z} '!' '@' '#' '$'; do
    for c2 in {0..9} '!' '@' '#' '$'; do
        echo "${base}${c1}${c2}" >> "$OUTPUT"
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 9: Welcome + 2 chars (capitalized)
# ============================================================================

echo "[GAP 9] Generating: 'Welcome' + 2 ASCII chars"
OUTPUT="gap9_Welcome_plus2.txt"
> "$OUTPUT"

base="Welcome"
for c1 in {0..9} '!' '@' '#' '$'; do
    for c2 in {0..9} '!' '@' '#' '$'; do
        echo "${base}${c1}${c2}" >> "$OUTPUT"
    done
done
COUNT=$(wc -l < "$OUTPUT")
echo "[+] Generated $COUNT → $OUTPUT"

# ============================================================================
# GAP 10: 8 lowercase starting with common letters (partitioned)
# ============================================================================

echo "[GAP 10] Generating: 8 lowercase starting with 'p' (password* space)"
echo "         WARNING: 26^7 = 8 billion - TOO BIG for one file!"
echo "         Use hashcat mask instead: hashcat -m 11300 -a 3 hash.txt 'p?l?l?l?l?l?l?l'"
echo "         Skipping file generation..."

# ============================================================================
# Summary
# ============================================================================

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                      Generation Complete                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "Files created:"
ls -lh gap*.txt 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
echo ""
TOTAL=$(cat gap*.txt 2>/dev/null | wc -l)
echo "Total candidates across all gaps: $(printf "%'d" $TOTAL)"
echo ""
echo "Test with hashcat:"
echo "  for file in gap*.txt; do"
echo "    hashcat -m 11300 -a 0 -w 3 -O -D 2 hash.txt \$file"
echo "  done"
echo ""
echo "Or combine all:"
echo "  cat gap*.txt > all_untested_gaps.txt"
echo "  hashcat -m 11300 -a 0 -w 3 -O -D 2 hash.txt all_untested_gaps.txt"
