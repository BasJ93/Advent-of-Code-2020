
def findFactorsInList(targetValue, dataList):
    print("value target factor factor3")
    for value in dataList:
        target = targetValue - value
        if target in dataList:
            print(f"Solution 1: {value * target}")
            break

def find3FactorsInList(targetValue, dataList):
    for value in dataList:
        target = targetValue - value
        for factor in dataList:
            if factor != value and factor < target:
                factor3 = target - factor
                if factor3 > 0:
                    if factor3 in dataList:
                        if factor3 != factor:
                            print(f"Solution 2 {value * factor * factor3}")
                            break

input_file = open("Day 1/input.txt", "r")

input_data = set(map(int, input_file.read().split('\n')))

input_file.close()

findFactorsInList(2020, input_data)
find3FactorsInList(2020, input_data)
