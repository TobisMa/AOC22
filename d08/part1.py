import contextlib
import itertools
from re import S
from util import get_data


data = get_data(("\n"))
data = [list(map(int, d)) for d in data if d]

# data = [
#     [3, 0, 3, 7, 3],
#     [2, 5, 5, 1, 2],
#     [6, 5, 3, 3, 2],
#     [3, 3, 5, 4, 9],
#     [3, 5, 3, 9, 0],
# ]

def get_neightbours(x: int, y: int):
    for i in range(-1, 1, 2):
        try:
            yield data[y + i][x]
            yield data[y][x + i]
        except IndexError:
            yield -1

visible = set()
for y, trees in enumerate(data):
    # visible.append([])
    for x, tree in enumerate(trees):
        for delta in range(-1, 2, 2):
            if x == 0 or y == 0 or x == len(trees) - 1 or y == len(data) - 1:
                visible.add((x, y))
                continue
            
            stop = 0 if delta < 0 else len(trees)
            for delta_x in range(x + delta, stop + min(0, delta), delta):
                if data[y][delta_x] >= tree:
                    break
            else:
                if len(range(x + delta, stop + min(0, delta), delta)):
                    visible.add((x, y))
                
            stop = 0 if delta < 0 else len(data)
            for delta_y in range(y + delta, stop + min(0, delta), delta):
                if data[delta_y][x] >= tree:
                    break
            else:
                if len(range(y + delta, stop + min(0, delta), delta)):
                    visible.add((x, y))
        
print(len(visible))
# print(visible)