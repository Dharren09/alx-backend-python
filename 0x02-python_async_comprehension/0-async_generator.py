#!/usr/bin/env python3
"""writes a coroutine that takes in no arg"""

import asyncio
import random


async def async_generator():
    """coroutine will loop 10 times"""
    for i in range(10):
        """each time synchronously waits 1 sec"""
        await asyncio.sleep(i)
        """then yeilds a random number btn 0  and 10"""
        yield random.randint(0, 10) 
