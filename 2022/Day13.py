import aocd
import typing as t
from functools import cmp_to_key
from copy import deepcopy


def compare_lists(x: t.List, y: t.List) -> bool:

    # return -1 if in the right order

    # print(" - Compare: {} vs {}".format(str(x), str(y)))

    if type(x) == type(y) == int:

        if x == y:
            return 0  # "Go next"
        elif x < y:
            return -1
        else:
            return 1

    if type(x) == list and type(y) == int:

        return compare_lists(x, [y])

    if type(x) == int and type(y) == list:

        return compare_lists([x], y)

    if type(x) == type(y) == list:

        z = zip(x, y)

        for pair in z:

            outcome = compare_lists(pair[0], pair[1])

            if outcome == -1:
                return -1
            elif outcome == 0:
                continue
            elif outcome == 1:
                return 1

        if len(x) < len(y):
            return -1

        if len(x) > len(y):
            return 1

        if len(x) == len(y):
            return 0

        return None


def DayQ1(data: t.List[str]) -> int:

    correct_indices = []

    for i, two_line in enumerate(data):

        line1, line2 = two_line.split("\n")

        x = eval(line1)
        y = eval(line2)

        if compare_lists(x, y) == -1:
            correct_indices.append(i + 1)

    print(correct_indices)
    return sum(correct_indices)


def DayQ2(data: t.List[str]) -> int:

    signal1 = [[2]]
    signal2 = [[6]]
    all_lists = [signal1, signal2]

    for i, two_line in enumerate(data):

        line1, line2 = two_line.split("\n")

        all_lists.append(eval(line1))
        all_lists.append(eval(line2))

    all_lists_sorted = sorted(all_lists, key=cmp_to_key(compare_lists))

    signal1_size = all_lists_sorted.index(signal1) + 1
    signal2_size = all_lists_sorted.index(signal2) + 1

    return signal1_size * signal2_size


if __name__ == "__main__":

    data = aocd.get_data(
        day=13,
        year=2022,
    ).split("\n\n")

    # data = "[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]".split(
    #    "\n\n"
    # )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
