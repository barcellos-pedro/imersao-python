#!/usr/bin/python3.10

def find_the_redheads(members):
    hair_filter = lambda person: person[1] == 'red'
    red_hair_members = dict(filter(hair_filter, members.items()))
    return list(red_hair_members.keys())


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
