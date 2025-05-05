from src.vacancy import Vacancy
from src.json_handler import JsonHandler
from src.API import HH

data = "data/file_worker.json"
handler = JsonHandler(data)


def main():
    hh_parser(data)
    user_interaction()


def user_interaction():
    while True:
        user_choice = int(
            input(
                """Выберите действие:
        1. Просмотр вакансий
        2. Поиск вакансий 
        3. Показать топ N вакансий с зарплатами
        4. Мои вакансии
        5. Создание анкеты
        6. Редактирование вакансии
        7. Удаление анкеты
        8. Закрыть\n"""
            )
        )

        if user_choice == 1:
            handler.show_vacancy()
        elif user_choice == 2:
            user_search = input("Введите ключевые слова для поиска: ").split()
            handler.search_vacancy(user_search)
        elif user_choice == 3:
            user_number = int(input("Напишите количество вакансий: "))
            handler.top_n(user_number)
        elif user_choice == 4:
            handler.my_vacancies()
        elif user_choice == 5:
            vacancy = create_new_vacancy()
            handler.add_vacancy(vacancy)
        elif user_choice == 6:
            edit_vacancy()
        elif user_choice == 7:
            user_delete = input("Укажите id вакансии для удаления: ")
            handler.delete_vacancy(user_delete)
        elif user_choice == 8:
            break
        else:
            print("Введите правильное число")


def create_new_vacancy() -> Vacancy:
    name = input("Название вакансии: ")
    user_input_sal = int(input("Введите начальную зарплату: "))
    user_input_cur = input("Введите валюту: ")
    user_input_des = input("Опишите основные свойства вакансии: ")
    new_vacancy = Vacancy(name, user_input_sal, user_input_cur, user_input_des)
    return new_vacancy


def hh_parser(path_json: str) -> None:
    parser = HH(path_json)
    user_choice = input("Введите название вакансии: ")
    parser.load_vacancies(user_choice)


def edit_vacancy():

    user_id = input("Введите id вакансии: ")
    if user_id in Vacancy.my_vacancies_id:
        try:
            user_edit_choice = int(
                input(
                    """Изменить в:
            1. Название вакансии 
            2. Зарплате 
            3. Валюте
            4. Описании\n"""
                )
            )
            user_edit = input("Введите изменения: ")

            if user_edit_choice == 1:
                if not isinstance(user_edit, str):
                    raise ValueError("Название должно быть строкой")
                handler.edit_vacancy(user_id, user_edit_choice, user_edit)
            elif user_edit_choice == 2:
                int(user_edit)
                if not isinstance(int(user_edit), int):
                    raise ValueError("Зарплата должна быть числом")
                handler.edit_vacancy(user_id, user_edit_choice, user_edit)
            elif user_edit_choice == 3:
                if not isinstance(user_edit, str):
                    raise ValueError("Название должно быть строкой")
                handler.edit_vacancy(user_id, user_edit_choice, user_edit)
            elif user_edit_choice == 4:
                if not isinstance(user_edit, str):
                    raise ValueError("Название должно быть строкой")
                handler.edit_vacancy(user_id, user_edit_choice, user_edit)
        except (ValueError, TypeError):
            print("Ошибка ввода")
    else:
        print(f"У вас нет доступа к вакансии {user_id}")


if __name__ == "__main__":
    main()
