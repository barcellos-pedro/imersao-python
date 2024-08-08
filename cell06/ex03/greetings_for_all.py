#!/usr/bin/python3.10

def greetings(name = "noble stranger"):
    if not isinstance(name, str):
        return print('Error! It was not a name.')
    print(f"Hello, {name}.")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
