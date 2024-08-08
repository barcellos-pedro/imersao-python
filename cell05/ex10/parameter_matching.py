#!/usr/bin/python3

import sys

has_param = len(sys.argv) > 1

if not has_param:
    print('none')
    exit()

expected = sys.argv[1]
actual = input('What was the parameter? ')

if expected != actual:
    print('Nope, sorry...')
else:
    print('Good job!')
