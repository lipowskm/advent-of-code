from pathlib import Path

f = open(Path(__file__).parent / "input.txt")

result = 0
card_mapping = {}

for line in f.readlines():
    line = line.rstrip("\n")
    card, data = line.split(": ")
    card_id = int(card.replace(" ", "").split("d")[1])
    winning_numbers, my_numbers = data.split(" | ")
    winning_numbers = [number for number in winning_numbers.split(" ") if number != ""]
    my_numbers = [number for number in my_numbers.split(" ") if number != ""]

    score = 0

    for number in my_numbers:
        if number not in winning_numbers:
            continue
        score += 1

    card_mapping[card_id] = score


def process_scratchcard(card_id: int) -> None:
    global result
    result += 1
    for i in range(
        card_id + 1, min(card_mapping[card_id] + card_id + 1, len(card_mapping) + 1)
    ):
        process_scratchcard(i)


for k in card_mapping.keys():
    process_scratchcard(k)

print(result)
