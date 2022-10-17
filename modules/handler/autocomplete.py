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
        self.years = self._handler.get_years()

    def search_years(self, current_key):
        if not current_key:
            return []

        res = []

        ex_ = re.compile(f"{current_key}")

        for year in self.years:
            if not ex_.search(year) is None:
                res.append((year, self.years[year]))

        return res


    def search_by_code(self, current_key):
        if not current_key:
            return []

        res = []

        ex_ = re.compile(f"{current_key}+")   

        for i in range(len(self.codes)):
            # res.append(word)
            if not ex_.search(self.codes[i].value) is None:
                res.append((self.codes[i], self.names[i]))

        return res

        # return [word.value for word in self.codes if not ex_.search(word) is None or not ex_.search(word) == ""]


