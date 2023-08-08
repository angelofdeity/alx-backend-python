#!/usr/bin/env python3
"""Measure runtime"""
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension
async def measure_runtime():
    start_time = time.time()
    for _ in range(4):
        await async_comprehension()
    end_time = time.time()
    return end_time - start_time
