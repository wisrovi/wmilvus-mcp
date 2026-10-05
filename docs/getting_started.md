# Getting Started with `wmilvus-mcp`

This guide explains how to install and configure the `wmilvus-mcp` server for AI agents.

---

## 1. Installation

Install `wmilvus-mcp` from PyPI:

```bash
pip install wmilvus-mcp
```

---

## 2. Running the MCP Server

The server communicates via `stdio` using FastMCP:

```bash
wmilvus-mcp --start
```

---

## 3. Configuring AI Agent Clients

Add `wmilvus-mcp` to your MCP client configuration (e.g. Anthropic Claude Desktop, Antigravity, or Cursor):

```json
{
  "mcpServers": {
    "wmilvus-mcp": {
      "command": "wmilvus-mcp",
      "args": ["--start"]
    }
  }
}
```
