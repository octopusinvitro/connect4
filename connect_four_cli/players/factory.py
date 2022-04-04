from ..mark import Mark
from .human import Human
from .random import Random


class Factory:
    def __init__(self, ui):
        self._ui = ui
        self._table = {
            'human_human': ('Human vs Human', self._human_human),
            'human_random': ('Human vs Random', self._human_random),
            'random_human': ('Random vs Human', self._random_human),
            # 'human_robot': ('Human vs robot', self._human_robot),
            # 'robot_human': ('Robot vs Human', self._robot_human)
        }

    def create_players(self):
        option = self._ui.get_option(self._display_names())
        creator = self._creators()[option]

        return creator()

    def _display_names(self):
        return [(key, display) for key, (display, _) in self._table.items()]

    def _creators(self):
        return {key: creator for key, (_, creator) in self._table.items()}

    def _human_human(self):
        return [
            Human(Mark.ROUND, self._ui),
            Human(Mark.CROSS, self._ui)
        ]

    def _human_random(self):
        return [
            Random(Mark.ROUND),
            Human(Mark.CROSS, self._ui)
        ]

    def _random_human(self):
        pair = self._human_random()
        pair.reverse()

        return pair
