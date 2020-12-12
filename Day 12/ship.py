import copy
import math

class Movement():

    def __init__(self, raw):
        self.Direction = raw[0]
        self.Amount = int(raw[1:])

class Position():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Ship():

    def __init__(self):
        self.position = Position(0, 0)
        self.rotation = 90

    def move(self, action: Movement):
        if action.Direction == "F":
            if self.rotation == 0:
                self.position.y += action.Amount
            if self.rotation == 90:
                self.position.x += action.Amount
            if self.rotation == 180:
                self.position.y -= action.Amount
            if self.rotation == 270:
                self.position.x -= action.Amount
        if action.Direction == "R":
            self.rotation += action.Amount
            self.rotation %= 360
        if action.Direction == "L":
            self.rotation -= action.Amount
            self.rotation %= 360
        if action.Direction == "N":
            self.position.y += action.Amount
        if action.Direction == "E":
            self.position.x += action.Amount
        if action.Direction == "S":
            self.position.y -= action.Amount
        if action.Direction == "W":
            self.position.x -= action.Amount

    def mahattanDistance(self) -> int:
        return abs(self.position.x) + abs(self.position.y)

class Ship2(Ship):
    def __init__(self):
        super(Ship2, self).__init__()
        self.waypoint = Position(10, 1)

    def move(self, action: Movement):
        if action.Direction == "F":
            self.position.x += self.waypoint.x * action.Amount
            self.position.y += self.waypoint.y * action.Amount

        if action.Direction == "R":
            angle = -math.radians(action.Amount)
            old = copy.copy(self.waypoint)
            self.waypoint.x = round(math.cos(angle) * old.x - math.sin(angle) * old.y)
            self.waypoint.y = round(math.sin(angle) * old.x + math.cos(angle) * old.y)
        if action.Direction == "L":
            angle = math.radians(action.Amount)
            old = copy.copy(self.waypoint)
            self.waypoint.x = round(math.cos(angle) * old.x - math.sin(angle) * old.y)
            self.waypoint.y = round(math.sin(angle) * old.x + math.cos(angle) * old.y)
        if action.Direction == "N":
            self.waypoint.y += action.Amount
        if action.Direction == "E":
            self.waypoint.x += action.Amount
        if action.Direction == "S":
            self.waypoint.y -= action.Amount
        if action.Direction == "W":
            self.waypoint.x -= action.Amount
