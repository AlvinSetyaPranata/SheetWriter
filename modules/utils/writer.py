# from openpyxl.workbook import Workbook
from os import listdir, remove
from openpyxl import load_workbook
from modules.utils.reader import XlsSupport
from os.path import (
    basename, join
)
from xlutils.copy import copy
from xlrd import open_workbook_xls
from openpyxl.styles import Alignment
from xlwt import easyxf



class Writer(XlsSupport):
    def __init__(self, f_target, f_source):
        self.f_target = f_target
        self.f_source = f_source
        self._xls_type = False

        self._wb, self._ws = self.load_file()



    def load_file(self):
        if basename(self.f_source).endswith(".xls"):
            self._xls_type = True

            _wb = copy(open_workbook_xls(self.f_source, formatting_info=True))

            return _wb, _wb.get_sheet(0)


        _wb = load_workbook(self.f_source)

        return _wb, _wb.active


    def modify(self, coord, value):
        """"
        :coord coordinate of the cell that want to be modified

        :value the value for the cell that want to be modified
        """


        if self._xls_type:
            row, col = self.convert_coord_xls(coord, reverse=True)
            self._ws.write(row, col, value, easyxf("align: horiz center"))

            return

        self._ws[coord] = value
        self._ws[coord].alignment = Alignment(horizontal="center", vertical="center")


    @classmethod
    def clean_temp(cls):
        for file in listdir("temp"):
            remove(join("temp", file))


    def save(self):
        self._wb.save(self.f_target)
        self.clean_temp()


    # def __del__(self):
    #     """
    #     Clean all temporary file
    #     """
    #     self.clean_temp()


