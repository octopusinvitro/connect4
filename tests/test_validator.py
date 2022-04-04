from unittest import TestCase

from connect_four_cli.error_code import ErrorCode
from connect_four_cli.validator import Validator


class TestValidator(TestCase):
    def test_detects_not_a_digit(self):
        self.assertEqual(self.error('hello'), ErrorCode.NOTADIGIT)

    def test_detects_below_range(self):
        self.assertEqual(self.error('0'), ErrorCode.NOTINRANGE)

    def test_detects_above_range(self):
        self.assertEqual(self.error('3'), ErrorCode.NOTINRANGE)

    def test_detects_not_available(self):
        self.assertEqual(self.error('1'), ErrorCode.NOTAVAILABLE)

    def test_detects_valid_input(self):
        self.assertEqual(self.error('2'), ErrorCode.NONE)

    def error(self, input):
        total_columns = 2
        available_values = [1]

        return Validator(total_columns, available_values).validate(input)
