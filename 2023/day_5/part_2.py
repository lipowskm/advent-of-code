from multiprocessing import Pool
from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

seeds = f.readline().strip("\n").split(": ")[1].split(" ")
seeds = [[int(seeds[i]), int(seeds[i + 1])] for i in range(0, len(seeds), 2)]

lines = [line.strip("\n") for line in f.readlines() if line != "\n"]
mappings = []

mapping_index = -1

for line in lines:
    if line[0].isalpha():
        mapping_index += 1
        mappings.append([])
    else:
        mappings[mapping_index].append([int(number) for number in line.split(" ")])


def process_data(data: list) -> int:
    result = None
    for seed in range(data[0], data[0] + data[1]):
        final = seed
        for data in mappings:
            for numbers in data:
                if numbers[1] <= final < numbers[1] + numbers[2]:
                    final = final + numbers[0] - numbers[1]
                    break
        if not result:
            result = final
            continue
        if result > final:
            result = final
    return result


if __name__ == "__main__":
    with Pool(10) as p:
        results = p.map(process_data, seeds)

    print(min(results))
