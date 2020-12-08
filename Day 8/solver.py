import copy
from instruction import Instruction

class AoC8():
    def __init__(self):
        self.data = None

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        instructions = []
        for line in input_data:
            parts = line.split(" ")
            instructions.append(Instruction(parts[0], int(parts[1])))

        self.data = instructions

    def runProgram(self, instructions):
        index = 0
        accumulator = 0
        while True:
            if index == len(instructions):
                return (False, accumulator)
            inst = instructions[index]
            if inst.ran:
                return (True, accumulator)
            if inst.operation == "nop":
                inst.ran = True
                index += 1
            if inst.operation == "acc":
                inst.ran = True
                accumulator += inst.argument
                index += 1
            if inst.operation == 'jmp':
                inst.ran = True
                index += inst.argument
        return (False, accumulator)


    def Task1(self) -> int:
        return self.runProgram(copy.deepcopy(self.data))[1]

    def Task2(self) -> int:
        for i in range(0, len(self.data)):
            modified_program = copy.deepcopy(self.data)
            if modified_program[i].operation != "acc":
                if modified_program[i].operation == "jmp":
                    modified_program[i].operation = "nop"
                    result = self.runProgram(modified_program)
                    if not result[0]:
                        return result[1]
                else:
                    modified_program[i].operation = "jmp"
                    result = self.runProgram(modified_program)
                    if not result[0]:
                        return result[1]
        return -1

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC8()
    day.Run("Day 8/input")
