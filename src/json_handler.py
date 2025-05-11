from .file_manager import FileManager
from .abstract_classes import BaseJsonHandler


class JsonHandler(BaseJsonHandler):

    def __init__(self, path_json):
        super().__init__()
        self._path_json = path_json
        self._data = FileManager.load_json(path_json)

    @property
    def data(self) -> list[dict]:
        return self._data

    @property
    def path_json(self):
        return self._path_json

    @path_json.setter
    def path_json(self, new_path):
        self._path_json = new_path
