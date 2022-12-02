from player import Player;
from score import Score;

class TennisGame:
    def __init__(self, playerA: Player, playerB: Player, score: Score):
        self._players = [playerA, playerB]
        self._score = score

    def add_point(self, winner: Player):
        # add point to the winning player
        for player in self._players:
            if winner == player:
                player.add_point()
            
        # update the score
        self._score.update(self._players)

    def get_players(self):
        return self._players
    
    def get_score(self):
        # get current score
        return self._score.current()
