# Frequently Asked Questions (FAQ)

## 1. What protocol transport does `wmilvus-mcp` use?
`wmilvus-mcp` uses standard input/output (`stdio`) transport via FastMCP (`mcp.server.fastmcp`).

---

## 2. Can I use `wmilvus-mcp` with Anthropic Claude Desktop?
Yes, add the JSON server configuration to your `claude_desktop_config.json`.

---

## 3. How does `wmilvus-mcp` validate model code without executing it?
It uses Python's built-in `ast` (Abstract Syntax Tree) module to safely parse and inspect Pydantic class definitions without evaluating un-trusted code.
