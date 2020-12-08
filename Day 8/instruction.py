class Instruction():
    def __init__(self, operation: str, argument: int):
        self.operation = operation
        self.argument = argument
        self.ran = False

    def __repr__(self):
        return f"{self.operation} {self.argument} {self.ran}"
