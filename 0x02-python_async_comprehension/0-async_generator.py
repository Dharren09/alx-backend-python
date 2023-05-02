#!/usr/bin/env python3
"""writes a coroutine that takes in no arg"""

from typing import Generator
import asyncio
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times"""
    for _ in range(10):
        """each time synchronously waits 1 sec"""
        await asyncio.sleep(1)
        """then yeilds a random number btn 0  and 10"""
        yield uniform(0, 10)
