# Bitcoin Wallet Encryption Tests

This directory contains test environments for Bitcoin wallet encryption across different versions.

## Directory Structure

### Unencrypted Wallets (v0.3.x)
- bitcoin-v0.3.21
- bitcoin-v0.3.22
- bitcoin-v0.3.23
- bitcoin-v0.3.24

### Encrypted Wallets (v0.4.0+)
- bitcoin-v0.4.0
- bitcoin-v0.5.0
- bitcoin-v0.5.1

### Converted and Encrypted Wallets
For each combination of unencrypted source (0.3.21-0.3.24) and encryption target (0.4.0, 0.5.0, 0.5.1):
- enc_0.3.xx_to_0.y.z

## Test Process

1. For each version, create and activate the corresponding Conda environment:
   ```
   conda create -n bitcoin-vX.X.X python
   conda activate bitcoin-vX.X.X
   ```

2. For unencrypted wallets (v0.3.x):
   - Install/unpack the Bitcoin Core binary
   - Launch it once to generate an unencrypted wallet.dat
   - Keep only the wallet.dat file

3. For encrypted wallets (v0.4.0+):
   - Install/unpack the Bitcoin Core or Bitcoin-Qt binary
   - Launch it and use the Encrypt Wallet feature
   - Keep only the wallet.dat file

4. For converting v0.3.x wallets to encrypted:
   - Use the appropriate Bitcoin Core/Qt version (0.4.0, 0.5.0, or 0.5.1)
   - Load the unencrypted wallet from v0.3.x
   - Encrypt it with passphrase "badpassword123"
   - Keep only the encrypted wallet.dat file

## Conda Environment Setup

For each Bitcoin version, create a separate Conda environment:

```bash
# Example for v0.3.21
conda create -n bitcoin-v0.3.21 python
conda activate bitcoin-v0.3.21
# Then install/unpack and run Bitcoin Core v0.3.21
```
