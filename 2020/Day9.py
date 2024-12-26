import typing as t

import aocd

import itertools


def Day9Q1(xmas_code: t.List[int]) -> int:

    for i in range(25, len(xmas_code[25:])):
        match_found = False
        for preamble in itertools.combinations(xmas_code[i - 25 : i], 2):
            if sum(preamble) == xmas_code[i]:
                match_found = True
        if not (match_found):
            # print(xmas_code[i])
            return xmas_code[i]


def Day9Q2(xmas_code: t.List[int], invalid_number: int) -> int:

    contiguous_counter = 2

    while contiguous_counter < len(xmas_code):
        for i in range(contiguous_counter, len(xmas_code)):
            if sum(xmas_code[i - contiguous_counter : i]) == invalid_number:
                # print(xmas_code[i - contiguous_counter : i])
                return min(xmas_code[i - contiguous_counter : i]) + max(
                    xmas_code[i - contiguous_counter : i]
                )
        contiguous_counter += 1


if __name__ == "__main__":
    xmas_code = [int(x) for x in aocd.get_data(day=9, year=2020).splitlines()]
    invalid_number = Day9Q1(xmas_code)
    print("Part 1 - Invalid number:", invalid_number)
    print("Part 2 - Encryption weakness:", Day9Q2(xmas_code, invalid_number))
