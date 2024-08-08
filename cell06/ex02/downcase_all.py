#!/usr/bin/python3.10

import sys

params = sys.argv[1:]

if len(params) == 0:
    print('none')
    exit()

def downcase_it(text):
    if text is None or len(text.strip()) == 0:
        return 'none'
    
    return text.lower()

for param in params:
    print(downcase_it(param))
