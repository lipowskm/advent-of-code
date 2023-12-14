from itertools import cycle
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

directions = [0 if direction == "L" else 1 for direction in f.readline().strip("\n")]
nodes_mapping = {}

for line in f.readlines():
    if line == "\n":
        continue
    line = line.strip("\n")
    start_node, end_nodes = line.split(" = ")
    nodes_mapping[start_node] = end_nodes.replace("(", "").replace(")", "").split(", ")


current_node = "AAA"
result = 0

for direction in cycle(directions):
    result += 1
    if nodes_mapping[current_node][direction] == "ZZZ":
        break
    current_node = nodes_mapping[current_node][direction]

print(result)
