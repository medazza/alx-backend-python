#!/usr/bin/env python3
""" Module documentation """
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """docomentation of func wait_n"""
    list_delays = []
    for _ in range(n):
        list_delays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*list_delays))
