#!/usr/bin/env python3
"""Augments a code with correct duck-typed annotations"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        """returns list"""
        return lst[0]
    else:
        return None
