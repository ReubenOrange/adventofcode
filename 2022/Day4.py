import aocd
import typing as t
import re


def Day2Q1(data: t.List[str]) -> int:

    cleaning_subsets = 0

    for pair in data:
        l1, h1, l2, h2 = [int(x) for x in re.split(",|-", pair)]
        cleaning_subsets += l1 >= l2 and h1 <= h2 or l1 <= l2 and h1 >= h2

    return cleaning_subsets


def Day2Q2(data: t.List[str]) -> int:

    cleaning_subsets = 0

    for pair in data:
        l1, h1, l2, h2 = [int(x) for x in re.split(",|-", pair)]
        cleaning_subsets += h1 >= l2 and l1 <= h2

    return cleaning_subsets


if __name__ == "__main__":

    data = aocd.get_data(
        day=4,
        year=2022,
    ).splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
