"""Offline bootstrap smoke test — no Azure resources required."""
from fastapi.testclient import TestClient
from backend.app.main import app


def test_health() -> None:
    """Ensure the health endpoint declares the read-only bootstrap mode."""
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "mode": "bootstrap-read-only"}
