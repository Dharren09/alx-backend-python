#!/usr/bin/env python3
""" imports a function from previous task then writes a coroutine that takes no arg """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine collects 10 random numbers from the imported function and returns the random numbers"""
    numbers = [num async for num in async_generator()]
    return numbers
