import unittest

from solver import AoC

class SolverUnitTests(unittest.TestCase):
    def test_two_movement_steps(self):
        solver = AoC()
        solver.data = ["L.LL.LL.LL", "LLLLLLL.LL", "L.L.L..L..", "LLLL.LL.LL",
                       "L.LL.LL.LL", "L.LLLLL.LL", "..L.L.....", "LLLLLLLLLL",
                       "L.LLLLLL.L", "L.LLLLL.LL"]
        _map = solver.generateMap(solver.data)
        solver.simulateMovements(_map)
        self.assertEqual(71, solver.countOccupiedSeats(_map))
        solver.simulateMovements(_map)
        self.assertEqual(20, solver.countOccupiedSeats(_map))

    def test_Task1(self):
        solver = AoC()
        solver.data = ["L.LL.LL.LL", "LLLLLLL.LL", "L.L.L..L..", "LLLL.LL.LL",
                       "L.LL.LL.LL", "L.LLLLL.LL", "..L.L.....", "LLLLLLLLLL",
                       "L.LLLLLL.L", "L.LLLLL.LL"]
        solver.data = solver.generateMap(solver.data)
        self.assertEqual(37, solver.Task1())

if __name__ == '__main__':
    unittest.main()
