import requests
import json
from .abstract_classes import Parser


class HH(Parser):

    def __init__(self, file_worker):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        self.file_worker = file_worker
        super().__init__()

    def _get_response(self, keyword: str):
        self.params["text"] = keyword
        self.params["page"] = 0
        self.vacancies = []

        while self.params["page"] < 5:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                print(f"Ошибка при запросе: {response.status_code}")
                break

            data = response.json()
            items = data.get("items", [])
            self.vacancies.extend(items)
            self.params["page"] += 1

    def load_vacancies(self, keyword: str):
        self._get_response(keyword)
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=2)
