#!/usr/bin/python3.10

def birth_filter(person):
    [name, info] = person
    return info["date_of_birth"]


def famous_births(births):
    sorted_births = sorted(births.items(), key=birth_filter)
    
    for name, info in sorted_births:
        print(f"{name} is a great scientist born in {info['date_of_birth']}.")


women_scientists = {
    "ada": {
        "name": "Ada Lovelace",
        "date_of_birth": "1815"
    },
    "cecilia": {
        "name": "Cecila Payne",
        "date_of_birth": "1900"
    },
    "lise": {
        "name": "Lise Meitner",
        "date_of_birth": "1878"
    },
    "grace": {
        "name": "Grace Hopper",
        "date_of_birth": "1906"
    }
}

famous_births(women_scientists)
