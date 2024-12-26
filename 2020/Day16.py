import aocd
import re
import typing as t
import copy
import itertools


def Day16Q1(
    valid_ranges_dict: t.Dict[str, t.List[str]], nearby_tickets: t.List[t.List[str]]
) -> int:

    # build a list of all the valid values that a ticket field can be

    valid_values = set()

    for range_name, range_values in valid_ranges_dict.items():
        for min_max_pair in range_values:
            min_range, max_range = min_max_pair.split("-")
            for i in range(int(min_range), int(max_range) + 1):
                valid_values.add(i)

    ticket_scanning_error_rate = 0

    for ticket in nearby_tickets:
        for field in ticket:
            if int(field) not in valid_values:
                ticket_scanning_error_rate += int(field)

    return ticket_scanning_error_rate


def Day16Q2(
    valid_ranges_dict: t.Dict[str, t.List[str]],
    your_ticket: t.List,
    nearby_tickets: t.List[t.List[str]],
) -> int:

    # build a set of all the valid values that a ticket field can be
    valid_values = set()
    for range_name, range_values in valid_ranges_dict.items():
        for min_max_pair in range_values:
            min_range, max_range = min_max_pair.split("-")
            for i in range(int(min_range), int(max_range) + 1):
                valid_values.add(i)

    # build a list of all the valid tickets by dicarding the invalid ones
    valid_nearby_tickets = []
    for ticket in nearby_tickets:
        ticket_valid = True
        for field in ticket:
            if int(field) not in valid_values:
                ticket_valid = False
                break
        if ticket_valid:
            valid_nearby_tickets.append([int(x) for x in ticket])

    # create valid ranges dict set
    valid_ranges_set_dict = {}

    for range_name, range_values in valid_ranges_dict.items():
        for min_max_pair in range_values:
            min_range, max_range = min_max_pair.split("-")
            for i in range(int(min_range), int(max_range) + 1):
                if range_name in valid_ranges_set_dict:
                    valid_ranges_set_dict[range_name].add(i)
                else:
                    valid_ranges_set_dict[range_name] = set()
                    valid_ranges_set_dict[range_name].add(i)

    # transpose the valid_nearby_tickets list of lists
    possibility_check = list(map(list, zip(*valid_nearby_tickets)))
    possibilities = [[] for i in range(len(possibility_check))]

    for i in range(len(possibility_check)):
        for key, value in valid_ranges_set_dict.items():
            if set(possibility_check[i]).issubset(value):
                possibilities[i].append(key)

    # Had help on this part from:
    # https://www.youtube.com/watch?v=OhqvfoaBljY
    MAP = [None for _ in range(len(possibilities))]

    while True:
        for i in range(len(possibilities)):
            if len(possibilities[i]) == 1:
                MAP[i] = possibilities[i][0]
                for j in range(len(possibilities)):
                    if MAP[i] in possibilities[j]:
                        possibilities[j].remove(MAP[i])
                break
        if sum(x is not None for x in MAP) == 20:
            break

    departure_product = 1

    for i, field in enumerate(MAP):
        if field[:9] == "departure":
            departure_product *= int(your_ticket[i])

    return departure_product


if __name__ == "__main__":

    ticket_data = aocd.get_data(
        day=16,
        year=2020,
    )

    valid_ranges, your_ticket, nearby_tickets = ticket_data.split("\n\n")

    # Build valid ranges dictionary
    valid_ranges_list = valid_ranges.splitlines()
    valid_range_pattern = re.compile(r"(?P<field>\w+(\s\w+)?)\: (?P<minmax>.+)")
    valid_ranges_dict = {}
    for valid_range in valid_ranges_list:
        parsed_line = valid_range_pattern.match(valid_range).groupdict()
        valid_ranges_dict[parsed_line["field"]] = parsed_line["minmax"].split(" or ")

    # build ticket lists
    your_ticket = your_ticket.splitlines()[1].split(",")
    nearby_tickets = [x.split(",") for x in nearby_tickets.splitlines()[1:]]

    print("Part 1:", Day16Q1(valid_ranges_dict, nearby_tickets))
    print("Part 2:", Day16Q2(valid_ranges_dict, your_ticket, nearby_tickets))
