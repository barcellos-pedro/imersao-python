#!/usr/bin/python3.10

import sys

params = sys.argv[1:]

match params:
    case [*words]:
        for param in words:
            if param.endswith('ism'):
                continue
            print(f'{param}ism')
    case _:
        print('none')
