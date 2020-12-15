import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):

    def test_Task1(self):
        solver = AoC()
        solver.data = [0, 3, 6]
        result = solver.Task1(2020)
        self.assertEqual(436, result)

        solver.data = [1, 3, 2]
        result = solver.Task1(2020)
        self.assertEqual(1, result)

        solver.data = [2, 1, 3]
        result = solver.Task1(2020)
        self.assertEqual(10, result)

        solver.data = [1, 2, 3]
        result = solver.Task1(2020)
        self.assertEqual(27, result)

        solver.data = [2, 3, 1]
        result = solver.Task1(2020)
        self.assertEqual(78, result)

        solver.data = [3, 2, 1]
        result = solver.Task1(2020)
        self.assertEqual(438, result)

        solver.data = [3, 1, 2]
        result = solver.Task1(2020)
        self.assertEqual(1836, result)

    def test_Task2(self):
        solver = AoC()
        solver.data = [0, 3, 6]
        result = solver.Task2()
        self.assertEqual(175594, result)

    def test_Task2_2(self):
        solver = AoC()
        solver.data = [1, 3, 2]
        result = solver.Task2()
        self.assertEqual(2578, result)

    def test_Task2_3(self):
        solver = AoC()
        solver.data = [2, 1, 3]
        result = solver.Task2()
        self.assertEqual(3544142, result)

    def test_Task2_4(self):
        solver = AoC()
        solver.data = [1, 2, 3]
        result = solver.Task2()
        self.assertEqual(261214, result)

    def test_Task2_5(self):
        solver = AoC()
        solver.data = [2, 3, 1]
        result = solver.Task2()
        self.assertEqual(6895259, result)

    def test_Task2_6(self):
        solver = AoC()
        solver.data = [3, 2, 1]
        result = solver.Task2()
        self.assertEqual(18, result)

    def test_Task2_7(self):
        solver = AoC()
        solver.data = [3, 1, 2]
        result = solver.Task2()
        self.assertEqual(362, result)

if __name__ == '__main__':
    unittest.main()
