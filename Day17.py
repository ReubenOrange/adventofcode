import aocd
import typing as t


def create_point_set(initial_state: t.List[t.List[str]]) -> t.Set[tuple]:

    point_set = set()

    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if initial_state[i][j] == "#":
                point_set.add((i, j, 0))

    return point_set


def create_hyper_point_set(initial_state: t.List[t.List[str]]) -> t.Set[tuple]:

    point_set = set()

    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if initial_state[i][j] == "#":
                point_set.add((i, j, 0, 0))

    return point_set


def get_neighbours(point: tuple()) -> set(tuple()):

    neighbour_positions = set()

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                neighbour_positions.add((point[0] + i, point[1] + j, point[2] + k))

    neighbour_positions.remove((point[0], point[1], point[2]))

    return neighbour_positions


def get_hyper_neighbours(point: tuple()) -> set(tuple()):

    neighbour_positions = set()

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    neighbour_positions.add(
                        (point[0] + i, point[1] + j, point[2] + k, point[3] + l)
                    )

    neighbour_positions.remove((point[0], point[1], point[2], point[3]))

    return neighbour_positions


def Day17Q1(initial_state: t.List[t.List[str]]) -> int:

    point_set = create_point_set(initial_state)

    cycle = 0

    while cycle < 6:

        new_point_set = set()
        full_neighbour_set = set()

        for point in point_set:

            full_neighbour_set.add(point)
            point_neighbours = get_neighbours(point)

            for point_neighbour in point_neighbours:

                full_neighbour_set.add(point_neighbour)

        for neighbour in full_neighbour_set:

            neighbour_neighbours = get_neighbours(neighbour)
            active_neighbours = len(neighbour_neighbours & point_set)

            if (neighbour in point_set and active_neighbours == 2) or active_neighbours == 3:
                new_point_set.add(neighbour)

        point_set = new_point_set

        cycle += 1

    return len(point_set)


def Day17Q2(initial_state: t.List[t.List[str]]) -> int:

    point_set = create_hyper_point_set(initial_state)

    cycle = 0

    while cycle < 6:

        new_point_set = set()
        full_neighbour_set = set()

        for point in point_set:

            full_neighbour_set.add(point)
            point_neighbours = get_hyper_neighbours(point)

            for point_neighbour in point_neighbours:
                full_neighbour_set.add(point_neighbour)

        for neighbour in full_neighbour_set:

            neighbour_neighbours = get_hyper_neighbours(neighbour)
            active_neighbours = len(neighbour_neighbours & point_set)

            if (neighbour in point_set and active_neighbours == 2) or active_neighbours == 3:
                new_point_set.add(neighbour)

        point_set = new_point_set

        cycle += 1

    return len(point_set)


if __name__ == "__main__":

    initial_state = [list(x.strip()) for x in open("input.txt")]

    # initial_state = [list(x) for x in aocd.get_data(day=17, year=2020).splitlines()]

    print("Part 1:", Day17Q1(initial_state))
    print("Part 2:", Day17Q2(initial_state))