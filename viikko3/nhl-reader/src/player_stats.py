def sort_by_points(player):
    return player.points

class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, player_nationality):
        players_by_nationality = filter(
            lambda player: player.nationality == player_nationality,
            self._players
        )

        sorted_players = sorted(
            players_by_nationality,
            reverse=True,
            key=sort_by_points
        )

        return sorted_players
