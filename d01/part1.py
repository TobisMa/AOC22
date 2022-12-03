
total: int = 0
m: int = 0
with open("d01/data.txt") as f:
    for line in f:
        if line.strip():
            total += int(line.strip())
        else:
            if total > m:
                m = total
            total = 0
            
print(m)