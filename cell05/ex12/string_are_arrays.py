#!/usr/bin/python3

import sys

has_param = len(sys.argv) > 1

if not has_param:
    print('none')
    exit()

text = sys.argv[1]

if 'z' not in text:
    print('none')
    exit()

count = 0

for char in text:
    if char == 'z':
        count += 1

# exibe 'z' 'n' vezes
print('z' * count)
