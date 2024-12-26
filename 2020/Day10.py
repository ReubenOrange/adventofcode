import aocd


def Day10Q1(adapter_list):

    three_count = 0
    one_count = 0

    for i in range(len(adapter_list) - 1):
        jolt_diff = adapter_list[i + 1] - adapter_list[i]
        # print(jolt_diff)
        if jolt_diff == 1:
            one_count += 1
        elif jolt_diff == 3:
            three_count += 1

    return one_count * three_count


def Day10Q2(adapter_list):
    combinations_dict = {}

    # find combinations of last 3 elements
    combinations_dict[adapter_list[-1]] = 1
    if adapter_list[-1] - adapter_list[-2] <= 3:
        combinations_dict[adapter_list[-2]] = combinations_dict[adapter_list[-1]]
    if adapter_list[-2] - adapter_list[-3] <= 3:
        combinations_dict[adapter_list[-3]] = combinations_dict[adapter_list[-2]]
    if adapter_list[-1] - adapter_list[-3] <= 3:
        combinations_dict[adapter_list[-3]] += combinations_dict[adapter_list[-1]]

    # print(combinations_dict)

    # start from the end of the adapter list, and work backwards adding up the subproblems
    for i in range(len(adapter_list) - 4, -1, -1):

        node_count = 0

        if adapter_list[i + 1] - adapter_list[i] <= 3:
            node_count += combinations_dict[adapter_list[i + 1]]
        if adapter_list[i + 2] - adapter_list[i] <= 3:
            node_count += combinations_dict[adapter_list[i + 2]]
        if adapter_list[i + 3] - adapter_list[i] <= 3:
            node_count += combinations_dict[adapter_list[i + 3]]

        combinations_dict[adapter_list[i]] = node_count

    # print(combinations_dict)

    return combinations_dict[adapter_list[0]]


if __name__ == "__main__":
    adapter_list = sorted([int(x) for x in aocd.get_data(day=10, year=2020).splitlines()])

    # add the charging outlet and the device's built-in adapter
    adapter_list = [0] + adapter_list + [adapter_list[-1] + 3]

    print("Part 1:", Day10Q1(adapter_list))
    print("Part 2:", Day10Q2(adapter_list))