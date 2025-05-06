from abc import ABC, abstractmethod

from src.file_manager import FileManager


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self):
        pass


class BaseJsonHandler(ABC):

    def __init__(self, path_json):
        self._path_json = path_json
        self._data = FileManager.load_json(path_json)


class Parser(ABC):

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
