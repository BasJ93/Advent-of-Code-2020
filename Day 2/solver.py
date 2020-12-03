from password import Password

def parseInput(data):
    passwords = []
    for line in data:
        text = line.split(": ")[1]
        char = line.split(": ")[0].split(" ")[1]
        minCount, maxCount = line.split(": ")[0].split(" ")[0].split("-")
        passwords.append(Password(minCount, maxCount, char, text))

    return passwords

input_file = open("Day 2/input", "r")

input_data = input_file.read().split('\n')

input_file.close()

passwordList = parseInput(input_data)

valid = 0

for pw in passwordList:
    if pw.checkPasswordCount():
        valid += 1

print(f"Number of valid passwords for policy 1: {valid}")


valid = 0

for pw in passwordList:
    if pw.checkPasswordPosition():
        valid += 1

print(f"Number of valid passwords for policy 2: {valid}")
