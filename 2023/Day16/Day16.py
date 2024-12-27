import aocd
import typing as t
import re
from itertools import product


def parse_input(data: t.List[str]) -> dict:
    valves = {}
    for line in data:
        valve_name = re.search("Valve (..)", line).group(1)
        flow_rate = int(re.search("=(\d+);", line).group(1))
        leads_to = re.search("valve[s]* (.*)$", line).group(1).split(", ")
        valves[valve_name] = [flow_rate, leads_to]
    return valves


def DayQ1(data: t.List[str]) -> int:

    valves = parse_input(data)

    # At each index we want to track everything that we have done up to that point
    # This will include, where we are currently, and all of the valves we have opened, and the amount of pressure currently released

    # Set all the valves with no flow rate to open, so that we don't attempt to open them later.
    opened_valves = frozenset(k for k, v in valves.items() if v[0] == 0)

    # [Where we are string, opened valves frozenset, amount of pressure released int]
    positions_at_each_minute = [set([("AA", opened_valves, 0)])]

    num_minutes = 30

    for minute in range(1, num_minutes + 1):

        positions_at_each_minute.append(set())

        for position in positions_at_each_minute[-2]:

            current_valve = position[0]
            opened_valves = position[1]
            pressure_released = position[2]

            if current_valve not in opened_valves:

                # multiplying by the number of minutes remaining that the valve will stay open for
                current_valve_flow_rate = valves[current_valve][0] * (
                    num_minutes - minute
                )

                positions_at_each_minute[-1].add(
                    (
                        current_valve,
                        opened_valves | {current_valve},
                        pressure_released + current_valve_flow_rate,
                    )
                )

            possible_moves = valves[current_valve][1]

            for move in possible_moves:

                positions_at_each_minute[-1].add(
                    (move, opened_valves, pressure_released)
                )

        # Filter down to only the top 10000 best paths so that the number of paths does not get too large
        if len(positions_at_each_minute[-1]) > 10000:

            top10000 = sorted(list(positions_at_each_minute[-1]), key=lambda f: f[2])[
                -10000:
            ]

            positions_at_each_minute[-1] = set(top10000)

    max_pressure_released = max(p[2] for p in positions_at_each_minute[-1])

    return max_pressure_released


def DayQ2(data: t.List[str]) -> int:

    valves = parse_input(data)

    # Set all the valves with no flow rate to open, so that we don't attempt to open them later.
    opened_valves = frozenset(k for k, v in valves.items() if v[0] == 0)

    # [Where we are and where the elephant is tuple, opened valves frozenset, amount of pressure released int]
    positions_at_each_minute = [set([(("AA", "AA"), opened_valves, 0)])]

    num_minutes = 26

    for minute in range(1, num_minutes + 1):

        positions_at_each_minute.append(set())

        for position in positions_at_each_minute[-2]:

            current_valve_me = position[0][0]
            current_valve_elephant = position[0][1]
            opened_valves = position[1]
            pressure_released = position[2]

            possible_moves_me = valves[current_valve_me][1]
            possible_moves_elephant = valves[current_valve_elephant][1]

            # what to do if we are not in the same spot, and we both open
            if (
                current_valve_me not in opened_valves
                and current_valve_elephant not in opened_valves
                and current_valve_me != current_valve_elephant
            ):

                current_valve_flow_rate = (
                    valves[current_valve_me][0] + valves[current_valve_elephant][0]
                ) * (num_minutes - minute)

                positions_at_each_minute[-1].add(
                    (
                        (current_valve_me, current_valve_elephant),
                        opened_valves | {current_valve_me} | {current_valve_elephant},
                        pressure_released + current_valve_flow_rate,
                    )
                )

            # I open and elephant doesn't
            # this will happen if we're in the same spot, or if we're not and I open and elephant moves
            # if we're both at the same valve, I open it, and the elephant moves
            elif current_valve_me not in opened_valves:

                # multiplying by the number of minutes remaining that the valve will stay open for
                current_valve_flow_rate = valves[current_valve_me][0] * (
                    num_minutes - minute
                )

                for move_elephant in possible_moves_elephant:
                    positions_at_each_minute[-1].add(
                        (
                            (current_valve_me, move_elephant),
                            opened_valves | {current_valve_me},
                            pressure_released + current_valve_flow_rate,
                        )
                    )

            # what to do if we are not in the same spot and I don't open and elephant does
            elif current_valve_elephant not in opened_valves:

                current_valve_flow_rate = valves[current_valve_elephant][0] * (
                    num_minutes - minute
                )

                for move_me in possible_moves_me:
                    positions_at_each_minute[-1].add(
                        (
                            (move_me, current_valve_elephant),
                            opened_valves | {current_valve_elephant},
                            pressure_released + current_valve_flow_rate,
                        )
                    )

            # finally, loop for if we both move and don't open
            possible_moves = product(possible_moves_me, possible_moves_elephant)

            for move in possible_moves:

                move_me = move[0]
                move_elephant = move[1]

                positions_at_each_minute[-1].add(
                    ((move_me, move_elephant), opened_valves, pressure_released)
                )

        # Filter down to only the top 10000 best paths so that the number of paths does not get too large
        if len(positions_at_each_minute[-1]) > 10000:

            top10000 = sorted(list(positions_at_each_minute[-1]), key=lambda f: f[2])[
                -10000:
            ]
            positions_at_each_minute[-1] = set(top10000)

    max_pressure_released = max(p[2] for p in positions_at_each_minute[-1])

    return max_pressure_released


if __name__ == "__main__":

    data = aocd.get_data(
        day=16,
        year=2022,
    ).split("\n")

    test_data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split(
        "\n"
    )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))
