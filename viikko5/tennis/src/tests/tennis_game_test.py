import unittest
from tennis_game import TennisGame
from player import Player
from score import Score


class TestTennis(unittest.TestCase):
    def setUp(self):
        self.playerA = Player("PlayerA")
        self.playerB = Player("PlayerA")
        self.score = Score()
        self.game = TennisGame(self.playerA, self.playerB, self.score)

    def test_game_has_an_initial_score(self):
        self.assertEqual(self.game.get_score(), "Love - All")

    def test_game_has_two_players_with_name_and_points(self):
        players = self.game.get_players()

        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name(), "PlayerA")
        self.assertEqual(players[0].points(), 0)
        