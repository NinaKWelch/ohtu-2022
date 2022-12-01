from tennis_game import TennisGame
from player import Player

def main():
    game = TennisGame()
    players = game.assign_players(Player("player1"), Player("player2"))
    print(game.get_players)

    # print(game.get_score())

    # game.won_point("player1")
    # print(game.get_score())

    # game.won_point("player1")
    # print(game.get_score())

    # game.won_point("player2")
    # print(game.get_score())

    # game.won_point("player1")
    # print(game.get_score())

    # game.won_point("player1")
    # print(game.get_score())


if __name__ == "__main__":
    main()
