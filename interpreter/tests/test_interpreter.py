#pip install mypy
import pytest
from interpreter import Interpreter, Token, TokenType, Number, BinOp, UnaryOp, NodeVisitor


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
    
    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0
    
    def test_mul(self, interpreter):
        assert interpreter.eval("5*5") == 25

    def test_div(self, interpreter):
        assert interpreter.eval("25/5") == 5
    
    def test_float(self, interpreter):
        assert interpreter.eval("5.5+5.5") == 11

    def test_unary_op_plus(self, interpreter):
        assert interpreter.eval("+++2") == 2
    
    def test_unary_minus(self, interpreter):
        assert interpreter.eval("-2") == -2
    
    def test_expr(self, interpreter):
        assert interpreter.eval("2-2/2+2*2") == 5

    def test_expr_break(self, interpreter):
        assert interpreter.eval("2+3*2/2") == 8

    def test_unary_expr(self, interpreter):
        assert interpreter.eval("+2-2-2") == -2
        
    def test_priority(self, interpreter):
        assert interpreter.eval("2+2*2") == 6

    def test_parentheses(self, interpreter):
        assert interpreter.eval("(2+2)*2") == 8

    def test_parentheses_error(self, interpreter):
        with pytest.raises(SyntaxError):
            assert interpreter.eval("(2+2")

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")


    def test_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+()")

    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2+     2"),
                                  (interpreter, "2 +2 "),
                                  (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4

    def test_node_visitor(self):
        assert NodeVisitor().visit() is None

    def test_visit_binop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "&"), Number(Token(TokenType.NUMBER, 3))))

    def test_visit_unaryop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_unaryop(UnaryOp(Token(TokenType.OPERATOR, "&"), Number(Token(TokenType.NUMBER, 3))))

class TestAst:

    def test_str(self):
        num = Number("2")
        assert num.__str__()=='Number (2)'

    def test_binop_str(self):
        binop = BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "+"), Number (Token(TokenType.NUMBER, 2)))
        assert binop.__str__() == "BinOp+ (Number (Token(TokenType.NUMBER, 2)), Number (Token(TokenType.NUMBER, 2)))"

    def test_unop_str(self):
        unaryop = UnaryOp(Token(TokenType.OPERATOR, "-"), Number(Token(TokenType.NUMBER, 2)))
        assert unaryop.__str__() == "UnaryOp- Number (Token(TokenType.NUMBER, 2))"


