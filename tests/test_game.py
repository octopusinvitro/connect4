from io import StringIO
import sys

from unittest import TestCase

from connect_four_cli.board import Board
from connect_four_cli.game import Game
from connect_four_cli.mark import Mark
from connect_four_cli.players.human import Human
from connect_four_cli.ui import UI


class TestGame(TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

        rows = [[Mark.EMPTY, Mark.EMPTY], [Mark.EMPTY, Mark.EMPTY]]
        ui = UI(cells=2)
        self.game = Game(Board(rows, connected=2), ui)
        self.players = [Human(Mark.ROUND, ui), Human(Mark.CROSS, ui)]

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_plays_until_game_over(self):
        sys.stdin = StringIO('1\n2\n1\n')
        self.game.play(self.players)
        self.assertEqual(self.output.getvalue().count(UI.COLUMN_PROMPT), 3)

    def test_breaks_on_win(self):
        sys.stdin = StringIO('1\n2\n1\n')
        self.game.play(self.players)
        self.assertIn('wins!', self.output.getvalue())

    def test_breaks_on_tie(self):
        sys.stdin = StringIO('1\n2\n2\n1\n')
        self.game.play(self.players)
        self.assertIn(UI.TIE, self.output.getvalue())
