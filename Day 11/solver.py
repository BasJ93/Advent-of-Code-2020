from copy import deepcopy
from seat import Seat, Seat2
import asyncio

class AoC():
    def __init__(self):
        self.data = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.data = self.generateMap(input_data)

    def generateMap(self, _input) -> [Seat]:
        _map = []
        for x, line in enumerate(_input):
            for y, state in enumerate(line):
                seat = Seat(x, y, state)
                if not _map.__contains__(seat):
                    _map.append(seat)
        return _map

    def simulateMovements(self, _map):
        for _seat in _map:
            _seat.getNeighbors(_map)

    def countOccupiedSeats(self, _map) -> int:
        occupied = 0
        for _seat in _map:
            occupied += _seat.isOccupied()

        return occupied

    def Task1(self) -> int:
        lastCount = 0
        iterations = 1
        _map = deepcopy(self.data)
        while True:
            print(f"Interation: {iterations}")
            self.simulateMovements(_map)
            currentCount = self.countOccupiedSeats(_map)
            if lastCount == currentCount:
                return lastCount
            lastCount = currentCount
            iterations += 1

    def Task2(self) -> int:
        pass

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 11/input")
