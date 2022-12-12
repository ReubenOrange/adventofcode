import aocd
import typing as t
from math import floor


def DayQ1(data: t.List[str]) -> int:

    monkey_list = []
    inspections = [0] * len(data)
    for monkey in data:

        M = monkey.splitlines()
        M_number = int(M[0][7])
        M_items = [int(_) for _ in M[1][18:].split(", ")]
        M_op1, M_op2, M_op3 = M[2][19:].split(" ")
        M_test = int(M[3][21:])
        M_true = int(M[4][29:])
        M_false = int(M[5][30:])

        monkey_list.append(
            [M_number, M_items, M_op1, M_op2, M_op3, M_test, M_true, M_false]
        )

    for _ in range(20):

        for i, monkey in enumerate(monkey_list):

            for _ in range(len(monkey[1])):

                # inspect
                item = monkey[1].pop()
                old = item
                item = eval(monkey[2] + monkey[3] + monkey[4])
                item = floor(item / 3)
                inspections[i] += 1

                # test
                # throw
                if item % monkey[5] == 0:
                    monkey_list[monkey[6]][1] = monkey_list[monkey[6]][1] + [item]
                else:
                    monkey_list[monkey[7]][1] = monkey_list[monkey[7]][1] + [item]

    sorted_inspections = sorted(inspections)
    return sorted_inspections[-1] * sorted_inspections[-2]


def DayQ2(data: t.List[str]) -> int:

    monkey_list = []
    inspections = [0] * len(data)
    for monkey in data:

        M = monkey.splitlines()
        M_number = int(M[0][7])
        M_items = [int(_) for _ in M[1][18:].split(", ")]
        M_op1, M_op2, M_op3 = M[2][19:].split(" ")
        M_test = int(M[3][21:])
        M_true = int(M[4][29:])
        M_false = int(M[5][30:])

        monkey_list.append(
            [M_number, M_items, M_op1, M_op2, M_op3, M_test, M_true, M_false]
        )

    divisor = 1
    for monkey in monkey_list:
        divisor *= monkey[5]

    for _ in range(10000):

        # print(_)
        # print(monkey_list[0][1])

        for i, monkey in enumerate(monkey_list):

            for _ in range(len(monkey[1])):

                # inspect
                item = monkey[1].pop()
                old = item
                item = eval(monkey[2] + monkey[3] + monkey[4])

                item = item % divisor
                inspections[i] += 1

                # test
                # throw
                if item % monkey[5] == 0:
                    monkey_list[monkey[6]][1] = monkey_list[monkey[6]][1] + [item]
                else:
                    monkey_list[monkey[7]][1] = monkey_list[monkey[7]][1] + [item]

    sorted_inspections = sorted(inspections)
    return sorted_inspections[-1] * sorted_inspections[-2]


if __name__ == "__main__":

    data = aocd.get_data(
        day=11,
        year=2022,
    ).split("\n\n")

    # data = "Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1\n".split(
    #    "\n\n"
    # )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
