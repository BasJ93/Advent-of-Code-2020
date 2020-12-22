class Player():
    def __init__(self, raw: str):
        parts = [x for x in raw.split("\n") if x]
        self.name = parts[0].strip(":")
        self.cards = list(map(int, parts[1:]))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False

class Combat():
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def playRound(self):
        card1 = self.player1.cards.pop(0)
        card2 = self.player2.cards.pop(0)

        if card1 > card2:
            self.player1.cards += [card1, card2]
        else:
            self.player2.cards += [card2, card1]

    def checkWinner(self):
        if len(self.player1.cards) == 0:
            self.winner = self.player2
        if len(self.player2.cards) == 0:
            self.winner = self.player1

    def calculateWinner(self) -> int:
        score = 0
        multiplier = len(self.winner.cards)
        for card in self.winner.cards:
            score += card * multiplier
            multiplier -= 1
        return score

    def play(self):
        while self.winner is None:
            self.playRound()
            self.checkWinner()
