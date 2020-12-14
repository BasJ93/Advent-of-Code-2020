import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):

    def test_Task1(self):
        solver = AoC()
        solver.data = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
                       "mem[8] = 11",
                       "mem[7] = 101",
                       "mem[8] = 0"]
        result = solver.Task1()
        self.assertEqual(165, result)

    def test_Task2(self):
        solver = AoC()
        solver.data = ["mask = 000000000000000000000000000000X1001X",
                       "mem[42] = 100",
                       "mask = 00000000000000000000000000000000X0XX",
                       "mem[26] = 1"]
        result = solver.Task2()
        self.assertEqual(208, result)

if __name__ == '__main__':
    unittest.main()
