# AGENTS.md — Agent Guidelines for `wmilvus-mcp`

Welcome AI Agent! This file defines the repository architecture, developer instructions, coding standards, and operational guidelines for working on **`wmilvus-mcp`**.

---

## 1. Repository Overview

`wmilvus-mcp` is the Model Context Protocol (MCP) server for **WMilvus**. It exposes tools to AI agents (Claude, Antigravity, Cursor) for validating Pydantic schemas, deploying scaffolding, searching design patterns, generating CRUD code, and fetching architect blueprints.

### Core Technologies
- **Python**: 3.10+
- **Protocol**: Model Context Protocol (MCP)
- **Server Framework**: FastMCP (`mcp.server.fastmcp`)
- **Data Validation & AST**: Pydantic 2.x & Python `ast` module
- **Code Quality**: `ruff`, `pre-commit`
- **Testing**: `pytest`, `pytest-cov`, Docker (`run_tests_docker.sh`)

---

## 2. Directory Structure

```
wmilvus-mcp/
├── src/wmilvus_mcp/
│   ├── server.py       # FastMCP server definition and tool registration
│   ├── catalog.py      # Exposed MCP tools catalog definitions
│   ├── templates.py    # Code generation templates and scaffolds
│   └── validators.py   # AST-based schema validation functions
├── tests/              # Server unit & integration tests
├── .agents/skills/     # Local agent skills for MCP server architecting
├── run_tests_docker.sh # Dockerized test runner script
└── run_coverage.sh     # Local test coverage report generator
```

---

## 3. Developer & Agent Rules

1. **Language Standards**:
   - Code, docstrings, inline comments, and commit messages MUST be written in **English**.
   - Ensure clean typing and syntax compatible with Python 3.10+.

2. **Testing & Quality Assurance**:
   - Always run unit tests via Docker: `./run_tests_docker.sh`.
   - Ensure pre-commit checks pass: `pre-commit run --all-files`.
   - Maintain high test coverage: `./run_coverage.sh`.

3. **Git Commit Rules**:
   - Strict **1 file per commit** policy.
   - Commit messages must start with a category tag in brackets (e.g. `[FEATURE]`, `[FIX]`, `[DOCS]`, `[TEST]`, `[CHORE]`).

4. **Documentation**:
   - Keep `README.md` updated with all exposed MCP tools and Technical Stack details.

---

## 4. Agent Skills Location

Skills specific to this codebase are maintained in `.agents/skills/`:
- `.agents/skills/wmilvus-mcp-architect/SKILL.md`: Guide to FastMCP server tool handlers, code generators, and scaffolding rules.
