from enum import Enum, auto


class ErrorCode(Enum):
    NONE = auto()
    NOTADIGIT = auto()
    NOTINRANGE = auto()
    NOTAVAILABLE = auto()
