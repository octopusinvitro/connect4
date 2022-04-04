from unittest import TestCase

from connect_four_cli.mark import Mark
from connect_four_cli.players.random import Random


class TestRandom(TestCase):
    def setUp(self):
        self.random = Random(Mark.CROSS)

    def test_has_mark(self):
        self.assertEqual(self.random.mark, Mark.CROSS)

    def test_plays_turn(self):
        column = self.random.play_turn([0])
        self.assertEqual(column, 0)
