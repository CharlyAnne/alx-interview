## This directory contains the solution to a common interview task - Log Parsing

# Task Description

The task requires writing a script that reads input from stdin line by line and computes metrics based on the input format. After every 10 lines or a keyboard interruption (CTRL + C), the script should print the following statistics:

1. Total file size: The sum of all previous file sizes.
2. Number of lines by status code: Count of lines for each status code in ascending order. The possible status codes are 200, 301, 400, 401, 403, 404, 405, and 500.

## Solution Breakdown

1. Initialize necessary variables:
   - 'status_code_counts': A dictionary to store the count of lines for each status.
   - 'total_file_size': A var to keep track of the total file size.
   - 'line_count': A var to count the number of processed lines.
2. Used a 'try - execpt' block to handle keyboard interruption (CTRL + C) and ensure the script terminates gracefully.
3. Iterate over each line from standard input(stdin) using 'for line in sys.stdin'. This reads input line by line..
4. Strip any leading or trailing whitespace from the line using 'line.strip()'.
5. Split the line into parts using the space character as the delimeter using 'line.split(' ')'. This separates the different components of the input line.
6. Check if the number of parts is 7. If not, skip the line using 'continue;. This endures that the line matches the expected input format.
7. Extract the relevant information from the line_parts:
   - 'ip_address': (line_parts[0])
   - 'date'
   - 'status_code'
   - 'file_size': the file size converted to an integer from line_parts[6]
8. Update the total file size by adding the current file size to 'total_file_size'.
9. Update status_code_count:
   - Check if the status code is a digit using status_code.isdigit().
   - If it is a digit, convert it to an integer and update the count in the status_code_counts dictionary.
   - Use status_code_counts.get(status_code, 0) to retrieve the current count and increment it by 1.
10. Increment the 'line_count' by 1.
11. After processing every 10 lines (when line_count % 10 == 0), or when interrupted by a keyboard interruption, print the statistics:

- Print the total file size using print("Total file size:", total_file_size).
- Iterate over the keys of status_code_counts in ascending order using sorted(status_code_counts.keys()).
- For each code, print the code and its count using print(f"{code}: {status_code_counts[code]}").

12.
