import re
from bag import Bag

class AoC7():
    def __init__(self):
        self.bagRegex = re.compile("(^[a-z ]+) bags contain")
        self.contentRegex = re.compile("([0-9]{1}) ([a-z ]+) bags?")
        self.data = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        data = self.generateBags(input_data)

        return data

    def generateBags(self, input_data):
        bags = []
        for line in input_data:
            color = self.bagRegex.match(line).group(1).strip()
            contents = self.contentRegex.findall(line)
            bag = Bag(color, contents)
            bags.append(bag)
        return bags

    def Task1(self, color) -> int:
        canContain = []
        # Find all the bags that can contain the color directly
        for bag in self.data:
            if bag.CanContain(color):
                canContain.append(bag)
        # Find all the bags tha can contian the color indectly
        for indirect in canContain:
            for bag in self.data:
                if bag.CanContain(indirect.Color):
                    if not bag in canContain:
                        canContain.append(bag)
        return len(canContain)

    def CalculateChildBags(self, bag: Bag) -> int:
        count = 0
        for child in bag.Contains:
            childBag = self.GetBagByColor(child[1])
            if childBag:
                children = self.CalculateChildBags(childBag)
                if children:
                    count += int(child[0]) * children
                else:
                    count += int(child[0])
            else:
                count += 1
        return count + 1

    def GetBagByColor(self, color: str):
        return next((x for x in self.data if x.Color == color), None)

    def Task2(self, color: str) -> int:
        bag = self.GetBagByColor(color)
        return self.CalculateChildBags(bag) - 1

    def Run(self, filename):
        self.data = self.ParseInput(filename)
        print(f"Task1: {self.Task1('shiny gold')}")
        print(f"Task2: {self.Task2('shiny gold')}")

if __name__ == "__main__":
    day = AoC7()
    day.Run("Day 7/input")
