import json

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_tested():
    name = "Вакансия1"
    salary = {"salary": {"from": 50000, "currency": "RUR"}}
    description = {"snippet": {"responsibility": "Описание вакансии1"}}
    vacancy = Vacancy(name, salary, description)
    return vacancy
