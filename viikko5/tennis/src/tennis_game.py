from player import Player;

class TennisGame:
    def __init__(self):
        self._players = []

    def assign_players(self, playerA: Player, playerB: Player):
        self._players = [playerA, playerB]

    def get_players(self):
        return self._players
    # def won_point(self, name):
    #     if name == self._players[0].name:
    #         self._players[0].add_point()
    #     else:
    #         self._players[1].add_point()

    # def get_score(self):
    #     score = ""
    #     temp_score = 0

    #     if self.m_score1 == self.m_score2:
    #         if self.m_score1 == 0:
    #             score = "Love-All"
    #         elif self.m_score1 == 1:
    #             score = "Fifteen-All"
    #         elif self.m_score1 == 2:
    #             score = "Thirty-All"
    #         elif self.m_score1 == 3:
    #             score = "Forty-All"
    #         else:
    #             score = "Deuce"
    #     elif self.m_score1 >= 4 or self.m_score2 >= 4:
    #         minus_result = self.m_score1 - self. m_score2

    #         if minus_result == 1:
    #             score = "Advantage player1"
    #         elif minus_result == -1:
    #             score = "Advantage player2"
    #         elif minus_result >= 2:
    #             score = "Win for player1"
    #         else:
    #             score = "Win for player2"
    #     else:
    #         for i in range(1, 3):
    #             if i == 1:
    #                 temp_score = self.m_score1
    #             else:
    #                 score = score + "-"
    #                 temp_score = self.m_score2

    #             if temp_score == 0:
    #                 score = score + "Love"
    #             elif temp_score == 1:
    #                 score = score + "Fifteen"
    #             elif temp_score == 2:
    #                 score = score + "Thirty"
    #             elif temp_score == 3:
    #                 score = score + "Forty"

    #     return score
