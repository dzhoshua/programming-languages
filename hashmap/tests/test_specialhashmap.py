import pytest
from specialhashmap import SpecialHashMap


@pytest.fixture()
def data_iloc():
    map = SpecialHashMap()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["1, 5"] = 100
    map["5, 5"] = 200
    map["10, 5"] = 300
    return map

@pytest.fixture()
def data_ploc():
    map = SpecialHashMap()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["(1, 5)"] = 100
    map["(5, 5)"] = 200
    map["(10, 5)"] = 300
    map["(1, 5, 3)"] = 400
    map["(5, 5, 4)"] = 500
    map["(10, 5, 5)"] = 600
    return map


class Test_SpecialHashMap:

    def test_iloc(self, data_iloc):
        assert data_iloc.iloc[0] == 10
        assert data_iloc.iloc[2] == 300
        assert data_iloc.iloc[5] == 200
        assert data_iloc.iloc[8] == 3

    def test_ploc(self, data_ploc):
        assert data_ploc.ploc[">=1"] == "{1=10, 2=20, 3=30}"
        assert data_ploc.ploc["<3"] == "{1=10, 2=20}"
        assert data_ploc.ploc[">0, >0"] == "{(1, 5)=100, (5, 5)=200, (10, 5)=300}"
        assert data_ploc.ploc[">=10, >0"] == "{(10, 5)=300}"
        assert data_ploc.ploc["<5, >=5, >=3"] == "{(1, 5, 3)=400}"

    def test_iloc_invalid_index(self, data_iloc):
        with pytest.raises(ValueError, match="Invalid index"):
            data_iloc.iloc[20]

    def test_iloc_invalid_index_alpha(self, data_iloc):
        with pytest.raises(ValueError, match="Invalid index"):
            data_iloc.iloc["zlata"]
    
    def test_ploc_bad_condition(self, data_ploc):
        with pytest.raises(SyntaxError, match="bad condition"):
            data_ploc.ploc[">0, >z"]
            
    def test_ploc_bad_condition_alpha(self, data_ploc):
        with pytest.raises(SyntaxError, match="bad condition"):
            data_ploc.ploc[">0, z"]

    def test_ploc_invalid_condition(self, data_ploc):
        with pytest.raises(SyntaxError, match="invalid condition"):
            data_ploc.ploc[20]
