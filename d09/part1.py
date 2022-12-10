import json
from math import sqrt
from typing import List, Literal
from util import get_data

d: List[str] = get_data(("\n",), day=9)
# d = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".split("\n")

data = [x.split(" ") for x in d if x]
print(data)
data = [(x[0], int(x[1])) for x in data]

head, tail = [0, 0], [0, 0]


def add(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1]]


def neg(vec):
    return [-vec[0], -vec[1]]


def sub(vec1, vec2):
    return add(vec1, neg(vec2))

def mul(n, vec):
    return [vec[0] * n, vec[1] * n]


def sign(n: int) -> Literal[-1, 0, 1]:
    if n < 0:
        return -1
    return 1 if n != 0 else 0


moves = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}


def distance(vec1, vec2):
    t = sub(vec1, vec2)
    return sqrt(t[0] ** 2 + t[1] ** 2)


def adjacent(vec1, vec2):
    return distance(vec1, vec2) <=  sqrt(2) + 0.1

def diagonally_adjacent(vec1, vec2):
    return distance(vec1, vec2) >= sqrt(2) - 0.1

positions = []
diagonal = False
last_direction = None
for step, (direction, count) in enumerate(data):
    for i in range(count):
        head = add(head, moves[direction])
        if not adjacent(head, tail):
            tail = add(tail, moves[direction])
            if diagonally_adjacent(head, tail) and last_direction != direction:
                if abs(head[0] - tail[0]) >= 1 and direction in ("U", "D"):
                    tail[0] += sign(head[0] - tail[0])
                elif abs(head[1] - tail[1]) >= 1 and direction in ("L", "R"):
                    tail[1] += sign(head[1] - tail[1])
                
        print(f"{head=}; {tail=}; {direction=}; {step=}")
        # input()
        positions.append(tuple(tail))
    last_direction = direction

# print(json.dumps(positions, indent=4))
print(len(set(positions)))
            
        
        