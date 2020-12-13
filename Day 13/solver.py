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
        firstBus = self.busses[0]
        lastBus = self.busses[-1]
        deltaT = len(self.busses) - 1
        uniqueBusses = set(self.busses)
        if 0 in uniqueBusses:
            uniqueBusses.remove(0)
        nrOfBusses = len(uniqueBusses)

        t = offset - offset % self.busses[0]
        increment = self.busses[0]

        while True:
            if (t % firstBus) == 0 and (t + deltaT) % lastBus == 0:
                correct = 0
                for i, bus in enumerate(self.busses):
                    if bus != 0:
                        if ((t + i) % bus) == 0:
                            correct += 1

                if correct == nrOfBusses:
                    return t
            t += increment

        return -1

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2(100000000000000)}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 13/input")
