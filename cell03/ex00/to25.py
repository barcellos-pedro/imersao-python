#!/usr/bin/python3

end = 25
current = int(input(f"Enter a number less than {end}: "))

if current > end:
    print("Error\n")
    exit()

while current <= end:
    print(f"Inside the loop, my variable is {current}")
    current += 1
