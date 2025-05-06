def test_vacancy(vacancy_tested):
    assert vacancy_tested.name == "Вакансия1"
    assert vacancy_tested.salary == 50000
    assert vacancy_tested.currency == "RUB"
    assert vacancy_tested.description == "Описание вакансии1"
    assert vacancy_tested.id == "-1"


def test_printing_vacancy(vacancy_tested):
    expected = "ID: -1\n" "Название: Вакансия1\n" "Зарплата: 50000 RUB\n" "Описание: Описание вакансии1"
    assert str(vacancy_tested) == expected
