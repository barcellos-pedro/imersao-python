#!/usr/bin/python3.10

numbers = [2, 8, 9, 48, 8, 22, -12, 2]

result = []

for number in numbers:
    if number > 5:
        result.append(number + 2)

# Usando filter() e map()
# new_array = list(filter(lambda number: number > 5, numbers))
# new_array = list(map(lambda number: number + 2, new_array))

print(numbers)
print(result)
