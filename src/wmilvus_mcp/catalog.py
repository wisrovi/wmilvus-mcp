"""Patterns Catalog for WMilvus Vector Database architectural designs."""

from typing import Any, ClassVar


class PatternsCatalog:
    """Repository of production-grade WMilvus design patterns."""

    PATTERNS: ClassVar[list[dict[str, Any]]] = [
        {
            "name": "Single Collection Pydantic CRUD",
            "feature": "Single Collection ORM",
            "origin": "wmilvus/examples/01_crud",
            "module": "wmilvus",
            "description": (
                "Standard single-collection vector CRUD operations using Pydantic BaseModel and context manager."
            ),
        },
        {
            "name": "KNN Vector Similarity Search with Scores",
            "feature": "KNN Vector Search",
            "origin": "wmilvus/examples/02_vector_search",
            "module": "wmilvus",
            "description": (
                "Top-k nearest neighbor vector similarity search returning typed Pydantic models or distance scores."
            ),
        },
        {
            "name": "Similarity Range Threshold Search",
            "feature": "Range Search",
            "origin": "wmilvus/examples/03_range_search",
            "module": "wmilvus",
            "description": (
                "Radius threshold search filtering matches by minimum similarity score (e.g. radius >= 0.95)."
            ),
        },
        {
            "name": "Bulk Vector Ingestion with Chunking",
            "feature": "Bulk Ingestion",
            "origin": "wmilvus/examples/04_batch_ingestion",
            "module": "wmilvus",
            "description": (
                "High-throughput vector ingestion inserting thousands of records in configurable batch chunks."
            ),
        },
        {
            "name": "Non-Blocking Async Client",
            "feature": "Async Client",
            "origin": "wmilvus/examples/05_async_client",
            "module": "wmilvus",
            "description": "AsyncWMilvus client using async with for asyncio and FastAPI applications.",
        },
        {
            "name": "Collection Schema Verification",
            "feature": "Schema Verification",
            "origin": "wmilvus/examples/06_schema_verification",
            "module": "wmilvus",
            "description": (
                "Validating active Milvus collection vector dimension and index schema against Pydantic models."
            ),
        },
        {
            "name": "Hybrid Multi-Modal Similarity Search",
            "feature": "Hybrid Search",
            "origin": "wmilvus/examples/07_hybrid_search",
            "module": "wmilvus",
            "description": "Combining dense vector search with text/scalar metadata filter expressions.",
        },
        {
            "name": "Forensic Model Field Tracking",
            "feature": "Forensic Fields",
            "origin": "wmilvus/examples/16_forensic_fields",
            "module": "wmilvus",
            "description": "Tracking create_by, create_in, update_by, and delete_in fields automatically.",
        },
        {
            "name": "Multi-Collection Repository Routing",
            "feature": "Multi-Collection Mode",
            "origin": "wmilvus/examples/17_multi_table",
            "module": "wmilvus",
            "description": (
                "Managing multiple collections in one WMilvus instance with dictionary indexing or auto-routing."
            ),
        },
        {
            "name": "Enterprise Ghost Audit Log",
            "feature": "Ghost Audit Log",
            "origin": "wmilvus/examples/18_ghost_table_audit",
            "module": "wmilvus",
            "description": (
                "Global _forensic_audit_log ghost collection tracking all INSERT, UPDATE, and DELETE operations."
            ),
        },
        {
            "name": "Auto-ID and INT64 Primary Keys",
            "feature": "Auto-ID and INT64 PK",
            "origin": "wmilvus/examples/19_auto_id_and_int64_pk",
            "module": "wmilvus",
            "description": "Automatic integer primary key generation for Milvus collections with INT64 auto_id.",
        },
        {
            "name": "Declarative Query Builder (filter_by)",
            "feature": "Query Builder",
            "origin": "wmilvus/examples/20_query_builder_filter_by",
            "module": "wmilvus",
            "description": (
                "Chained fluent query filtering with comparison operators (__gt, __gte, __in, __like) and limit/offset."
            ),
        },
        {
            "name": "Streaming Large Result Sets (iter_all)",
            "feature": "Streaming Iterator",
            "origin": "wmilvus/examples/21_streaming_iter_all",
            "module": "wmilvus",
            "description": (
                "Memory-efficient generator streaming records in chunked batches across large Milvus collections."
            ),
        },
        {
            "name": "Partition Routing and Partition Search",
            "feature": "Partition Management",
            "origin": "wmilvus/examples/22_partition_routing",
            "module": "wmilvus",
            "description": (
                "Targeted vector insertion and similarity search scoped to specific collection partitions."
            ),
        },
        {
            "name": "Batch and Expression Deletion",
            "feature": "Deletion Operations",
            "origin": "wmilvus/examples/23_batch_and_expr_deletion",
            "module": "wmilvus",
            "description": (
                "High-performance batch deletion by primary key list and conditional deletion using Milvus expressions."
            ),
        },
    ]

    def search(self, query: str) -> list[dict[str, Any]]:
        """Search catalog patterns by keyword query."""
        q = query.lower()
        return [
            p
            for p in self.PATTERNS
            if q in p["name"].lower()
            or q in p["feature"].lower()
            or q in p["description"].lower()
            or q in p["module"].lower()
        ]
