#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer arg
with default value that awaits for a random delay
between 0 and max_delay then returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async awaits random delay anf then returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
