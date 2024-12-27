import aocd
import typing as t


def Day2Q1(data: t.List[str]) -> int:

    for i, c in enumerate(data):
        if i < 3:
            continue
        elif len(set(data[i - 3 : i + 1])) == len(data[i - 3 : i + 1]):
            return i + 1


def Day2Q2(data: t.List[str]) -> int:

    for i, c in enumerate(data):
        if i < 13:
            continue
        elif len(set(data[i - 13 : i + 1])) == len(data[i - 13 : i + 1]):
            return i + 1


if __name__ == "__main__":

    data = aocd.get_data(
        day=6,
        year=2022,
    )

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
