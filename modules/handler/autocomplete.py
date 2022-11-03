import re

MONTHS = ("JAN", "FEB", "MAR", "APR", "MEI", "JAN", "JUL", "AGS", "SEP", "OKT", "NOV", "DES")


class AutoSearch:
    def __init__(self, reader_handler, onAlert):
        """
        :path_to_file should be a file path that represent what is going to search
        :config_path is the path of the configuration file
        """

        self._handler = reader_handler
        self.data_loaded = False
        self.codes = []
        self.names = []
        self.years = {}
        self.onAlert = onAlert

        self.load_data()


    def load_data(self):
        if not self._handler.loaded:
            return

        self.codes = self._handler.get_codes()
        self.names = self._handler.get_names()
        self._handler.get_years()
        self.years = self._handler.get_months()


        if len(self.years) < 3:
            self.onAlert("warning", "tidak bisa memuat data dikarenakan cell dalam file tidak sama dengan konfigurasi, harap ubah konfigurasi cell bulan ke file tersebut!")
            return


        if type(self.years) is str:
            # self.years contain a message from the reader
            self.onAlert("warning", self.years)
            return

        self.data_loaded = True

    def search_years(self, current_key):
        if not current_key or self.data_loaded == False:
            return []

        res = []

        ex_ = re.compile(f"{current_key}")

        for year in self.years:
            try:
                if not ex_.search(year) is None:
                    res.append((year, self.years[year]))

            except:
                self.onAlert("warning", "tidak bisa memuat data dikarenakan cell dalam file tidak sama dengan konfigurasi, harap ubah konfigurasi cell bulan ke file tersebut!")
                return

        return res


    @classmethod
    def convert_month(self, index):

        return MONTHS[int(index) - 1]



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
            if ex_.search(str(self.codes[i].value)):
                res.append((self.codes[i], self.names[i]))

        return res

        # return [word.value for word in self.codes if not ex_.search(word) is None or not ex_.search(word) == ""]

    def find_month_coord(self, year, month):
        if not year in self.years:
            return []


        month = self.convert_month(month)
        ex_ = re.compile(r"\w*" + month)


        return [m for m in self.years[year] if ex_.search(m.value)]



    def find_code_obj(self, code):
        
        ex_ = re.compile(code)

        return [c for c in self.codes if ex_.search(str(c.value))]
