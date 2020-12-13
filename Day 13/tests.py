import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):

    def test_generateDataset(self):
        solver = AoC()
        input_data = ["939", "7,13,x,x,59,x,31,19"]
        solver.generateDataset(input_data)
        self.assertEqual(939, solver.timestamp)
        self.assertEqual(8, len(solver.busses))

    def test_Task1(self):
        solver = AoC()
        input_data = ["939", "7,13,x,x,59,x,31,19"]
        solver.generateDataset(input_data)
        result = solver.Task1()
        self.assertEqual(295, result)

    def test_Task2(self):
        solver = AoC()
        input_data = ["939", "7,13,x,x,59,x,31,19"]
        solver.generateDataset(input_data)
        result = solver.Task2()
        self.assertEqual(1068781, result)

    def test_Task2_2(self):
        solver = AoC()
        input_data = ["939", "17,x,13,19"]
        solver.generateDataset(input_data)
        result = solver.Task2()
        self.assertEqual(3417, result)

    def test_Task2_3(self):
        solver = AoC()
        input_data = ["939", "67,7,59,61"]
        solver.generateDataset(input_data)
        result = solver.Task2()
        self.assertEqual(754018, result)

    def test_Task2_4(self):
        solver = AoC()
        input_data = ["939", "67,x,7,59,61"]
        solver.generateDataset(input_data)
        result = solver.Task2()
        self.assertEqual(779210, result)

    def test_Task2_5(self):
        solver = AoC()
        input_data = ["939", "67,7,x,59,61"]
        solver.generateDataset(input_data)
        result = solver.Task2()
        self.assertEqual(1261476, result)

    def test_Task2_6(self):
        solver = AoC()
        input_data = ["939", "1789,37,47,1889"]
        solver.generateDataset(input_data)
        result = solver.Task2(offset=1202161400)
        self.assertEqual(1202161486, result)

if __name__ == '__main__':
    unittest.main()
