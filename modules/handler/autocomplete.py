import re

class AutoSearch:
    def __init__(self, data):
        """
        data should be an array that represent what is going to search in?
        """
        self.data = data


    def search(self, current_key):
        if not current_key:
            return []


        ex_ = re.compile(f"{current_key}+")        

        # for word in self.data:
        #     found = ex_.search(word)
        #     print(found)


        return [word for word in self.data if not ex_.search(word) is None]


