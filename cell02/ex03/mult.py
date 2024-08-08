#!/usr/bin/python3

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

result = a * b

print()

if result > 0:
    print(f'{a} x {b} = {result}')
    print('The result is positive.')
elif result < 0:
    print(f'{a} x {b} = {result}')
    print('The result is negative.')
elif result == 0:
    print(f'{a} x {b} = {result}')
    print('The result is positive and negative.')
