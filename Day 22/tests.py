import unittest

from game import Player, Combat
from solver import AoC

class SolverUnitTests(unittest.TestCase):

    def test_player_init(self):
        player = Player("Player 1:\n9\n2\n6\n3\n1")
        self.assertEqual("Player 1", player.name)
        self.assertEqual(5, len(player.cards))

    def test_player_eq(self):
        player1 = Player("Player 1:\n9\n2\n6\n3\n1")
        player2 = Player("Player 1:\n9")
        self.assertEqual(player1, player2)

    def test_game_playRound(self):
        player1 = Player("Player 1:\n9\n2\n6\n3\n1")
        player2 = Player("Player 2:\n5\n8\n4\n7\n10")
        game = Combat(player1, player2)
        game.playRound()
        self.assertEqual(6, len(game.player1.cards))
        self.assertEqual(4, len(game.player2.cards))
        self.assertEqual(9, game.player1.cards[-2])
        self.assertEqual(5, game.player1.cards[-1])

    def test_game_checkWinner(self):
        player1 = Player("Player 1:\n1")
        player2 = Player("Player 2:\n10")
        game = Combat(player1, player2)
        game.playRound()
        game.checkWinner()
        self.assertEqual(0, len(game.player1.cards))
        self.assertEqual(2, len(game.player2.cards))
        self.assertEqual(player2, game.winner)

    def test_game_play(self):
        player1 = Player("Player 1:\n9\n2\n6\n3\n1")
        player2 = Player("Player 2:\n5\n8\n4\n7\n10")
        game = Combat(player1, player2)
        game.play()
        self.assertEqual(player2, game.winner)

    def test_Task1(self):
        solver = AoC()
        solver.data = ["Player 1:\n9\n2\n6\n3\n1", "Player 2:\n5\n8\n4\n7\n10"]
        result = solver.Task1()
        self.assertEqual(306, result)

    def test_Task2(self):
        solver = AoC()
        # solver.data = [0, 3, 6]
        # result = solver.Task2()
        # self.assertEqual(175594, result)

if __name__ == '__main__':
    unittest.main()
