#!/usr/bin/python3
"""Minimum operations"""

import math


def minOperations(n):
    """Returns the fewest number of ops to complete a taskt"""
    ops = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            ops += i

    if n > 1:
        ops += n

    return ops
