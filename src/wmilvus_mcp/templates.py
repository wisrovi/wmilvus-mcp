"""Templates Generator for WMilvus project scaffolding and code generation."""

from typing import Dict, List


class TemplateGenerator:
    """Generator for WMilvus project boilerplate files."""

    @staticmethod
    def get_folders(scaffold_type: str = "standard") -> List[str]:
        """Return folder layout for project scaffolding."""
        return [
            "src",
            "src/models",
            "src/services",
            "examples",
            "tests",
        ]

    @staticmethod
    def get_files_blueprint(scaffold_type: str, project_name: str) -> Dict[str, str]:
        """Return file blueprint map relative_path -> content."""
        return {
            "pyproject.toml": f"""[project]
name = "{project_name}"
version = "0.1.0"
description = "WMilvus Vector Application"
dependencies = [
    "wmilvus",
    "pydantic>=2.0.0",
]
""",
            "src/models/vector_entity.py": """from typing import List
from pydantic import BaseModel
from wmilvus import FieldVector, MetricType, ForensicModel

class UserFace(ForensicModel):
    id: str
    name: str
    email: str
    face_embedding: List[float] = FieldVector(dim=128, metric_type=MetricType.COSINE)
""",
            "src/services/vector_service.py": """from typing import List, Optional
from wmilvus import WMilvus
from src.models.vector_entity import UserFace

milvus_uri = "http://localhost:19530"

def index_user_face(user: UserFace) -> UserFace:
    with WMilvus(UserFace, uri=milvus_uri) as db:
        return db.insert(user)

def search_nearest_faces(query_vec: List[float], top_k: int = 5) -> List[UserFace]:
    with WMilvus(UserFace, uri=milvus_uri) as db:
        return db.search_similar(vector=query_vec, top_k=top_k)
""",
            "main.py": """from src.models.vector_entity import UserFace
from src.services.vector_service import index_user_face, search_nearest_faces

def main():
    print("WMilvus Application Initialized")
    user = UserFace(id="u_001", name="William Rodriguez", email="william@example.com", face_embedding=[0.1] * 128)
    index_user_face(user)
    matches = search_nearest_faces([0.1] * 128, top_k=1)
    print(f"Top Match: {matches[0].name}")

if __name__ == "__main__":
    main()
""",
            "README.md": f"""# {project_name}

WMilvus Vector Application powered by Pydantic ORM.

## Usage

```bash
python main.py
```
""",
        }

    @staticmethod
    def generate_crud_code(model_name: str = "VectorEntity", vector_dim: int = 128, fields: str = "id:str,name:str") -> str:
        """Generate ready-to-run WMilvus CRUD code."""
        parsed_fields = []
        for pair in fields.split(","):
            if ":" in pair:
                fname, ftype = pair.split(":", 1)
                parsed_fields.append(f"    {fname.strip()}: {ftype.strip()}")

        fields_block = "\n".join(parsed_fields) if parsed_fields else "    id: str\n    name: str"

        return f'''from typing import List
from pydantic import BaseModel
from wmilvus import FieldVector, MetricType, WMilvus

class {model_name}(BaseModel):
{fields_block}
    embedding: List[float] = FieldVector(dim={vector_dim}, metric_type=MetricType.COSINE)

milvus_config = {{"uri": "http://localhost:19530"}}

def main():
    with WMilvus({model_name}, milvus_config) as db:
        record = {model_name}(id="1", name="Sample Entity", embedding=[0.1] * {vector_dim})
        db.insert(record)
        print("Inserted:", record)

        matches = db.search_similar(vector=[0.1] * {vector_dim}, top_k=5)
        print("Matches:", matches)

if __name__ == "__main__":
    main()
'''
