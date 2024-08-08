#!/usr/bin/python3.10

import sys, re

params = sys.argv[1:]
no_params = len(params) < 2

if no_params:
    print('none')
    exit()

[search_word, text] = params
count = len(re.findall(search_word, text))
# count = text.count(search_word)

if count > 0:
    print(count)
else:
    print('none')
