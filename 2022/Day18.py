import aocd
import typing as t


def find_neighbours(cube: t.Tuple[int]) -> int:

    dx = dy = dz = (-1, 1)

    neighbours = set()

    for i in dx:
        neighbours.add((cube[0] + i, cube[1], cube[2]))
    for j in dy:
        neighbours.add((cube[0], cube[1] + j, cube[2]))
    for k in dz:
        neighbours.add((cube[0], cube[1], cube[2] + k))

    return neighbours


def DayQ1(data: t.List[str]) -> int:

    cube_set = set(tuple(int(y) for y in x.split(",")) for x in data)

    surface_area = 0

    for cube in cube_set:

        surface_area += 6 - len(find_neighbours(cube) & cube_set)

    return surface_area


def DayQ2(data: t.List[str]) -> int:

    # find the outer bounds of the box, can make it one larger in every dimension
    # start filling the outside peice by peice
    # when completely filled (size doesn't increase after 1 iteration) then
    # look for all the boxes that are adjacent to one of the outside bits add one for each adjacent face

    cube_set = set(tuple(int(y) for y in x.split(",")) for x in data)

    max_x = max(r[0] for r in cube_set) + 1
    max_y = max(r[1] for r in cube_set) + 1
    max_z = max(r[2] for r in cube_set) + 1

    outer_bounds = (max_x, max_y, max_z)

    outside_points = set([outer_bounds])

    all_points_found = False
    dx = dy = dz = (-1, 1)

    while not all_points_found:

        outside_points_size = len(outside_points)

        outside_points_copy = outside_points.copy()
        for cube in outside_points_copy:

            neighbours = set()

            for i in dx:
                neighbours.add((cube[0] + i, cube[1], cube[2])) if -1 <= cube[
                    0
                ] + i <= max_x else None
            for j in dy:
                neighbours.add((cube[0], cube[1] + j, cube[2])) if -1 <= cube[
                    1
                ] + j <= max_y else None
            for k in dz:
                neighbours.add((cube[0], cube[1], cube[2] + k)) if -1 <= cube[
                    2
                ] + k <= max_z else None

            outside_neighbours = neighbours - cube_set

            outside_points |= outside_neighbours

        if outside_points_size < len(outside_points):
            outside_points_size = len(outside_points)
        else:
            all_points_found = True

    num_outside_points = 0

    for cube in outside_points:

        neighbours = find_neighbours(cube)

        num_outside_points += len(neighbours & cube_set)

    return num_outside_points


if __name__ == "__main__":

    data = aocd.get_data(
        day=18,
        year=2022,
    ).split("\n")

    test_data = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split(
        "\n"
    )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
