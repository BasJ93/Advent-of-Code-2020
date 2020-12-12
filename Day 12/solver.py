from ship import Movement, Ship, Ship2

class AoC():
    def __init__(self):
        self.data = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.generateDirections(input_data)

    def generateDirections(self, data):
        self.data = []
        for line in data:
            self.data.append(Movement(line))

    def Task1(self) -> int:
        ship = Ship()
        for move in self.data:
            ship.move(move)
        return ship.mahattanDistance()

    def Task2(self) -> int:
        ship = Ship2()
        for move in self.data:
            ship.move(move)
        return ship.mahattanDistance()

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 12/input")
