from util import get_data


crates, steps = get_data(("\n\n",))
# crates = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 """
# steps = """move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """

c = {int(x): [] for x in crates.split("\n")[-1] if x.strip()}
print(crates)

for line in list(reversed(crates.split("\n")))[1:]:
    s = list(line.split(" "))
    i = 0
    ci = 1
    while i < len(s):
        if not s[i]:
            i += 4
        else:
            c[ci].append(s[i][1])
            i += 1
        # print(s[i], i, end=" ")
        ci += 1

for step in steps.split("\n"):
    if not step: continue
    nums = [int(x) for x in step.split() if x.isdigit()]
    print(nums, step)
    to_move = c[nums[1]][-nums[0]:]
    c[nums[1]] = c[nums[1]][:-nums[0]]
    c[nums[2]].extend(reversed(to_move))

print(''.join(c[x][-1] for x in c))