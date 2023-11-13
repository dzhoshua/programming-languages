
import pytest
from interpreter import Token, TokenType, Number, BinOp, UnaryOp, Assignment, Variable, Empty, Semi


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

    def test_variable_str(self):
        var = Variable(Token(TokenType.ID, "a"))
        assert var.__str__() == "Variable (Token(TokenType.ID, a))"

    def test_assignment_str(self):
        assign = Assignment(Variable(Token(TokenType.ID, "a")), Token(TokenType.NUMBER, "3"))
        assert assign.__str__() == "Assignment (Variable (Token(TokenType.ID, a)) := Token(TokenType.NUMBER, 3))"
    
    def test_empty_str(self):
        assert Empty().__str__() == "Empty"

    def test_semicolon_str(self):
        semi = Semi(Token(TokenType.NUMBER, "1"), Variable(Token(TokenType.ID, "a")))
        assert semi.__str__() == "Semicolon (Token(TokenType.NUMBER, 1), Variable (Token(TokenType.ID, a)))"


