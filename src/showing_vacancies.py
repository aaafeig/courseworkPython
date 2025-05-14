from .file_manager import FileManager
from .utils import Utils


class ShowingVacancies:
    def __init__(self, data: list[dict]):
        self._data = data
        self.__printer = Utils.printing_vacancies

    def show_vacancy(self):
        self._data = FileManager.load_json("data/file_worker.json")
        for vacancy in self._data:
            self.__printer(vacancy)

    def top_n(self, n: int):
        top_vacancies = sorted(
            [v for v in self._data if isinstance(v, dict) and isinstance(v.get("salary"), dict)],
            key=lambda x: x["salary"].get("from", 0) or 0,
            reverse=True,
        )[:n]

        for vacancy in top_vacancies:
            self.__printer(vacancy)
