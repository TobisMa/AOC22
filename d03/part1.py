from util import get_data
from math import ceil


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
for items in data:
    length = len(items) / 2
    left, right = items[:ceil(length)], items[int(length):]
    sl = set(left)
    sr = set(right)
    both = sl & sr
    
    prio += get_prio(both)
    
print(prio)