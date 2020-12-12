class Seat():
    def __init__(self, x: int, y: int, state: str):
        self.position = (x, y)
        self.state = state
        self.occupiedNeighbors = 0

    def getNeighbors(self, _map):
        neighbors = []

        for pos in [(x, y) for x in range(-1, 2) for y in range(-1, 2)]:
            if pos != (0, 0):
                neighbor = [z for z in _map if z.position == (self.position[0] + pos[0], self.position[1] + pos[1])]
                if neighbor:
                    neighbors.append(neighbor[0].state)

        self.occupiedNeighbors = "".join(neighbors).count("#")

    def isOccupied(self) -> bool:
        if self.state == ".":
            return False
        if self.state == "L":
            if self.occupiedNeighbors == 0:
                self.state = "#"
                return True
            return False
        if self.state == "#":
            if self.occupiedNeighbors >= 4:
                self.state = "L"
                return False
            return True

    def __repr__(self):
        return f"{self.position} {self.state}"

    def  __hash__(self):
        return hash(self.position)

class Seat2(Seat):
    def getVisbleSeats(self, _map):
        neighbors = []

        for pos in [(x, y) for x in range(-1, 2) for y in range(-1, 2)]:
            if pos != (0, 0):
                neighbor = [z for z in _map if z.position == (self.position[0] + pos[0], self.position[1] + pos[1])]
                if neighbor:
                    neighbors.append(neighbor[0].state)

        self.occupiedNeighbors = "".join(neighbors).count("#")
