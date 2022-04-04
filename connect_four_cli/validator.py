from .error_code import ErrorCode


class Validator:
    def __init__(self, cells, available_values):
        self._cells = cells
        self._available_values = available_values

    def validate(self, column):
        self._column = column

        if not self._digit():
            return ErrorCode.NOTADIGIT

        self._column = int(self._column) - 1

        if not self._inrange():
            return ErrorCode.NOTINRANGE

        if not self._available():
            return ErrorCode.NOTAVAILABLE

        return ErrorCode.NONE

    def _digit(self):
        return self._column.isdigit()

    def _inrange(self):
        return (0 <= self._column) and (self._column < self._cells)

    def _available(self):
        return self._column in self._available_values
