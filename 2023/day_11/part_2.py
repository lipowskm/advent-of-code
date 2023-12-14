import itertools
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0
galaxies_indexes = []
empty_rows = []
empty_columns = []

lines = [list(line.strip("\n")) for line in f.readlines()]

for idx, line in enumerate(lines):
    if "#" not in line:
        empty_rows.append(idx)

for idy in range(0, len(lines[0])):
    for idx in range(0, len(lines)):
        if lines[idx][idy] == "#":
            break
    else:
        empty_columns.append(idy)

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == "#":
            galaxies_indexes.append((x, y))

for combination in itertools.combinations(galaxies_indexes, 2):
    x_range = (combination[0][0], combination[1][0])
    y_range = (combination[0][1], combination[1][1])
    rows_to_add = len([e for e in empty_rows if max(x_range) > e > min(x_range)])
    columns_to_add = len([e for e in empty_columns if max(y_range) > e > min(y_range)])

    result += (
        abs(combination[1][0] - combination[0][0])
        + abs(combination[1][1] - combination[0][1])
        + (rows_to_add * 999999)
        + (columns_to_add * 999999)
    )

print(result)
