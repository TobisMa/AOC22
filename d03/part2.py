from util import get_data
from math import ceil
from string import ascii_letters


data = get_data(("\n", ))

# data =  [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw"
# ]

def get_prio(s):
    r = 0
    for l in s:
        if l.isupper():
            r += ord(l) - 38
        elif l.islower():
            r += ord(l) - 96
    return r

prio = 0
while data:
    lines = data[:3]
    data = data[3:]
    
    lines = list(map(set, lines))    
    all_elves = set(ascii_letters)
    for set_ in lines:
        all_elves &= set_
        print(set_)
        
    print(all_elves)
    prio += get_prio(all_elves)
    
print(prio)