#!/bin/bash
# Script to test Bitcoin wallet creation and encryption using Conda environments

# Base directory for all tests
BASE_DIR=$(pwd)
ENCRYPTION_PASSWORD="badpassword123"
VERSION_DIR="${BASE_DIR}/bitcoin.versions"

# Create base directories for different wallet types
mkdir -p wallet_tests/unencrypted
mkdir -p wallet_tests/encrypted
mkdir -p wallet_tests/converted

# Function to create a Conda environment for a specific Bitcoin version
create_conda_env() {
  local version=$1
  local env_name="bitcoin-v${version}"
  
  echo "Creating Conda environment for Bitcoin v${version}..."
  conda create -y -n ${env_name} python=3.8
  
  echo "Conda environment ${env_name} created."
}

# Function to extract Bitcoin source code for a specific version
extract_bitcoin_source() {
  local version=$1
  local target_dir="${BASE_DIR}/bitcoin-v${version}"
  
  echo "Extracting Bitcoin v${version} source code..."
  
  # Find the corresponding source code archive
  local archive=$(find "${VERSION_DIR}" -name "*v${version}*.tar.gz")
  
  if [ -z "${archive}" ]; then
    echo "ERROR: Source code archive for Bitcoin v${version} not found in ${VERSION_DIR}"
    return 1
  fi
  
  # Create directory if it doesn't exist
  mkdir -p "${target_dir}"
  
  # Extract the source code
  tar -xzf "${archive}" -C "${target_dir}" --strip-components=1
  
  echo "Bitcoin v${version} source code extracted to ${target_dir}."
}

# Function to compile Bitcoin for a specific version
compile_bitcoin() {
  local version=$1
  local source_dir="${BASE_DIR}/bitcoin-v${version}"
  
  echo "Compiling Bitcoin v${version}..."
  
  # Activate the Conda environment
  conda activate bitcoin-v${version}
  
  # Change to source directory
  cd "${source_dir}"
  
  # Compile Bitcoin based on version
  if [[ "${version}" == 0.3.* ]]; then
    # Compile 0.3.x versions
    make -f makefile.unix bitcoind
  elif [[ "${version}" == 0.4.0 ]]; then
    # Compile 0.4.0
    make -f makefile.unix bitcoind
  elif [[ "${version}" == 0.5.* ]]; then
    # Compile 0.5.x versions (Qt versions)
    qmake
    make
  fi
  
  # Return to base directory
  cd "${BASE_DIR}"
  
  # Deactivate Conda environment
  conda deactivate
  
  echo "Bitcoin v${version} compiled successfully."
}

# Function to create an unencrypted wallet with Bitcoin 0.3.x
create_unencrypted_wallet() {
  local version=$1
  local env_name="bitcoin-v${version}"
  local source_dir="${BASE_DIR}/bitcoin-v${version}"
  local wallet_dir="${BASE_DIR}/wallet_tests/unencrypted/bitcoin-v${version}"
  
  echo "Creating unencrypted wallet with Bitcoin v${version}..."
  mkdir -p "${wallet_dir}"
  
  # Activate the Conda environment
  conda activate ${env_name}
  
  # Run Bitcoin to generate wallet.dat
  cd "${source_dir}"
  ./bitcoind -datadir="${wallet_dir}" -daemon
  
  # Wait for wallet.dat to be created
  sleep 10
  
  # Stop Bitcoin
  ./bitcoind -datadir="${wallet_dir}" stop
  
  # Create README
  echo "# Bitcoin Wallet" > "${wallet_dir}/README.md"
  echo "" >> "${wallet_dir}/README.md"
  echo "Created unencrypted by Bitcoin Core v${version}." >> "${wallet_dir}/README.md"
  
  # Return to base directory
  cd "${BASE_DIR}"
  
  # Deactivate Conda environment
  conda deactivate
  
  echo "Unencrypted wallet created with Bitcoin v${version}."
}

# Function to create an encrypted wallet with Bitcoin 0.4.0+
create_encrypted_wallet() {
  local version=$1
  local env_name="bitcoin-v${version}"
  local source_dir="${BASE_DIR}/bitcoin-v${version}"
  local wallet_dir="${BASE_DIR}/wallet_tests/encrypted/bitcoin-v${version}"
  
  echo "Creating encrypted wallet with Bitcoin v${version}..."
  mkdir -p "${wallet_dir}"
  
  # Activate the Conda environment
  conda activate ${env_name}
  
  # Run Bitcoin to generate wallet.dat
  cd "${source_dir}"
  if [[ "${version}" == 0.4.0 ]]; then
    ./bitcoind -datadir="${wallet_dir}" -daemon
  elif [[ "${version}" == 0.5.* ]]; then
    # For 0.5.x, use bitcoin-qt with a configuration file
    echo "rpcuser=user" > "${wallet_dir}/bitcoin.conf"
    echo "rpcpassword=pass" >> "${wallet_dir}/bitcoin.conf"
    echo "server=1" >> "${wallet_dir}/bitcoin.conf"
    ./bitcoin-qt -datadir="${wallet_dir}" -daemon
  fi
  
  # Wait for wallet.dat to be created
  sleep 10
  
  # Encrypt the wallet
  if [[ "${version}" == 0.4.0 ]]; then
    ./bitcoind -datadir="${wallet_dir}" encryptwallet "${ENCRYPTION_PASSWORD}"
  elif [[ "${version}" == 0.5.* ]]; then
    ./bitcoin-cli -datadir="${wallet_dir}" encryptwallet "${ENCRYPTION_PASSWORD}"
  fi
  
  # Wait for encryption
  sleep 5
  
  # Stop Bitcoin
  if [[ "${version}" == 0.4.0 ]]; then
    ./bitcoind -datadir="${wallet_dir}" stop
  elif [[ "${version}" == 0.5.* ]]; then
    ./bitcoin-cli -datadir="${wallet_dir}" stop
  fi
  
  # Create README
  echo "# Bitcoin Wallet" > "${wallet_dir}/README.md"
  echo "" >> "${wallet_dir}/README.md"
  echo "Encrypted by Bitcoin Core v${version} with built-in wallet encryption." >> "${wallet_dir}/README.md"
  
  # Return to base directory
  cd "${BASE_DIR}"
  
  # Deactivate Conda environment
  conda deactivate
  
  echo "Encrypted wallet created with Bitcoin v${version}."
}

# Function to convert unencrypted wallet to encrypted
convert_and_encrypt_wallet() {
  local source_version=$1
  local target_version=$2
  local source_wallet="${BASE_DIR}/wallet_tests/unencrypted/bitcoin-v${source_version}/wallet.dat"
  local target_dir="${BASE_DIR}/wallet_tests/converted/enc_${source_version}_to_${target_version}"
  local target_source_dir="${BASE_DIR}/bitcoin-v${target_version}"
  
  echo "Converting wallet from v${source_version} to v${target_version} and encrypting..."
  
  # Check if source wallet exists
  if [ ! -f "${source_wallet}" ]; then
    echo "ERROR: Source wallet.dat not found for v${source_version}"
    return 1
  fi
  
  # Create target directory
  mkdir -p "${target_dir}"
  
  # Copy source wallet.dat to the target directory
  cp "${source_wallet}" "${target_dir}/wallet.dat"
  
  # Activate the target Conda environment
  conda activate bitcoin-v${target_version}
  
  # Run Bitcoin with the target version
  cd "${target_source_dir}"
  if [[ "${target_version}" == 0.4.0 ]]; then
    ./bitcoind -datadir="${target_dir}" -daemon
  elif [[ "${target_version}" == 0.5.* ]]; then
    # For 0.5.x, use bitcoin-qt with a configuration file
    echo "rpcuser=user" > "${target_dir}/bitcoin.conf"
    echo "rpcpassword=pass" >> "${target_dir}/bitcoin.conf"
    echo "server=1" >> "${target_dir}/bitcoin.conf"
    ./bitcoin-qt -datadir="${target_dir}" -daemon
  fi
  
  # Wait for it to start
  sleep 10
  
  # Encrypt the wallet
  if [[ "${target_version}" == 0.4.0 ]]; then
    ./bitcoind -datadir="${target_dir}" encryptwallet "${ENCRYPTION_PASSWORD}"
  elif [[ "${target_version}" == 0.5.* ]]; then
    ./bitcoin-cli -datadir="${target_dir}" encryptwallet "${ENCRYPTION_PASSWORD}"
  fi
  
  # Wait for encryption
  sleep 5
  
  # Stop Bitcoin
  if [[ "${target_version}" == 0.4.0 ]]; then
    ./bitcoind -datadir="${target_dir}" stop
  elif [[ "${target_version}" == 0.5.* ]]; then
    ./bitcoin-cli -datadir="${target_dir}" stop
  fi
  
  # Create README
  echo "# Bitcoin Wallet Conversion" > "${target_dir}/README.md"
  echo "" >> "${target_dir}/README.md"
  echo "Converted from Bitcoin Core v${source_version} to v${target_version} and encrypted with 'badpassword123'." >> "${target_dir}/README.md"
  
  # Return to base directory
  cd "${BASE_DIR}"
  
  # Deactivate Conda environment
  conda deactivate
  
  echo "Wallet converted from v${source_version} to v${target_version} and encrypted successfully."
}

# Create Conda environments for all Bitcoin versions
for version in 0.3.21 0.3.22 0.3.23 0.3.24 0.4.0 0.5.0 0.5.1; do
  create_conda_env "${version}"
done

# Extract and compile Bitcoin for all versions
for version in 0.3.21 0.3.22 0.3.23 0.3.24 0.4.0 0.5.0 0.5.1; do
  extract_bitcoin_source "${version}"
  compile_bitcoin "${version}"
done

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

echo "All wallets created and converted successfully with Conda environments."