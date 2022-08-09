#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times, each time asynchronously wait 1"""
    n = 10
    while (n > 0):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        n = n - 1
