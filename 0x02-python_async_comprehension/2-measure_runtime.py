#!/usr/bin/env python3
"""imports a previous function and writes a coroutine"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """defining the start time"""
    start = asyncio.get_running_loop().time()
    """executes the imported function 4 times in parallel using the gather method"""
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end = asyncio.get_running_loop().time()
    """returns the total runtime measured"""
    return end - start
