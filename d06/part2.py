from util import get_data


d = get_data("\n")
# d = ["bvwbjplbgvbhsrlpgdmjqwftvncz"]
print(d)

m = 0
for data in d:
    if not data: continue
    for i in range(0, len(data[:-14])):
        if len(set(data[i:i+14])) == 14:
            m += i + 14
            break

print(m)