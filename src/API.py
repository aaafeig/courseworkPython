import  requests
import json
from .abstract_classes import Parser


class HH(Parser):

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str):
        self.params['text'] = keyword
        self.params['page'] = 0
        vacancies = []

        while self.params['page'] < 5:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                print(f"Ошибка при запросе: {response.status_code}")
                break

            data = response.json()
            items = data.get('items', [])
            vacancies.extend(items)
            self.params['page'] += 1
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=2)
        print(repr(self))

    def __repr__(self):
        return f"{len(self.vacancies)} вакансий сохранено в файл {self.file_worker}"
