from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

result = 0

for line in f.readlines():
    game_possible = True
    game, data = line.split(": ")
    game_id = int(game.split(" ")[-1])

    cubes_sets = data.rstrip("\n").split("; ")
    for cubes_set in cubes_sets:
        if not game_possible:
            break
        cubes_set = cubes_set.split(", ")
        for cube in cubes_set:
            cube_count, cube_color = cube.split(" ")
            cube_count = int(cube_count)
            if (
                (cube_color == "red" and cube_count > MAX_RED)
                or (cube_color == "green" and cube_count > MAX_GREEN)
                or (cube_color == "blue" and cube_count > MAX_BLUE)
            ):
                game_possible = False
                break
    if game_possible:
        result += game_id

print(result)
