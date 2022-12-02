class Player:
    def __init__(self, name: str):
        self._name = name
        self._points = 0

    def name(self):
        return self._name

    def points(self):
        return self._points

    def add_point(self):
        self._points += 1