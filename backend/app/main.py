"""Read-only bootstrap API for TCHWD Azure Manager.

This file intentionally does not contact Azure or perform mutations.
"""
from fastapi import FastAPI

app = FastAPI(title="TCHWD Azure Manager", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Return the service status without using Azure credentials."""
    return {"status": "ok", "mode": "bootstrap-read-only"}
