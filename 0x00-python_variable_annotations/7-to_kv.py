#!/usr/bin/env python3
"""function takes in a str and an int or float as arg and
returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """returns a tuple containing k and the square of v"""
    return (k, float(v ** 2))
