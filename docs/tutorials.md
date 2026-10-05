# Tutorials

Step-by-step tutorials for invoking `wmilvus-mcp` tools from AI agents or Python scripts.

---

## Tutorial 1: Validating Pydantic Model Schemas

Use `validate_model_schema` to verify if a Python Pydantic model string complies with `wmilvus` vector conventions:

```python
from wmilvus_mcp.validators import validate_pydantic_code

code = """
from pydantic import BaseModel
from typing import List
from wmilvus import FieldVector, MetricType

class Face(BaseModel):
    id: str
    emb: List[float] = FieldVector(dim=128, metric_type=MetricType.COSINE)
"""

result = validate_pydantic_code(code)
print(f"Schema Valid: {result['valid']}")
```

---

## Tutorial 2: Generating CRUD Scaffolding

Generate CRUD code for a Pydantic vector model automatically:

```python
from wmilvus_mcp.templates import generate_crud_code

crud_script = generate_crud_code(
    model_name="DocumentChunk",
    vector_dim=384,
    metric_type="COSINE"
)
print(crud_script)
```
