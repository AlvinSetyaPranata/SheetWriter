# from openpyxl.workbook import Workbook
from os import listdir, remove
from openpyxl import load_workbook
from modules.utils.reader import ABREVIATIONS
from os.path import (
    basename, join
)




class Writer:
    def __init__(self, f_target, f_source):
        self.f_target = f_target
        self.f_source = f_source

        self._wb = self.load_file()
        self._ws = self._wb.active


    def load_file(self):
        if self.f_source.endswith("xls"):
            f_src = open(self.f_source, "rb")
            f_target =  open(join("temp", basename(self.f_source)), "wb")

            f_target.write(f_src.read())

            f_src.close()
            f_target.close()

            return load_workbook(join("temp", basename(self.f_source)))

        return load_workbook(self.f_source)


    def modify(self, coord, value):
        self._ws[coord] = value


    @classmethod
    def clean_temp(cls):
        for file in listdir("temp"):
            remove(join("temp", file))


    def save(self):
        self._wb.save(self.f_target)
        self._wb.close()
        self.clean_temp()


    def __del__(self):
        """
        Clean all temporary file
        """
        self.clean_temp()


