#!/usr/bin/python3.10

import sys

if len(sys.argv) == 1:
    print('none')
    exit()

prompt = sys.argv[1]
print(prompt.lower())
