from unittest import TestCase

from connect_four_cli.mark import Mark


class TestMark(TestCase):
    def test_switches_cross_for_round(self):
        self.assertEqual(Mark.switch(Mark.CROSS), Mark.ROUND)

    def test_switches_round_for_cross(self):
        self.assertEqual(Mark.switch(Mark.ROUND), Mark.CROSS)

    def test_does_nothing_if_empty_mark(self):
        self.assertEqual(Mark.switch(Mark.EMPTY), Mark.EMPTY)
