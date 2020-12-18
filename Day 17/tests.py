import unittest

from solver import AoC
from cube import Point, Cube

class SolverUnitTests(unittest.TestCase):

    def test_point_eq(self):
        point1 = Point(1, 2, 3)
        point2 = Point(1, 2, 3)
        self.assertAlmostEqual(point1, point2)

    def test_cube_has_position(self):
        cube = Cube(0, 0, 0, "#")
        point = Point(0, 0, 0)
        self.assertEqual(point, cube.position)

    def test_cube_in_list_has_position(self):
        cube = Cube(0, 0, 0, "#")
        cubes = [cube]
        point = Point(0, 0, 0)
        self.assertEqual(point, cubes[0].position)

    def test_cube_has_active_neighbors(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "."))
        _map.append(Cube(2, 0, 0, "#"))

        _map[1].collectNeighbors(_map)
        self.assertEqual(2, _map[1].activeNeighbors)

    def test_cube_has_active_neighbors_in_2d(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "."))
        _map.append(Cube(2, 0, 0, "#"))
        _map.append(Cube(0, 1, 0, "#"))
        _map.append(Cube(1, 1, 0, "."))
        _map.append(Cube(2, 1, 0, "#"))
        _map.append(Cube(0, 2, 0, "#"))
        _map.append(Cube(1, 2, 0, "."))
        _map.append(Cube(2, 2, 0, "#"))

        _map[4].collectNeighbors(_map)
        self.assertEqual(6, _map[4].activeNeighbors)

    def test_cube_has_active_neighbors_in_3d(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "#"))
        _map.append(Cube(2, 0, 0, "#"))
        _map.append(Cube(0, 1, 0, "#"))
        _map.append(Cube(1, 1, 0, "."))
        _map.append(Cube(2, 1, 0, "#"))
        _map.append(Cube(0, 2, 0, "#"))
        _map.append(Cube(1, 2, 0, "#"))
        _map.append(Cube(2, 2, 0, "#"))

        _map.append(Cube(0, 0, -1, "#"))
        _map.append(Cube(1, 0, -1, "#"))
        _map.append(Cube(2, 0, -1, "#"))
        _map.append(Cube(0, 1, -1, "#"))
        _map.append(Cube(1, 1, -1, "#"))
        _map.append(Cube(2, 1, -1, "#"))
        _map.append(Cube(0, 2, -1, "#"))
        _map.append(Cube(1, 2, -1, "#"))
        _map.append(Cube(2, 2, -1, "#"))

        _map.append(Cube(0, 0, 1, "#"))
        _map.append(Cube(1, 0, 1, "#"))
        _map.append(Cube(2, 0, 1, "#"))
        _map.append(Cube(0, 1, 1, "#"))
        _map.append(Cube(1, 1, 1, "#"))
        _map.append(Cube(2, 1, 1, "#"))
        _map.append(Cube(0, 2, 1, "#"))
        _map.append(Cube(1, 2, 1, "#"))
        _map.append(Cube(2, 2, 1, "#"))

        _map[4].collectNeighbors(_map)
        self.assertEqual(26, _map[4].activeNeighbors)

    def test_cube_determineState_stays_inactive(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "."))
        _map.append(Cube(2, 0, 0, "#"))

        _map[1].collectNeighbors(_map)
        _map[1].determineState()
        self.assertEqual(".", _map[1].state)

    def test_cube_determineState_becomes_active(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "."))
        _map.append(Cube(2, 0, 0, "#"))
        _map.append(Cube(0, 1, 0, "#"))

        _map[1].collectNeighbors(_map)
        _map[1].determineState()
        self.assertEqual("#", _map[1].state)

    def test_cube_determineState_becomes_inactive_not_enough_neighbors(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "#"))
        _map.append(Cube(2, 0, 0, "."))

        _map[1].collectNeighbors(_map)
        _map[1].determineState()
        self.assertEqual(".", _map[1].state)

    def test_cube_determineState_becomes_inactive_to_many_neighbors(self):
        _map = []
        _map.append(Cube(0, 0, 0, "#"))
        _map.append(Cube(1, 0, 0, "."))
        _map.append(Cube(2, 0, 0, "#"))
        _map.append(Cube(0, 1, 0, "#"))
        _map.append(Cube(1, 1, 0, "#"))
        _map.append(Cube(2, 1, 0, "#"))

        _map[1].collectNeighbors(_map)
        _map[1].determineState()
        self.assertEqual(".", _map[1].state)

    def test_Datagenerator(self):
        solver = AoC()
        solver.data = [".#.", "..#", "###"]
        solver.generateData()
        self.assertEqual(27, len(solver.pocket))

    def cube_plus_point_return_cube(self):
        cube = Cube(0, 0, 0, "#")
        point = Point(10, 10, 10)

        result = cube + point

        self.assertIsInstance(result, Cube)
        self.assertEqual(result.position, point)
        self.assertEqual(".", result.state)

    def test_Task1(self):
        solver = AoC()
        solver.data = [".#.", "..#", "###"]
        solver.generateData()
        result = solver.Task1(6)
        self.assertEqual(112, result)

    def test_Task2(self):
        solver = AoC()
        # solver.data = ["class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19", "nearby tickets:\n3,9,18\n15,1,5\n5,14,9"]
        # solver.generateData()
        # result = solver.Task2()

if __name__ == '__main__':
    unittest.main()
