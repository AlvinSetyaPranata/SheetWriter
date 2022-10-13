from openpyxl import load_workbook


class Writer:
    def __init__(self):
        self.w_book = load_workbook
        self.cur_sheet = None
        self.loaded = False

    def load(self, fname):
        self.fname = fname          
        self.w_book = self.w_book(self.fname)
        self.cur_sheet = self.w_book.active
        self.loaded = True



    def modify(self, coord, value=""):
        self.cur_sheet[coord] = value


    # def create_sheet(self, *sheet_names):
    #     for x in range(sheet_names):
    #         self.cur_sheet.create_sheet(sheet_names)


    def _save(self, name):
        self.w_book.save(name)

    @property
    def close_file(self):
        self.w_book.close()
