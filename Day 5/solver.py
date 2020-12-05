from boardingpass import BoardingPass


def ParseInput(filename):
    input_file = open(filename, "r")

    input_data = [x for x in input_file.read().split("\n") if x]

    input_file.close()

    input_data = GenerateBoardingpasses(input_data)

    return input_data

def GenerateBoardingpasses(data):
    boardingpasses = []

    for line in data:
        boardingpasses.append(BoardingPass(line))

    return boardingpasses

def sortKey(e):
    return e.seatId

def Task1(input_data):
    input_data.sort(reverse=True, key=sortKey)

    print(f"Task 1: Highest seat id: {input_data[0].seatId}")

def Task2(input_data):
    input_data.sort(reverse=False, key=sortKey)

    existingSeats = list(range(input_data[0].seatId, input_data[-1].seatId + 1))

    existingBoardingpasses = [x.seatId for x in input_data]

    for seat in existingSeats:
        if not seat in existingBoardingpasses:
            print(f"Task 2: missing boardingpass {seat}")

if __name__ == "__main__":
    data = ParseInput("Day 5/input")

    Task1(data)
    Task2(data)
