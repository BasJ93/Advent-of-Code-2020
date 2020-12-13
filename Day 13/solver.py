import operator
from math import ceil

class AoC():
    def __init__(self):
        self.timestamp = 0
        self.busses = []

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.generateDataset(input_data)

    def generateDataset(self, input_data):
        self.timestamp = int(input_data[0])

        for bus in input_data[1].split(","):
            if bus != "x":
                self.busses.append(int(bus))
            else:
                self.busses.append(0)

    def lcm(self, numbers: [int]) -> int:
        """Only valid for array of prime numbers"""
        result = 1
        for number in numbers:
            result *= number
        return result

    def Task1(self) -> int:
        waitTimes = {}
        for bus in self.busses:
            if bus:
                trips = self.timestamp / bus
                wait = (ceil(trips) * bus) - self.timestamp
                waitTimes[bus] = wait

        sortedTimes = sorted(waitTimes.items(), key=operator.itemgetter(1))

        return sortedTimes[0][0] * sortedTimes[0][1]

    def Task2(self, offset=0) -> int:

        actualBusses = [x for x in enumerate(self.busses) if x[1] != 0]

        t = offset - offset % self.busses[0]
        increment = self.busses[0]

        for i in range(len(actualBusses) - 1):
            while True:
                currentBus = actualBusses[i]
                nextBus = actualBusses[i + 1]
                tCurrentBus = t + currentBus[0]
                tNextBus = t + nextBus[0]
                if (tCurrentBus % currentBus[1]) == 0 and tNextBus % nextBus[1] == 0:
                    increment = self.lcm([x[1] for x in actualBusses[:i+2]])
                    break
                t += increment

        return t

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2(100000000000000)}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 13/input")
