import re
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")


def transform(substring: str, line: str, char_index: int) -> list[int]:
    numbers = []
    if re.fullmatch("[0-9][0-9][0-9]", substring):
        numbers.append(int(substring))
    elif re.fullmatch("[0-9][0-9][^0-9]", substring):
        number = int(
            "".join(c for c in line[char_index - 2 : char_index + 1] if c.isnumeric())
        )
        numbers.append(number)
    elif re.fullmatch("[0-9][^0-9][^0-9]", substring):
        number = [line[char_index - 1]]
        c = 2
        while True:
            if line[char_index - c].isnumeric():
                number.insert(0, line[char_index - c])
                c += 1
            else:
                break
        number = int("".join(number))
        numbers.append(number)
    elif re.fullmatch("[^0-9][0-9][0-9]", substring):
        number = int(
            "".join(c for c in line[char_index : char_index + 3] if c.isnumeric())
        )
        numbers.append(number)
    elif re.fullmatch("[^0-9][^0-9][0-9]", substring):
        number = [line[char_index + 1]]
        c = 2
        while True:
            if line[char_index + c].isnumeric():
                number.append(line[char_index + c])
                c += 1
            else:
                break
        number = int("".join(number))
        numbers.append(number)
    elif re.fullmatch("[^0-9][0-9][^0-9]", substring):
        numbers.append(int(line[char_index]))
    elif re.fullmatch("[0-9][^0-9][0-9]", substring):
        number_1 = [line[char_index - 1]]
        c = 2
        while True:
            if line[char_index - c].isnumeric():
                number_1.insert(0, line[char_index - c])
                c += 1
            else:
                break
        number_1 = int("".join(number_1))

        number_2 = [line[char_index + 1]]
        c = 2
        while True:
            if line[char_index + c].isnumeric():
                number_2.append(line[char_index + c])
                c += 1
            else:
                break
        number_2 = int("".join(number_2))

        numbers.append(number_1)
        numbers.append(number_2)
    return numbers


lines = [
    f".{line.rstrip('\n')}." for line in f.readlines()
]  # add dots at both ends to prevent bound checking
result = 0

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char != "*":
            continue
        numbers = []
        # check if number is on the left
        if line[char_index - 1].isnumeric():
            number = [line[char_index - 1]]
            c = 2
            while True:
                if line[char_index - c].isnumeric():
                    number.insert(0, line[char_index - c])
                    c += 1
                else:
                    break
            number = int("".join(number))
            numbers.append(number)
        # check if number is on the right
        if line[char_index + 1].isnumeric():
            number = [line[char_index + 1]]
            c = 2
            while True:
                if line[char_index + c].isnumeric():
                    number.append(line[char_index + c])
                    c += 1
                else:
                    break
            number = int("".join(number))
            numbers.append(number)
        # check if numbers are above
        if line_index > 0:
            line_above = lines[line_index - 1]
            substring = line_above[char_index - 1 : char_index + 2]
            numbers.extend(transform(substring, line_above, char_index))
        # check if numbers are below
        if line_index != len(lines) - 1:
            line_below = lines[line_index + 1]
            substring = line_below[char_index - 1 : char_index + 2]
            numbers.extend(transform(substring, line_below, char_index))

        if len(numbers) == 2:
            result += numbers[0] * numbers[1]


print(result)
