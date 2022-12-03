from math import ceil
from typing import List, Set

from util import get_data

data: List[str] = get_data(("\n", ))

# data =  [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw"
# ]

def get_prio(s) -> int:
    r: int = 0
    for l in s:
        if l.isupper():
            r += ord(l) - 38
        elif l.islower():
            r += ord(l) - 96
    return r

prio: int = 0
for items in data:
    length: float = len(items) / 2
    left, right = items[:ceil(length)], items[int(length):]
    
    sl: Set[str] = set(left)
    sr: Set[str] = set(right)
    
    both: Set[str] = sl & sr
    
    prio += get_prio(both)
    
print(prio)