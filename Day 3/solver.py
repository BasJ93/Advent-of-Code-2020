
def ParseInput(filename):
    input_file = open(filename, "r")

    input_data = [x for x in input_file.read().split('\n') if x]

    input_file.close()

    return input_data

def CountTrees(slope_x, slope_y, terrain, show=False):
    _trees = 0

    line_width = len(terrain[0])

    for i, row in enumerate(range(0, len(terrain), slope_y)):
        index = (i * slope_x) % line_width
        if terrain[row][index] == "#":
            _trees += 1
            if show:
                print(terrain[row][:index] + "X" + terrain[row][index + 1:])
        else:
            if show:
                print(terrain[row][:index] + "O" + terrain[row][index + 1:])

    return _trees


def Task1(input_data):
    trees = CountTrees(3, 1, input_data)
    print(f"Encountered {trees} trees for task 1")

def Task2(input_data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees = 1
    for slope in slopes:
        subtrees = CountTrees(slope[0], slope[1], input_data)
        trees *= subtrees

    print(f"Encountered {trees} trees for task 2")

data = ParseInput("Day 3/input")
Task1(data)
Task2(data)
