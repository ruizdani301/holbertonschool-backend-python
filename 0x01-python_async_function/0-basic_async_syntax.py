#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument
   and waits for a random dalay between 0 and integer RETURN a float
"""
import asyncio
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    timer = random.uniform(0, max_delay)
    await asyncio.sleep(timer)
    return timer
