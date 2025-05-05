from src.vacancy import Vacancy, JsonSaver

def main():
    saver = JsonSaver("data/example.json")
    while True:
        user_choice = int(input("""Выберите действие:
        1. Просмотр анкет
        2. Поиск анкеты
        3. показать топ N вакансий с зарплатами
        4. Создание анкеты
        5. Удаление анкеты
        6. Закрыть\n"""))

        if user_choice == 1:
            saver.show_vacancy()
        elif user_choice == 2:
            user_search = input("Введите название вакансии ")
            saver.search_vacancy_name(user_search)
        elif user_choice == 3:
            user_number = int(input("Напишите количество вакансий: "))
            saver.top_n(user_number)
        elif user_choice == 4:
            vacancy = create_new_vacancy()
            saver.add_vacancy(vacancy)
        elif user_choice == 5:
            user_delete = input("Введите название вакансии для удаления ")
            saver.delete_vacancy(user_delete)
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

if __name__ == "__main__":
    main()
