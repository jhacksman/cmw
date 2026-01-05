#!/bin/bash
# Script to set up Bitcoin wallet testing across multiple versions

# Password to encrypt wallets with
PASSWORD="badpassword123"

# Create the main directory structure
mkdir -p bitcoin_wallet_tests
cd bitcoin_wallet_tests

# Function to extract Bitcoin version
extract_version() {
  local archive=$1
  local version=$(echo "$archive" | sed -E 's/.*v([0-9]+\.[0-9]+\.[0-9]+).*/\1/')
  echo "$version"
}

# Set up test for each version
setup_version_test() {
  local archive=$1
  local version=$(extract_version "$archive")
  
  echo "Setting up test for Bitcoin $version..."
  
  # Create directory for this version
  mkdir -p "bitcoin_$version"
  
  # Extract Bitcoin to the version directory
  tar -xzf "../bitcoin.versions/$archive" -C "bitcoin_$version"
  
  # Create a directory to store the resulting wallet and hash
  mkdir -p "wallet_$version"
  
  echo "Test environment for Bitcoin $version is ready."
}

# Set up for all versions
for archive in $(ls ../bitcoin.versions/*.tar.gz); do
  setup_version_test $(basename "$archive")
done

# Create a README with instructions
cat > README.md << 'EOF'
# Bitcoin Wallet Testing

This directory contains environments for testing wallet creation and encryption across different Bitcoin versions.

## Test Procedure

For each version:

1. Start with 0.3.21 to create an unencrypted wallet.
2. For versions 0.4.0 and later, use that version to encrypt the wallet with "badpassword123".
3. Extract the wallet.dat file and run bitcoin2john on it to generate a hash.
4. Store both the wallet.dat and the hash in the corresponding "wallet_X.X.X" directory.

## Expected Results

Check how different versions affect the wallet encryption and hashing, with special attention to changes in the encryption process between versions.

EOF

echo "Setup complete. See the README.md file for test instructions."