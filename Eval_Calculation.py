class Eval:
    def __init__(self):
        pass

    def calculate(self, expression, x=0):
        expression = expression.replace("^", "**")
        expression = expression.replace("X", "x")

        return eval(expression)