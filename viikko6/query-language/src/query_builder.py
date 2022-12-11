from matchers import All, And, Or, Not, PlaysIn, HasAtLeast, HasFewerThan
from statistics import Statistics

class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def build(self):
        print(self.query)
        return self.query
        