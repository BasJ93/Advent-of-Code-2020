from collections import defaultdict

class AoC():
    def __init__(self):
        self.data = []

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.data = input_data

    def Task1(self, nth: int) -> int:
        #Dict of int, list(int), ie spoken number, list of turns
        spoken = defaultdict(list)
        lastValue = 0
        for turn in enumerate(self.data, start=1):
            spoken[turn[1]].append(turn[0])
            lastValue = turn[1]
        for i in range(len(self.data) + 1, nth + 1):
            if spoken[lastValue]:
                times = spoken[lastValue]
                if len(times) > 1:
                    lastValue = times[-1] - times[-2]
                    spoken[lastValue].append(i)
                else:
                    lastValue = 0
                    spoken[lastValue].append(i)

        return lastValue

    def Task2(self) -> int:
        return self.Task1(30000000)

    def Run(self, filename):
        #self.ParseInput(filename)
        self.data = [0, 14, 1, 3, 7, 9]
        print(f"Task1: {self.Task1(2020)}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 15/input")
