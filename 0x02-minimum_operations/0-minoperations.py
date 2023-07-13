#!/usr/bin/python3
"""Minimum operations"""

"""
initialize ops to 0 to keep track of the number of op needed
Check if i is a factor of n:
    If yes, update the value of n by dividing it by i and increment the number of ops by i.
    Repeat until i is no longer a factor of n.
After the loop, if n is greater than 1, it means n itself is a prime number.
In this case, n is added to the number of ops.
"""




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
