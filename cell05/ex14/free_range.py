#!/usr/bin/python3.10

import sys

no_params = len(sys.argv) == 1

if no_params:
    print('none')
    exit()

params = sys.argv[1:] # params = [value1, value2]
start = params[0]
end = params[1]

if start >= end:
    print('none')
    exit()

numbers = []
start = int(start)
end = int(end)

for number in range(start, end + 1):
    numbers.append(number)

print(numbers)
