class BoardingPass():
    def __init__(self, seatSpecification: str):
        self.row = self.calculateRow(seatSpecification[:7])
        self.column = self.calculateColumn(seatSpecification[7:])
        self.seatId = self.calculateSeatId()

    def calculateRow(self, rowId) -> int:
        _bInt = rowId.replace("F", "0").replace("B", "1")
        return int(_bInt, base=2)

    def calculateColumn(self, columnId) -> int:
        _bInt = columnId.replace("L", "0").replace("R", "1")
        return int(_bInt, base=2)

    def calculateSeatId(self) -> int:
        return self.row * 8 + self.column

    def __repr__(self):
        return f"{self.row} {self.column} {self.seatId}"
