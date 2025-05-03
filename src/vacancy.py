import json
import secrets
from .abstract_classes import BaseVacancy, BaseApi


class Api(BaseApi):

    def __init__(self, api):
        self.api = api
        super().__init__()


class Vacancy(BaseVacancy):

    def __init__(
        self,
        name: str,
        salary: dict,
        description: dict,
        url: str
    ):
        super().__init__()
        if not name:
            raise ValueError("Название вакансии обязательно")
        if salary and salary.get('from') and salary['from'] < 0:
            raise ValueError("Зарплата не может быть отрицательной")

        self.name = name
        self.salary =  salary['salary']['from']
        self.currency = salary["salary"]["currency"]
        self.description = description.get('snippet', {}).get('responsibility', 'Нет описания')
        self.url = url
        self.dictForJson = {
                "title": self.name,
                "salary": self.salary,
                "description": self.description,
                "url": self.url
            }


class JsonSaver:

    def __init__(self, path_json, vacancy: Vacancy):
        self.path_json = path_json
        self.vacancy = vacancy
        with open(self.path_json, 'r', encoding='utf-8') as file:
            self.data = json.load(file)['items']


    def add_vacancy(self):
        self.data.append(self.vacancy)
        self._save_to_file()
        print(f"Вакансия '{self.vacancy.name}' была добавлена")

    def _save_to_file(self):
        with open(self.path_json, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)


    def delete_vacancy(self, del_vacancy):
        self.data = [v for v in self.data if v != del_vacancy]
        self._save_to_file()
        print(f"Вакансия '{self.vacancy.name}' была удаленна")

    def show_vacancy(self):
        for vacancy in self.data:
            print(
                f"ID: {vacancy.get('id', 'N/A')}\n"
                f"Название: {vacancy.get('name', 'N/A')}\n"
                f"Зарплата: {vacancy.get('salary')}\n"
                f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                "----------------------------------------"
            )


    def search_vacancy(self, name):
        for vacancy in self.data:
            if name in vacancy.get("name"):
                print(
                    f"ID: {vacancy.get('id')}\n"
                    f"Название: {vacancy.get('name', 'N/A')}\n"
                    f"Зарплата: {vacancy.get('salary')}\n"
                    f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                    "----------------------------------------"
                )

