import random


class Random:
    def __init__(self, mark):
        self.mark = mark

    def play_turn(self, available_columns):
        return random.choice(available_columns)
