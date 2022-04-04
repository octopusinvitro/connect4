class Game:
    def __init__(self, board, ui):
        self._board = board
        self._ui = ui

    def play(self, players):
        self._ui.display_board(self._board.rows())

        while True:
            players.reverse()
            self._play_turn(players[0])

            if self._board.win():
                self._ui.display_win(players[0].mark)
                break

            if self._board.tie():
                self._ui.display_tie()
                break

    def _play_turn(self, player):
        mark = player.mark

        self._ui.display_turn(mark)
        column = player.play_turn(self._board.available_columns())
        self._board.place(column, mark)

        self._ui.display_board(self._board.rows())
        self._ui.display_move(column, mark)
