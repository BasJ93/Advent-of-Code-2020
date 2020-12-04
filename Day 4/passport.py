import re

class Passport():
    def __init__(self, byr=None, iyr=None, eyr=None, hgt="", hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

        self.byrRange = (1920, 2002)
        self.iyrRange = (2010, 2020)
        self.eyrRange = (2020, 2030)
        self.validHgt = re.compile("[0-9]{2,3}(cm|in)")
        self.hgtRangeCm = (150, 193)
        self.hgtRangeIn = (59, 76)
        self.validHcl = re.compile("#[0-9a-f]{6}")
        self.eclRange = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        self.validPid = re.compile("^[0-9]{9}$")


    def IsValid(self):
        if (self.byr and self.iyr and self.eyr and
                self.hgt and self.hcl and self.ecl and self.pid):
            return True
        return False


    def isValidHgt(self):
        if not self.validHgt.match(self.hgt):
            return False
        if "cm" in self.hgt:
            _hgt = self.hgt.split("cm")[0]
            if not (self.hgtRangeCm[0] <= int(_hgt) <= self.hgtRangeCm[1]):
                return False
        else:
            _hgt = self.hgt.split("in")[0]
            if not (self.hgtRangeIn[0] <= int(_hgt) <= self.hgtRangeIn[1]):
                return False
        return True

    def isValidByr(self):
        return self.byrRange[0] <= int(self.byr) <= self.byrRange[1]

    def isValidIyr(self):
        return self.iyrRange[0] <= int(self.iyr) <= self.iyrRange[1]

    def isValidEyr(self):
        return self.eyrRange[0] <= int(self.eyr) <= self.eyrRange[1]

    def isValidHcl(self):
        return self.validHcl.match(self.hcl)

    def isValidEcl(self):
        return self.ecl in self.eclRange

    def isValidPid(self):
        return self.validPid.match(self.pid)

    def IsValidWhenStricter(self):
        if not self.IsValid():
            return False
        if not self.isValidByr():
            return False
        if not self.isValidIyr():
            return False
        if not self.isValidEyr():
            return False
        if not self.isValidHgt():
            return False
        if not self.isValidHcl():
            return False
        if not self.isValidEcl():
            return False
        if not self.isValidPid():
            return False
        return True
