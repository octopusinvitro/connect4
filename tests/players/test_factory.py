from unittest import TestCase

from connect_four_cli.mark import Mark
from connect_four_cli.players.factory import Factory
from connect_four_cli.players.human import Human
from connect_four_cli.players.random import Random

from tests.fake_ui import FakeUI


class TestFactory(TestCase):
    def setUp(self):
        self.fakeui = FakeUI()
        self.factory = Factory(self.fakeui)

    def test_creates_two_human_players(self):
        self.fakeui.set_fake_option('human_human')
        player, oponent = self.factory.create_players()
        self.assertIsInstance(player, Human)
        self.assertIsInstance(oponent, Human)

    def test_creates_two_human_players_with_opposite_marks(self):
        self.fakeui.set_fake_option('human_human')
        player, oponent = self.factory.create_players()
        self.assertEqual(player.mark, Mark.switch(oponent.mark))

    def test_creates_human_random_players(self):
        self.fakeui.set_fake_option('human_random')
        player, oponent = self.factory.create_players()
        self.assertIsInstance(player, Random)
        self.assertIsInstance(oponent, Human)

    def test_creates_human_random__with_opposite_marks(self):
        self.fakeui.set_fake_option('human_random')
        player, oponent = self.factory.create_players()
        self.assertEqual(player.mark, Mark.switch(oponent.mark))
