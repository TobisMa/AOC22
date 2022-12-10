from math import sqrt
from turtle import position
from util import get_data
from vectormath import Vector2

data = get_data(("\n"))
data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")
data = [[s[0], int(s[2:])] for s in data if s]

head = Vector2(0, 0)
tail = Vector2(0, 0)
positions = []

deltas = {
    "L": Vector2(-1, 0),
    "R": Vector2(1, 0),
    "D": Vector2(0, -1),
    "U": Vector2(0, 1),
}

oppposites = {
    "L": "R",
    "R": "L",
    "U": "D",
    "D": "U",
}

last_direction = None

def is_diagonally_adjacent(pos1: Vector2, pos2: Vector2) -> bool:
    return sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) > 1.1

def adjacent(pos1: Vector2, pos2: Vector2) -> bool:
    return sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) <= sqrt(5) - 0.1
 

# sourcery skip: merge-else-if-into-elif
direction: str
count: int
diagonal: bool = False

for direction, count in data:
    for _ in range(max(count, 1)):
        d = deltas[direction]
        head.x += d.x
        head.y += d.y

        if not adjacent(head, tail):
            tail.x += d.x
            tail.y += d.y
            
        # if is_diagonally_adjacent(head, tail):
        #     diagonal = True

        
        if is_diagonally_adjacent(head, tail):
            if last_direction in ("R", "L"):
                if head.y > tail.y:
                    tail.y += 1
                elif head.y < tail.y:
                    tail.y -= 1
            else:
                if head.x > tail.x:
                    tail.x += 1
                elif head.x < tail.x:
                    tail.x -= 1
            
            diagonal = False
        
                    
        # print(tuple(map(int, (tail.x, tail.y))), "| adjacent", adjacent(head, tail), "| diagonal", is_diagonally_adjacent(head, tail), end="\n")
        positions.append((tail.x, tail.y))
        # print(f"{direction=}; {count=}; {head=}; {tail=}")
        # print("------------------------------------")

print([tuple(map(int, x)) for x in positions])
print(len(set(positions)))
