from fastapi.testclient import TestClient

from src.api.server import app

import json

client = TestClient(app)


def test_get_lines():
    response = client.get("/lines/50/line")
    assert response.status_code == 200

    with open("test/lines/50.json", encoding="utf-8") as f:
        assert response.json() == json.load(f)


def test_get_char_lines():
    response = client.get("/lines/3/character")
    assert response.status_code == 200

    with open("test/lines/char1.json", encoding="utf-8") as f:
        assert response.json() == json.load(f)


def test_get_conv():
    response = client.get("/lines/3/conversations")
    assert response.status_code == 200

    with open("test/lines/conv1.json", encoding="utf-8") as f:
        assert response.json() == json.load(f)
