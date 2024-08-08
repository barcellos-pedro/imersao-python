#!/usr/bin/python3

number = input('Give me a number: ')

if '.' not in number:
    print('This number is an integer.')
    exit()

if str(float(number)).endswith('.0'):
    print('This number is an integer.')
else:
    print('This number is a decimal.')
