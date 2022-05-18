from calculation.node import *
from calculation.values import Number


class Interpreter:
    def __init__(self, x: float = 0):
        self.x = x

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Divide by Zero Error")

    def visit_VarNode(self, node):
        return Number(self.x)

    def visit_PowNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
