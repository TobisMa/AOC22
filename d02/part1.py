from typing import Dict, List, Literal, Union

from util import get_data

guide: List[List[str]] = get_data(("\n", " "))
# guide = [
#     ["A", "Y"],
#     ["B", "X"],
#     ["C", "Z"]
# ]
scores: Dict[str, int] = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3    
}


def game(left: Union[Literal["A"], Literal["B"], Literal["C"]], right: Union[Literal["X"], Literal["Y"], Literal["Z"]]) -> int:
    sl: int = scores[left]
    sr: int = scores[right]
    if sl == sr:
        return 3

    return 6 if sl == (sr - 2) % 3 + 1 else 0
    
print(sum(game(*x) + scores[x[1]] for x in guide))