#!/usr/bin/env python3
"""function takes in a str and an int or float as arg and return a tuple"""

from typing import Union


def to_kv(k: str, v: Union[float, int]) -> tuple[str, float]:
    """returns a tuple containing k and the square of v"""
    return (k, float(v ** 2))
