
from game import Player, Combat

class AoC():
    def __init__(self):
        self.data = []

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n\n") if x]

        input_file.close()

        self.data = input_data

    def Task1(self) -> int:
        player1 = Player(self.data[0])
        player2 = Player(self.data[1])

        game = Combat(player1, player2)

        game.play()

        return game.calculateWinner()

    def Task2(self) -> int:
        pass

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 22/input")
