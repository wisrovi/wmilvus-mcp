# wmilvus-mcp

<p align="center">
    <a href="https://pypi.org/project/wmilvus-mcp/">
        <img src="https://img.shields.io/pypi/v/wmilvus-mcp.svg" alt="PyPI version">
    </a>
    <a href="https://pypi.org/project/wmilvus-mcp/">
        <img src="https://img.shields.io/pypi/pyversions/wmilvus-mcp.svg" alt="Python versions">
    </a>
    <a href="https://github.com/wisrovi/wmilvus-mcp/blob/main/LICENSE">
        <img src="https://img.shields.io/pypi/l/wmilvus-mcp.svg" alt="License">
    </a>
</p>

**wmilvus-mcp** is the Model Context Protocol (MCP) server for architecting, validating, scaffolding, and generating code for **WMilvus** vector database applications.

## Technical Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Protocol Core | Model Context Protocol (MCP) |
| Server Framework | FastMCP (mcp.server.fastmcp) |
| Validation Engine | AST & Pydantic 2.x |
| Testing Framework | pytest, pytest-cov |
| Code Formatting | ruff |

## Features & Exposed MCP Tools

1. `validate_model_schema` — Validate Pydantic models for WMilvus compatibility.
2. `search_wmilvus_pattern` — Search production-ready WMilvus design patterns.
3. `deploy_wmilvus_scaffolding` — Deploy a complete WMilvus vector application structure.
4. `get_wmilvus_architect_blueprints` — Runnable code reference for CRUD, vector search, range search, batch ingestion, async client, and ghost audit log.
5. `get_wmilvus_architect_manual` — Comprehensive architectural manual for Milvus memory and vector indexing.
6. `generate_wmilvus_crud` — Generate ready-to-run CRUD code for WMilvus models.
7. `generate_mcp_client_config` — Generate JSON configuration snippet for Anthropic Claude, Antigravity, or Cursor.

## Quick Start

Run the server via stdio:

```bash
pip install -e .
wmilvus-mcp --start
```

## Running Tests

Execute tests inside an isolated Docker container:

```bash
./run_tests_docker.sh
```

Calculate code coverage:

```bash
./run_coverage.sh
```
