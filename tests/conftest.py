from unittest.mock import Mock

import pytest

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
def json_handler_fixture():
    handler = JsonHandler.__new__(JsonHandler)
    handler._data = []
    handler._path_json = "fake_path.json"
    handler._JsonHandler__saver = Mock()
    handler._JsonHandler__printer = Mock()
    handler._JsonHandler__validate = Mock(return_value=True)
    handler._JsonHandler__get_index = Mock(return_value=0)
    handler._JsonHandler__get_my_index = Mock(return_value=0)
    return handler
