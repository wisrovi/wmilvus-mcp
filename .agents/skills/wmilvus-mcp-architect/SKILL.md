---
name: wmilvus-mcp-architect
description: "Guide to FastMCP server tool handlers, code generation templates, schema validators, and scaffolding."
---

# `wmilvus-mcp` Architect & Tool Registration Guide

This skill provides architectural guidance for developing and extending the `wmilvus-mcp` FastMCP server.

## Exposed MCP Tools

1. **`validate_model_schema`**:
   - Parses python code strings via `ast` to ensure Pydantic model definitions follow `wmilvus` vector conventions (`FieldVector`, `MetricType`, `IndexType`).

2. **`search_wmilvus_pattern`**:
   - Searches design pattern catalog for vector search, range search, async clients, forensic tracking, multi-table routing, and `wsqlite` backup.

3. **`deploy_wmilvus_scaffolding`**:
   - Generates project directory structure with pre-configured `pyproject.toml`, Docker runner scripts, and sample vector model definitions.

4. **`get_wmilvus_architect_blueprints`**:
   - Returns runnable reference implementations for complex WMilvus workflows.

5. **`get_wmilvus_architect_manual`**:
   - Provides theoretical and practical guidance on Milvus vector dimensions, index selection (HNSW, IVF_FLAT, FLAT), and memory allocation.

6. **`generate_wmilvus_crud`**:
   - Generates CRUD helper classes for Pydantic vector models.

7. **`generate_mcp_client_config`**:
   - Produces JSON configuration snippets for Anthropic Claude Desktop, Antigravity, and Cursor MCP client setup.
