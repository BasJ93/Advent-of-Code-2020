import unittest

from solver import AoC6

class PassportUnitTests(unittest.TestCase):
    def test_Task1_works(self):
        solver = AoC6()
        data = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
        self.assertEqual(11, solver.Task1(data))

    def test_Task2_works(self):
        solver = AoC6()
        data = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
        self.assertEqual(6, solver.Task2(data))

if __name__ == '__main__':
    unittest.main()
