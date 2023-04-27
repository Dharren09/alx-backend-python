#!/usr/bin/python3
"""function takes a list of integers and returns the sum of floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
