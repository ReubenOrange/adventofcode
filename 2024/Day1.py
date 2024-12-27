import aocd
import typing as t


def Q1(lines: t.List[str]) -> int:

    sum = 0
    x1_list = []
    x2_list = []

    for line in lines:
        x1, x2 = line.split()
        x1_list += [int(x1)]
        x2_list += [int(x2)]

    x1_list.sort()
    x2_list.sort()

    for x1, x2 in zip(x1_list, x2_list):
        sum += abs(x1 - x2)

    return sum


def Q2(lines: t.List[str]) -> int:

    sim_score = 0
    x1_list = []
    x2_list = []

    for line in lines:
        x1, x2 = line.split()
        x1_list += [int(x1)]
        x2_list += [int(x2)]

    for x1 in x1_list:
        for x2 in x2_list:
            if x1 == x2:
                sim_score += x1

    return sim_score


if __name__ == "__main__":

    lines = aocd.get_data(day=1, year=2024).split("\n")

    print("Part 1:", Q1(lines))
    print("Part 2:", Q2(lines))
