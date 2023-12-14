import re
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")


def is_symbol(char: str) -> bool:
    return not (char.isnumeric() or char == ".")


lines = [
    f".{line.rstrip('\n')}." for line in f.readlines()
]  # add dots at both ends to prevent bound checking
result = 0

for line_index, line in enumerate(lines):
    numbers = re.findall(r"\d+", line)
    number_indexes = []
    for number in numbers:
        start_index = line.find(
            number, number_indexes[-1][1][1] + 1 if number_indexes else 0
        )
        number_indexes.append(
            (int(number), (int(start_index), (int(start_index) + len(number) - 1)))
        )
    for number, indexes in number_indexes:
        start_index, last_index = indexes
        # check if symbol is on the left
        if is_symbol(line[start_index - 1]):
            result += number
            continue
        # check if symbol is on the right
        if is_symbol(line[last_index + 1]):
            result += number
            continue
        # check if symbol is above
        if line_index > 0:
            found = False
            for char in lines[line_index - 1][start_index - 1 : last_index + 2]:
                if is_symbol(char):
                    found = True
                    result += number
                    break
            if found:
                continue
        # check if symbol is below
        if line_index != len(lines) - 1:
            for char in lines[line_index + 1][start_index - 1 : last_index + 2]:
                if is_symbol(char):
                    result += number
                    break

print(result)
