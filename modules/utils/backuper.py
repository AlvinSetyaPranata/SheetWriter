# from datetime import datetime
from os import remove
from csv import writer, reader

class Backuper:
    def __init__(self, max_counter):
        self.fname = "backup.csv"
        self.max_counter = max_counter
        self.f_handler = open(self.fname, "w")
        self.handler = writer(self.f_handler)
        self.counter = 0
        self._temp_data = []


    def listen(self, data):
        if self.counter < self.max_counter:
            self.counter += 1
            self._temp_data.append(data)
            return

        self.handler.writerows(self._temp_data)
        self.counter = 0


    def close(self):
        self.f_handler.close()
        remove(self.fname)



class Loader:
    def __init__(self):
        self.f_handler = None
        self.fname =  None


    def load(self, fname):
        self.f_handler = open(fname, "r")
        self.fname = fname
        return reader([self.f_handler])


    def close(self):
        self.f_handler.close()
        remove(self.fname)