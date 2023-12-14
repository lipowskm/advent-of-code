from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0

for line in f.readlines():
    sequences = [list(reversed([int(e) for e in line.strip("\n").split(" ")]))]
    while len(set(sequences[-1])) != 1:
        sequences.append(
            [
                sequences[-1][i] - sequences[-1][i - 1]
                for i in range(1, len(sequences[-1]))
            ]
        )
    result += sum(e[-1] for e in sequences)

print(result)
