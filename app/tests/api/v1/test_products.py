from typing import Dict

from fastapi.testclient import TestClient

from app.core import settings


def test_create_train(client: TestClient, random_train: Dict[str, str]) -> None:
    response = client.post(f"{settings.API_V1_STR}/trains", json=random_train)
    train = response.json()
    assert response.status_code == 200
    assert train.get("name") == random_train.get("name")
    assert train.get("price") == random_train.get("price")


def test_read_trains(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/trains")
    trains = response.json()
    assert response.status_code == 200
    assert len(trains) > 0


def test_update_train(client: TestClient, random_train: Dict[str, str]) -> None:
    random_train["price"] = 100
    response = client.put(f"{settings.API_V1_STR}/trains", json=random_train)
    train = response.json()
    assert response.status_code == 200
    assert train.get("price") == random_train.get("price")


def test_delete_train(client: TestClient, random_train: Dict[str, str]) -> None:
    response = client.delete(f"{settings.API_V1_STR}/trains/{random_train.get('id')}")
    message = response.json()
    assert response.status_code == 200
    assert "message" in message
