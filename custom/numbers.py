from talon import *

mod = Module()


@mod.capture
def number(m) -> int:
    """Capture spoken numbers in any form"""


ctx = Context()

ones_map = {
    'zero':  0,
    'one':   1,
    'two':   2,
    'three': 3,
    'four':  4,
    'five':  5,
    'six':   6,
    'seven': 7,
    'eight': 8,
    'nine':  9,
}
alt_ones = '|'.join(ones_map.keys())


@ctx.capture(rule=f'({alt_ones})+')
def number(m):
    return int(''.join([str(ones_map[n]) for n in m]))


ctx.commands = {
    'number <self.number>': lambda m: print(m.number),
}
