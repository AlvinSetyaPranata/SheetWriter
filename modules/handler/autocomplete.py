
class AutoSearch:
    def __init__(self, data):
        """
        data should be an array that represent what is going to search in?
        """
        self.data = data


    def search(self, current_key):
        return [word for word in self.data if current_key in word]
        


