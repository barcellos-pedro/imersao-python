#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    print('none')
    exit()

multiplicador, multiplicando = 0, 0
maximo = 10

while multiplicador <= maximo:
    print(f'\nTable de {multiplicador}: ', end='')
    
    while multiplicando <= 10:
        print(multiplicador * multiplicando, end=' ')
        multiplicando += 1

    multiplicando = 0
    multiplicador += 1
