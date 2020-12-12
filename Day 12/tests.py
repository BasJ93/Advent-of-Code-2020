import unittest

from solver import AoC
from ship import Movement, Ship, Ship2

class SolverUnitTests(unittest.TestCase):
    def test_movement_generation(self):
        move = Movement("F10")
        self.assertEqual(move.Direction, "F")
        self.assertEqual(move.Amount, 10)

    def test_ship_movement(self):
        move = Movement("F10")
        ship = Ship()
        ship.move(move)
        self.assertEqual(ship.position.x, 10)
        self.assertEqual(ship.position.y, 0)
        self.assertEqual(ship.rotation, 90)

    def test_ship_rotation(self):
        move = Movement("R270")
        ship = Ship()
        ship.move(move)
        self.assertEqual(ship.rotation, 0)

    def test_Task1(self):
        solver = AoC()
        solver.generateDirections(["F10", "N3", "F7", "R90", "F11"])
        result = solver.Task1()
        self.assertEqual(25, result)

    def test_ship2_rotation(self):
        move = Movement("R360")
        ship = Ship2()
        ship.waypoint.y = 4
        ship.move(move)
        self.assertEqual(ship.waypoint.x, 10)
        self.assertEqual(ship.waypoint.y, 4)
        move = Movement("L90")
        ship.move(move)
        self.assertEqual(ship.waypoint.x, -4)
        self.assertEqual(ship.waypoint.y, 10)
        move = Movement("R90")
        ship.move(move)
        self.assertEqual(ship.waypoint.x, 10)
        self.assertEqual(ship.waypoint.y, 4)

    def test_ship2_movement(self):
        move = Movement("F10")
        ship = Ship2()
        ship.move(move)
        self.assertEqual(ship.position.x, 100)
        self.assertEqual(ship.position.y, 10)

    def test_Task2(self):
        solver = AoC()
        solver.generateDirections(["F10", "N3", "F7", "R90", "F11"])
        result = solver.Task2()
        self.assertEqual(286, result)

if __name__ == '__main__':
    unittest.main()
