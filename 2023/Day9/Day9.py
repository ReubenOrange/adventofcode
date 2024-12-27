import aocd
import typing as t


def sign(n: int) -> int:
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def Day2Q1(data: t.List[str]) -> int:

    moves = [[0, 0] for x in data]

    for i, x in enumerate(data):
        moves[i][0] = x.split(" ")[0]
        moves[i][1] = int(x.split(" ")[1])

    head_pos = [4000, 4000]  # [row, col]
    tail_pos = [4000, 4000]  # [row, col]
    visited_grid = [[False] * 8000 for i in range(8000)]
    visited_grid[4000][4000] = True
    visited_count = 1

    for move in moves:

        if move[0] == "L":
            for i in range(move[1]):
                head_pos[1] -= 1
                if (head_pos[0] - tail_pos[0]) ** 2 + (
                    head_pos[1] - tail_pos[1]
                ) ** 2 > 2:
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = head_pos[1] + 1
                    if visited_grid[tail_pos[0]][tail_pos[1]] == False:
                        visited_grid[tail_pos[0]][tail_pos[1]] = True
                        visited_count += 1

        if move[0] == "R":
            for i in range(move[1]):
                head_pos[1] += 1
                if (head_pos[0] - tail_pos[0]) ** 2 + (
                    head_pos[1] - tail_pos[1]
                ) ** 2 > 2:
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = head_pos[1] - 1
                    if visited_grid[tail_pos[0]][tail_pos[1]] == False:
                        visited_grid[tail_pos[0]][tail_pos[1]] = True
                        visited_count += 1

        if move[0] == "U":
            for i in range(move[1]):
                head_pos[0] -= 1
                if (head_pos[0] - tail_pos[0]) ** 2 + (
                    head_pos[1] - tail_pos[1]
                ) ** 2 > 2:
                    tail_pos[0] = head_pos[0] + 1
                    tail_pos[1] = head_pos[1]
                    if visited_grid[tail_pos[0]][tail_pos[1]] == False:
                        visited_grid[tail_pos[0]][tail_pos[1]] = True
                        visited_count += 1

        if move[0] == "D":
            for i in range(move[1]):
                head_pos[0] += 1
                if (head_pos[0] - tail_pos[0]) ** 2 + (
                    head_pos[1] - tail_pos[1]
                ) ** 2 > 2:
                    tail_pos[0] = head_pos[0] - 1
                    tail_pos[1] = head_pos[1]
                    if visited_grid[tail_pos[0]][tail_pos[1]] == False:
                        visited_grid[tail_pos[0]][tail_pos[1]] = True
                        visited_count += 1

    return visited_count


def Day2Q2(data: t.List[str]) -> int:

    moves = [[0, 0] for x in data]
    move_dict = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    for i, x in enumerate(data):

        moves[i][0] = move_dict[x.split(" ")[0]]
        moves[i][1] = int(x.split(" ")[1])

    # just make a huge grid, and put the rope in the middle
    rope = [[4000, 4000] for i in range(10)]  # [row, col]
    visited_grid = [[False] * 8000 for i in range(8000)]
    visited_grid[4000][4000] = True
    visited_count = 1

    for move in moves:

        for i in range(move[1]):

            rope[0][0] += move[0][0]
            rope[0][1] += move[0][1]

            for j in range(1, len(rope)):

                if (
                    (rope[j - 1][0] - rope[j][0]) ** 2
                    + (rope[j - 1][1] - rope[j][1]) ** 2
                ) in [4, 5, 8]:
                    rope[j][0] += sign(rope[j - 1][0] - rope[j][0])
                    rope[j][1] += sign(rope[j - 1][1] - rope[j][1])
            if visited_grid[rope[-1][0]][rope[-1][1]] == False:
                visited_grid[rope[-1][0]][rope[-1][1]] = True
                visited_count += 1

    return visited_count


if __name__ == "__main__":

    data = aocd.get_data(
        day=9,
        year=2022,
    ).splitlines()

    # data = "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n".splitlines()
    # data = "R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20\n".splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
