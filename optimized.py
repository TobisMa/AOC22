from util import get_data

print(max(sum(x) for x in get_data(("\n\n", "\n"), type_=int)))
print(sum(sorted(sum(x) for x in get_data(("\n\n", "\n"), type_=int))[-3:]))