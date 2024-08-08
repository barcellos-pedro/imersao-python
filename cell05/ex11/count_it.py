#!/usr/bin/python3

import sys

has_param = len(sys.argv) > 1

if not has_param:
    print('none')
    exit()

params = sys.argv[1:]

print(f'parameters: {len(params)}')

for param in params:
    print(f"{param}: {len(param)}")
