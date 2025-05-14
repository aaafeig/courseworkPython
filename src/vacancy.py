from .abstract_classes import BaseVacancy


class Vacancy(BaseVacancy):
    my_vacancies = []
    my_vacancies_id = []

    def __init__(
        self,
        name: str,
        salary: int,
        currency: str,
        description: str,
    ):
        super().__init__()
        if not name:
            raise ValueError("Название вакансии обязательно")
        if salary is not None and salary <= 0:
            raise ValueError("Зарплата не может быть отрицательной")

        self.__id = "-1"
        self.name = name
        self.salary = salary
        self.currency = currency
        self.description = description

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, new_currency):
        self.__currency = new_currency

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def dict_for_json(self):
        dict_for_json = {
            "id": self.id,
            "name": self.__name,
            "salary": {"from": self.__salary, "currency": self.__currency},
            "snippet": {"responsibility": self.__description},
        }
        return dict_for_json

    def __str__(self):
        return f"""ID: {self.id}
Название: {self.name}
Зарплата: {self.salary} {self.currency}
Описание: {self.description}"""
