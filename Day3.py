import aocd
import typing as t


def Day2Q1(data: t.List[str]) -> int:

    priority_sum = 0

    for rucksack in data:
        middle = int(len(rucksack) / 2)
        compartment1 = rucksack[:middle]
        compartment2 = rucksack[middle:]

        for item in compartment1:
            if item in compartment2:
                if ord(item) > 96:
                    priority_sum += ord(item) - 96
                else:
                    priority_sum += ord(item) - 64 + 26
                break

    return priority_sum


def Day2Q2(data: t.List[str]) -> int:

    priority_sum = 0

    for i in range(len(data)):

        if i % 3 == 2:
            for item in data[i]:
                if (item in data[i - 1]) and (item in data[i - 2]):
                    if ord(item) > 96:
                        priority_sum += ord(item) - 96
                    else:
                        priority_sum += ord(item) - 64 + 26
                    break

    return priority_sum


if __name__ == "__main__":

    data = aocd.get_data(
        day=3,
        year=2022,
    ).splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
