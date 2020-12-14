from collections import defaultdict

class AoC():
    def __init__(self):
        self.data = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = list(map(int, [x for x in input_file.read().split("\n") if x]))

        input_file.close()

        self.data = input_data

    def calculateDeltas(self) -> [int]:
        inOrder = sorted(self.data)
        inOrder = [0] + inOrder + [inOrder[-1] + 3]

        deltas = [int]

        pos = 0
        while pos + 2 < len(inOrder):
            pair = inOrder[pos:pos + 2]
            deltas.append(pair[1] - pair[0])
            pos += 1

        deltas.append(inOrder[-1] - inOrder[-2])

        return deltas

    def Task1(self) -> int:
        deltas = self.calculateDeltas()

        delta1 = deltas.count(1)
        delta3 = deltas.count(3)

        return delta1 * delta3

    def Task2(self) -> int:
        inOrder = sorted(self.data)
        inOrder = [0] + inOrder + [inOrder[-1] + 3]

        paths = defaultdict(int)
        paths[0] = 1

        for adapter in inOrder:
            for diff in range(1, 4):
                next_adapter = adapter + diff
                if next_adapter in inOrder:
                    paths[next_adapter] += paths[adapter]

        return paths[inOrder[-1]]

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 10/input")
