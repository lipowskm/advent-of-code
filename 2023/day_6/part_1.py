import re
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")


def parse_file(lines: list[str]) -> list[dict[str, int]]:
    time, distance = (re.findall(r"\d+", line) for line in lines)
    return [{"time": int(e[0]), "distance": int(e[1])} for e in zip(time, distance)]


result = 1

for data in parse_file(f.readlines()):
    total = 0
    time, distance = data["time"], data["distance"]
    for i in range(0, time + 1):
        if i * (time - i) > distance:
            total += 1
    result = result * total

print(result)
