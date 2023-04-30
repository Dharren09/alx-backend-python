#!/usr/bin/env python3

"""imports a module, takes in two args spawns them
and the returns a list of all delays"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """define the coroutine variable"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)

    """sorting the delays to be returned in a ascending order"""
    for i in range(1, n):
        j = i
        while j > 0 and delays[j-1] > delays[j]:
            delays[j-1], delays[j] = delays[j], delays[j-1]
            j -= 1
    return delays
