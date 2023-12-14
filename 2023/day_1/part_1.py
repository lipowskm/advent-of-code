from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0

for line in f.readlines():
    line = "".join(c for c in line if c.isnumeric())
    result += int(line[0] + line[-1])

print(result)
