from .vacancy_manager import VacancyManager
from .showing_vacancies import ShowingVacancies
from .json_handler import JsonHandler
from .search_vacancies import SearchVacancies
from .vacancy import Vacancy


class Facade:
    def __init__(self, json_path="data/file_worker.json"):
        self._json_handler = JsonHandler(path_json=json_path)
        self._showing_vacancies = ShowingVacancies(self._json_handler.data)
        self._vacancy_manager = VacancyManager(self._json_handler.data, self._json_handler.path_json)
        self._search_vacancy = SearchVacancies(self._json_handler.data)

    def show_vacancy(self):
        self._showing_vacancies.show_vacancy()

    def top_n(self, n: int):
        self._showing_vacancies.top_n(n)

    def add_vacancy(self, vacancy: Vacancy):
        self._vacancy_manager.add_vacancy(vacancy)

    def delete_vacancy(self, id_v: str):
        self._vacancy_manager.delete_vacancy(id_v)

    def edit_vacancy(self, id_v: str, edit_choice: int, edit: int or str):
        self._vacancy_manager.edit_vacancy(id_v, edit_choice, edit)

    def search_vacancy(self, key_words: list):
        self._search_vacancy.search_vacancy(key_words)
