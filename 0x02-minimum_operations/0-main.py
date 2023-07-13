#!/usr/bin/python3
"""
Main file for testing
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
