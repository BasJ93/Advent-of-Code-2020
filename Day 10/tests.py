import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):
    def test_Task1_1(self):
        solver = AoC()
        solver.data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        result = solver.Task1()
        self.assertEqual(35, result)

    def test_Task1_2(self):
        solver = AoC()
        solver.data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
                       24, 23, 49, 45, 19, 38, 39, 11, 1, 32,
                       25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        result = solver.Task1()
        self.assertEqual(220, result)

    def test_Task2_1(self):
        solver = AoC()
        solver.data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        result = solver.Task2()
        self.assertEqual(8, result)

    def test_Task2_2(self):
        solver = AoC()
        solver.data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
                       24, 23, 49, 45, 19, 38, 39, 11, 1, 32,
                       25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        result = solver.Task2()
        self.assertEqual(19208, result)

if __name__ == '__main__':
    unittest.main()
