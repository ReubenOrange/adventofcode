import aocd
import typing as t
import string


def Day2Q1(data: t.List[str]) -> int:

    stack = data[0]
    moves = data[1]

    stack_list = [[] for _ in range(9)]
    # NOT [[]] * 9

    for r, row in enumerate(stack.splitlines()):
        for c, col in enumerate(row):
            if row[c] in string.ascii_letters:
                stack_list[int((c - 1) / 4)].append(row[c])

    for move in moves.splitlines():

        _, num_boxes, _, move_from, _, move_to = move.split(" ")

        for i in range(int(num_boxes)):
            stack_list[int(move_to) - 1].insert(
                0, stack_list[int(move_from) - 1].pop(0)
            )

    return "".join([b[0] for b in stack_list])


def Day2Q2(data: t.List[str]) -> int:

    stack = data[0]
    moves = data[1]

    stack_list = [[] for _ in range(9)]
    # NOT [[]] * 9

    for r, row in enumerate(stack.splitlines()):
        for c, col in enumerate(row):
            if row[c] in string.ascii_letters:
                stack_list[int((c - 1) / 4)].append(row[c])

    for move in moves.splitlines():

        _, num_boxes, _, move_from, _, move_to = move.split(" ")

        temp_list = []

        for i in range(int(num_boxes)):

            temp_list.append(stack_list[int(move_from) - 1].pop(0))

        for i in range(int(num_boxes)):

            stack_list[int(move_to) - 1].insert(0, temp_list.pop())

    return "".join([b[0] for b in stack_list])


if __name__ == "__main__":

    data = aocd.get_data(
        day=5,
        year=2022,
    ).split("\n\n")

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
