from src.vacancy import Vacancy, JsonHandler
from src.API import HH

def main():
    data = "data/file_worker.json"
    hh_parser(data)
    handler = JsonHandler(data)
    while True:
        user_choice = int(input("""Выберите действие:
        1. Просмотр анкет
        2. Поиск анкеты
        3. Показать топ N вакансий с зарплатами
        4. Создание анкеты
        5. Удаление анкеты
        6. Закрыть\n"""))

        if user_choice == 1:
            handler.show_vacancy()
        elif user_choice == 2:
            user_search = input("Введите ключевые слова для поиска: ").split()
            handler.search_vacancy(user_search)
        elif user_choice == 3:
            user_number = int(input("Напишите количество вакансий: "))
            handler.top_n(user_number)
        elif user_choice == 4:
            vacancy = create_new_vacancy()
            handler.add_vacancy(vacancy)
        elif user_choice == 5:
            user_delete = input("Укажите id вакансии для удаления: ")
            handler.delete_vacancy(user_delete)
        elif user_choice == 6:
            break
        else:
            print("Введите правильное число")


def create_new_vacancy() -> Vacancy:
    name = input('Название вакансии: ')
    user_input_sal = int(input('Введите начальную зарплату: '))
    user_input_cur = input('Введите валюту: ')
    salary = {"salary": {"from": user_input_sal, "currency": user_input_cur}}
    user_input_des = input('Опишите основные свойства вакансии: ')
    description = {"snippet": {"responsibility": user_input_des}}
    new_vacancy = Vacancy(name, salary, description)
    return new_vacancy


def hh_parser(path_json: str) -> None:
    parser = HH(path_json)
    user_choice = input('Введите название вакансии: ')
    parser.load_vacancies(user_choice)


if __name__ == "__main__":
    main()
