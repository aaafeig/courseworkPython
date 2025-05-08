from abc import ABC, abstractmethod

from src.file_manager import FileManager


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self):
        pass


class BaseJsonHandler(ABC):

    def __init__(self, path_json):
        pass

class Parser(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
