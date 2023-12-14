from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0

for line in f.readlines():
    min_red = 0
    min_green = 0
    min_blue = 0
    game, data = line.split(": ")
    game_id = int(game.split(" ")[-1])

    cubes_sets = data.rstrip("\n").split("; ")
    for cubes_set in cubes_sets:
        cubes_set = cubes_set.split(", ")
        for cube in cubes_set:
            cube_count, cube_color = cube.split(" ")
            cube_count = int(cube_count)
            if cube_color == "red" and cube_count > min_red:
                min_red = cube_count
            elif cube_color == "green" and cube_count > min_green:
                min_green = cube_count
            elif cube_color == "blue" and cube_count > min_blue:
                min_blue = cube_count

    power = min_red * min_green * min_blue
    result += power

print(result)
