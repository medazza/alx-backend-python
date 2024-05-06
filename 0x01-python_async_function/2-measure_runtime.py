#!/usr/bin/env python3
""" 2-measure_runtime.py """

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """doc for measure_time function"""
    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_t = time.time()

    return (end_t - start_t) / n
