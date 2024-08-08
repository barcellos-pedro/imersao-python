#!/usr/bin/python3.10

numbers = [2, 8, 9, 48, 8, 22, -12, 2]

result = []

for number in numbers:
    result.append(number + 2)

# Usando map()
# new_array = list(map(lambda number: number + 2, numbers))

print(f"Original array:", numbers)
print(f"New array:", result)
