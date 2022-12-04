from util import get_data
import builtins

def range(x, y=None, z=None):
    if y is None and z is None:
        return builtins.range(x)
    elif z is None:
        return builtins.range(x, y + 1)
    return builtins.range(x, y + 1, z)

data = get_data(("\n", ","))
# data = [
#     ["2-4", "2-8"]
# ]
data = [[set(range(*map(int, x.split("-")))) for x in d] for d in data]

same = 0
for d in data:
    result = d[0] & d[1]
    if result in d:
        same += 1
print(same)