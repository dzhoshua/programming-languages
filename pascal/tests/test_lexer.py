
import pytest
from interpreter import Lexer, TokenType


@pytest.fixture(scope="function")
def lexer():
    return Lexer()

class TestLexer:

    def test_number(self, lexer):
        lexer.init("66.66")
        token = lexer.next()
        assert token.type_ == TokenType.NUMBER
        assert token.value == "66.66"


    def test_operators(self, lexer):
        lexer.init("+-*/")
        operators = ["+", "-", "*", "/"]
        for op in operators:
            token = lexer.next()
            assert token.type_ == TokenType.OPERATOR
            assert token.value == op


    def test_parens(self, lexer):
        lexer.init(")(")
        token = lexer.next()
        assert token.type_ == TokenType.RPAREN
        assert token.value == ")"
        token = lexer.next()
        assert token.type_ == TokenType.LPAREN
        assert token.value == "("


    def test_assign(self, lexer):
        lexer.init(":=")
        token = lexer.next()
        assert token.type_ == TokenType.ASSIGN
        assert token.value == ":="


    def test_semi(self, lexer):
        lexer.init(";")
        token = lexer.next()
        assert token.type_ == TokenType.SEMI
        assert token.value == ";"

    def test_begin(self, lexer):
        lexer.init("BEGIN")
        token = lexer.next()
        assert token.type_ == TokenType.BEGIN
        assert token.value == "BEGIN"

    def test_end(self, lexer):
        lexer.init("END")
        token = lexer.next()
        assert token.type_ == TokenType.END
        assert token.value == "END"

    def test_dot(self, lexer):
        lexer.init(".")
        token = lexer.next()
        assert token.type_ == TokenType.DOT
        assert token.value == "."


    def test_bad_token(self, lexer):
        with pytest.raises(SyntaxError):
            lexer.init("@$!%")
            lexer.next()