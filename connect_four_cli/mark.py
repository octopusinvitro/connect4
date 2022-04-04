from enum import Enum


class Mark(Enum):
    EMPTY = ' '
    CROSS = 'x'
    ROUND = 'o'

    @classmethod
    def switch(cls, mark):
        switch_table = {
            cls.EMPTY.value: cls.EMPTY,
            cls.CROSS.value: cls.ROUND,
            cls.ROUND.value: cls.CROSS
        }

        return switch_table[mark.value]
