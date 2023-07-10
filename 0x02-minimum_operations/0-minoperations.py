#!/usr/bin/python3
"""Minimum operations"""
import math


def minOperations(n):
    """
    Returns the fewest number of ops to result in exactly n, H characters
    """
    op = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            op += i
    if n > i:
        op += n

    return op


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
