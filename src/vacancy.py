import json
import secrets
from .abstract_classes import BaseVacancy


class CreateVacancy(BaseVacancy):

    def __init__(
        self,
        name: str,
        salary: dict,
        description: dict,
    ):
        super().__init__()
        if not salary['salary']['from'] or salary['salary']['from'] <= 0:
            raise ValueError("Зарплата не может быть равна нулю или ниже")

        self.name = name
        self.salary =  salary['salary']['from']
        self.currency = salary["salary"]["currency"]
        self.description = description.get('snippet', {}).get('responsibility', 'Нет описания')
        self.id =  secrets.randbelow(1_000_000)




class AddVacancyToJson:
    def __init__(self, path_json: str, vacancy: CreateVacancy):
        self.path_json = path_json
        self.vacancy = vacancy

    def add_vacancy(self):
        with open(self.path_json, "w", encoding="utf-8") as file:
            pass

class DeleteVacancy:

    def __init__(self, path_json, index):
        self.pathJson = path_json
        self.id = index

    def delete_vacancy(self):
        pass


class ShowVacancies:

    def __init__(self, path_json: str):
        self.pathJson = path_json
        with open(self.pathJson, encoding="utf-8") as file:
            self.dictVacancy = json.load(file)["items"]

    def show(self):

        a = [
            f"название: {vacancy['name']}, описание: {vacancy['snippet']['responsibility']}, зарплата: {f'от {vacancy["salary"]["from"]} {vacancy["salary"]["currency"]}' if vacancy.get('salary') else 'n/a'}"
            for vacancy in self.dictVacancy
        ]

        for i in range(len(a)):
            print(a[i])

