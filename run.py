from connect_four_cli.board import Board
from connect_four_cli.game import Game
from connect_four_cli.mark import Mark
from connect_four_cli.players.factory import Factory
from connect_four_cli.ui import UI


def main():
    total_columns = 7
    total_rows = 8
    rows = [[Mark.EMPTY for _ in range(total_columns)] for _ in range(total_rows)]
    board = Board(rows)

    ui = UI(total_columns)
    factory = Factory(ui)
    game = Game(board, ui)

    ui.display_intro()
    players = factory.create_players()
    game.play(players)


main()
