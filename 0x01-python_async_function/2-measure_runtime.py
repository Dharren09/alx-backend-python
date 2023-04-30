#!/usr/bin/env python3
"""imports a module then uses two int inform of args to
make function which measures total execution time"""

import time
from typing import List
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """get the current time"""
    start = time.time()
    """run the function with 2 args which returns random delays"""
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    average_time = total_time / n
    return average_time
