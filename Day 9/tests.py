import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):
    def test_Task1(self):
        solver = AoC()
        solver.preambleLength = 5
        solver.data = [35, 20, 15, 25, 47, 40, 62, 55,
                       65, 95, 102, 117, 150, 182, 127,
                       219, 299, 277, 309, 576]
        fault = solver.Task1()
        self.assertEqual(127, fault)

    def test_Task2(self):
        solver = AoC()
        solver.preambleLength = 5
        solver.data = [35, 20, 15, 25, 47, 40, 62, 55,
                       65, 95, 102, 117, 150, 182, 127,
                       219, 299, 277, 309, 576]
        result = solver.Task2(127)
        self.assertEqual(62, result)

if __name__ == '__main__':
    unittest.main()
