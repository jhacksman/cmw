#!/bin/bash
# Script to clean up directories, leaving only wallet.dat and README.md

BASE_DIR=$(pwd)

# Clean up unencrypted wallet directories
echo "Cleaning up unencrypted wallet directories..."
for version in 0.3.21 0.3.22 0.3.23 0.3.24; do
  dir="bitcoin-v${version}"
  echo "Cleaning up ${dir}..."
  
  # Check if wallet.dat exists
  if [ ! -f "${dir}/wallet.dat" ]; then
    echo "WARNING: wallet.dat not found in ${dir}"
    continue
  fi
  
  # Create a temporary directory to store wallet.dat and README.md
  mkdir -p "${dir}_temp"
  cp "${dir}/wallet.dat" "${dir}_temp/"
  cp "${dir}/README.md" "${dir}_temp/" 2>/dev/null || echo "Creating new README.md in ${dir}"
  
  # If README.md doesn't exist, create it
  if [ ! -f "${dir}_temp/README.md" ]; then
    cat > "${dir}_temp/README.md" << EOF
# Bitcoin Wallet

Created unencrypted by Bitcoin Core v${version}.
EOF
  fi
  
  # Remove original directory and rename temp directory
  rm -rf "${dir}"
  mv "${dir}_temp" "${dir}"
  
  echo "${dir} cleaned successfully."
done

# Clean up encrypted wallet directories
echo "Cleaning up encrypted wallet directories..."
for version in 0.4.0 0.5.0 0.5.1; do
  dir="bitcoin-v${version}"
  echo "Cleaning up ${dir}..."
  
  # Check if wallet.dat exists
  if [ ! -f "${dir}/wallet.dat" ]; then
    echo "WARNING: wallet.dat not found in ${dir}"
    continue
  fi
  
  # Create a temporary directory to store wallet.dat and README.md
  mkdir -p "${dir}_temp"
  cp "${dir}/wallet.dat" "${dir}_temp/"
  cp "${dir}/README.md" "${dir}_temp/" 2>/dev/null || echo "Creating new README.md in ${dir}"
  
  # If README.md doesn't exist, create it
  if [ ! -f "${dir}_temp/README.md" ]; then
    cat > "${dir}_temp/README.md" << EOF
# Bitcoin Wallet

Encrypted by Bitcoin Core v${version} with built-in wallet encryption.
EOF
  fi
  
  # Remove original directory and rename temp directory
  rm -rf "${dir}"
  mv "${dir}_temp" "${dir}"
  
  echo "${dir} cleaned successfully."
done

# Clean up conversion directories
echo "Cleaning up conversion directories..."
for source in 0.3.21 0.3.22 0.3.23 0.3.24; do
  for target in 0.4.0 0.5.0 0.5.1; do
    dir="enc_${source}_to_${target}"
    echo "Cleaning up ${dir}..."
    
    # Check if wallet.dat exists
    if [ ! -f "${dir}/wallet.dat" ]; then
      echo "WARNING: wallet.dat not found in ${dir}"
      continue
    fi
    
    # Create a temporary directory to store wallet.dat and README.md
    mkdir -p "${dir}_temp"
    cp "${dir}/wallet.dat" "${dir}_temp/"
    cp "${dir}/README.md" "${dir}_temp/" 2>/dev/null || echo "Creating new README.md in ${dir}"
    
    # If README.md doesn't exist, create it
    if [ ! -f "${dir}_temp/README.md" ]; then
      cat > "${dir}_temp/README.md" << EOF
# Bitcoin Wallet Conversion

Converted from Bitcoin Core v${source} to v${target} and encrypted with 'badpassword123'.
EOF
    fi
    
    # Remove original directory and rename temp directory
    rm -rf "${dir}"
    mv "${dir}_temp" "${dir}"
    
    echo "${dir} cleaned successfully."
  done
done

echo "All directories cleaned up successfully. Each directory now contains only wallet.dat and README.md."