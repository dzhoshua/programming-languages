#pip install mypy
import pytest
from interpreter import Interpreter

@pytest.fixture
def interpreter(scope="function"):
    return Interpreter()

class TestInterpreter():
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4

    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")
            interpreter.eval("a+2")

    def test_wrong_operator(self, interpreter):
           with pytest.raises(ValueError):
               interpreter.eval("2&3")

    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2 + 2"), (interpreter, "2 +2 "), (interpreter, " 2+2")]
     )    
    
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4

