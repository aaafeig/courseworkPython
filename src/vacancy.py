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
    ):
        super().__init__()
        if not name:
            raise ValueError("Название вакансии обязательно")
        if salary and salary.get("from") and salary["from"] < 0:
            raise ValueError("Зарплата не может быть отрицательной")

        self.name = name
        self.salary = salary["salary"]["from"]
        self.currency = salary["salary"]["currency"]
        self.description = description.get("snippet", {}).get(
            "responsibility", "Нет описания"
        )
        self.dictForJson = {
            "name": self.name,
            "salary": {"from": self.salary, "currency": self.currency},
            "snippet": {"responsibility": self.description},
        }


class JsonSaver:

    def __init__(self, path_json):
        self.path_json = path_json
        with open(self.path_json, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def add_vacancy(self, vacancy: Vacancy):
        self.data.append(vacancy.dictForJson)
        self._save_to_file()
        print(f"Вакансия '{vacancy.name}' была добавлена")

    def _save_to_file(self):
        with open(self.path_json, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2)

    def delete_vacancy(self, del_vacancy: str):
        self.data = [v for v in self.data if v["name"] != del_vacancy]
        self._save_to_file()
        print(f"Вакансия '{del_vacancy}' была удаленна")

    def show_vacancy(self):
        for vacancy in self.data:
            print(
                f"ID: {vacancy.get('id', 'N/A')}\n"
                f"Название: {vacancy.get('name', 'N/A')}\n"
                f"Зарплата: {vacancy.get('salary')}\n"
                f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                "----------------------------------------"
            )

    def top_n(self, n: int):
        print(sorted(
            [v for v in self.data if v],
            key=lambda x: (
                x.get('salary', {}).get('from', 0)
                if x and isinstance(x, dict) and isinstance(x.get('salary'), dict)
                else 0
            ),
            reverse=True
        )[:n])

    def search_vacancy_name(self, search_word):
        for vacancy in self.data:
            name = vacancy.get("name", "")
            snippet = vacancy.get("snippet", {})
            responsibility = snippet.get("responsibility", "")


            if (name and search_word.lower() in name.lower()) or \
                    (responsibility and search_word.lower() in responsibility.lower()):
                print(
                    f"ID: {vacancy.get('id', 'N/A')}\n"
                    f"Название: {name}\n"
                    f"Зарплата: {vacancy.get('salary', 'N/A')}\n"
                    f"Описание: {responsibility}\n"
                    "----------------------------------------"
                )


