import json
from os.path import isfile

class Config:
    def __init__(self, fname="sheet_config"):
        self.fname = "".join(fname, ".json")

        self.f_obj = json.load(open(self.fname, ""))

    def add_config(self, **conf):
        json.dump(conf, open(self.fname, "w"))


    def get_config(self, key):
        return self.f_obj["config_data"][key]