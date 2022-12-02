from player import Player;

class Score:
    def __init__(self):
        self._score = "Love - All"

    def update(self, players):
        playerA = players[0]
        playerB = players[1]

        if playerA.points() == playerB.points():
            match playerA.points():
                case 0:
                    self._score = "Love - All"
                case 1:
                    self._score = "Fifteen - All"
                case 2:
                    self._score = "Thirty - All"
                case 3:
                    self._score = "Forty - All"
                case 4:
                    self._score = "Deuce"
        elif playerA.points() >= 4 or playerB.points() >= 4:
            point_difference = playerA.points() - playerB.points() 

            if point_difference == 1:
                self._score = f"Advantage {playerA.name()}"
            elif point_difference == -1:
                self._score = f"Advantage {playerB.name()}"
            elif point_difference >= 2:
                self._score = f"Win for {playerA.name()}"
            else:
                self._score = f"Win for {playerB.name()}"
        elif playerA.points() < 4 and playerA.points() < 4:
            def set_point(point):
                match point:
                    case 0:
                        return "Love"
                    case 1:
                        return "Fifteen"
                    case 2:
                        return "Thirty"
                    case 3:
                        return "Forty"

            self._score = f"{set_point(playerA.points())} - {set_point(playerB.points())}"

    def current(self):
        return self._score