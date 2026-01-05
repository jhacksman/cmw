#!/bin/bash
# Script to test Bitcoin wallet creation and encryption using Docker

# Create base directories
mkdir -p wallets/unencrypted wallets/encrypted wallets/converted

# Function to create unencrypted wallet with Bitcoin 0.3.x
create_unencrypted_wallet() {
  local version=$1
  local dir="wallets/unencrypted/bitcoin-v${version}"
  
  echo "Creating unencrypted wallet with Bitcoin v${version}..."
  mkdir -p "${dir}"
  
  # Use ruimarinho/bitcoin-core Docker image with the specific version
  docker run --rm -v "${PWD}/${dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${version} bitcoind -daemon
  
  # Wait a bit for wallet.dat to be created
  sleep 5
  
  # Stop Bitcoin
  docker run --rm -v "${PWD}/${dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${version} bitcoin-cli stop
  
  # Create README
  echo "# Bitcoin Wallet" > "${dir}/README.md"
  echo "" >> "${dir}/README.md"
  echo "Created unencrypted by Bitcoin Core v${version}." >> "${dir}/README.md"
  
  echo "Unencrypted wallet created with Bitcoin v${version}."
}

# Function to create encrypted wallet with Bitcoin 0.4.0+ 
create_encrypted_wallet() {
  local version=$1
  local dir="wallets/encrypted/bitcoin-v${version}"
  
  echo "Creating encrypted wallet with Bitcoin v${version}..."
  mkdir -p "${dir}"
  
  # Use ruimarinho/bitcoin-core Docker image with the specific version
  docker run --rm -v "${PWD}/${dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${version} bitcoind -daemon
  
  # Wait a bit for wallet.dat to be created
  sleep 5
  
  # Encrypt the wallet
  docker run --rm -v "${PWD}/${dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${version} bitcoin-cli encryptwallet "badpassword123"
  
  # Wait for encryption
  sleep 5
  
  # Stop Bitcoin
  docker run --rm -v "${PWD}/${dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${version} bitcoin-cli stop
  
  # Create README
  echo "# Bitcoin Wallet" > "${dir}/README.md"
  echo "" >> "${dir}/README.md"
  echo "Encrypted by Bitcoin Core v${version} with built-in wallet encryption." >> "${dir}/README.md"
  
  echo "Encrypted wallet created with Bitcoin v${version}."
}

# Function to convert unencrypted wallet to encrypted
convert_and_encrypt_wallet() {
  local source_version=$1
  local target_version=$2
  local source_dir="wallets/unencrypted/bitcoin-v${source_version}"
  local target_dir="wallets/converted/enc_${source_version}_to_${target_version}"
  
  echo "Converting wallet from v${source_version} to v${target_version} and encrypting..."
  
  # Check if source wallet exists
  if [ ! -f "${source_dir}/wallet.dat" ]; then
    echo "ERROR: Source wallet.dat not found for v${source_version}"
    return 1
  fi
  
  # Create target directory
  mkdir -p "${target_dir}"
  
  # Copy source wallet.dat to the target directory
  cp "${source_dir}/wallet.dat" "${target_dir}/wallet.dat"
  
  # Use the target version to encrypt the wallet
  docker run --rm -v "${PWD}/${target_dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${target_version} bitcoind -daemon
  
  # Wait for it to start
  sleep 5
  
  # Encrypt the wallet
  docker run --rm -v "${PWD}/${target_dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${target_version} bitcoin-cli encryptwallet "badpassword123"
  
  # Wait for encryption
  sleep 5
  
  # Stop Bitcoin
  docker run --rm -v "${PWD}/${target_dir}:/bitcoin/.bitcoin" \
    ruimarinho/bitcoin-core:${target_version} bitcoin-cli stop
  
  # Create README
  echo "# Bitcoin Wallet Conversion" > "${target_dir}/README.md"
  echo "" >> "${target_dir}/README.md"
  echo "Converted from Bitcoin Core v${source_version} to v${target_version} and encrypted with 'badpassword123'." >> "${target_dir}/README.md"
  
  echo "Wallet converted from v${source_version} to v${target_version} and encrypted successfully."
}

# Create unencrypted wallets for v0.3.x
for version in 0.3.21 0.3.22 0.3.23 0.3.24; do
  create_unencrypted_wallet "${version}"
done

# Create encrypted wallets for v0.4.0+
for version in 0.4.0 0.5.0 0.5.1; do
  create_encrypted_wallet "${version}"
done

# Convert and encrypt wallets
for source in 0.3.21 0.3.22 0.3.23 0.3.24; do
  for target in 0.4.0 0.5.0 0.5.1; do
    convert_and_encrypt_wallet "${source}" "${target}"
  done
done

echo "All wallets created and converted successfully."