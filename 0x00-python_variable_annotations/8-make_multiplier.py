#!/usr/bin/python3
"""function that takes a float as arg and returns a function tha multiplies a float by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_fn(num: float) -> float:
        return num * multiplier
    return multiplier_fn
