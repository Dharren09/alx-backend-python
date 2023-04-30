#!/usr/bin/env python3
"""imports a module then uses two int inform of args to
make function which measures total execution time"""

wait_n = __import__('1-concurrent_coroutines').wait_n

import time
from typing import List
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    average_time = total_time / n
    return average_time
