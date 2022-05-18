from calculation.lexer import Lexer
from calculation.parser_ import Parser
from calculation.interpreter import Interpreter


class evaluation:
    def __init__(self):
        pass

    def calculate(self, expression, x=0):
        try:
            expression = expression.replace('X', 'x')
            l = Lexer(expression)
            tokens = l.generate_tokens()
            parser = Parser(tokens)
            t = parser.parse()
            if t:
                interpreter = Interpreter(x)
                value = interpreter.visit(t).value
                return float(value)

        except Exception as e:
            raise e
