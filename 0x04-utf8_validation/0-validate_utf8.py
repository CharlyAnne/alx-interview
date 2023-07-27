#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """function determines if given data is valid UTF-8 encoding"""
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if num >> 7 == 0b0:  # 1-byte character (0xxxxxxx)
                continue
            elif num >> 5 == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif num >> 4 == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif num >> 3 == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:  # Check if the next byte is 10xxxxxx
                return False
            num_bytes -= 1

    return num_bytes == 0