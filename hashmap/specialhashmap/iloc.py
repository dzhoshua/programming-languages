
class Iloc(dict):
    
    def __init__(self, _dict: dict):
        self._dict = _dict

    def __getitem__(self, index):
        sorted_keys = sorted(self._dict.keys())
        return self._dict[sorted_keys[index]] 