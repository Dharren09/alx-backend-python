#!/usr/bin/env python3
"""takes in wait_n code, alters it into a new function"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function that awaits a random delay"""
    tasks = tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times) 
