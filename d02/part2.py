from util import get_data

guide = get_data(("\n", " "))
# guide = [
#     ["A", "Y"],
#     ["B", "X"],
#     ["C", "Z"]
# ]
scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3    
}


def choose(left, right) -> str:
    for p in "XYZ":
        s = game(left, p)
        if (right == "X" and s == 0) or (right == "Y" and s == 3) or (right == "Z" and s == 6):
            return p
    

def game(left, right) -> int:
    sl = scores[left]
    sr = scores[right]
    if sl == sr:
        return 3

    return 6 if sl == (sr - 2) % 3 + 1 else 0
    
print(sum(game(x[0], choose(x[0], x[1])) + scores[choose(x[0], x[1])] for x in guide))