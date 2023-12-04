
class Iloc(dict):
    
    def __init__(self, _dict: dict):
        self._dict = _dict

    def __getitem__(self, index):
        if not isinstance(index, int) or index > len(self._dict) or index < 0:
            raise ValueError("Invalid index")
        sorted_keys = sorted(self._dict.keys())
        return self._dict[sorted_keys[index]] 