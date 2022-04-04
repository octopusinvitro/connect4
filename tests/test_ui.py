from io import StringIO
import sys

from unittest import TestCase

from connect_four_cli.error_code import ErrorCode
from connect_four_cli.mark import Mark
from connect_four_cli.ui import UI


class TestUI(TestCase):
    TOTAL_COLUMNS = 7
    AVAILABLE_COLUMNS = [0]

    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output
        self.ui = UI(self.TOTAL_COLUMNS)

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_displays_player_options(self):
        sys.stdin = StringIO('1\n')
        options = [('human_human', 'Human vs Human'), ('human_robot', 'Human vs Robot')]
        self.ui.get_option(options)
        self.assertIn('1) Human vs Human', self.output.getvalue())
        self.assertIn('2) Human vs Robot', self.output.getvalue())

    def test_displays_prompt_to_ask_for_player_options(self):
        sys.stdin = StringIO('1\n')
        options = [('human_human', 'Human vs Human'), ('human_robot', 'Human vs Robot')]
        self.ui.get_option(options)
        self.assertIn(UI.OPTION_PROMPT, self.output.getvalue())

    def test_gets_option_as_a_key(self):
        sys.stdin = StringIO('1\n')
        options = [('human_human', 'Human vs Human'), ('human_robot', 'Human vs Robot')]
        self.assertEqual(self.ui.get_option(options), 'human_human')

    def test_displays_board_header(self):
        rows = [
            [Mark.EMPTY, Mark.ROUND],
            [Mark.CROSS, Mark.EMPTY]
        ]
        UI(2).display_board(rows)
        self.assertIn('\n  1   2 \n', self.output.getvalue())

    def test_displays_horizontal_lines(self):
        rows = [[Mark.EMPTY, Mark.ROUND, Mark.CROSS]]
        UI(3).display_board(rows)
        self.assertIn('\n+---+---+---+\n', self.output.getvalue())

    def test_displays_marks_with_padding(self):
        rows = [[Mark.EMPTY, Mark.ROUND, Mark.CROSS]]
        UI(3).display_board(rows)
        value = '\n|   |   |   |\n|   | o | x |\n|   |   |   |\n'
        self.assertIn(value, self.output.getvalue())

    def test_displays_last_horizontal_line(self):
        rows = [[Mark.CROSS]]
        UI(1).display_board(rows)
        value = '\n  1 \n+---+\n|   |\n| x |\n|   |\n+---+\n'
        self.assertIn(value, self.output.getvalue())

    def test_displays_turn(self):
        mark = Mark.ROUND
        self.ui.display_turn(mark)
        self.assertIn(mark.value, self.output.getvalue())

    def test_displays_prompt_to_ask_for_column(self):
        sys.stdin = StringIO('1\n')
        self.ui.get_column(self.AVAILABLE_COLUMNS)
        self.assertIn(UI.COLUMN_PROMPT, self.output.getvalue())

    def test_gets_column_as_integer(self):
        sys.stdin = StringIO('1\n')
        column = self.ui.get_column(self.AVAILABLE_COLUMNS)
        self.assertEqual(column, 0)

    def test_reports_column_not_a_digit(self):
        sys.stdin = StringIO('hello\n1\n')
        self.ui.get_column(self.AVAILABLE_COLUMNS)
        self.assertIn(UI.ERRORS[ErrorCode.NOTADIGIT.value], self.output.getvalue())

    def test_reports_column_below_lower_limit(self):
        sys.stdin = StringIO('0\n1\n')
        self.ui.get_column(self.AVAILABLE_COLUMNS)
        self.assertIn(UI.ERRORS[ErrorCode.NOTINRANGE.value], self.output.getvalue())

    def test_reports_column_beyond_upper_limit(self):
        sys.stdin = StringIO(f'{self.TOTAL_COLUMNS + 1}\n1\n')
        self.ui.get_column(self.AVAILABLE_COLUMNS)
        self.assertIn(UI.ERRORS[ErrorCode.NOTINRANGE.value], self.output.getvalue())

    def test_reports_full_column(self):
        sys.stdin = StringIO('2\n1\n')
        self.ui.get_column(self.AVAILABLE_COLUMNS)
        self.assertIn(UI.ERRORS[ErrorCode.NOTAVAILABLE.value], self.output.getvalue())

    def test_displays_available_columns_separated_by_comma(self):
        sys.stdin = StringIO('2\n3\n')
        self.ui.get_column([0, 2])
        error_message = f'{UI.ERRORS[ErrorCode.NOTAVAILABLE.value]} 1, 3'
        self.assertIn(error_message, self.output.getvalue())

    def test_displays_last_move(self):
        self.ui.display_move(3, Mark.CROSS)
        self.assertIn('Placed x in column 3', self.output.getvalue())

    def test_displays_tie(self):
        self.ui.display_tie()
        self.assertIn(UI.TIE, self.output.getvalue())

    def test_displays_win(self):
        self.ui.display_win(Mark.CROSS)
        self.assertIn(Mark.CROSS.value, self.output.getvalue())
