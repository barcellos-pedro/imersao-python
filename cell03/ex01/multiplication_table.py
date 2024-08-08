#!/usr/bin/python3

print("Digite um número:")
multiplier = int(input())

count = 0
max_number = 9

while count <= max_number:
    print(f"{count} x {multiplier} = {count * multiplier}")
    count += 1
