from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0

for line in f.readlines():
    line = line.rstrip("\n")
    data = line.split(": ")[1]
    winning_numbers, my_numbers = data.split(" | ")
    winning_numbers = [number for number in winning_numbers.split(" ") if number != ""]
    my_numbers = [number for number in my_numbers.split(" ") if number != ""]

    score = 0

    for number in my_numbers:
        if number not in winning_numbers:
            continue
        if not score:
            score = 1
        else:
            score = score * 2

    result += score

print(result)
