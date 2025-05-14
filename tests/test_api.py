import requests
from unittest.mock import patch


def get_vacancies():
    response = requests.get(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "", "page": 0, "per_page": 20},
    )
    return response.json()


@patch("requests.get")
def test_json_handler_show(mock_get):
    mock_get.return_value.json.return_value = {
        "id": "id",
        "name": "name",
        "salary": {"from": "price_from", "to": "to", "currency": "currency"},
        "snippet": {"responsibility": "responsibility"},
    }
    assert get_vacancies() == {
        "id": "id",
        "name": "name",
        "salary": {"from": "price_from", "to": "to", "currency": "currency"},
        "snippet": {"responsibility": "responsibility"},
    }
    mock_get.assert_called_once()
