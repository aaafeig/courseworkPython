from .utils import Utils


class SearchVacancies:
    def __init__(self, data: list[dict]):
        self._data = data
        self.__printer = Utils.printing_vacancies

    def search_vacancy(self, search_words: list):
        for vacancy in self._data:
            responsibility = vacancy.get("snippet", {}).get("responsibility")
            if responsibility is None:
                continue

            if any(word.lower() in responsibility for word in search_words):
                self.__printer(vacancy)
