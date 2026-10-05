#!/usr/bin/env bash
set -e

echo "=== Running WMilvus MCP Unit Tests inside Docker ==="
docker build -t wmilvus-mcp-test-runner -f - . <<'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir .[dev]
CMD ["pytest"]
EOF

docker run --rm wmilvus-mcp-test-runner
echo "=== Docker Tests Completed Successfully ==="
