from .parser import Parser
from .ast import Number, BinOp, UnaryOp, Assignment, Variable, Empty, Semi

class NodeVisitor:
    
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self.parser = Parser()
        self.vars_and_values = {}

    def visit(self, node): 
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, UnaryOp):
            return self.visit_unaryop(node)
        elif isinstance(node, Assignment):
            return self.visit_assignment(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif isinstance(node, Empty):
            return self.visit_empty()
        elif isinstance(node, Semi):
            return self.visit_semi(node)

    def visit_number(self, node):
        return float(node.token.value)
    
    def visit_binop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case _:
                raise ValueError("Invalid operator")
            
    def visit_unaryop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.right)
            case "-":
                return -self.visit(node.right)
            case _:
                raise ValueError("Invalid operator")
            
    
    def visit_variable(self, node):
        var = node.token.value
        if var in self.vars_and_values.keys():
            return self.vars_and_values[var]
        raise ValueError(f"Unknown variable {var}")

    def visit_assignment(self, node):
        var = node.left.value
        value = self.visit(node.right)
        self.vars_and_values[var] = value

    def visit_empty(self):
        return ''

    def visit_semi(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def eval(self, code):
        tree = self.parser.parse(code)
        self.visit(tree)
        return self.vars_and_values
