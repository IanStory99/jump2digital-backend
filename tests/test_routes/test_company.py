from fastapi.testclient import TestClient


def test_get_all(client: TestClient):
    # ACT
    response = client.post('/company')

    # ASSERT
    assert response.status_code == 200
