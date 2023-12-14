from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
combinations = {
    "eighthree": "eightthree",
    "eightwo": "eighttwo",
    "oneight": "oneeight",
    "twone": "twoone",
    "threeight": "threeeight",
    "fiveight": "fiveeight",
    "sevenine": "sevennine",
}


result = 0

for line in f.readlines():
    for k, v in combinations.items():
        line = line.replace(k, v)
    for k, v in words.items():
        line = line.replace(k, v)
    line = "".join(c for c in line if c.isnumeric())
    result += int(line[0] + line[-1])

print(result)
