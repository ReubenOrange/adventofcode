import aocd


def Day6Q1(data):

    # Remove duplicate answers from the groups, by converting the data in each group to a set
    group_list = [set(x.replace("\n", "")) for x in data]

    # Sum the length of each set
    return sum(len(i) for i in group_list)


def Day6Q2(data):

    return sum(count_intersection(group) for group in data)


def count_intersection(group):

    # Create a set for each person in the group, then return the size of the intersection
    set_list = [set(x) for x in group.splitlines()]
    return len(set.intersection(*set_list))


if __name__ == "__main__":

    data = aocd.get_data(day=6, year=2020).split("\n\n")

    print("Day6Q1: ", Day6Q1(data))
    print("Day6Q2: ", Day6Q2(data))