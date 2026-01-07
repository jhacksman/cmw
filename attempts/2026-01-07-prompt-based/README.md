# Prompt-Based Password Attempt

**Date:** January 7, 2026  
**Candidates:** ~72M  
**Runtime:** ~4.4 minutes at 270k H/s

## Hypothesis

Dean saw this exact prompt when encrypting his wallet:

```
Enter a passphrase to encrypt your wallet.
Use 10 or more random characters, or eight or more words.
New passphrase:
Repeat passphrase:
```

He may have typed something based on or mocking this prompt text itself.

## Base Phrases (15 variations)

1. `Enter a passphrase to encrypt your wallet` (original, 7 words)
2. `Enter a bad passphrase to encrypt your wallet` (8 words)
3. `Enter a dumb passphrase to encrypt your wallet`
4. `Enter a stupid passphrase to encrypt your wallet`
5. `Enter a shitty passphrase to encrypt your wallet`
6. `Enter a shit passphrase to encrypt your wallet`
7. `Enter a poop passphrase to encrypt your wallet`
8. `Enter a poopy passphrase to encrypt your wallet`
9. `Enter a potato passphrase to encrypt your wallet`
10. `Enter a p0t4t0 passphrase to encrypt your wallet` (leetspeak)
11. `Enter a crappy passphrase to encrypt your wallet`
12. `Enter a awful passphrase to encrypt your wallet`
13. `Enter a weak passphrase to encrypt your wallet`
14. `Enter a derp passphrase to encrypt your wallet`
15. `Enter a derpy passphrase to encrypt your wallet`

## Configuration

- **Separators:** Spaces, periods, or no separator
  - `Enter a passphrase to encrypt your wallet`
  - `Enter.a.passphrase.to.encrypt.your.wallet`
  - `Enterapassphrasetoencryptyourwallet`

- **Trailing period:** With and without
  - `Enter a passphrase to encrypt your wallet`
  - `Enter a passphrase to encrypt your wallet.`

- **Case:** lowercase and First-letter-capitalized
  - `enter a passphrase to encrypt your wallet`
  - `Enter a passphrase to encrypt your wallet`

- **Trailing:** 0-6 chars from `1234!@#$`
  - With and without space/separator before trailing

## Run Command

```bash
python3 generate_prompt_based.py | hashcat -m 11300 -a 0 -w 3 -O hash.txt
```
