import unittest
from calculation.evaluation import evaluation
from Eval_Calculation import Eval


class TestEvaluation(unittest.TestCase):
    def __init__(self):
        self.Eval = evaluation()

    def xTest(self):
        self.assertEqual(self.Eval.calculate("(x+2)*3", 2), 12)

    def parenthesesTest(self):
        self.assertEqual(self.Eval.calculate("(2+2)*3"), 12)

    def powerTest(self):
        self.assertEqual(self.Eval.calculate("10^2"), 100)

    def orderTest(self):
        self.assertEqual(self.Eval.calculate("2+2*3"), 8)

    def divisionTest(self):
        self.assertEqual(self.Eval.calculate("2/x", 2), 1)

    def multiplicationTest(self):
        self.assertEqual(self.Eval.calculate("2*x", 2), 4)

    def expressionEvaluation(self):
        self.assertEqual(self.Eval.calculate("x-"), ValueError)
        self.assertEqual(self.Eval.calculate("sds"), ValueError)


class TestEval(unittest.TestCase):
    def __init__(self):
        self.e = Eval()

    def xTest(self):
        self.assertEqual(self.e.calculate("(x+2)*3", 2), 12)

    def parenthesesTest(self):
        self.assertEqual(self.e.calculate("(2+2)*3"), 12)

    def powerTest(self):
        self.assertEqual(self.e.calculate("10^2"), 100)

    def orderTest(self):
        self.assertEqual(self.e.calculate("2+2*3"), 8)

    def divisionTest(self):
        self.assertEqual(self.e.calculate("2/x", 2), 1)

    def multiplicationTest(self):
        self.assertEqual(self.e.calculate("2*x", 2), 4)

    def expressionEvaluation(self):
        self.assertEqual(self.e.calculate("x-"), ValueError)
        self.assertEqual(self.e.calculate("sds"), ValueError)


if __name__ == "__main__":
    testOb1 = TestEvaluation()
    testOb2 = TestEval()
