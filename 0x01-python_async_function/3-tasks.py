#!/usr/bin/env python3
"""imports a module, makes a function tha takes in
an int arg and returns a task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a task that awaits a random delay"""
    task = wait_random(max_delay)
    return asyncio.create_task(task)
