from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_make_sprite_default_values():
    response = client.get("/sprite")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
