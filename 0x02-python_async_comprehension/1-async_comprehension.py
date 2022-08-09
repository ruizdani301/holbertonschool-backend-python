#!/usr/bin/env python3
"""Import async_generator from the previous task and then write a
   coroutine called async_comprehension
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """The coroutine will collect 10 random numbers using an async
        comprehensing over async_generator
    """

    return [x async for x in (async_generator())]
