"""Unit tests for WMilvus MCP Server tools."""

from unittest.mock import patch
from wmilvus_mcp.server import (
    deploy_wmilvus_scaffolding,
    generate_mcp_client_config,
    generate_wmilvus_crud,
    get_wmilvus_architect_blueprints,
    get_wmilvus_architect_manual,
    remove_pid,
    save_pid,
    search_wmilvus_pattern,
    stop_daemon,
    validate_model_schema,
)


def test_validate_model_schema() -> None:
    """Test validating Pydantic model code."""
    valid_code = """
from pydantic import BaseModel
from wmilvus import FieldVector, MetricType

class FaceEmbedding(BaseModel):
    id: str
    face_vec: list[float] = FieldVector(dim=128, metric_type=MetricType.COSINE)
"""
    res = validate_model_schema(valid_code)
    assert "100% valid" in res or "Valid" in res

    # Warning branch (no FieldVector)
    no_vector_code = """
from pydantic import BaseModel
class User(BaseModel):
    id: str
"""
    res_warn = validate_model_schema(no_vector_code)
    assert "Warnings:" in res_warn or "No explicit FieldVector" in res_warn

    # Issue branch (no BaseModel)
    no_model_code = "x = 10"
    res_issue = validate_model_schema(no_model_code)
    assert "Issues:" in res_issue

    # Syntax error branch
    syntax_err_code = "class Bad("
    res_syntax = validate_model_schema(syntax_err_code)
    assert "Syntax Error" in res_syntax


def test_search_wmilvus_pattern() -> None:
    """Test searching patterns catalog."""
    res = search_wmilvus_pattern("vector")
    assert "production-ready" in res

    res_empty = search_wmilvus_pattern("nonexistent_pattern_12345")
    assert "No pattern matching" in res_empty


def test_get_blueprints_and_manual() -> None:
    """Test fetching blueprints and architectural manual."""
    blueprints = get_wmilvus_architect_blueprints()
    assert "SINGLE COLLECTION" in blueprints

    manual = get_wmilvus_architect_manual()
    assert "Architectural Manual" in manual


def test_generate_wmilvus_crud() -> None:
    """Test generating CRUD boilerplate code."""
    code = generate_wmilvus_crud(model_name="UserFace", vector_dim=128, fields="id:str,name:str")
    assert "class UserFace(BaseModel):" in code
    assert "FieldVector(dim=128" in code

    code_default = generate_wmilvus_crud(model_name="CustomEntity", vector_dim=64, fields="no_colon")
    assert "class CustomEntity(BaseModel):" in code_default


def test_generate_mcp_client_config() -> None:
    """Test generating MCP client config JSON."""
    cfg = generate_mcp_client_config(server_name="wmilvus-mcp")
    assert "mcpServers" in cfg
    assert "wmilvus-mcp" in cfg


def test_deploy_wmilvus_scaffolding(tmp_path) -> None:
    """Test deploying project scaffolding to target directory."""
    target_dir = str(tmp_path / "my_project")
    res = deploy_wmilvus_scaffolding(target_dir=target_dir, project_name="test_proj")
    assert "Success" in res

    # Error case (relative path)
    res_err = deploy_wmilvus_scaffolding(target_dir="relative/path")
    assert "Error: target_dir must be an absolute path" in res_err


def test_pid_and_daemon_management(tmp_path) -> None:
    """Test PID file and daemon management functions."""
    pid_file = str(tmp_path / ".wmilvus_mcp.pid")
    with patch("wmilvus_mcp.server.PID_FILE", pid_file), patch("os.kill") as mock_kill:
        save_pid()
        assert (tmp_path / ".wmilvus_mcp.pid").exists()

        stop_daemon()
        assert mock_kill.called
        assert not (tmp_path / ".wmilvus_mcp.pid").exists()

        # Call again when no PID file exists
        stop_daemon()
