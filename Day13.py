import aocd
import typing as t
import math


def Day13Q1(earliest_departure: int, bus_ids: t.Set[int]) -> int:

    id_found = False
    i = 0

    while not (id_found):
        for id in bus_ids:
            if (earliest_departure + i) % id == 0:
                print("Id: {}, Wait time: {}".format(id, i))
                return id * i
        i += 1


def Day13Q2(bus_ids: t.List[str]) -> int:

    # create a list for each position
    bus_id_list = list(enumerate(bus_ids))

    new_bus_id_list = []

    # create a list of the of bus ids and minutes they must come after the first bus
    for i in range(len(bus_id_list)):
        if bus_id_list[i][1] != "x":
            new_bus_id_list.append((bus_id_list[i][0], int(bus_id_list[i][1])))

    # The bus arrival intervals are pairwise coprime, so we can use the Chinese remainder theorem:
    # https://www.youtube.com/watch?v=zIFehsBHB8o
    # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Using_the_existence_construction

    n = [i[1] for i in new_bus_id_list]  # mod n
    b = [(i[1] - i[0]) % i[1] for i in new_bus_id_list]  # remainders
    N_scalar = math.prod(n)  # product of all n
    N = [round(N_scalar / i) for i in n]  # N_i
    x = [pow(N[i], -1, n[i]) for i in range(len(n))]  # Modular multiplicative inverse of N_i

    timestamp = sum(b[i] * N[i] * x[i] for i in range(len(n)))
    earliest_timestamp = timestamp % N_scalar

    return earliest_timestamp


if __name__ == "__main__":
    two_lines = aocd.get_data(day=13, year=2020).splitlines()
    earliest_departure = int(two_lines[0])
    bus_ids = set(int(x) for x in two_lines[1].split(",") if x != "x")
    print("Part 1:", Day13Q1(earliest_departure, bus_ids))

    bus_ids = two_lines[1].split(",")
    print("Part 2:", Day13Q2(bus_ids))
