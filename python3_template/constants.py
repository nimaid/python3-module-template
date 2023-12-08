from enum import Enum

DESCRIPTION = "A python 3 module."


class OpCodes(Enum):
    ADD = "+"
    SUB = "-"
    MULT = "*"
    DIV = "/"


DEFAULTS = {
    "second": 1.0,
    "opcode": OpCodes.ADD
}
