from .token import Token

class Node:
    pass

class Number(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number ({self.token})"

class BinOp(Node):
    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp{self.op.value} ({self.left}, {self.right})"
    
class UnaryOp(Node):
    def __init__(self, op: Token, right: Node):
        self.op = op
        self.right = right

    def __str__(self):
        return f"UnaryOp{self.op.value} {self.right}"
    
#-----------------------------------


class Variable(Node):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return f"Variable ({self.token})"

class Empty(Node):
    def __init__(self):
        pass

    def __str__(self):
        return "Empty"

class Assignment(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __str__(self):
        return f"Assignment ({self.left} := {self.right})"

class Semi(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __str__(self):
        return f"Semicolon ({self.left}, {self.right})"

