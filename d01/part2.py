
sums = []
total = 0
with open("d01/data.txt") as f:
    for line in f:
        if line.strip():
            total += int(line.strip())
        else:
            sums.append(total)
            total = 0

print(sum(list(sorted(sums))[-3:]))