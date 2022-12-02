import unittest
from tennis_game import TennisGame
from player import Player
from score import Score

class TestTennisGame(unittest.TestCase):
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


# test_cases = [
#     (0, 0, "Love-All"),
#     (1, 1, "Fifteen-All"),
#     (2, 2, "Thirty-All"),
#     (3, 3, "Forty-All"),
#     (4, 4, "Deuce"),

#     (1, 0, "Fifteen-Love"),
#     (0, 1, "Love-Fifteen"),
#     (2, 0, "Thirty-Love"),
#     (0, 2, "Love-Thirty"),
#     (3, 0, "Forty-Love"),
#     (0, 3, "Love-Forty"),
#     (4, 0, "Win for player1"),
#     (0, 4, "Win for player2"),

#     (2, 1, "Thirty-Fifteen"),
#     (1, 2, "Fifteen-Thirty"),
#     (3, 1, "Forty-Fifteen"),
#     (1, 3, "Fifteen-Forty"),
#     (4, 1, "Win for player1"),
#     (1, 4, "Win for player2"),

#     (3, 2, "Forty-Thirty"),
#     (2, 3, "Thirty-Forty"),
#     (4, 2, "Win for player1"),
#     (2, 4, "Win for player2"),

#     (4, 3, "Advantage player1"),
#     (3, 4, "Advantage player2"),
#     (5, 4, "Advantage player1"),
#     (4, 5, "Advantage player2"),
#     (15, 14, "Advantage player1"),
#     (14, 15, "Advantage player2"),

#     (6, 4, "Win for player1"),
#     (4, 6, "Win for player2"),
#     (16, 14, "Win for player1"),
#     (14, 16, "Win for player2"),
# ]


# def play_game(p1_points, p2_points):
#     game = TennisGame("player1", "player2")
#     for i in range(max(p1_points, p2_points)):
#         if i < p1_points:
#             game.won_point("player1")
#         if i < p2_points:
#             game.won_point("player2")
#     return game


# class TestTennis(unittest.TestCase):
#     def test_score(self):
#         for test_case in test_cases:
#             (p1_points, p2_points, score) = test_case
#             game = play_game(p1_points, p2_points)
#             self.assertEqual(score, game.get_score())
