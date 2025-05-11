def test_show_vacancy(facade_fixture):
    facade_fixture.show_vacancy()

def test_top_n(facade_fixture):
    facade_fixture.top_n(3)

def test_add_vacancy(facade_fixture, vacancy_tested):
    facade_fixture.add_vacancy(vacancy_tested)

def test_delete_vacancy(facade_fixture):
    facade_fixture.delete_vacancy("123")

def test_edit_vacancy(facade_fixture):
    facade_fixture.edit_vacancy("123", 1, "Новое имя")

def test_search_vacancy(facade_fixture):
    facade_fixture.search_vacancy(["Python", "Django"])
