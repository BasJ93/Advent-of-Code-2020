from collections import defaultdict
from ticket import Rule, Ticket

class AoC():
    def __init__(self):
        self.data = []
        self.rules = [Rule]
        self.nearbyTickets = [Ticket]
        self.myTicket = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n\n") if x]

        input_file.close()

        self.data = input_data

        self.generateData()

    def generateData(self):
        for block in self.data:
            if not "ticket" in block:
                self.rules = [Rule(x) for x in block.split("\n") if x]
            if "nearby" in block:
                self.nearbyTickets = [Ticket(x) for x in block.split("\n") if x and ":" not in x]
            if "your" in block:
                self.myTicket = [Ticket(x) for x in block.split("\n") if x and ":" not in x][0]


    def Task1(self) -> int:
        totalErrorRate = 0
        for ticket in self.nearbyTickets:
            totalErrorRate += ticket.validate(self.rules)
        return totalErrorRate

    def Task2(self) -> int:
        validTickets = [x for x in self.nearbyTickets if not x.validate(self.rules)]

        fieldOptions = defaultdict(list)
        for ticket in validTickets:
            options = ticket.findValidFields(self.rules)
            for option in options.items():
                for i in option[1]:
                    fieldOptions[option[0]].append(i)

        fieldMappings = defaultdict(list)
        for option in fieldOptions.items():
            localMapping = defaultdict(int)
            for i in range(len(validTickets[0].values) + 1):
                localMapping[i] = option[1].count(i)
            highest_likelyhood = max(localMapping.values())
            for mapping in localMapping.items():
                if mapping[1] == highest_likelyhood:
                    fieldMappings[option[0]].append(mapping[0])

        updated = 1
        while updated > 0:
            determined = [x for x in fieldMappings.items() if len(x[1]) == 1]
            updated = 0
            for x in determined:
                for mapping in fieldMappings.items():
                    if len(mapping[1]) > 1:
                        if x[1][0] in mapping[1]:
                            fieldMappings[mapping[0]].remove(x[1][0])
                            updated += 1

        fieldsOfInterrest = [x for x in fieldMappings.items() if x[0].startswith("departure")]
        values = []
        for field in fieldsOfInterrest:
            values.append(self.myTicket.values[field[1][0]])

        result = 1
        for value in values:
            result *= value

        return result

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 16/input")
