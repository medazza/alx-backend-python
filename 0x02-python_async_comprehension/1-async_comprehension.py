#!/usr/bin/env python3
""" Module documentation """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Creates a list of 10 numbers from a 10-number generator"""
    return [random_num async for random_num in async_generator()]
