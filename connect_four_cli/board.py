from .mark import Mark


class Board:
    def __init__(self, rows, connected=4):
        self._rows = rows
        self._connected = connected

    def total_cells(self):
        return len(self._rows[0])

    def rows(self):
        return self._rows

    def place(self, index, mark):
        row = self._column(index).count(Mark.EMPTY) - 1
        self._rows[row][index] = mark

    def available_columns(self):
        indices = range(self.total_cells())

        return [index for index in indices if not self._full(index)]

    def win(self):
        indices = range(self.total_cells())
        columns = [''.join(cell.value for cell in self._column(index)) for index in indices]

        fourX = self._connect_four(Mark.CROSS)
        fourO = self._connect_four(Mark.ROUND)

        return any(fourX in column or fourO in column for column in columns)

    def tie(self):
        indices = range(self.total_cells())

        return all(map(self._full, indices))

    def _connect_four(self, mark):
        return ''.join([mark.value] * self._connected)

    def _full(self, index):
        return Mark.EMPTY not in self._column(index)

    def _column(self, index):
        return [row[index] for row in self._rows]
