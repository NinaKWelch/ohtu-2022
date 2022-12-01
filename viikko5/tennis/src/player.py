class Player:
    def __init__(self, name: str):
        self._name = name
        self._points = 0

    def player_name(self):
        return self._name

    def add_point(self):
        self._points += 1

    def points(self):
        return self._points
