import json
from os.path import (
    dirname, join
)


class Config:
    def __init__(self, path):
        """
        the filepath should not contain .json
        """
        self.f_name = "".join((path, ".json"))
        self.data = json.load(open(self.f_name, "r"))


    def add_config(self, **conf):
        for key, value in conf.items():
            self.data[key] = value

        json.dump(conf, open(self.f_name, "w"))


    def get_config(self, key):
        if key == "all":
            return self.data

        return self.data[key]


    @staticmethod
    def resolve_parent_path(cur_path, f_target_name, parent_=0):
        """
        :parent is parent of the file
        0 means the current dir
        1 means the upper parent
        2 means the grandparent
        ...
        """

        dir_path = dirname(cur_path)

        if parent_ == 0:
            return dir_path


        for _ in range(parent_):
            dir_path = dirname(dir_path)



        return join(dir_path, f_target_name)

        
