#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """write an async routine called wait_n that takes in 2 int argument"""
    i = 0;
    list: List[float] = []
    while n >= 0:
        valor = await (wait_random(max_delay))
        list.append(valor)
        i += 1
    list = sorted(list)
    return list
