#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """function determines if given data is valid UTF-8 encoding"""
    if any(val < 0 or val >= 256 for val in data):
        return False

    try:
        decodedText = bytes(data).decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
