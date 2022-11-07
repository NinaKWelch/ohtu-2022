import unittest
from statistics import SortBy
from statistics import Statistics
from player import Player
 
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_player_success(self):
        player = self.statistics.search("Kurri")

        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_search_player_fail(self):
        player = self.statistics.search("Nobody")

        self.assertEqual(player, None)

    def test_find_players_by_team_success(self):
        players = self.statistics.team("EDM")

        self.assertEqual(len(players), 3)

    def test_find_players_by_team_fail(self):
        players = self.statistics.team("EEE")

        self.assertEqual(len(players), 0)

    def test_find_top_scorers_success_by_points_with_one_parameter(self):
        players = self.statistics.top(1)

        self.assertEqual(len(players), 2)
        self.assertEqual(str(players[0]), "Gretzky EDM 35 + 89 = 124")

    def test_find_top_scorers_success_by_points_with_two_parameters(self):
        players = self.statistics.top(1, SortBy.POINTS)

        self.assertEqual(str(players[0]), "Gretzky EDM 35 + 89 = 124")

    def test_find_top_scorers_success_by_goals(self):
        players = self.statistics.top(1, SortBy.GOALS)

        self.assertEqual(str(players[0]), "Lemieux PIT 45 + 54 = 99")

    def test_find_top_scorers_success_by_assists(self):
        players = self.statistics.top(1, SortBy.ASSISTS)
       
        self.assertEqual(str(players[0]), "Gretzky EDM 35 + 89 = 124")

    def test_find_top_scorers_fail(self):
        players = self.statistics.top(-1)
        
        self.assertEqual(len(players), 0)