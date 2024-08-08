#!/usr/bin/python3

value = input('Digite alguma coisa: ')

print('Resultado: ', end='')

for char in value:
    if char.isupper():
        print(char.lower(), end='')
    else:
        print(char.upper(), end='')

print()
