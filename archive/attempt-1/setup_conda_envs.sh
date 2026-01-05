#!/bin/bash
# Script to set up Conda environments for each Bitcoin version

# Create Conda environments for v0.3.x versions
echo "Creating Conda environments for v0.3.x..."
for version in 0.3.21 0.3.22 0.3.23 0.3.24; do
  echo "Setting up environment for Bitcoin v${version}..."
  conda create -y -n bitcoin-v${version} python
done

# Create Conda environments for v0.4.0+ versions
echo "Creating Conda environments for v0.4.0+..."
for version in 0.4.0 0.5.0 0.5.1; do
  echo "Setting up environment for Bitcoin v${version}..."
  conda create -y -n bitcoin-v${version} python
done

echo "All Conda environments created successfully."
echo ""
echo "To activate an environment, use:"
echo "conda activate bitcoin-vX.X.X"
echo ""
echo "After activation, install/unpack the appropriate Bitcoin binary for that version."