import aocd
import typing as t


def Day15Q1(starting_numbers: t.List[int]) -> int:

    i = len(starting_numbers)

    while i < 2020:

        if starting_numbers[-1] not in starting_numbers[:-1]:
            starting_numbers.append(0)
        else:
            occurence_indices = [
                i for i, x in enumerate(starting_numbers) if x == starting_numbers[-1]
            ]
            ultimate_index = occurence_indices[-1]
            penultimate_index = occurence_indices[-2]
            starting_numbers.append(ultimate_index - penultimate_index)
        i += 1

    return starting_numbers[-1]


def Day15Q2Attempt1(starting_numbers: t.List[int]) -> int:

    # This attempt takes too long to run
    i = len(starting_numbers)

    while i < 30000000:

        if starting_numbers[-1] not in starting_numbers[:-1]:
            starting_numbers.append(0)
        else:
            occurence_indices = [
                i for i, x in enumerate(starting_numbers) if x == starting_numbers[-1]
            ]
            ultimate_index = occurence_indices[-1]
            penultimate_index = occurence_indices[-2]
            starting_numbers.append(ultimate_index - penultimate_index)
        i += 1

    return starting_numbers[-1]


def Day15Q2(starting_numbers: t.List[int]) -> int:

    i = len(starting_numbers)

    seen_dict = {k: v + 1 for v, k in enumerate(starting_numbers[:-1])}
    current_number = starting_numbers[-1]

    while i < 30000000:
        if current_number not in seen_dict:
            seen_dict[current_number] = i
            current_number = 0
        else:
            current_number_copy = current_number
            current_number = i - seen_dict[current_number]
            seen_dict[current_number_copy] = i

        i += 1

    return current_number


if __name__ == "__main__":
    starting_numbers = [int(x) for x in aocd.get_data(day=15, year=2020).split(",")]

    print("Part 1:", Day15Q1(starting_numbers))
    print("Part 2:", Day15Q2(starting_numbers))