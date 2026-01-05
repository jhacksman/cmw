#!/bin/bash
# Script to extract Bitcoin binaries for each version

BASE_DIR=$(pwd)

# Extract v0.3.x binaries to their respective directories
echo "Extracting v0.3.x binaries..."
for version_file in bitcoin-bitcoin-v0.3.21-0-g64ad448.tar.gz bitcoin-bitcoin-v0.3.22-0-ge104c79.tar.gz bitcoin-bitcoin-v0.3.23-0-gce14894.tar.gz bitcoin-bitcoin-v0.3.24-0-gf087364.tar.gz; do
  version=$(echo $version_file | sed -E 's/.*v([0-9]+\.[0-9]+\.[0-9]+).*/\1/')
  target_dir="bitcoin-v${version}"
  
  echo "Extracting ${version_file} to ${target_dir}..."
  tar -xzf "${BASE_DIR}/bitcoin.versions/${version_file}" -C "${target_dir}"
done

# Extract v0.4.0+ binaries to their respective directories
echo "Extracting v0.4.0+ binaries..."
for version_file in bitcoin-bitcoin-v0.4.0-0-gc7eb151.tar.gz bitcoin-bitcoin-v0.5.0-0-gf53c5ed.tar.gz bitcoin-bitcoin-v0.5.1-0-gb12fc3e.tar.gz; do
  version=$(echo $version_file | sed -E 's/.*v([0-9]+\.[0-9]+\.[0-9]+).*/\1/')
  target_dir="bitcoin-v${version}"
  
  echo "Extracting ${version_file} to ${target_dir}..."
  tar -xzf "${BASE_DIR}/bitcoin.versions/${version_file}" -C "${target_dir}"
done

echo "All Bitcoin binaries extracted successfully."