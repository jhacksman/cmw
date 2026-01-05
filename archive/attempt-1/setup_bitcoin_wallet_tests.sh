#!/bin/bash
# Script to set up Bitcoin wallet testing environments

BASE_DIR=$(pwd)
ENCRYPTION_PASSWORD="badpassword123"

# Create directories for unencrypted v0.3.x wallets
echo "Setting up directories for unencrypted v0.3.x wallets..."
mkdir -p bitcoin-v0.3.21 bitcoin-v0.3.22 bitcoin-v0.3.23 bitcoin-v0.3.24

# Create directories for encrypted v0.4.0+ wallets
echo "Setting up directories for encrypted v0.4.0+ wallets..."
mkdir -p bitcoin-v0.4.0 bitcoin-v0.5.0 bitcoin-v0.5.1

# Create directories for converting v0.3.x wallets to encrypted with v0.4.0+
echo "Setting up directories for converting v0.3.x wallets to encrypted with v0.4.0+..."
for source in 0.3.21 0.3.22 0.3.23 0.3.24; do
  for target in 0.4.0 0.5.0 0.5.1; do
    mkdir -p "enc_${source}_to_${target}"
    # Create README for each conversion directory
    cat > "enc_${source}_to_${target}/README.md" << EOF
# Bitcoin Wallet Conversion

Converted from Bitcoin Core v${source} to v${target} and encrypted with 'badpassword123'.
EOF
  done
done

# Create README files for unencrypted v0.3.x wallets
for version in 0.3.21 0.3.22 0.3.23 0.3.24; do
  cat > "bitcoin-v${version}/README.md" << EOF
# Bitcoin Wallet

Created unencrypted by Bitcoin Core v${version}.
EOF
done

# Create README files for encrypted v0.4.0+ wallets
for version in 0.4.0 0.5.0 0.5.1; do
  cat > "bitcoin-v${version}/README.md" << EOF
# Bitcoin Wallet

Encrypted by Bitcoin Core v${version} with built-in wallet encryption.
EOF
done

# Create a master README with instructions
cat > README_WALLET_TESTS.md << 'EOF'
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
EOF

echo "Directory structure and README files created successfully."
echo "Next steps:"
echo "1. Create Conda environments for each Bitcoin version"
echo "2. Install/unpack Bitcoin binaries in their respective directories"
echo "3. Follow the instructions in README_WALLET_TESTS.md to generate wallets"