import re
from json import load
from modules.utils.reader import Reader
from os.path import join, dirname


class AutoSearch:
    def __init__(self, reader_handler):
        """
        :path_to_file should be a file path that represent what is going to search
        :config_path is the path of the configuration file
        """

        self._handler = reader_handler

        self.codes = self._handler.get_codes()
        self.names = self._handler.get_names()



    def search_by_code(self, current_key):
        if not current_key:
            return []

        ex_ = re.compile(f"{current_key}+")   


        return [word for word in self.codes if not ex_.search(word) is None]


