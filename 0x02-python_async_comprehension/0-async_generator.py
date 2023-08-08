#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random
from collections.abc import Iterator
async def async_generator() -> Iterator[int]:
    """asynchronously generate random values"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
