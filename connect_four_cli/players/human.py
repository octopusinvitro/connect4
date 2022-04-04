class Human:
    def __init__(self, mark, ui):
        self.mark = mark
        self._ui = ui

    def play_turn(self, available_columns):
        return self._ui.get_column(available_columns)
