import unittest

from boardingpass import BoardingPass

class PassportUnitTests(unittest.TestCase):
    def test_calculations_work(self):
        boardingpass = BoardingPass("FBFBBFFRLR")
        self.assertEqual(44, boardingpass.row)
        self.assertEqual(5, boardingpass.column)
        self.assertEqual(357, boardingpass.seatId)

    def test_calculations_work2(self):
        boardingpass = BoardingPass("BFFFBBFRRR")
        self.assertEqual(70, boardingpass.row)
        self.assertEqual(7, boardingpass.column)
        self.assertEqual(567, boardingpass.seatId)

    def test_calculations_work3(self):
        boardingpass = BoardingPass("FFFBBBFRRR")
        self.assertEqual(14, boardingpass.row)
        self.assertEqual(7, boardingpass.column)
        self.assertEqual(119, boardingpass.seatId)

    def test_calculations_work4(self):
        boardingpass = BoardingPass("BBFFBBFRLL")
        self.assertEqual(102, boardingpass.row)
        self.assertEqual(4, boardingpass.column)
        self.assertEqual(820, boardingpass.seatId)

if __name__ == '__main__':
    unittest.main()
