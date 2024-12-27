import aocd
import typing as t


def Day2Q1(data: t.List[str]) -> int:

    grid = [list(map(int, x)) for x in data]

    num_visible = 0

    # First look up and left
    for i, row in enumerate(grid):

        for j, col in enumerate(row):

            visible = False

            # num_trees_to_left = j
            # num_trees_to_right = len(grid) - j - 1
            # num_trees_to_up = i
            # num_trees_to_down = len(row) - i - 1

            # look left
            visible = all(grid[i][j - jj] < col for jj in range(1, j + 1)) or visible
            # look right
            visible = (
                all(grid[i][j + jj] < col for jj in range(1, len(grid) - j)) or visible
            )
            # look up
            visible = all(grid[i - ii][j] < col for ii in range(1, i + 1)) or visible
            # look down
            visible = (
                all(grid[i + ii][j] < col for ii in range(1, len(row) - i)) or visible
            )

            if visible:
                num_visible += 1

    return num_visible


def Day2Q2(data: t.List[str]) -> int:

    grid = [list(map(int, x)) for x in data]

    vis_grid = [[False] * len(data)] * len(data[0])

    scenic_score = 0

    # Look around each tree position
    for i, row in enumerate(grid):

        for j, col in enumerate(row):

            # [left, right, up, down]
            scenic = [0, 0, 0, 0]
            left_scenic = 0
            right_scenic = 0
            up_scenic = 0
            down_scenic = 0

            # num_trees_to_left = j
            # num_trees_to_right = len(grid) - j - 1
            # num_trees_to_up = i
            # num_trees_to_down = len(row) - i - 1

            # look left
            for jj in range(1, j + 1):
                scenic[0] += 1
                if grid[i][j - jj] >= col:
                    break

            # look right
            for jj in range(1, len(grid) - j):
                scenic[1] += 1
                if grid[i][j + jj] >= col:
                    break

            # look up
            for ii in range(1, i + 1):
                scenic[2] += 1
                if grid[i - ii][j] >= col:
                    break

            # look down
            for ii in range(1, len(row) - i):
                scenic[3] += 1
                if grid[i + ii][j] >= col:
                    break

            if scenic[0] * scenic[1] * scenic[2] * scenic[3] > scenic_score:
                scenic_score = scenic[0] * scenic[1] * scenic[2] * scenic[3]

    return scenic_score


if __name__ == "__main__":

    data = aocd.get_data(
        day=8,
        year=2022,
    ).splitlines()

    # test_data = "30373\n25512\n65332\n33549\n35390\n".splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
