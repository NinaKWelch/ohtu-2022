class Player:
    def __init__(self, name, team, goals, assists ):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        
        
    def __str__(self):
        return (f"{self.name:20} team {self.team:10} goals {str(self.goals):2} assists {str(self.assists):2}")
