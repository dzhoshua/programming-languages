
import pytest
from interpreter import Parser, Lexer, Token, TokenType, Number, BinOp, UnaryOp, NodeVisitor, Assignment, Variable, Empty, Semi,  Parser

@pytest.fixture(scope="function")
def parser():
    return Parser()
class TestParser:
   

    def test_invalid_factor(self, parser):
        with pytest.raises(SyntaxError):
            parser._current_token = Token(TokenType.INVALID, "INVALID")
            parser.factor()


    def test_invalid_statement(self, parser):
        with pytest.raises(SyntaxError):
            parser.statement()
   