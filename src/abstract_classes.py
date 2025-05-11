from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self):
        pass


class BaseJsonHandler(ABC):

    def __init__(self):
        pass


class Parser(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
