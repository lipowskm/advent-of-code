import itertools
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0
galaxies_indexes = []

lines = f.readlines()
expanded = []

for idx, line in enumerate(lines):
    line = list(line.strip("\n"))
    expanded.append(line)
    if "#" not in line:
        expanded.append(line)

columns_to_expand = []
for idy in range(0, len(expanded[0])):
    for idx in range(0, len(expanded)):
        if expanded[idx][idy] == "#":
            break
    else:
        columns_to_expand.append(idy)

for idx in range(0, len(expanded)):
    for i, idy in enumerate(columns_to_expand):
        expanded[idx].insert(idy + i, ".")

for x, line in enumerate(expanded):
    for y, char in enumerate(line):
        if char == "#":
            galaxies_indexes.append((x, y))

for combination in itertools.combinations(galaxies_indexes, 2):
    result += abs(combination[0][0] - combination[1][0]) + abs(
        combination[0][1] - combination[1][1]
    )

print(result)
