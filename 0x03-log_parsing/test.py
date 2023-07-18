#!/usr/bin/python3

import sys

status_code_count = {}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        # line is parsed based on the specified input format
        line_parts = line.split(' ')
        # if parts not 7, skip the line
        if len(line_parts) != 7:
            continue

        ip_address = line_parts[0]
        date = line_parts[3].strip('[]')
        status_code = line_parts[5]
        file_size = int(line_parts[6])

        # update total file size
        total_file_size += file_size

        # update status code count
        if status_code.isdigit():
            status_code = int(status_code)
            status_code_count[status_code] = status_code_count.get(
                status_code, 0)

        # increment line count by 1
        line_count += 1

        # to print statsistics after every 10 lines
        if line_count % 10 == 0:
            print('Total file size:', total_file_size)
            # Use sorted to iterate in ascending order
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] != 0:
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    # Print statistics when interrupted by keyboard
    print('Total file size:', total_file_size)
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")
