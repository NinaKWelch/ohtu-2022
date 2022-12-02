from tennis_game import TennisGame
from player import Player
from score import Score
def main():
    playerA = Player("player1")
    playerB = Player("player2")
    score = Score()
    game = TennisGame(playerA, playerB, score)
    
    print(game.get_score())
    game.add_point(playerA)
    print(game.get_score())
    game.add_point(playerA)
    game.add_point(playerA)
    game.add_point(playerB)
    print(game.get_score())
    game.add_point(playerA)
    print(game.get_score())
    

if __name__ == "__main__":
    main()
