import unittest

from instruction import Instruction
from solver import AoC8

class SolverUnitTests(unittest.TestCase):
    def test_Task1(self):
        solver = AoC8()
        solver.data = [Instruction("nop", 0), Instruction("acc", 1), Instruction("jmp", 4),
                       Instruction("acc", 3), Instruction("jmp", -3), Instruction("acc", -99),
                       Instruction("acc", 1), Instruction("jmp", -4), Instruction("acc", 6)]
        count = solver.Task1()
        self.assertEqual(5, count)

    def test_Task2(self):
        solver = AoC8()
        solver.data = [Instruction("nop", 0), Instruction("acc", 1), Instruction("jmp", 4),
                       Instruction("acc", 3), Instruction("jmp", -3), Instruction("acc", -99),
                       Instruction("acc", 1), Instruction("jmp", -4), Instruction("acc", 6)]
        count = solver.Task2()
        self.assertEqual(8, count)

if __name__ == '__main__':
    unittest.main()
