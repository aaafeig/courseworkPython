import pytest

from src.vacancy import Vacancy, JsonHandler

@pytest.fixture
def vacancy_tested():
    name = "Вакансия1"
    salary = {"salary": {"from": 50000, "currency": "RUR"}}
    description = {"snippet": {"responsibility": "Описание вакансии1"}}
    vacancy = Vacancy(name, salary, description)
    return vacancy

def test_vacancy(vacancy_tested):
    assert vacancy_tested.get_name == "Вакансия1"
    assert vacancy_tested.salary == 50000
    assert vacancy_tested.currency == "RUR"
    assert vacancy_tested.description == "Описание вакансии1"

def test_json_handler_show_vacancies():
    pass

def test_json_handler_search_vacancies():
    pass

def test_json_handler_add_vacancy():
    pass

def test_json_handler_delete_vacancy():
    pass

def test_json_top_n():
    pass