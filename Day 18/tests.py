import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):

    def test_solveEquation(self):
        solver = AoC()
        result = solver.solveEquation("1 + 2 * 3 + 4 * 5 + 6")
        self.assertEqual(71, result)

    def test_solveEquation_with_parentheses(self):
        solver = AoC()
        result = solver.solveEquation("1 + (2 * 3) + (4 * (5 + 6))")
        self.assertEqual(51, result)

    def test_solveEquation_with_parentheses_2(self):
        solver = AoC()
        result = solver.solveEquation("2 * 3 + (4 * 5)")
        self.assertEqual(26, result)

    def test_solveEquation_with_parentheses_3(self):
        solver = AoC()
        result = solver.solveEquation("5 + (8 * 3 + 9 + 3 * 4 * 3)")
        self.assertEqual(437, result)

    def test_solveEquation_with_parentheses_4(self):
        solver = AoC()
        result = solver.solveEquation("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
        self.assertEqual(12240, result)
        
    def test_solveEquation_with_high_complexity(self):
        solver = AoC()
        result = solver.solveEquation("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
        self.assertEqual(13632, result)

    def test_solveEquationAdditionPrecedent(self):
        solver = AoC()
        result = solver.solveEquationAdditionPrecedent("1 + 2 * 3 + 4 * 5 + 6")
        self.assertEqual(231, result)

    def test_solvesolveEquationAdditionPrecedent_with_parentheses(self):
        solver = AoC()
        result = solver.solveEquationAdditionPrecedent("1 + (2 * 3) + (4 * (5 + 6))")
        self.assertEqual(51, result)

    def test_solvesolveEquationAdditionPrecedent_with_parentheses_2(self):
        solver = AoC()
        result = solver.solveEquationAdditionPrecedent("2 * 3 + (4 * 5)")
        self.assertEqual(46, result)

    def test_solvesolveEquationAdditionPrecedent_with_parentheses_3(self):
        solver = AoC()
        result = solver.solveEquationAdditionPrecedent("5 + (8 * 3 + 9 + 3 * 4 * 3)")
        self.assertEqual(1445, result)

    def test_solvesolveEquationAdditionPrecedent_with_parentheses_4(self):
        solver = AoC()
        result = solver.solveEquationAdditionPrecedent("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
        self.assertEqual(669060, result)
        
    def test_solvesolveEquationAdditionPrecedent_with_high_complexity(self):
        solver = AoC()
        result = solver.solveEquationAdditionPrecedent("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
        self.assertEqual(23340, result)

    def test_Task1(self):
        solver = AoC()
        solver.data = ["1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))", "2 * 3 + (4 * 5)"]
        result = solver.Task1()
        self.assertEqual(148, result)

    def test_Task2(self):
        solver = AoC()
        solver.data = ["1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))", "2 * 3 + (4 * 5)"]
        result = solver.Task2()
        self.assertEqual(328, result)

if __name__ == '__main__':
    unittest.main()
