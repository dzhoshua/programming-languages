from .token import Token, TokenType

class Interpreter:
    
    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_token = None

    def next(self):
        if self._pos > len(self._text) - 1:
            return Token(TokenType.EOL, "")
        current_char = self._text[self._pos] # достаем из текста символ по позиции
        if current_char.isdigit():
            self._pos += 1
            return Token(TokenType.INTEGER, current_char)
        if current_char == "+":
            self._pos += 1
            return Token(TokenType.PLUS, current_char)
        raise SyntaxError("bad token")
    
    def check_token(self, type_:TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self.next()
        else:
            raise SyntaxError("invalid token order")

    def eval(self, code: str):
        self._text = code
        self._current_token = self.next()
        left = self._current_token
        self.check_token(TokenType.INTEGER)
        op = self._current_token
        self.check_token(TokenType.PLUS)
        right = self._current_token
        self.check_token(TokenType.INTEGER)

        if op.type_ == TokenType.PLUS:
            return int(left.value) + int(right.value)
        
        raise SyntaxError("Interpreter error")