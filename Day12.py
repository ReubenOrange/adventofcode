import aocd

import typing as t
import re
import math


def Day12Q1(directions: t.List[str]) -> int:

    pattern = re.compile(r"(?P<action>\w)(?P<magnitude>\d+)")

    # North, East, South, West, Forward direction, Position
    direction_mapping = {
        "N": [0, 1],
        "E": [1, 0],
        "S": [0, -1],
        "W": [-1, 0],
        "F": [1, 0],
        "P": [0, 0],
    }

    for direction in directions:
        direction_dict = pattern.match(direction).groupdict()
        action = direction_dict["action"]
        magnitude = int(direction_dict["magnitude"])

        # print("Action:", direction)

        if action == "L" or action == "R":
            # rotate the unit direction vector by given angle:
            # https://en.wikipedia.org/wiki/Rotation_matrix
            if action == "R":
                magnitude = -magnitude
            new_direction = [0, 0]
            new_direction[0] = round(
                direction_mapping["F"][0] * math.cos(magnitude * math.pi / 180)
                - direction_mapping["F"][1] * math.sin(magnitude * math.pi / 180)
            )
            new_direction[1] = round(
                direction_mapping["F"][0] * math.sin(magnitude * math.pi / 180)
                + direction_mapping["F"][1] * math.cos(magnitude * math.pi / 180)
            )
            direction_mapping["F"] = new_direction
        else:
            # update position to move in the indicated direction
            direction_mapping["P"][0] += round(direction_mapping[action][0] * magnitude)
            direction_mapping["P"][1] += round(direction_mapping[action][1] * magnitude)
        # print("Position:", direction_mapping["P"])
        # print("Facing direction:", direction_mapping["F"])

    manhattan_distance = sum(abs(x) for x in direction_mapping["P"])
    return manhattan_distance


def Day12Q2(directions: t.List[str]) -> int:

    pattern = re.compile(r"(?P<action>\w)(?P<magnitude>\d+)")

    # North, East, South, West, Waypoint, Position

    direction_mapping = {
        "N": [0, 1],
        "E": [1, 0],
        "S": [0, -1],
        "W": [-1, 0],
        "F": [10, 1],
        "P": [0, 0],
    }

    for direction in directions:
        direction_dict = pattern.match(direction).groupdict()
        action = direction_dict["action"]
        magnitude = int(direction_dict["magnitude"])

        print("Action:", direction)

        if action in ["L", "R"]:
            # rotate the waypoint vector by given angle:
            # https://en.wikipedia.org/wiki/Rotation_matrix
            if action == "R":
                magnitude = -magnitude
            new_direction = [0, 0]
            new_direction[0] = round(
                direction_mapping["F"][0] * math.cos(magnitude * math.pi / 180)
                - direction_mapping["F"][1] * math.sin(magnitude * math.pi / 180)
            )
            new_direction[1] = round(
                direction_mapping["F"][0] * math.sin(magnitude * math.pi / 180)
                + direction_mapping["F"][1] * math.cos(magnitude * math.pi / 180)
            )
            direction_mapping["F"] = new_direction
        elif action in ["N", "E", "S", "W"]:
            direction_mapping["F"][0] += round(direction_mapping[action][0] * magnitude)
            direction_mapping["F"][1] += round(direction_mapping[action][1] * magnitude)
        elif action == "F":
            direction_mapping["P"][0] += direction_mapping["F"][0] * magnitude
            direction_mapping["P"][1] += direction_mapping["F"][1] * magnitude

        print("Position:", direction_mapping["P"])
        print("Facing direction:", direction_mapping["F"])

    manhattan_distance = sum(abs(x) for x in direction_mapping["P"])
    return manhattan_distance


if __name__ == "__main__":
    directions = [x for x in aocd.get_data(day=12, year=2020).splitlines()]

    print("Part 1:", Day12Q1(directions))
    print("Part 2:", Day12Q2(directions))
