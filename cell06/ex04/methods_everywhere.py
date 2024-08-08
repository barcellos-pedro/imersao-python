#!/usr/bin/python3.10

import sys

params = sys.argv[1:]

def shrink(text):
    return text[:8]

def enlarge(text):
    count = 8 - len(text)
    text += 'Z' * count
    return text

if len(params) == 0:
    print('none')
    exit()

for text in params:
    if len(text) > 8:
        print(shrink(text))
    else:
        print(enlarge(text))
