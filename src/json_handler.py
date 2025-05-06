import json

from .vacancy import Vacancy
from .abstract_classes import BaseJsonHandler


class JsonHandler(BaseJsonHandler):

    def __init__(self, path_json):
        self.__path_json = path_json
        with open(self.__path_json, "r", encoding="utf-8") as file:
            self.__data = json.load(file)
        super().__init__()

    def add_vacancy(self, vacancy: Vacancy):
        list_id = [int(i.get("id", "0")) for i in self.__data]
        vacancy.id = str(max(list_id, default=0) + 1)
        self.__data.append(vacancy.dict_for_json)
        self._save_to_file()
        Vacancy.my_vacancies_id.append(vacancy.id)
        Vacancy.my_vacancies.append(vacancy)
        print(f"Вакансия '{vacancy}'")

    def _save_to_file(self):
        with open(self.__path_json, "w", encoding="utf-8") as file:
            json.dump(self.__data, file, ensure_ascii=False, indent=2)

    def delete_vacancy(self, id_v: str):
        if id_v in Vacancy.my_vacancies_id:
            index = Vacancy.my_vacancies_id.index(id_v)
            self.__data = [v for v in self.__data if v["id"] != id_v]
            self._save_to_file()
            del Vacancy.my_vacancies[index]
            print(f"Вакансия '{id_v}' была удаленна")
        else:
            print(f"У вас нет доступа к вакансии {id_v}")

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
            [v for v in self.__data if isinstance(v, dict) and isinstance(v.get("salary"), dict)],
            key=lambda x: x["salary"].get("from", 0) or 0,
            reverse=True,
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
            responsibility = vacancy.get("snippet", {}).get("responsibility")
            if responsibility is None:
                continue

            if any(word.lower() in responsibility for word in search_words):
                print(
                    f"ID: {vacancy.get('id', 'N/A')}\n"
                    f"Название: {vacancy.get('name', 'N/A')}\n"
                    f"Зарплата: {vacancy.get('salary')}\n"
                    f"Описание: {vacancy.get('snippet', {}).get('responsibility', 'N/A')}\n"
                    "----------------------------------------"
                )

    @staticmethod
    def my_vacancies():
        if len(Vacancy.my_vacancies) != 0:
            for v in Vacancy.my_vacancies:
                print(v)
        else:
            print("У вас еще нет вакансий")

    def edit_vacancy(self, id_v: str, edit_choice: int, edit: int or str):
        if id_v in Vacancy.my_vacancies_id:
            index = next((i for i, v in enumerate(self.__data) if v["id"] == id_v), None)
            my_index = Vacancy.my_vacancies_id.index(id_v)
            if index is not None:
                edited_vacancy = self.__data[index].copy()
                if edit_choice == 1:
                    edited_vacancy["name"] = edit
                    Vacancy.my_vacancies[my_index].name = edit
                elif edit_choice == 2:
                    edited_vacancy["salary"]["from"] = edit
                    Vacancy.my_vacancies[my_index].salary = edit
                elif edit_choice == 3:
                    edited_vacancy["salary"]["currency"] = edit
                    Vacancy.my_vacancies[my_index].currency = edit
                elif edit_choice == 4:
                    edited_vacancy["snippet"]["responsibility"] = edit
                    Vacancy.my_vacancies[my_index].description = edit
                else:
                    print("Выберите корректное действие")

                self.__data[index] = edited_vacancy
                self._save_to_file()
                print("Изменения сохранены")

            else:
                print("Такая вакансия не найдена")
        else:
            print(f"У вас нет доступа к вакансии {id_v}")
