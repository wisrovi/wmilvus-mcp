#!/usr/bin/env bash
set -e

echo "=== Installing wmilvus-mcp Package in Editable Mode ==="
pip install -e .[dev]
echo "=== Installation Successful ==="
