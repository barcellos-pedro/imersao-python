#!/usr/bin/python3.10

def array_of_names(name_book):
    names = []

    for name, last_name in name_book.items():
        full_name = f"{name.capitalize()} {last_name.capitalize()}"
        names.append(full_name)        
    
    return names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
