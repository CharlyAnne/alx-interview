#!/usr/bin/python3
""" Srcipt reads stdin line by line and computes metrics"""
import sys

total_file_size = 0
code = 0
line_counter = 0
dict_status_code = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dict_status_code.keys()):
                    dict_status_code[code] += 1

            if (line_counter == 10):
                print("File size: {}".format(total_file_size))
                for key, val in sorted(dict_status_code.items()):
                    if val != 0:
                        print("{}: {}".format(key, val))
                        counter = 0

finally:
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))
