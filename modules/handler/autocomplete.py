import re
from json import load
from modules.utils.reader import Reader
from os.path import join


class AutoSearch:
    def __init__(self, path_to_file, config_path=join(__file__, "default_config.json")):
        """
        :path_to_file should be a file path that represent what is going to search
        :config_path is the path of the configuration file
        """
        self._path = path_to_file
        self._config_path = config_path

        self.codes = []

        self.configs = load(open(self._config_path, "r"))

        self._handler = Reader(self._path, self.configs)




    def search(self, keyword, current_key):
        if not current_key:
            return []
        


        ex_ = re.compile(f"{current_key}+")        

        # for word in self.data:
        #     found = ex_.search(word)
        #     print(found)


        return [word for word in self.data if not ex_.search(word) is None]


