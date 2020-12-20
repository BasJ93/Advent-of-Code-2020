
class AoC():
    def __init__(self):
        self.data = []

    def ParseInput(self, filename):
        input_file = open(filename, "r")

        input_data = [x for x in input_file.read().split("\n") if x]

        input_file.close()

        self.data = input_data

    def solveEquation(self, equation: str) -> int:
        result = 0
        tokens = equation.split()
        i = 0
        while i < len(tokens):
            if tokens[i] != "+" and tokens[i] != "*" and "(" not in tokens[i] and ")" not in tokens[i]:
                if i - 1 >= 0:
                    if tokens[i - 1] == "+":
                        result += int(tokens[i])
                    else:
                        result *= int(tokens[i])
                else:
                    result += int(tokens[i])
            else:
                if "(" in tokens[i]:
                    closing = i
                    _equation = "".join(tokens[i])
                    while _equation.count("(") != _equation.count(")"):
                        _equation = " ".join(tokens[i:closing + 1])
                        closing += 1

                    _equation = _equation[1:-1]
                    if i - 1 >= 0:
                        if tokens[i - 1] == "+":
                            result += self.solveEquation(_equation)
                        else:
                            result *= self.solveEquation(_equation)
                    else:
                        result += self.solveEquation(_equation)
                    i = closing
            i += 1
        return result

    def solveEquationAdditionPrecedent(self, equation: str) -> int:
        # Addition now has precedent over multiplication
        result = 1
        tokens = equation.split()
        i = 0

        replaced_equition = []
        # find all + in the equation, check if they can be solved, and rebuild the equation
        # once done, parse the entire equation

        additions = [x[0] for x in enumerate(tokens) if x[1] == "+"]

        while i < len(tokens):
            if i + 1 in additions:
                if "(" not in tokens[i] and ")" not in tokens[i] and "(" not in tokens[i + 2] and ")" not in tokens[i + 2]:
                    temp = int(tokens[i]) + int(tokens[i + 2])
                    replaced_equition.append(str(temp))
                    i += 3
                else:
                    replaced_equition.append(tokens[i])
                    i += 1
            else:
                replaced_equition.append(tokens[i])
                i += 1

        solved_sub_equations = []
        i = 0
        while i < len(replaced_equition):
            if "(" in replaced_equition[i]:
                closing = i
                _equation = "".join(replaced_equition[i])
                while _equation.count("(") != _equation.count(")"):
                    _equation = " ".join(replaced_equition[i:closing + 1])
                    closing += 1

                _equation = _equation[1:-1]
                solved_sub_equations.append(str(self.solveEquationAdditionPrecedent(_equation)))
                i = closing
            else:
                solved_sub_equations.append(replaced_equition[i])
                i += 1

        if "+" not in solved_sub_equations:
            for token in solved_sub_equations:
                if token != "*":
                    result *= int(token)
        else:
            result = self.solveEquationAdditionPrecedent(" ".join(solved_sub_equations))

        return result

    def Task1(self) -> int:
        result = 0
        for line in self.data:
            result += self.solveEquation(line)

        return result

    def Task2(self) -> int:
        result = 0
        for line in self.data:
            result += self.solveEquationAdditionPrecedent(line)

        return result

    def Run(self, filename):
        self.ParseInput(filename)
        print(f"Task1: {self.Task1()}")
        print(f"Task2: {self.Task2()}")

if __name__ == "__main__":
    day = AoC()
    day.Run("Day 18/input")
