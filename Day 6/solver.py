
class AoC6():
    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n\n") if x]

        input_file.close()

        groups = []

        for line in input_data:
            group = [x for x in line.split("\n") if x]
            groups.append(group)

        return groups

    def Task1(self, input_data) -> int:
        count = 0
        for group in input_data:
            _group = "".join(group)
            count += len(set(_group))
        return count

    def Task2(self, input_data) -> int:
        count = 0
        for group in input_data:
            _group = "".join(group)
            _uniques = set(_group)
            for answer in _uniques:
                if _group.count(answer) == len(group):
                    count += 1
        return count

    def Run(self):
        data = self.ParseInput("Day 6/input")

        print(f"Task 1: {self.Task1(data)}")
        print(f"Task 2: {self.Task2(data)}")


if __name__ == "__main__":
    day = AoC6()
    day.Run()
