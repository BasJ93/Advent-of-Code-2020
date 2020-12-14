
from mask import Mask

class AoC():
    def __init__(self):
        self.data = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.data = input_data

    def Task1(self) -> int:
        # Value masking
        mem = {}
        mask = ""
        for line in self.data:
            if "mask" in line:
                mask = line.split(" = ")[-1]
            else:
                value = int(line.split(" = ")[-1])
                address = int(line.split("[")[-1].split("]")[0])
                valueBin = str(bin(value))[2:].rjust(len(mask), "0")
                for bit in enumerate(mask):
                    if bit[1] != "X":
                        valueBin = valueBin[:bit[0]] + bit[1] + valueBin[bit[0] + 1:]
                mem[address] = valueBin

        result = 0

        for value in mem.values():
            if int(value, base=2) != 0:
                result += int(value, base=2)

        return result

    def Task2(self) -> int:
        # Address masking
        mem = {}
        mask = None
        for line in self.data:
            if "mask" in line:
                mask = Mask(line.split(" = ")[-1])
                mask.mutate()
            else:
                value = int(line.split(" = ")[-1])
                address = int(line.split("[")[-1].split("]")[0])

                intermediate = mask.apply(address, value)

                mem = {**mem, **intermediate}

        result = 0

        for value in mem.values():
            if value != 0:
                result += value

        return result

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 14/input")
