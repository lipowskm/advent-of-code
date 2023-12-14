from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0

pipes_directions_mapping = {
    "|": ("N", "S"),
    "-": ("W", "E"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
}

direction_indexes_mapping = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}


def get_start_direction(lines: list[list[str]], start_position: tuple[int, int]) -> str:
    for direction, indexes in direction_indexes_mapping.items():
        row_index = start_position[0] + indexes[0]
        column_index = start_position[1] + indexes[1]
        if row_index == -1 or column_index == -1:
            continue
        for pipe, possible_directions in pipes_directions_mapping.items():
            if (
                lines[row_index][column_index] == pipe
                and direction in possible_directions
            ):
                return direction


def get_reverse_direction(direction: str):
    if direction == "N":
        return "S"
    if direction == "S":
        return "N"
    if direction == "E":
        return "W"
    if direction == "W":
        return "E"


lines: list[list[str]] = []
start_position = None

for idx, line in enumerate(f.readlines()):
    lines.append(list(line.strip("\n")))
    if "S" in line:
        start_position = (idx, line.find("S"))

last_position = start_position
next_direction = get_start_direction(lines, start_position)
last_direction = get_reverse_direction(next_direction)
current_position = tuple(
    map(lambda x, y: x + y, last_position, direction_indexes_mapping[next_direction])
)
current_pipe = lines[current_position[0]][current_position[1]]

result = 1

while current_pipe != "S":
    next_direction = tuple(
        direction
        for direction in pipes_directions_mapping[current_pipe]
        if direction != last_direction
    )[0]
    last_direction = get_reverse_direction(next_direction)
    last_position = current_position
    current_position = tuple(
        map(
            lambda x, y: x + y,
            current_position,
            direction_indexes_mapping[next_direction],
        )
    )
    current_pipe = lines[current_position[0]][current_position[1]]
    result += 1

print(result // 2)
