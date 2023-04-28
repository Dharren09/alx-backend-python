#!/usr/bin/env python3
"""annotate a function's parameters and returns values with appopriate types"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
