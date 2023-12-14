import re
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")


def parse_file(lines: list[str]) -> dict[str, int]:
    time, distance = (int("".join(re.findall(r"\d+", line))) for line in lines)
    return {"time": time, "distance": distance}


result = 0

data = parse_file(f.readlines())
time, distance = data["time"], data["distance"]

min_time, max_time = 0, 0
for i in range(0, time + 1):
    if i * (time - i) > distance:
        min_time = i
        break
for i in range(time, min_time, -1):
    if i * (time - i) > distance:
        max_time = i
        break

print(max_time - min_time + 1)
