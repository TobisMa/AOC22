import json, pygame
from time import time
from math import sqrt
from typing import List, Literal
from util import get_data

d: List[str] = get_data(("\n",), day=9)
d = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")

pygame.init()
screen = pygame.display.set_mode((800, 600))

data = [x.split(" ") for x in d if x]
data = [(x[0], int(x[1])) for x in data]

knots = [[0, 0] for _ in range(10)]


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

color_cycle = [
    [255, 0, 0],
    [255, 255, 0],
    [255, 0, 255],
    [255, 255, 255],
    [0, 255, 0],
    [0, 255, 255],
    [0, 0, 255],
    [200, 200, 200],
    [100, 0, 100],
    [100, 100, 0]
]

def draw():
    delta = [400, 300]
    screen.fill([0]*3)
    for i, knot in enumerate(knots):
        pos = knot.copy()
        pos[1] *= -1
        pos = add(delta, mul(10, pos))
        pygame.draw.circle(screen, color_cycle[i % len(color_cycle)], pos, 5)

    for i in range(5, 800, 10):
        pygame.draw.line(screen, [255]*3, [i, 0], [i, 600])

    for i in range(5, 600, 10):
        pygame.draw.line(screen, [255]*3, [0, i], [800, i])

    tc = time()
    te = tc + 0.1
    while tc < te:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(-1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    break_ = False
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit(-1)
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    break_=True
                        if break_:
                            break
        tc = time()
    pygame.display.flip()
        


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
    return distance(vec1, vec2) >= sqrt(2) - 0.3

positions = []
diagonal = False
last_direction = None

for step, (direction, count) in enumerate(data):
    for _ in range(count):
        knots[0] = add(knots[0], moves[direction])
        for j in range(len(knots) - 1):
            if adjacent(knots[j], knots[j+1]): 
                continue
            
            knots[j+1] = add(knots[j+1], moves[direction])
            if diagonally_adjacent(knots[j], knots[j+1]) and last_direction != direction:
                if abs(knots[j][0] - knots[j+1][0]) >= 1 and direction in ("U", "D"):
                    knots[j+1][0] += sign(knots[j][0] - knots[j+1][0])
                elif abs(knots[j][1] - knots[j+1][1]) >= 1 and direction in ("L", "R"):
                    knots[j+1][1] += sign(knots[j][1] - knots[j+1][1])
                
        draw()
        positions.append(tuple(knots[-1]))
    print(f"{knots=}; {direction=}, {count=}; {step=}")
    # input()
    last_direction = direction

# print(positions)
print(len(set(positions)))
pygame.quit()
        
        