import json

from .abstract_classes import BaseVacancy, BaseJsonHandler

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
        salary_from = salary.get("from")
        if salary_from is not None and salary_from < 0:
            raise ValueError("Зарплата не может быть отрицательной")

        self.__id = "-1"
        self.__name = name
        self.__salary = salary["salary"]["from"]
        self.__currency = salary["salary"]["currency"]
        self.__description = description.get("snippet", {}).get(
            "responsibility", "Нет описания"
        )

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def currency(self):
        return self.__currency

    @property
    def description(self):
        return self.__description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def _dict_for_json(self):
        dict_for_json = {
            "id": self.id,
            "name": self.__name,
            "salary": {"from": self.__salary, "currency": self.__currency},
            "snippet": {"responsibility": self.__description},
        }
        return dict_for_json

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Название: {self.name}\n"
            f"Зарплата: {self.salary} {self.currency}\n"
            f"Описание: {self.description}\n"
        )



class JsonHandler(BaseJsonHandler):

    def __init__(self, path_json):
        self.__path_json = path_json
        with open(self.__path_json, "r", encoding="utf-8") as file:
            self.__data = json.load(file)
        super().__init__()

    def add_vacancy(self, vacancy: Vacancy):
        list_id = [int(i.get('id', "0")) for i in self.__data]
        vacancy.id = str(max(list_id) + 1)
        self.__data.append(vacancy._dict_for_json)
        self._save_to_file()
        print(f"Вакансия '{vacancy}'")

    def _save_to_file(self):
        with open(self.__path_json, "w", encoding="utf-8") as file:
            json.dump(self.__data, file, ensure_ascii=False, indent=2)

    def delete_vacancy(self, id_del: str):
        self.__data = [v for v in self.__data if v["id"] != id_del]
        self._save_to_file()
        print(f"Вакансия '{id_del}' была удаленна")

    def show_vacancy(self):
        for vacancy in self.__data:
            print(
                f"ID: {vacancy.get('id', 'N/A')}\n"
                f"Название: {vacancy.get('name', 'N/A')}\n"
                f"Зарплата: {vacancy.get('salary')}\n"
                f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                "----------------------------------------"
            )

    def top_n(self, n: int):
        top_vacancies = sorted(
            [v for v in self.__data if isinstance(v, dict) and isinstance(v.get('salary'), dict)],
            key=lambda x: x['salary'].get('from', 0) or 0,
            reverse=True
        )[:n]

        for vacancy in top_vacancies:
            print(
                f"ID: {vacancy.get('id', 'N/A')}\n"
                f"Название: {vacancy.get('name', 'N/A')}\n"
                f"Зарплата: {vacancy.get('salary')}\n"
                f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                "----------------------------------------"
            )

    def search_vacancy(self, search_words: list):
        for vacancy in self.__data:
            name = vacancy.get("name", "")
            snippet = vacancy.get("snippet", {})
            responsibility = snippet.get("responsibility", 1)


            if any(word.lower() in name or word.lower() in responsibility for word in search_words):
                print(
                    f"ID: {vacancy.get('id', 'N/A')}\n"
                    f"Название: {vacancy.get('name', 'N/A')}\n"
                    f"Зарплата: {vacancy.get('salary')}\n"
                    f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                    "----------------------------------------"
                )


