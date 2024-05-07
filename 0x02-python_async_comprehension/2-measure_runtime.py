#!/usr/bin/env python3
""" Module documentation """
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Function documentation"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
