import json
import math
import pathlib
from textwrap import wrap
data = pathlib.Path("d11/data.txt").read_text()

# data = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# """

monkeys = []

monkey = {}
for line in data.split("\n"):
    if not line:
        monkey["inspects"] = 0
        monkeys.append(monkey)
        monkey = {}
        continue

    if line.strip().startswith("Starting"):
        monkey["items"] = list(map(int, line.split(":")[1].replace(" ", "").split(",")))

    elif line.strip().startswith("Operation"):
        op = line.strip().split(" = ")[-1]
        monkey["operation"] = eval(f"lambda old: {op}")

    elif line.strip().startswith("Test"):
        monkey["test"] = int(line.split(" ")[-1])

    elif line.strip().startswith("If true"):
        monkey["true"] = int(line.split(" ")[-1])

    elif line.strip().startswith("If false"):
        monkey["false"] = int(line.split(" ")[-1])


def divisible(modulo):
    def wrapper(item):
        return item % modulo == 0
    return wrapper

def not_divisible(modulo):
    def wrapper(item):
        return item % modulo != 0
    return wrapper

cm = math.prod(m["test"] for m in monkeys)
print(cm)
for _ in range(10000):
    for m in monkeys:
        m["inspects"] += len(m["items"])
        items = list(map(m["operation"], m["items"]))
        f = eval("lambda x : x % cm")
        items = list(map(f, items))
        modulo = m["test"]
        monkeys[m["true"]]["items"].extend(filter(divisible(modulo), items))
        monkeys[m["false"]]["items"].extend(filter(not_divisible(modulo), items))
        m["items"] = []

# print(monkeys)
print(inspects := [m["inspects"] for m in monkeys])
print(math.prod(sorted([m["inspects"] for m in monkeys])[-2:]))