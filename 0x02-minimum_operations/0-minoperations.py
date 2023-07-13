"""Minimum operations"""
import math


def minOperations(n):
    """Returns the fewest number of ops to complete a taskt"""
    """initialize ops to 0 to keep track of the number of op needed"""
    ops = 0
    """
    Check if i is a factor of n:
        If yes, update the value of n by dividing it by i and increment the number of ops by i.
        Repeat until i is no longer a factor of n.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            ops += i
    """
    After the loop, if n is greater than 1, it means n itself is a prime number.
    In this case, n is added to the number of ops.
    """
    if n > i:
        ops += n

    return ops


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

print(minOperations(14))
n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
