import aocd
import typing as t


def Day2Q1(directions: t.List[t.List[str]]) -> int:

    # [horizonal, vertical]
    direction_dict = {"forward": [1, 0], "up": [0, -1], "down": [0, 1]}

    h = sum(direction_dict[d[0]][0] * int(d[1]) for d in directions)
    v = sum(direction_dict[d[0]][1] * int(d[1]) for d in directions)

    return h * v


def Day2Q2(directions: t.List[t.List[str]]) -> int:

    # [horizonal, vertical]
    direction_dict = {"forward": [1, 0], "up": [0, -1], "down": [0, 1]}
    aim = 0
    h = 0
    v = 0

    for d in directions:
        h += direction_dict[d[0]][0] * int(d[1])
        v += direction_dict[d[0]][0] * int(d[1]) * aim
        aim += direction_dict[d[0]][1] * int(d[1])

    return h * v


if __name__ == "__main__":

    data = aocd.get_data(day=1, year=2021).splitlines()
    directions = [x.split() for x in data]

    print("Part 1:", Day2Q1(directions))
    print("Part 2:", Day2Q2(directions))
