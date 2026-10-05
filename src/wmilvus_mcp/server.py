"""WMilvus MCP Server providing tools for Milvus vector ORM architecting, scaffolding, and code generation."""

import argparse
import ast
import json
import logging
import os
import signal
import subprocess
import sys
from functools import lru_cache

from mcp.server.fastmcp import FastMCP

from wmilvus_mcp.catalog import PatternsCatalog
from wmilvus_mcp.templates import TemplateGenerator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stderr)
logger = logging.getLogger(__name__)

PID_FILE = os.path.expanduser("~/.wmilvus_mcp.pid")

mcp = FastMCP("wmilvus-mcp-server")


@lru_cache(maxsize=1)
def get_catalog() -> PatternsCatalog:
    """Return shared patterns catalog instance."""
    return PatternsCatalog()


def _is_pydantic_model(cls: ast.ClassDef) -> bool:
    """Return True if class inherits from BaseModel or ForensicModel."""
    return any(
        isinstance(b, ast.Name) and b.id in ("BaseModel", "ForensicModel")
        for b in cls.bases
    )


@mcp.tool()
def validate_model_schema(model_code: str) -> str:
    """Validate a Pydantic model definition for WMilvus vector storage compatibility."""
    try:
        tree = ast.parse(model_code)
        issues = []
        warnings = []

        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        model_classes = [c for c in classes if _is_pydantic_model(c)]

        if not model_classes:
            issues.append("No Pydantic BaseModel or ForensicModel subclass found.")

        has_vector_field = "FieldVector" in model_code or "embedding" in model_code or "vector" in model_code
        if not has_vector_field:
            warnings.append("No explicit FieldVector annotation detected. Defaulting to 128-dim COSINE vector.")

        result = "WMilvus Model Validation Result:\n"
        if issues:
            result += "Issues:\n" + "\n".join(f"  ❌ {i}" for i in issues) + "\n"
        if warnings:
            result += "Warnings:\n" + "\n".join(f"  ⚠️ {w}" for w in warnings) + "\n"
        if not issues and not warnings:
            result += "✅ Model is 100% valid for WMilvus vector indexing & ORM storage!"
        return result

    except SyntaxError as e:
        return f"❌ Syntax Error in model code: {e}"
    except Exception as e:
        return f"❌ Validation Error: {type(e).__name__}: {e}"


@mcp.tool()
def search_wmilvus_pattern(query: str) -> str:
    """Search for production-ready WMilvus architectural patterns in the catalog."""
    results = get_catalog().search(query)
    if not results:
        return f"No pattern matching '{query}' was found in WMilvus catalog."

    response = "Found production-ready architectural patterns in w-suite:\n\n"
    for p in results:
        response += f"🚀 [{p['origin']}] {p['name']}\n"
        response += f"   - Feature: {p['feature']}\n"
        response += f"   - Module: {p['module']}\n"
        response += f"   - Description: {p['description']}\n\n"
    return response


@mcp.tool()
def deploy_wmilvus_scaffolding(
    target_dir: str,
    project_name: str = "wmilvus_project",
    scaffold_type: str = "standard",
) -> str:
    """Deploys a professional WMilvus vector application project structure."""
    try:
        if not os.path.isabs(target_dir):
            return "Error: target_dir must be an absolute path."

        for folder in TemplateGenerator.get_folders(scaffold_type):
            os.makedirs(os.path.join(target_dir, folder), exist_ok=True)

        blueprints = TemplateGenerator.get_files_blueprint(scaffold_type, project_name)
        for rel_path, content in blueprints.items():
            full_path = os.path.join(target_dir, rel_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

        return f"Success: WMilvus project '{project_name}' deployed at {target_dir}"
    except Exception as e:
        return f"Error deploying scaffolding: {str(e)}"


@mcp.tool()
def get_wmilvus_architect_blueprints() -> str:
    """Complete reference with runnable code examples for every WMilvus feature."""
    return '''=== WMilvus Architect Blueprints ===

1. SINGLE COLLECTION Pydantic CRUD & Context Manager:
from pydantic import BaseModel
from wmilvus import FieldVector, MetricType, WMilvus

class Person(BaseModel):
    id: str
    name: str
    embedding: list[float] = FieldVector(dim=128, metric_type=MetricType.COSINE)

with WMilvus(Person, uri="http://localhost:19530") as db:
    db.insert(Person(id="1", name="Juan", embedding=[0.1] * 128))
    results = db.search_similar(vector=[0.1] * 128, top_k=5)

2. VECTOR SIMILARITY & DISTANCE SCORES:
matches = db.search_similar_with_scores(vector=[0.1] * 128, top_k=5)

3. SIMILARITY RANGE THRESHOLD SEARCH:
matches = db.search_range_with_scores(vector=[0.1] * 128, radius=0.95, top_k=10)

4. BULK VECTOR INGESTION WITH CHUNKING:
result = db.insert_batch(records_list, batch_size=1000)

5. ASYNC CLIENT (AsyncWMilvus):
async with AsyncWMilvus(Person, uri="http://localhost:19530") as db:
    await db.insert(person)
    matches = await db.search_similar(vector=[0.1] * 128, top_k=5)

6. ENTERPRISE GHOST AUDIT LOG (_forensic_audit_log):
class BankAccountVector(ForensicModel):
    id: str
    balance: float
    account_vec: list[float] = FieldVector(dim=128)

db.insert(account, user_id=100)
logs = db.get_ghost_audit_log()
'''


@mcp.tool()
def get_wmilvus_architect_manual() -> str:
    """Architectural manual explaining vector indexing, Milvus memory management, and forensic audit logs."""
    return '''=== WMilvus Architectural Manual ===

1. FieldVector Annotation & Inspection:
WMilvus uses FieldVector(...) metadata inside Pydantic models to inspect vector dimension, index algorithm (HNSW, IVF_FLAT, FLAT), and similarity metric (MetricType.COSINE, MetricType.L2, MetricType.IP).

2. Multi-Collection Repository Routing:
WMilvus([ModelA, ModelB], config) creates isolated CollectionRepository instances for each model.
Routing methods:
- db[ModelA].insert(item)
- db.modela.insert(item)
- db.insert(item) [Auto-routing by class]

3. Enterprise Ghost Audit Log (_forensic_audit_log):
When models inherit from ForensicModel or forensic=True is enabled, WMilvus automatically logs audit entries to global _forensic_audit_log collection on INSERT, UPDATE, SOFT_DELETE, and HARD_DELETE.
'''


@mcp.tool()
def generate_wmilvus_crud(
    model_name: str = "VectorEntity",
    vector_dim: int = 128,
    fields: str = "id:str,name:str",
) -> str:
    """Generate ready-to-run WMilvus CRUD code snippet."""
    return TemplateGenerator.generate_crud_code(model_name=model_name, vector_dim=vector_dim, fields=fields)


@mcp.tool()
def generate_mcp_client_config(
    server_name: str = "wmilvus-mcp",
    command: str = "python3",
) -> str:
    """Generate MCP Client JSON configuration snippet for Anthropic Claude, Antigravity, or Cursor."""
    config = {
        "mcpServers": {
            server_name: {
                "command": command,
                "args": ["-m", "wmilvus_mcp.server"],
            }
        }
    }
    return json.dumps(config, indent=2)


# --- Daemon Management ---

def save_pid() -> None:
    """Save server PID to file."""
    with open(PID_FILE, "w", encoding="utf-8") as f:
        f.write(str(os.getpid()))


def remove_pid() -> None:
    """Remove PID file on clean exit."""
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)


def stop_daemon() -> None:
    """Stop running daemon instance."""
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, encoding="utf-8") as f:
                pid = int(f.read().strip())
            os.kill(pid, signal.SIGTERM)
            print(f"Stopped WMilvus MCP daemon (PID {pid})")
        except ProcessLookupError:
            print("Daemon process not running.")
        except Exception as e:
            print(f"Error stopping daemon: {e}")
        finally:
            remove_pid()
    else:
        print("No PID file found.")


def main() -> None:
    """Main entrypoint for CLI commands and FastMCP server execution."""
    parser = argparse.ArgumentParser(description="WMilvus MCP Server CLI")
    parser.add_argument("--start", action="store_true", help="Start FastMCP server via stdio")
    parser.add_argument("--stop", action="store_true", help="Stop background daemon process")
    args = parser.parse_args()

    if args.stop:
        stop_daemon()
        sys.exit(0)

    save_pid()
    try:
        mcp.run()
    finally:
        remove_pid()


if __name__ == "__main__":
    main()
