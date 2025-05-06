from unittest.mock import Mock
from src.vacancy import Vacancy


def test_add_vacancy(vacancy_tested, json_handler_fixture):
    Vacancy.my_vacancies.clear()
    Vacancy.my_vacancies_id.clear()
    json_handler_fixture._save_to_file = lambda: None

    json_handler_fixture.add_vacancy(vacancy_tested)

    assert len(json_handler_fixture._JsonHandler__data) == 1
    assert json_handler_fixture._JsonHandler__data[0]["name"] == vacancy_tested.name
    assert json_handler_fixture._JsonHandler__data[0]["salary"]["from"] == vacancy_tested.salary
    assert json_handler_fixture._JsonHandler__data[0]["salary"]["currency"] == vacancy_tested.currency
    assert json_handler_fixture._JsonHandler__data[0]["snippet"]["responsibility"] == vacancy_tested.description


def test_show_vacancies(json_handler_fixture):
    json_handler_fixture.show_vacancy = Mock(return_value=[])
    json_handler_fixture.show_vacancy()
    json_handler_fixture.show_vacancy.assert_called_once()


def test_top_n(json_handler_fixture):
    json_handler_fixture.top_n = Mock(return_value=[])
    json_handler_fixture.top_n()
    json_handler_fixture.top_n.assert_called_once()


def test_edit_vacancy(vacancy_tested, json_handler_fixture):
    Vacancy.my_vacancies.clear()
    Vacancy.my_vacancies_id.clear()
    json_handler_fixture._JsonHandler__data.append(vacancy_tested.dict_for_json)
    json_handler_fixture._JsonHandler__path_json = "fake_path.json"
    Vacancy.my_vacancies.append(vacancy_tested)
    Vacancy.my_vacancies_id.append(vacancy_tested.id)
    json_handler_fixture.edit_vacancy(vacancy_tested.id, 1, "Новая вакансия")
    updated_dict = next((v for v in json_handler_fixture._JsonHandler__data if v["id"] == vacancy_tested.id), None)
    assert updated_dict is not None
    assert updated_dict["name"] == "Новая вакансия"

    assert Vacancy.my_vacancies[0].name == "Новая вакансия"
