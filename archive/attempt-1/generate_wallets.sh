#!/bin/bash
# Script to generate Bitcoin wallets (unencrypted for v0.3.x and encrypted for v0.4.0+)

BASE_DIR=$(pwd)
BITCOIN_DATA_DIR="${BASE_DIR}/bitcoin_data"
ENCRYPTION_PASSWORD="badpassword123"

# Function to run Bitcoin Core and generate an unencrypted wallet (v0.3.x)
generate_unencrypted_wallet() {
  local version=$1
  local version_dir="bitcoin-v${version}"
  
  echo "Generating unencrypted wallet for Bitcoin v${version}..."
  
  # Find the actual binary directory (may vary based on extraction structure)
  local bin_dir=$(find "${version_dir}" -type d -name "bitcoin-*" | head -n 1)
  
  if [ -z "${bin_dir}" ]; then
    echo "ERROR: Could not find Bitcoin binary directory for v${version}"
    return 1
  fi
  
  # Create data directory for this version
  mkdir -p "${BITCOIN_DATA_DIR}/${version}"
  
  # Run Bitcoin to generate wallet.dat
  # Note: The exact command might need adjustment based on the specific version
  cd "${bin_dir}"
  ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${version}" -daemon
  
  # Wait a bit for wallet.dat to be created
  sleep 20
  
  # Stop Bitcoin
  ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${version}" stop
  
  # Wait for it to shut down
  sleep 10
  
  # Copy wallet.dat to the version directory
  cp "${BITCOIN_DATA_DIR}/${version}/wallet.dat" "${BASE_DIR}/${version_dir}/"
  
  # Clean up
  cd "${BASE_DIR}"
  echo "Unencrypted wallet.dat generated for v${version}"
}

# Function to generate an encrypted wallet for v0.4.0+
generate_encrypted_wallet() {
  local version=$1
  local version_dir="bitcoin-v${version}"
  
  echo "Generating encrypted wallet for Bitcoin v${version}..."
  
  # Find the actual binary directory (may vary based on extraction structure)
  local bin_dir=$(find "${version_dir}" -type d -name "bitcoin-*" | head -n 1)
  
  if [ -z "${bin_dir}" ]; then
    echo "ERROR: Could not find Bitcoin binary directory for v${version}"
    return 1
  fi
  
  # Create data directory for this version
  mkdir -p "${BITCOIN_DATA_DIR}/${version}"
  
  # For v0.4.0+, we need to run the binary, then use RPC to encrypt the wallet
  cd "${bin_dir}"
  
  # Start Bitcoin
  if [[ "${version}" == "0.5.0" || "${version}" == "0.5.1" ]]; then
    # For v0.5.0+, we might be using Bitcoin-Qt
    ./bitcoin-qt -datadir="${BITCOIN_DATA_DIR}/${version}" &
  else
    ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${version}" -daemon
  fi
  
  # Wait for it to start
  sleep 20
  
  # Encrypt wallet using RPC
  # Note: For GUI versions, this step would be manual
  if [[ "${version}" == "0.4.0" ]]; then
    # For v0.4.0, use RPC
    ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${version}" encryptwallet "${ENCRYPTION_PASSWORD}"
  else
    echo "For v${version}, wallet encryption needs to be done through the GUI."
    echo "Please manually encrypt the wallet with password: ${ENCRYPTION_PASSWORD}"
    echo "Then press Enter to continue..."
    read
  fi
  
  # Wait for encryption
  sleep 10
  
  # Stop Bitcoin
  if [[ "${version}" == "0.4.0" ]]; then
    ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${version}" stop
  else
    echo "Please manually close Bitcoin-Qt, then press Enter to continue..."
    read
  fi
  
  # Wait for it to shut down
  sleep 10
  
  # Copy wallet.dat to the version directory
  cp "${BITCOIN_DATA_DIR}/${version}/wallet.dat" "${BASE_DIR}/${version_dir}/"
  
  # Clean up
  cd "${BASE_DIR}"
  echo "Encrypted wallet.dat generated for v${version}"
}

# Function to convert unencrypted wallet to encrypted
convert_and_encrypt_wallet() {
  local source_version=$1
  local target_version=$2
  local conversion_dir="enc_${source_version}_to_${target_version}"
  
  echo "Converting wallet from v${source_version} to v${target_version} and encrypting..."
  
  # Find the source wallet.dat
  local source_wallet="${BASE_DIR}/bitcoin-v${source_version}/wallet.dat"
  
  if [ ! -f "${source_wallet}" ]; then
    echo "ERROR: Source wallet.dat not found for v${source_version}"
    return 1
  fi
  
  # Find the target binary directory
  local bin_dir=$(find "bitcoin-v${target_version}" -type d -name "bitcoin-*" | head -n 1)
  
  if [ -z "${bin_dir}" ]; then
    echo "ERROR: Could not find Bitcoin binary directory for v${target_version}"
    return 1
  fi
  
  # Create data directory for this conversion
  mkdir -p "${BITCOIN_DATA_DIR}/${conversion_dir}"
  
  # Copy source wallet.dat to the data directory
  cp "${source_wallet}" "${BITCOIN_DATA_DIR}/${conversion_dir}/wallet.dat"
  
  # Start the target Bitcoin version
  cd "${bin_dir}"
  
  if [[ "${target_version}" == "0.5.0" || "${target_version}" == "0.5.1" ]]; then
    # For v0.5.0+, we might be using Bitcoin-Qt
    ./bitcoin-qt -datadir="${BITCOIN_DATA_DIR}/${conversion_dir}" &
  else
    ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${conversion_dir}" -daemon
  fi
  
  # Wait for it to start
  sleep 20
  
  # Encrypt wallet
  if [[ "${target_version}" == "0.4.0" ]]; then
    # For v0.4.0, use RPC
    ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${conversion_dir}" encryptwallet "${ENCRYPTION_PASSWORD}"
  else
    echo "For v${target_version}, wallet encryption needs to be done through the GUI."
    echo "Please manually encrypt the wallet with password: ${ENCRYPTION_PASSWORD}"
    echo "Then press Enter to continue..."
    read
  fi
  
  # Wait for encryption
  sleep 10
  
  # Stop Bitcoin
  if [[ "${target_version}" == "0.4.0" ]]; then
    ./bitcoin -datadir="${BITCOIN_DATA_DIR}/${conversion_dir}" stop
  else
    echo "Please manually close Bitcoin-Qt, then press Enter to continue..."
    read
  fi
  
  # Wait for it to shut down
  sleep 10
  
  # Copy wallet.dat to the conversion directory
  cp "${BITCOIN_DATA_DIR}/${conversion_dir}/wallet.dat" "${BASE_DIR}/${conversion_dir}/"
  
  # Clean up
  cd "${BASE_DIR}"
  echo "Wallet converted from v${source_version} to v${target_version} and encrypted successfully"
}

# Create the main data directory
mkdir -p "${BITCOIN_DATA_DIR}"

# Generate unencrypted wallets for v0.3.x
for version in 0.3.21 0.3.22 0.3.23 0.3.24; do
  generate_unencrypted_wallet "${version}"
done

# Generate encrypted wallets for v0.4.0+
for version in 0.4.0 0.5.0 0.5.1; do
  generate_encrypted_wallet "${version}"
done

# Convert and encrypt wallets
for source in 0.3.21 0.3.22 0.3.23 0.3.24; do
  for target in 0.4.0 0.5.0 0.5.1; do
    convert_and_encrypt_wallet "${source}" "${target}"
  done
done

echo "All wallets generated successfully."