#!/usr/bin/python3.10

import sys

params = sys.argv[1:]

if len(params) < 2:
    print('none')
    exit()

reversed_params = reversed(params)

for param in reversed_params:
    print(param)
