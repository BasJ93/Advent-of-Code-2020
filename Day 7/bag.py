class Bag():
    def __init__(self, color: str, contents):
        self.Color = color
        self.Contains = contents

    def CanContain(self, color: str):
        return color in [x[1] for x in self.Contains]
