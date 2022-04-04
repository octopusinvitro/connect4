from unittest import TestCase

from connect_four_cli.board import Board
from connect_four_cli.mark import Mark


class TestBoard(TestCase):
    def setUp(self):
        self.rows = [[Mark.EMPTY for _ in range(2)] for _ in range(3)]
        self.board = Board(self.rows)

    def test_knows_total_cells(self):
        self.assertEqual(self.board.total_cells(), 2)

    def test_gets_rows(self):
        expected = [
            [Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY]
        ]
        self.assertEqual(self.board.rows(), expected)

    def test_places_mark_at_the_bottom_if_column_empty(self):
        self.board.place(0, Mark.CROSS)
        expected = [
            [Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY],
            [Mark.CROSS, Mark.EMPTY]
        ]
        self.assertEqual(self.board.rows(), expected)

    def test_places_mark_on_top_of_last_if_column_not_empty(self):
        self.board.place(0, Mark.ROUND)
        self.board.place(0, Mark.CROSS)
        expected = [
            [Mark.EMPTY, Mark.EMPTY],
            [Mark.CROSS, Mark.EMPTY],
            [Mark.ROUND, Mark.EMPTY]
        ]
        self.assertEqual(self.board.rows(), expected)

    def test_detects_available_columns(self):
        rows = [
            [Mark.CROSS, Mark.EMPTY],
            [Mark.CROSS, Mark.EMPTY]
        ]
        self.assertEqual(Board(rows).available_columns(), [1])

    def test_detects_available_columns_when_semi_full(self):
        rows = [
            [Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.ROUND]
        ]
        self.assertEqual(Board(rows).available_columns(), [0, 1])

    def test_detects_no_available_columns_if_none(self):
        rows = [
            [Mark.CROSS, Mark.ROUND],
            [Mark.CROSS, Mark.ROUND]
        ]
        self.assertEqual(Board(rows).available_columns(), [])

    def test_detects_a_tie(self):
        rows = [
            [Mark.CROSS, Mark.CROSS],
            [Mark.ROUND, Mark.ROUND]
        ]
        self.assertTrue(Board(rows).tie())

    def test_detects_a_win_of_cross(self):
        rows = [
            [Mark.CROSS, Mark.EMPTY],
            [Mark.CROSS, Mark.EMPTY]
        ]
        self.assertTrue(Board(rows, connected=2).win())

    def test_detects_a_win_of_round(self):
        rows = [
            [Mark.ROUND, Mark.EMPTY],
            [Mark.ROUND, Mark.EMPTY]
        ]
        self.assertTrue(Board(rows, connected=2).win())
