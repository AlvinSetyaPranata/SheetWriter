import re
from json import load
from modules.utils.reader import Reader
from os.path import join, dirname

MONTHS = ("JAN", "FEB", "MAR", "APR", "MEI", "JAN", "JUL", "AGS", "SEP", "OKT", "NOV", "DES")


class AutoSearch:
    def __init__(self, reader_handler):
        """
        :path_to_file should be a file path that represent what is going to search
        :config_path is the path of the configuration file
        """

        self._handler = reader_handler
        self.data_loaded = False
        self.codes = []
        self.names = []
        self.years = {}


        self.load_data()


    def load_data(self):
        if not self._handler.loaded:
            return

        self.codes = self._handler.get_codes()
        self.names = self._handler.get_names()
        self._handler.get_years()
        self.years = self._handler.get_months()
        self.data_loaded = True

    def search_years(self, current_key):
        if not current_key or self.data_loaded == False:
            return []

        res = []

        ex_ = re.compile(f"{current_key}")

        for year in self.years:
            if not ex_.search(year) is None:
                res.append((year, self.years[year]))

        return res


    @classmethod
    def convert_month(self, month_name):
        return MONTHS[int(month_name) - 1]



    def search_months(self, current_key):
        if not current_key or self.data_loaded == False:
            return []

        res = []

        # print(self.years)

        for year in self.years:
            months = [x.value for x in self.years[year]]
            if self.convert_month(current_key) in months:
                res.append(self.years[year])

        return res

    def search_by_code(self, current_key):
        if not current_key or self.data_loaded == False:
            return []

        res = []

        ex_ = re.compile(f"{current_key}+")   


        for i in range(len(self.codes)):
            # res.append(word)
            if ex_.search(str(self.codes[i].value)):
                res.append((self.codes[i], self.names[i]))

        return res

        # return [word.value for word in self.codes if not ex_.search(word) is None or not ex_.search(word) == ""]


