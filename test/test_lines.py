from fastapi.testclient import TestClient

from src.api.server import app

import json

client = TestClient(app)


def test_get_lines():
    response = client.get("/lines/1")
    assert response.status_code == 200

    with open("test/lines/char1.json", encoding="utf-8") as f:
        assert response.json() == json.load(f)


def test_get_char_lines():
    response = client.get("/lines/char1")
    assert response.status_code == 200

    with open("test/lines/char1.json", encoding="utf-8") as f:
        assert response.json() == json.load(f)
