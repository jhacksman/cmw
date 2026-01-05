#!/bin/bash
# Master script to run all steps in sequence

echo "Starting Bitcoin wallet encryption test process..."

# Make all scripts executable
chmod +x setup_bitcoin_wallet_tests.sh
chmod +x setup_conda_envs.sh
chmod +x extract_bitcoin_binaries.sh
chmod +x generate_wallets.sh
chmod +x cleanup_directories.sh

# Step 1: Set up directory structure
echo "Setting up directory structure..."
./setup_bitcoin_wallet_tests.sh

# Step 2: Set up Conda environments
echo "Setting up Conda environments..."
./setup_conda_envs.sh

# Step 3: Extract Bitcoin binaries
echo "Extracting Bitcoin binaries..."
./extract_bitcoin_binaries.sh

# Step 4: Generate wallets
echo "Generating wallets..."
./generate_wallets.sh

# Step 5: Clean up directories
echo "Cleaning up directories..."
./cleanup_directories.sh

echo "Bitcoin wallet encryption test process completed successfully!"
echo ""
echo "Directory structure:"
echo "- Unencrypted wallets (v0.3.x): bitcoin-v0.3.xx"
echo "- Encrypted wallets (v0.4.0+): bitcoin-v0.4.xx/bitcoin-v0.5.xx"
echo "- Converted and encrypted wallets: enc_0.3.xx_to_0.y.z"
echo ""
echo "Each directory contains:"
echo "- wallet.dat: The Bitcoin wallet file"
echo "- README.md: Documentation on how the wallet was created/encrypted"