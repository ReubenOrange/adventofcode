import aocd
import typing as t


def DayQ1(data: t.List[str]) -> int:

    grid_list = []
    for line in data:

        grid_list.append([])
        for block in line.split(" -> "):

            x, y = block.split(",")
            grid_list[-1].append((int(x), int(y)))

    print(grid_list)

    filled_grid_dict = dict()
    for line in grid_list:

        # 486,40 -> 486,44 -> 482,44 -> 482,49 -> 499,49 -> 499,44 -> 491,44 -> 491,40
        for i in range(1, len(line)):

            lowx = min(line[i][0], line[i - 1][0])
            highx = max(line[i][0], line[i - 1][0])

            lowy = min(line[i][1], line[i - 1][1])
            highy = max(line[i][1], line[i - 1][1])

            for j in range(lowx, highx + 1):
                filled_grid_dict[(j, line[i][1])] = "#"

            for j in range(lowy, highy + 1):
                filled_grid_dict[(line[i][0], j)] = "#"

    for y in range(500):
        for x in range(400, 600):
            if (x, y) in filled_grid_dict:
                print("#", end="\n" if x == 599 else "")
            else:
                print(".", end="\n" if x == 599 else "")

    # sand start falling from point 500,0

    lowest_point = max(key[1] for key in filled_grid_dict)

    filled_sand_dict = dict()
    all_stable = False

    while not all_stable:

        # sand start falling from point 500,0
        sand = [500, 0]

        spot_found = False

        while not spot_found:

            if sand[1] > lowest_point:  # sand has fallen to the bottom
                all_stable = True
                break
            # Go down
            elif (sand[0], sand[1] + 1) not in filled_sand_dict and (
                sand[0],
                sand[1] + 1,
            ) not in filled_grid_dict:
                sand[1] += 1
                print("Go down")
            # Go left
            elif (sand[0] - 1, sand[1] + 1) not in filled_sand_dict and (
                sand[0] - 1,
                sand[1] + 1,
            ) not in filled_grid_dict:
                sand[0] -= 1
                sand[1] += 1
            # Go right
            elif (sand[0] + 1, sand[1] + 1) not in filled_sand_dict and (
                sand[0] + 1,
                sand[1] + 1,
            ) not in filled_grid_dict:
                sand[0] += 1
                sand[1] += 1

                print(
                    "filled_sand_dict[sand[0], sand[1]]:",
                    (sand[0], sand[1]),
                )

    return len(filled_sand_dict)


def DayQ2(data: t.List[str]) -> int:

    grid_list = []
    for line in data:

        grid_list.append([])
        for block in line.split(" -> "):

            x, y = block.split(",")
            grid_list[-1].append((int(x), int(y)))

    print(grid_list)

    filled_grid_dict = dict()
    for line in grid_list:

        # 486,40 -> 486,44 -> 482,44 -> 482,49 -> 499,49 -> 499,44 -> 491,44 -> 491,40
        for i in range(1, len(line)):

            lowx = min(line[i][0], line[i - 1][0])
            highx = max(line[i][0], line[i - 1][0])

            lowy = min(line[i][1], line[i - 1][1])
            highy = max(line[i][1], line[i - 1][1])

            for j in range(lowx, highx + 1):
                filled_grid_dict[(j, line[i][1])] = "#"

            for j in range(lowy, highy + 1):
                filled_grid_dict[(line[i][0], j)] = "#"

    for y in range(500):
        for x in range(400, 600):
            if (x, y) in filled_grid_dict:
                print("#", end="\n" if x == 599 else "")
            else:
                print(".", end="\n" if x == 599 else "")

    # sand start falling from point 500,0

    lowest_point = max(key[1] for key in filled_grid_dict)

    filled_sand_dict = dict()
    all_stable = False

    while not all_stable:

        # sand start falling from point 500,0
        sand = [500, 0]

        spot_found = False

        while not spot_found:

            if (500, 0) in filled_sand_dict:
                all_stable = True
                break
            elif sand[1] == lowest_point + 2:
                filled_grid_dict[
                    sand[0], sand[1]
                ] = "#"  # if we reached the bottom platform, add more platform
                spot_found = True
            elif (sand[0], sand[1] + 1) not in filled_sand_dict and (
                sand[0],
                sand[1] + 1,
            ) not in filled_grid_dict:
                sand[1] += 1
            elif (sand[0] - 1, sand[1] + 1) not in filled_sand_dict and (
                sand[0] - 1,
                sand[1] + 1,
            ) not in filled_grid_dict:
                sand[0] -= 1
                sand[1] += 1
            elif (sand[0] + 1, sand[1] + 1) not in filled_sand_dict and (
                sand[0] + 1,
                sand[1] + 1,
            ) not in filled_grid_dict:
                sand[0] += 1
                sand[1] += 1
            else:
                filled_sand_dict[sand[0], sand[1]] = "#"
                spot_found = True
                print(
                    "filled_sand_dict[sand[0], sand[1]]:",
                    (sand[0], sand[1]),
                )

    return len(filled_sand_dict)


if __name__ == "__main__":

    data = aocd.get_data(
        day=14,
        year=2022,
    ).split("\n")

    test_data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split(
        "\n"
    )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
