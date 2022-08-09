#!/usr/bin/env python3
"""Tasks"""
import time
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Write a function task_wait_random that takes an integer max_delay """

    return asyncio.create_task(wait_random(max_delay))
