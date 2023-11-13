
import pytest
from interpreter import Interpreter, Token, TokenType, Number, BinOp, UnaryOp, NodeVisitor, Empty


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:

    def test_begin_end(self, interpreter):
        assert interpreter.eval("BEGIN END.") == {}

    def test_second_program(self, interpreter):
        assert interpreter.eval("BEGIN x:= 2 + 3 * (2 + 3); y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)); END.") == {'x': 17, 'y': 11}

    def test_three_program(self, interpreter):
        assert interpreter.eval("BEGIN y: = 2; BEGIN a := 3; a := a; b := 10 + a + (10 * y / 4); c := a - b END; x := 11; END.") \
            == {'y': 2, 'a': 3, 'b': 18, 'c': -15, 'x': 11}
        
    def test_unary_op(self, interpreter):
        assert interpreter.eval("BEGIN x:= -2 END.") == {'x':-2}
        assert interpreter.eval("BEGIN x:= +2 END.") == {'x':2}
        
    def test_fail(self,interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("BEGIN x := y; END.")

    def test_invalid_token_order(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("Begin END.")

    def test_bad_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN a = 3 END.")

    

    def test_node_visitor(self):
        assert NodeVisitor().visit() is None

    def test_visit_binop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "&"), Number(Token(TokenType.NUMBER, 3))))

    def test_visit_empty(self, interpreter):
        assert interpreter.visit_empty()==''
        assert interpreter.visit(Empty()) == ''

    def test_visit_unaryop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_unaryop(UnaryOp(Token(TokenType.OPERATOR, "&"), Number(Token(TokenType.NUMBER, 3))))


