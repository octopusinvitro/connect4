from unittest import TestCase

from connect_four_cli.mark import Mark
from connect_four_cli.players.human import Human

from tests.fake_ui import FakeUI


class TestHuman(TestCase):
    def setUp(self):
        self.human = Human(Mark.CROSS, FakeUI())

    def test_has_mark(self):
        self.assertEqual(self.human.mark, Mark.CROSS)

    def test_plays_turn(self):
        column = self.human.play_turn([0])
        self.assertEqual(column, 0)
