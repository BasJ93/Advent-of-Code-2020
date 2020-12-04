import re

from passport import Passport

def ParseInput(filename):
    input_file = open(filename, "r")

    input_data = [x for x in input_file.read().split("\n\n") if x]

    input_file.close()

    input_data = GeneratePassports(input_data)

    return input_data

def GeneratePassports(input_data):
    _passports = []
    pattern = re.compile("([a-z]{3}:[#a-z0-9]+)")
    for line in input_data:
        kvps = pattern.findall(line)
        _passport = Passport()
        for kvp in kvps:
            parts = kvp.split(':')
            setattr(_passport, parts[0], parts[1])
        _passports.append(_passport)
    return _passports


def Task1(input_data):
    validPassports = 0
    for passport in input_data:
        validPassports += passport.IsValid()
    print(f"Task1: Found {len(input_data)} passports with {validPassports} valid")

def Task2(input_data):
    validPassports = 0
    for passport in input_data:
        validPassports += passport.IsValidWhenStricter()
    print(f"Task2: Found {len(input_data)} passports with {validPassports} valid")

if __name__ == "__main__":
    data = ParseInput("Day 4/input")

    Task1(data)
    Task2(data)
