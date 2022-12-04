from typing import List, Optional, Set
from util import get_data
import builtins

def range(x: int, y: Optional[int]=None, z: Optional[int]=None, /) -> builtins.range:
    if y is None and z is None:
        return builtins.range(x)
    elif z is None:
        return builtins.range(x, y + 1)
    return builtins.range(x, y + 1, z)

data: List[List[str]] = get_data(("\n", ","))
# data = [
#     ["2-4", "2-8"]
# ]
data: List[List[Set[int]]] = [[set(range(*map(int, x.split("-")))) for x in d] for d in data]

same: int = 0
for d in data:
    result: Set[int] = d[0] & d[1]
    if result in d:
        same += 1
print(same)