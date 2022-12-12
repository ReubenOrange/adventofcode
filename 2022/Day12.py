import aocd
import typing as t
from string import ascii_lowercase


def shortest_path(
    data: t.List[t.List[str]], start: t.Tuple[int], end: t.Tuple[int]
) -> int:

    visited_points = set([start])
    possible_points = [set([start])]

    for i in range(1, len(data) * len(data[0])):

        possible_points.append(set())

        for pos in possible_points[i - 1]:

            go_from = pos  # e.g. (20,0)

            go_from_height = ascii_lowercase.find(data[pos[0]][pos[1]])

            # up down left right
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for direction in directions:
                y = go_from[0] + direction[0]
                x = go_from[1] + direction[1]

                if 0 <= y < len(data) and 0 <= x < len(data[0]):

                    go_to_height = ascii_lowercase.find(data[y][x])
                    if go_to_height - go_from_height <= 1:
                        new_point = (
                            go_from[0] + direction[0],
                            go_from[1] + direction[1],
                        )
                        if new_point not in visited_points:
                            possible_points[i].add(new_point)
                            visited_points.add(new_point)
                            if new_point == end:
                                return i

    return len(data) * len(data[0])  # max possible path length


def find_start_end(data: t.List[t.List[str]]):

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == "S":
                start = (i, j)
            if col == "E":
                end = (i, j)

    data[start[0]][start[1]] = "a"  # NOTE - this edits the list
    data[end[0]][end[1]] = "z"

    return start, end


def DayQ1(data: t.List[t.List[str]]) -> int:

    start, end = find_start_end(data)

    return shortest_path(data, start, end)


def DayQ2(data: t.List[str]) -> int:

    starting_positions = [
        (i, j)
        for i in range(len(data))
        for j in range(len(data[0]))
        if data[i][j] == "S" or data[i][j] == "a"
    ]

    _, end = find_start_end(data)

    path_lengths = [shortest_path(data, start, end) for start in starting_positions]

    return min(path for path in path_lengths if path is not None)


if __name__ == "__main__":

    data = aocd.get_data(
        day=12,
        year=2022,
    ).split("\n")

    # data = "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi".split("\n")

    print("Part 1:", DayQ1([list(row) for row in data]))
    print("Part 2:", DayQ2([list(row) for row in data]))
