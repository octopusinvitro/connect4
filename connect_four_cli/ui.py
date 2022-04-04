from .error_code import ErrorCode
from .validator import Validator


class UI:
    INTRO = 'C O N N E C T   F O U R'
    OPTION_PROMPT = 'Please select an option: '
    COLUMN_PROMPT = 'Please select a column: '
    ERRORS = {
        ErrorCode.NOTADIGIT.value: 'Please enter a number, available values:',
        ErrorCode.NOTINRANGE.value: 'Index out of range, available values:',
        ErrorCode.NOTAVAILABLE.value: 'Column is full, available values:'
    }
    LINE = '+---------------------+'
    TIE = "|   It's a tie!       |"

    def __init__(self, cells):
        self._cells = cells

    def display_intro(self):
        self._wrap(self.INTRO)
        print()

    def get_option(self, options):
        for index, (key, display) in enumerate(options):
            print(f'  {index + 1}) {display}')
        print()

        available_values = range(len(options))
        validator = Validator(len(options), available_values)
        option = self._get_valid_value(validator, available_values, self.OPTION_PROMPT)
        key, _ = options[int(option) - 1]

        return key

    def display_board(self, rows):
        self._display_header()

        for row in rows:
            self._display_horizontal_line()
            self._display_content(row)

        self._display_horizontal_line()

    def display_turn(self, mark):
        self._wrap(f'|   CURRENT TURN: {mark.value}   |')

    def get_column(self, available_columns):
        validator = Validator(self._cells, available_columns)
        column = self._get_valid_value(validator, available_columns, self.COLUMN_PROMPT)

        return int(column) - 1

    def display_move(self, column, mark):
        print(f'Placed {mark.value} in column {column}')

    def display_tie(self):
        self._wrap(self.TIE)

    def display_win(self, mark):
        self._wrap(f'|   {mark.value} wins!           |')

    def _display_header(self):
        print('\n' + ''.join(f'  {number + 1} ' for number in range(self._cells)))

    def _display_horizontal_line(self):
        line = ['+---'] * self._cells + ['+']

        print(''.join(line))

    def _display_content(self, row):
        padding = ''.join('|   ' for _ in row)
        content = ''.join(f'| {cell.value} ' for cell in row)

        print(padding + '|')
        print(content + '|')
        print(padding + '|')

    def _get_valid_value(self, validator, available_values, prompt):
        formatted_values = self._formatted_values(available_values)

        value = input(prompt)
        error = validator.validate(value)
        while (error is not ErrorCode.NONE):
            value = input(f'{self.ERRORS[error.value]} {formatted_values}: ')
            error = validator.validate(value)

        return value

    def _formatted_values(self, available_values):
        available_values = [index + 1 for index in available_values]
        formatted_values = ', '.join(map(str, available_values))

        return formatted_values

    def _wrap(self, message):
        print()
        print(self.LINE)
        print(message)
        print(self.LINE)
