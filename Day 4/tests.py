import unittest

from passport import Passport

class PassportUnitTests(unittest.TestCase):
    def test_hgt_cm_valid(self):
        passport = Passport()
        passport.hgt = "190cm"
        self.assertTrue(passport.isValidHgt())

    def test_hgt_in_valid(self):
        passport = Passport()
        passport.hgt = "60in"
        self.assertTrue(passport.isValidHgt())

    def test_hgt_in_invalid(self):
        passport = Passport()
        passport.hgt = "190in"
        self.assertFalse(passport.isValidHgt())

    def test_hgt_invalid(self):
        passport = Passport()
        passport.hgt = "190"
        self.assertFalse(passport.isValidHgt())

    def test_byr_valid(self):
        passport = Passport()
        passport.byr = "2002"
        self.assertTrue(passport.isValidByr())

    def test_byr_invalid_too_high(self):
        passport = Passport()
        passport.byr = "2003"
        self.assertFalse(passport.isValidByr())

    def test_byr_invalid_too_low(self):
        passport = Passport()
        passport.byr = "1919"
        self.assertFalse(passport.isValidByr())

    def test_iyr_valid(self):
        passport = Passport()
        passport.iyr = "2010"
        self.assertTrue(passport.isValidIyr())

    def test_iyr_invalid_too_high(self):
        passport = Passport()
        passport.iyr = "2022"
        self.assertFalse(passport.isValidIyr())

    def test_iyr_invalid_too_low(self):
        passport = Passport()
        passport.iyr = "2009"
        self.assertFalse(passport.isValidIyr())

    def test_eyr_valid(self):
        passport = Passport()
        passport.eyr = "2022"
        self.assertTrue(passport.isValidEyr())

    def test_eyr_invalid_too_high(self):
        passport = Passport()
        passport.eyr = "2032"
        self.assertFalse(passport.isValidEyr())

    def test_eyr_invalid_too_low(self):
        passport = Passport()
        passport.eyr = "2009"
        self.assertFalse(passport.isValidEyr())

    def test_hcl_valid(self):
        passport = Passport()
        passport.hcl = "#123abc"
        self.assertTrue(passport.isValidHcl())

    def test_hcl_invalid_character(self):
        passport = Passport()
        passport.hcl = "#123abz"
        self.assertFalse(passport.isValidHcl())

    def test_eyr_invalid_missing_hashtag(self):
        passport = Passport()
        passport.hcl = "123abc"
        self.assertFalse(passport.isValidHcl())

    def test_ecl_valid(self):
        passport = Passport()
        passport.ecl = "brn"
        self.assertTrue(passport.isValidEcl())

    def test_ecl_invalid(self):
        passport = Passport()
        passport.ecl = "wat"
        self.assertFalse(passport.isValidEcl())

    def test_pid_valid(self):
        passport = Passport()
        passport.pid = "000000001"
        self.assertTrue(passport.isValidPid())

    def test_pid_invalid_too_long(self):
        passport = Passport()
        passport.pid = "0123456789"
        self.assertFalse(passport.isValidPid())

    def test_pid_invalid_too_short(self):
        passport = Passport()
        passport.pid = "03456789"
        self.assertFalse(passport.isValidPid())

    def test_invalid_passport1(self):
        passport = Passport(eyr="1972", cid="100", hcl="#18171d", ecl="amb", hgt="170", pid="186cm", iyr="2018", byr="1926")
        self.assertFalse(passport.IsValidWhenStricter())

    def test_invalid_passport2(self):
        passport = Passport(iyr="2019", hcl="#602927", eyr="1967", hgt="170cm", ecl="grn", pid="012533040", byr="1946")
        self.assertFalse(passport.IsValidWhenStricter())

    def test_invalid_passport3(self):
        passport = Passport(hcl="dab227", iyr="2012", ecl="brn", hgt="182cm", pid="021572410", eyr="2020", byr="1992", cid="277")
        self.assertFalse(passport.IsValidWhenStricter())

    def test_invalid_passport4(self):
        passport = Passport(hgt="59cm", ecl="zzz", eyr="2038", hcl="74454a", iyr="2023", pid="3556412378", byr="2007")
        self.assertFalse(passport.IsValidWhenStricter())

if __name__ == '__main__':
    unittest.main()
