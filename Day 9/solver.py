
class AoC():
    def __init__(self):
        self.data = None
        self.preambleLength = 25

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = list(map(int, [x for x in input_file.read().split("\n") if x]))

        input_file.close()

        self.data = input_data

    def Task1(self) -> int:
        pos = 0
        while pos + self.preambleLength < len(self.data):
            solutions = 0
            window = self.data[pos:pos + self.preambleLength + 1]

            target = window[-1]
            values = window[:-1]
            for value in values:
                for value2 in values:
                    if value + value2 == target:
                        solutions += 1

            if not solutions:
                return target

            pos += 1

    def Task2(self, target) -> int:
        pos = 0
        size = 2
        while True:
            window = self.data[pos:pos + size]

            if target == sum(window):
                return min(window) + max(window)

            pos += 1

            if target in window:
                pos = 0
                size += 1

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2(self.Task1())}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 9/input")
