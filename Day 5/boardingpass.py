from math import floor


class BoardingPass():
    def __init__(self, seatSpecification: str):
        self.row = self.calculateRow(seatSpecification[:7])
        self.column = self.calculateColumn(seatSpecification[7:])
        self.seatId = self.calculateSeatId()

    def calculateRow(self, rowId) -> int:
        _rows = list(range(0, 128))
        for row in rowId:
            index = floor(len(_rows)/2)
            if row == "F":
                _rows = _rows[:index]
            else:
                _rows = _rows[index:]
        return _rows[0]

    def calculateColumn(self, columnId) -> int:
        _columns = list(range(0, 8))
        for column in columnId:
            index = floor(len(_columns)/2)
            if column == "L":
                _columns = _columns[:index]
            else:
                _columns = _columns[index:]
        return _columns[0]

    def calculateSeatId(self) -> int:
        return self.row * 8 + self.column

    def __repr__(self):
        return f"{self.row} {self.column} {self.seatId}"
