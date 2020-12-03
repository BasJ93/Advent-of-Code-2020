class Password:
    def __init__(self, minCount, maxCount, char, text):
        self.minCount = int(minCount)
        self.maxCount = int(maxCount)
        self.char = char
        self.text = text

    def checkPasswordCount(self):
        count = self.text.count(self.char)
        if self.minCount <= count and count <= self.maxCount:
            return True
        return False

    def checkPasswordPosition(self):
        matches = 0
        if self.text[self.minCount - 1] == self.char:
            matches += 1
        if self.text[self.maxCount - 1] == self.char:
            matches += 1
        
        if matches == 1:
            return True
        return False

    def __repr__(self):
        return f"{self.text} {self.char} {self.minCount} {self.maxCount}"
