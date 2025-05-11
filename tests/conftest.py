from unittest.mock import Mock, patch, MagicMock

import pytest

from src.facade import Facade
from src.json_handler import JsonHandler
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_tested():
    name = "Вакансия1"
    salary = 50000
    currency = "RUB"
    description = "Описание вакансии1"
    vacancy = Vacancy(name, salary, currency, description)
    return vacancy


@pytest.fixture
def facade_fixture():
    with patch("src.facade.JsonHandler") as MockJsonHandler:
        mock_handler = MagicMock()
        mock_handler.data = []
        MockJsonHandler.return_value = mock_handler
        return Facade(json_path="fake_path.json")

@pytest.fixture
def json_handler_tested():
    handler = JsonHandler.__new__(JsonHandler)
    handler._path_json = "fake_file.json"
    handler._data = []
    return handler