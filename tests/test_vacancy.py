import pytest

from src.vacancy import Vacancy
from .conftest import vacancy_tested


def test_vacancy(vacancy_tested):
    assert vacancy_tested.name == "Вакансия1"
    assert vacancy_tested.salary == 50000
    assert vacancy_tested.currency == "RUR"
    assert vacancy_tested.description == "Описание вакансии1"
