class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError(other)


class Cube():
    def __init__(self, x, y, z, initial_state):
        self.position = Point(x, y, z)
        self.state = initial_state
        self.activeNeighbors = 0

    def collectNeighbors(self, pocket):
        neighbors = []
        neigbor_coordinates = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]
        for pos in neigbor_coordinates:
            if pos != (0, 0, 0):
                position = Point(self.position.x + pos[0], self.position.y + pos[1], self.position.z + pos[2])
                neighbor = [a for a in pocket if a.position == position]
                if neighbor:
                    neighbors.append(neighbor[0].state)
                else:
                    neighbors.append(".")

        self.activeNeighbors = "".join(neighbors).count("#")

    def determineState(self):
        if self.state == "#":
            if self.activeNeighbors == 2 or self.activeNeighbors == 3:
                self.state = "#"
            else:
                self.state = "."
        else:
            if self.activeNeighbors == 3:
                self.state = "#"
            else:
                self.state = "."

    def __repr__(self):
        return f"{self.state}"

    def __add__(self, other):
        if isinstance(other, Point):
            cube = Cube(self.position.x, self.position.y, self.position.z, ".")
            cube.position += other
            return cube
        raise TypeError(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.position == other.position
        return False
