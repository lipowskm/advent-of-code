import functools
from collections import Counter
from pathlib import Path
from typing import Union

f = open(Path(__file__).parent / "input.txt")


class CamelCards:
    def __init__(self, lines: list[str]):
        self.data = self._parse_lines(lines)

    @staticmethod
    def _parse_lines(lines: list[str]) -> list[dict[str, Union[int, str]]]:
        data = []
        for line in lines:
            hand, bid = line.split(" ")
            data.append({"hand": hand, "bid": int(bid)})
        return data

    def get_total_winnings(self) -> int:
        self._rank_data()
        total_winnings = 0
        for i, dataset in enumerate(self.data):
            total_winnings += (i + 1) * dataset["bid"]
        return total_winnings

    def _rank_data(self) -> None:
        for dataset in self.data:
            dataset["type"] = self._get_type(dataset["hand"])
        self.data.sort(key=functools.cmp_to_key(self._compare))

    @staticmethod
    def _compare(dataset_1: dict, dataset_2: dict) -> int:
        if dataset_1["type"] == dataset_2["type"]:
            order = "AKQJT98765432"
            for i in range(0, 5):
                if dataset_1["hand"][i] == dataset_2["hand"][i]:
                    continue
                if order.find(dataset_1["hand"][i]) < order.find(dataset_2["hand"][i]):
                    return 11
                return -1
        if dataset_1["type"] < dataset_2["type"]:
            return 1
        return -1

    @staticmethod
    def _get_type(hand: str) -> int:
        """The lower the type, the stronger the hand is"""
        counts = list(Counter(hand).values())
        if 5 in counts:
            return 1
        elif 4 in counts:
            return 2
        elif 3 in counts and 2 in counts:
            return 3
        elif 3 in counts:
            return 4
        elif counts.count(2) == 2:
            return 5
        elif 2 in counts:
            return 6
        else:
            return 7


c = CamelCards(f.readlines())
print(c.get_total_winnings())
