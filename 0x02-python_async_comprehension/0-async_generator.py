#!/usr/bin/env python3
""" Module documentation of task 0"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Func async_generator doc"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
