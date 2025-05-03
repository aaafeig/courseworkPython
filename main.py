from src.vacancy import Vacancy

def main():
    name = input('Название вакансии: ')
    user_input_sal = int(input('Введите начальную зарплату: '))
    user_input_cur = input('Введите валюту: ')
    salary = {"salary": {"from": user_input_sal, "currency": user_input_cur}}
    user_input_des = input('Опишите основные свойства вакансии: ')
    description = {"snippet": {"responsibility": user_input_des}}
    new_vacancy = Vacancy(name, salary, description)

    print(new_vacancy.name)
    print(new_vacancy.salary)
    print(new_vacancy.currency)
    print(new_vacancy.description)
    print(new_vacancy.id)

if __name__ == "__main__":
    main()
