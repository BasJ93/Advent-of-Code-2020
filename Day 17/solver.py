from copy import deepcopy
from time import time

from cube import Cube, Point


class AoC():
    def __init__(self):
        self.data = []
        self.pocket = []

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.data = input_data

        self.generateData()

    def generateData(self):
        for line in enumerate(self.data):
            for point in enumerate(line[1]):
                self.pocket.append(Cube(point[0], line[0], 0, point[1]))
        
        last_cube = self.pocket[-1]

        for a in [(x, y, z) for x in range(last_cube.position.x + 1) for y in range(last_cube.position.y + 1) for z in range(-1, 2)]:
            if a[2] != 0:
                self.pocket.append(Cube(a[0], a[1], a[2], "."))

    def Task1(self, steps) -> int:
        for cycle in range(steps):
            pocket = deepcopy(self.pocket)
            for a in [Point(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]:
                for cube in pocket:
                    _cube = cube + a
                    if _cube not in self.pocket:
                        self.pocket.append(_cube)

            for cube in self.pocket:
                cube.collectNeighbors(self.pocket)
            for cube in self.pocket:
                cube.determineState()
        
        active = 0
        for cube in self.pocket:
            if cube.state == "#":
                active += 1
        
        return active

    def Task2(self) -> int:
        pass

    def Run(self, filename):
        self.ParseInput(filename)
        start_time = time()
        print(f"Task1: {self.Task1(6)}")
        print(f"Calculation took: {time() - start_time} seconds")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 17/input")
