def test_json_handler(json_handler_tested):
    assert json_handler_tested.path_json == "fake_file.json"
    assert json_handler_tested.data == []
