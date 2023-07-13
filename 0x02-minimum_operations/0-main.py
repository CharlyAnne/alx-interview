#!/usr/bin/python3
"""
Main file for testing
"""

"""
initialize ops to 0 to keep track of the number of op needed
Check if i is a factor of n:
    If yes, update the value of n by dividing it by i and increment the number of ops by i.
    Repeat until i is no longer a factor of n.
After the loop, if n is greater than 1, it means n itself is a prime number.
In this case, n is added to the number of ops.
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 74
"""This will give 39: 2 + 37"""
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 24
"""This will give 9: 2 + 2 + 2 + 3"""
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
