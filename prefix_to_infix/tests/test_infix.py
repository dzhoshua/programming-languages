import pytest
from prefix_to_infix import to_infix

@pytest.mark.parametrize(
        "prefix, infix", 
        [("+ - 13 4 55", "((13 - 4) + 55)"),
         ("+ 2 * 2 - 2 1", "(2 + (2 * (2 - 1)))"),
         ("+ + 10 20 30", "((10 + 20) + 30)"),
         ("/ + 3 10 * + 2 3 - 3 5", "((3 + 10) / ((2 + 3) * (3 - 5)))")]
    )
def test_to_infix(prefix, infix):
    assert to_infix(prefix) == infix

def test_to_infix_errors():
    with pytest.raises(ValueError):
        to_infix("- - 1 2")
    with pytest.raises(ValueError):
        to_infix("")
    with pytest.raises(TypeError):
        to_infix("hello++")
    with pytest.raises(TypeError):
        to_infix("+ 2 * 2-2 1")