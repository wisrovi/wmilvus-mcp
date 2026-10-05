#!/usr/bin/env bash
set -e

echo "=== Calculating Code Coverage for WMilvus MCP ==="
PYTHONPATH=src pytest --cov=wmilvus_mcp --cov-report=term-missing --cov-report=html
echo "=== Coverage Report Generated in htmlcov/index.html ==="
