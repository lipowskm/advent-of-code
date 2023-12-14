from itertools import cycle
from math import lcm
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


current_nodes = [key for key in nodes_mapping.keys() if key.endswith("A")]
path_lenghts = []

for idx in range(0, len(current_nodes)):
    length = 0
    for direction in cycle(directions):
        length += 1
        next_node = nodes_mapping[current_nodes[idx]][direction]
        if next_node.endswith("Z"):
            path_lenghts.append(length)
            break
        current_nodes[idx] = next_node

print(lcm(*path_lenghts))
