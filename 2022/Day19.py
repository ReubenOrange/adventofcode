import aocd
import typing as t
import re
import itertools


def parse_input(data: t.List[str]) -> t.List:

    robot_list = []

    for line in data:
        m = re.match(
            "Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
            line,
        )

        ore_rc = int(m.group(1))
        clay_rc = int(m.group(2))
        obsidian_rc_ore = int(m.group(3))
        obsidian_rc_clay = int(m.group(4))
        geode_rc_ore = int(m.group(5))
        geode_rc_obsidian = int(m.group(6))

        robot_list.append(
            (
                ore_rc,
                clay_rc,
                obsidian_rc_ore,
                obsidian_rc_clay,
                geode_rc_ore,
                geode_rc_obsidian,
            )
        )

    return robot_list


def get_next(position: t.Tuple[int], costs: t.Tuple[int]) -> t.Set[tuple]:

    # here we take a single position, and return all the possible next positions
    # 1. Add the option of building nothing
    # 2. Check if we can afford an ore robot, if we can, add the option of building it
    # 3. Check if we can afford each other robot, if we can, add the option of building it

    # Maybe part 2 will be where you can build as many robots as you like each minute

    (
        ore,
        clay,
        obsidian,
        geode,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ) = position

    (
        ore_rc,
        clay_rc,
        obsidian_rc_ore,
        obsidian_rc_clay,
        geode_rc_ore,
        geode_rc_obsidian,
    ) = costs  # robot costs

    # First possible position is where we don't build any robots
    position_set = {
        (
            ore + ore_robots,
            clay + clay_robots,
            obsidian + obsidian_robots,
            geode + geode_robots,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
        )
    }

    # if we have enough for an ore robot, build one
    if ore >= ore_rc:
        position_set.add(
            (
                ore - ore_rc + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots,
                geode + geode_robots,
                ore_robots + 1,
                clay_robots,
                obsidian_robots,
                geode_robots,
            )
        )

    # if we have enough for a clay robot, build one
    if ore >= clay_rc:
        position_set.add(
            (
                ore - clay_rc + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots,
                geode + geode_robots,
                ore_robots,
                clay_robots + 1,
                obsidian_robots,
                geode_robots,
            )
        )

    # if we have enough for an obsidian robot, build one
    if ore >= obsidian_rc_ore and clay >= obsidian_rc_clay:
        position_set.add(
            (
                ore - obsidian_rc_ore + ore_robots,
                clay - obsidian_rc_clay + clay_robots,
                obsidian + obsidian_robots,
                geode + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots + 1,
                geode_robots,
            )
        )

    # if we have enough for a geode robot, build one
    if ore >= geode_rc_ore and obsidian >= geode_rc_obsidian:
        position_set.add(
            (
                ore - geode_rc_ore + ore_robots,
                clay + clay_robots,
                obsidian - geode_rc_obsidian + obsidian_robots,
                geode + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots + 1,
            )
        )

    return position_set


def get_all_next(
    position_set: t.Set[t.Tuple[int]], costs: t.Tuple[int]
) -> t.Set[t.Tuple[int]]:

    # take as input a position set, and return all the possible next positions for that position set

    next_position_set = set()

    for position in position_set:

        next_position_set |= get_next(position, costs)

    return next_position_set


def simple_worse_position_trim(
    position_set: t.Set[t.Tuple[int]],
) -> t.Set[t.Tuple[int]]:

    position_set_copy = position_set.copy()

    for p1, p2 in itertools.combinations(position_set_copy, 2):

        p_diff = tuple(map(lambda i, j: i - j, p2, p1))

        # one or more resourses are lower, and none are higher
        if any(map(lambda x: x < 0, p_diff)) and all(map(lambda x: x <= 0, p_diff)):
            position_set.discard(p2)
        if any(map(lambda x: x > 0, p_diff)) and all(map(lambda x: x >= 0, p_diff)):
            position_set.discard(p1)

    return position_set


def score_position(position: t.Tuple[int], costs: t.Tuple[int], mins_remaining: int):

    # take as input a position and output a fitness score for that position, the positions with the lowest fitness will be culled
    # as a model for the fitness, converting the position into how much equivalent ore that position will produce

    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 3 ore and 16 obsidian.
    # 24 minutes, at minute 1:
    # 1 ore robot can make 24 ore
    # 1 clay robot can make 24 clay, worth 24*4 ore --- 1 clay is worth 4 ore
    # 1 obsidian robot can may 24 obsidian, worth 24*(4+14*4) ore --- 1 obsidian is worth (4+14*4)
    # 1 geode robot can make 24 geode, worth 24*(3+16*(4+14*4)) --- 1 geode is worth 3+16*(4+14*4)

    (
        ore_rc,
        clay_rc,
        obsidian_rc_ore,
        obsidian_rc_clay,
        geode_rc_ore,
        geode_rc_obsidian,
    ) = costs

    (
        ore,
        clay,
        obsidian,
        geode,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ) = position

    ore_value = mins_remaining * ore_robots + ore
    clay_value = mins_remaining * clay_robots * clay_rc + clay * clay_rc

    obsidian_value = mins_remaining * obsidian_robots * (
        obsidian_rc_ore + obsidian_rc_clay * clay_rc
    ) + obsidian * (obsidian_rc_ore + obsidian_rc_clay * clay_rc)

    geode_value = mins_remaining * geode_robots * (
        geode_rc_ore
        + geode_rc_obsidian * (obsidian_rc_ore + obsidian_rc_clay * clay_rc)
    ) + geode * (
        geode_rc_ore
        + geode_rc_obsidian * (obsidian_rc_ore + obsidian_rc_clay * clay_rc)
    )

    return ore_value + clay_value + obsidian_value + geode_value


def score_position_trim(
    position_set: t.Set[t.Tuple[int]], costs: t.Tuple[int], mins_remaining: int
):

    if len(position_set) < 100:
        return position_set

    position_set = set(
        sorted(
            list(position_set),
            key=lambda f: score_position(f, costs, mins_remaining),
        )[-99:]
    )

    return position_set


def DayQ1(data: t.List[str]) -> int:

    robot_list = parse_input(data)

    num_minutes = 24
    quality_levels = []

    for i, cost in enumerate(robot_list):

        # (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots)
        # start out with one ore_robot
        position_set = set([(0, 0, 0, 0, 1, 0, 0, 0)])

        for min in range(1, num_minutes + 1):

            position_set = get_all_next(position_set, cost)

            # Trim here where we remove any positions that are obviously worse e.g.:
            # (2, 0, 0, 0, 1, 1, 0, 0) vs (2, 1, 0, 0, 1, 1, 0, 0)
            # the second position is better because it has more clay, and the same amount of everything else
            position_set = simple_worse_position_trim(position_set)

            # Trim here by giving each position a score as described below
            # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 3 ore and 16 obsidian.
            # 24 minutes, at minute 1:
            # 1 ore robot can make 24 ore
            # 1 clay robot can make 24 clay, worth 24*4 ore --- 1 clay is worth 4 ore
            # 1 obsidian robot can may 24 obsidian, worth 24*(4+14*4) ore --- 1 obsidian is worth (4+14*4)
            # 1 geode robot can make 24 geode, worth 24*(3+16*(4+14*4)) --- 1 geode is worth 3+16*(4+14*4)
            position_set = score_position_trim(position_set, cost, num_minutes - min)

        quality_levels.append(max(p[3] for p in position_set) * (i + 1))

    return sum(quality_levels)


def DayQ2(data: t.List[str]) -> int:

    robot_list = parse_input(data)[:3]
    num_minutes = 32
    quality_levels_p2 = []

    for i, cost in enumerate(robot_list):

        # (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots)
        # start out with one ore_robot
        position_set = set([(0, 0, 0, 0, 1, 0, 0, 0)])

        for min in range(1, num_minutes + 1):

            position_set = get_all_next(position_set, cost)

            position_set = simple_worse_position_trim(position_set)

            position_set = score_position_trim(position_set, cost, num_minutes - min)

        quality_levels_p2.append(max(p[3] for p in position_set))

    return quality_levels_p2[0] * quality_levels_p2[1] * quality_levels_p2[2]


if __name__ == "__main__":

    data = aocd.get_data(
        day=19,
        year=2022,
    ).split("\n")

    test_data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".split(
        "\n"
    )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
