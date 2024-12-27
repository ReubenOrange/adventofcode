import aocd
import typing as t


def DayQ1(data: t.List[str]) -> int:

    rock0 = {(0, 0), (1, 0), (2, 0), (3, 0)}
    rock1 = {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}
    rock2 = {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}
    rock3 = {(0, 0), (0, 1), (0, 2), (0, 3)}
    rock4 = {(0, 0), (0, 1), (1, 0), (1, 1)}
    rocks = [rock0, rock1, rock2, rock3, rock4]

    # the initial floor
    stopped_rocks = set([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)])

    highest_point = -1

    # air count
    j = 0

    highest_point_list = []
    num_rocks = 2022

    for i in range(num_rocks):

        start_pos = {(x + 2, y + highest_point + 4) for (x, y) in rocks[i % 5]}
        rock = {(x + 2, y + highest_point + 4) for (x, y) in rocks[i % 5]}
        at_bottom = False

        while not at_bottom:

            # pushed by air left or right
            dx = 1 if data[j % len(data)] == ">" else -1
            new_pos = {(x + dx, y) for (x, y) in rock}

            # update rock to new position if it doesn't hit a wall or any stopped rocks
            if not bool(new_pos & stopped_rocks) and all(
                0 <= p[0] <= 6 for p in new_pos
            ):
                rock = new_pos

            j += 1

            # fall 1 unit
            new_pos = {(x, y - 1) for (x, y) in rock}

            # if we have reached the stopping position
            if new_pos & stopped_rocks:

                at_bottom = True
                stopped_rocks |= rock
                highest_point = max(p[1] for p in stopped_rocks)
                highest_point_list.append(highest_point)

            # if we haven't reached the stopping position
            else:
                rock = new_pos

            if len(stopped_rocks) > 1000:

                stopped_rocks = set(
                    sorted(list(stopped_rocks), key=lambda f: f[1])[-1000:]
                )

    highest_point = max(p[1] for p in stopped_rocks)

    return highest_point + 1


def DayQ2(data: t.List[str]) -> int:

    rock0 = {(0, 0), (1, 0), (2, 0), (3, 0)}
    rock1 = {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}
    rock2 = {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}
    rock3 = {(0, 0), (0, 1), (0, 2), (0, 3)}
    rock4 = {(0, 0), (0, 1), (1, 0), (1, 1)}
    rocks = [rock0, rock1, rock2, rock3, rock4]

    highest_point = -1
    highest_point_list = []
    stopped_rocks = set([(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)])
    j = 0  # wind blow counter

    num_rocks = 10000

    for i in range(num_rocks):

        # each rock appears so that the left edge is 2 units from the left wall (at -1), and 3 units above the current highest point
        rock = {(x + 2, y + highest_point + 4) for (x, y) in rocks[i % 5]}
        at_bottom = False

        while not at_bottom:

            j += 1
            # pushed by air left or right
            dx = 1 if data[j % len(data)] == ">" else -1
            new_pos = {(x + dx, y) for (x, y) in rock}

            # update rock to new position if it doesn't hit any walls or stopped rocks
            if not (new_pos & stopped_rocks) and all(0 <= p[0] <= 6 for p in new_pos):
                rock = new_pos

            # try to fall 1 unit
            new_pos = {(x, y - 1) for (x, y) in rock}

            # stop if we hit any stopped rocks
            if new_pos & stopped_rocks:
                at_bottom = True
                stopped_rocks |= rock
                highest_point = max(p[1] for p in stopped_rocks)
                highest_point_list.append(highest_point)

            # otherwise, rock falls 1 unit
            else:
                rock = new_pos

            # prevent the set of stopped rocks from getting too big, trim to 500 and assume that is enough to close all gaps
            if len(stopped_rocks) > 5000:
                stopped_rocks = set(
                    sorted(list(stopped_rocks), key=lambda f: f[1])[-500:]
                )

    # now we need to do something with the highest point list, try to find a repeating pattern that we can use
    rep_len = 1
    k = 0
    i = 2

    # build highest point differences list
    highest_point_diffs = [
        highest_point_list[x] - highest_point_list[x - 1]
        for x in range(1, len(highest_point_list))
    ]

    # assume that the length of the sequence will be more than 20
    while rep_len <= 20 and i < len(highest_point_diffs) / 2:

        for k in range(0, i):
            if (
                highest_point_diffs[k:i] == highest_point_diffs[i : i * 2 - k]
                and i - k > rep_len
            ):
                assert len(highest_point_diffs[k:i]) == len(
                    highest_point_diffs[i : i * 2 - k]
                )
                rep_len = i - k
                rep_start = k
                break

        i += 1

    # a1 is the height up to the first repetition
    # a2 is the height of the repeating section
    # a3 is the height of the last section
    # T is a trillion
    T = 1000000000000

    a1 = highest_point_list[k]

    a2 = ((T - rep_start) // rep_len) * (
        highest_point_list[rep_start + rep_len] - highest_point_list[rep_start]
    )

    a3 = (
        highest_point_list[rep_start - 2 + ((T - rep_start) % rep_len)]
        - highest_point_list[rep_start]
    )

    return a1 + a2 + a3 + 1


if __name__ == "__main__":

    data = aocd.get_data(
        day=17,
        year=2022,
    )

    test_data = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
