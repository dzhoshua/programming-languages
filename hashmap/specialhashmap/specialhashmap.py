from .iloc import Iloc
from .ploc import Ploc

class SpecialHashMap(dict):
    
    def __init__(self, _dict=None):
        if _dict is None:
            _dict = {}
        super().__init__(_dict)
        self.iloc = Iloc(self)
        self.ploc = Ploc(self)