from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self):
        pass


class BaseJsonHandler(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, name_del_vacancy):
        pass

    @abstractmethod
    def top_n(self, n: int):
        pass

    @abstractmethod
    def show_vacancy(self):
        pass


class Parser(ABC):

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
