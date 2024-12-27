import aocd
import typing as t
from collections import deque


import re
import itertools


def DayQ1(data: t.List[str]) -> int:

    seq = deque(data)

    print(seq)

    return


def DayQ2(data: t.List[str]) -> int:

    return


if __name__ == "__main__":

    data = aocd.get_data(
        day=20,
        year=2022,
    ).split("\n")

    test_data = """1
2
-3
3
-2
0
4""".split(
        "\n"
    )

    print("Part 1:", DayQ1(test_data))
    # print("Part 2:", DayQ2(data))
