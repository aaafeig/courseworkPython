from src.vacancy import Vacancy


class PrintingMyVacancies:

    @staticmethod
    def my_vacancies():
        if len(Vacancy.my_vacancies) != 0:
            for v in Vacancy.my_vacancies:
                print(v)
        else:
            print("У вас еще нет вакансий")
