from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = None

seeds = [int(e) for e in f.readline().strip("\n").split(": ")[1].split(" ")]
lines = [line.strip("\n") for line in f.readlines() if line != "\n"]
mappings = []

mapping_index = -1

for line in lines:
    if line[0].isalpha():
        mapping_index += 1
        mappings.append([])
    else:
        mappings[mapping_index].append([int(number) for number in line.split(" ")])


for seed in seeds:
    final = seed
    for data in mappings:
        for numbers in data:
            if numbers[1] <= final < numbers[1] + numbers[2]:
                final = final + numbers[0] - numbers[1]
                break
    if result is None:
        result = final
        continue
    if result > final:
        result = final

print(result)
