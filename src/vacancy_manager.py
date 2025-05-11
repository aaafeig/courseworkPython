from .utils import Utils
from .vacancy import Vacancy
from .file_manager import FileManager


class VacancyManager:
    def __init__(self, data: list[dict], path_json):
        self.__saver = FileManager.save_json
        self._path_json = path_json
        self._data = data
        self.__get_index = Utils.get_index
        self.__get_my_index = Utils.get_my_index
        self.__validate = Utils.validate_access

    def add_vacancy(self, vacancy: Vacancy):
        Utils.generate_id(self._data, vacancy)
        self._data.append(vacancy.dict_for_json)
        self.__saver(self._path_json, self._data)
        Vacancy.my_vacancies_id.append(vacancy.id)
        Vacancy.my_vacancies.append(vacancy)
        print(f"Вакансия '{vacancy}'")

    def delete_vacancy(self, id_v: str):
        if self.__validate(id_v):
            index = self.__get_my_index(id_v)
            self._data = [v for v in self._data if v["id"] != id_v]
            self.__saver(self._path_json, self._data)
            del Vacancy.my_vacancies[index]
            print(f"Вакансия '{id_v}' была удаленна")
        else:
            print(f"У вас нет доступа к вакансии {id_v}")

    def edit_vacancy(self, id_v: str, edit_choice: int, edit: int or str):
        if self.__validate(id_v):
            index = self.__get_index(self._data, id_v)
            my_index = self.__get_my_index(id_v)
            if index is not None:
                edited_vacancy = self._data[index].copy()
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

                self._data[index] = edited_vacancy
                self.__saver(self._path_json, self._data)
                print("Изменения сохранены")

            else:
                print("Такая вакансия не найдена")
        else:
            print(f"У вас нет доступа к вакансии {id_v}")
