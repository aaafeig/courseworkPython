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
    handler._JsonHandler__data = []
    return handler
