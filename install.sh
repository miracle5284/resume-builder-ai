#!/bin/bash

echo "Installing required packages..."

# yq installation

YQ_VERSION="v4.34.1"
YQ_BINARY_PATH="$HOME/.local/bin/yq"

mkdir -p "$HOME/.local/bin"
if ! command -v yq >/dev/null 2>&1; then
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # For Linux
    wget "https://github.com/mikefarah/yq/releases/download/${YQ_VERSION}/yq_linux_amd64" -O "$YQ_BINARY_PATH"
    echo "linux"
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "mac"
    # For macOS
    wget "https://github.com/mikefarah/yq/releases/download/${YQ_VERSION}/yq_darwin_amd64" -O "$YQ_BINARY_PATH"
  else
    echo "Unsupported OS: $OSTYPE"
    exit 1
  fi

  if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
  echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
  export PATH=$HOME/.local/bin:$PATH
fi

  chmod +x "$YQ_BINARY_PATH"

  # Verify installation
  if ! yq --version >/dev/null 2>&1; then
    echo "Error: yq installation failed."
    exit 1
  fi
fi
