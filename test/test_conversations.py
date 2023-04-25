from urllib import response

from fastapi.testclient import TestClient

from src.api.server import app

import json

client = TestClient(app)


def test_add_conversations():
    response1 = client.post("/movies/0/conversations/", json={
        "character_1_id": 10,
        "character_2_id": 11,
        "lines": [
            {
                "character_id": 10,
                "line_text": "I'm a line!"
            },
            {
                "character_id": 11,
                "line_text": "I'm a line too!"
            }
        ]
    })
    response2 = client.get("/lines/10")
    assert response.status_code == 200
    # assert response2 != response1


def test_add_conversations2():
    response1 = client.post("/movies/0/conversations/", json={
        "character_1_id": 10,
        "character_2_id": 11,
        "lines": [
            {
                "character_id": 10,
                "line_text": "I'm a line!"
            },
            {
                "character_id": 11,
                "line_text": "I'm a line too!"
            }
        ]
    })
    response2 = client.get("/lines/10")
    assert response.status_code == 200
    # assert response2 != response1
