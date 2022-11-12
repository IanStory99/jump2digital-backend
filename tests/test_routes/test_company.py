from tests.utils.before_insert import before_insert_company
from fastapi.testclient import TestClient


COMPANY_ENDPOINT = "/company"
COMPANY_SUMMARY_ENDPOINT = "/company/summary"

def test_company_get_all_order_by_founded(client: TestClient):
    # ARRANGE
    before_insert_company()
    before_insert_company(id="id2", founded=2001)
    before_insert_company(id="id3", founded=1999)
    params = {"order": "founded"}

    # ACT
    response = client.get(COMPANY_ENDPOINT, params=params)
    json_response = response.json()

    # ASSERT
    assert response.status_code == 200
    assert len(json_response['item']) == 3
    assert json_response['item'][0]['id'] == "id3"
    assert json_response['item'][1]['id'] == "id1"
    assert json_response['item'][2]['id'] == "id2"

def test_company_get_all_order_by_size(client: TestClient):
    # ARRANGE
    before_insert_company()
    before_insert_company(id="id2", size="11-50")
    before_insert_company(id="id3", size="1-5")
    params = {"order": "size"}

    # ACT
    response = client.get(COMPANY_ENDPOINT, params=params)
    json_response = response.json()

    # ASSERT
    assert response.status_code == 200
    assert len(json_response['item']) == 3
    assert json_response['item'][0]['id'] == "id3"
    assert json_response['item'][1]['id'] == "id1"
    assert json_response['item'][2]['id'] == "id2"

def test_company_get_all_invalid_order(client: TestClient):
    # ARRANGE
    params = {"order": "invalid"}

    # ACT
    response = client.get(COMPANY_ENDPOINT, params=params)
    json_response = response.json()
    print(json_response)

    # ASSERT
    assert response.status_code == 422
    assert json_response['detail'][0]['msg'].startswith("unexpected value")

def test_company_get_all_without_companies(client: TestClient):
    # ARRANGE
    params = {"order": "founded"}

    # ACT
    response = client.get(COMPANY_ENDPOINT, params=params)
    json_response = response.json()

    # ASSERT
    assert response.status_code == 200
    assert len(json_response['item']) == 0

def test_company_get_summary(client: TestClient):
    # ARRANGE
    before_insert_company()
    before_insert_company(id="id2", industry="industry2", size="11-50", founded=2001)
    before_insert_company(id="id3", industry="industry3", size="1-5", founded=1999)
    before_insert_company(id="id4", industry="industry2", size="11-50", founded=2001)
    before_insert_company(id="id5", industry="industry2", size="11-50", founded=2001)

    # ACT
    response = client.get(COMPANY_SUMMARY_ENDPOINT)
    json_response = response.json()

    # ASSERT
    assert response.status_code == 200
    assert json_response["item"]['industry_count'] == {"industry1": 1, "industry2": 3, "industry3": 1}
    assert json_response["item"]['size_count'] == {"1-10": 1, "11-50": 3, "1-5": 1}
    assert json_response["item"]['founded_year_count'] == {'2000': 1, '2001': 3, '1999': 1}

def test_company_get_summary_without_companies(client: TestClient):
    # ACT
    response = client.get(COMPANY_SUMMARY_ENDPOINT)
    json_response = response.json()

    # ASSERT
    assert response.status_code == 200
    assert json_response["item"]['industry_count'] == {}
    assert json_response["item"]['size_count'] == {}
    assert json_response["item"]['founded_year_count'] == {}
