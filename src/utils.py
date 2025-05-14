from src.vacancy import Vacancy


class Utils:

    @staticmethod
    def printing_vacancies(vacancy_list: dict):
        print(
            f"ID: {vacancy_list.get('id', 'N/A')}\n"
            f"Название: {vacancy_list.get('name', 'N/A')}\n"
            f"Зарплата: {vacancy_list.get('salary')}\n"
            f"Описание: {vacancy_list.get('snippet', {}).get('responsibility', 'N/A')}\n"
            "----------------------------------------"
        )

    @staticmethod
    def generate_id(data: list[dict], vacancy: Vacancy):
        list_id = [int(i.get("id", "0")) for i in data]
        vacancy.id = str(max(list_id, default=0) + 1)

    @staticmethod
    def validate_access(id_v: str) -> bool:
        return id_v in Vacancy.my_vacancies_id

    @staticmethod
    def get_index(data: list[dict], id_v: str) -> int | None:
        return next((i for i, v in enumerate(data) if v["id"] == id_v), None)

    @staticmethod
    def get_my_index(id_v: str) -> int:
        return Vacancy.my_vacancies_id.index(id_v)
