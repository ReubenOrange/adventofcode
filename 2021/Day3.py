import aocd
import typing as t


def Day3Q1(diagnostic_report: t.List[str]) -> int:

    matrix = [list(line) for line in diagnostic_report]

    transposed_matrix = map(list, zip(*matrix))

    gamma_rate = ""
    epsilon_rate = ""

    for line in transposed_matrix:

        zeroes = sum(bit == "0" for bit in line)
        ones = sum(bit == "1" for bit in line)

        gamma_rate += str((ones > zeroes) * 1)
        epsilon_rate += str((ones < zeroes) * 1)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def Day3Q2(diagnostic_report: t.List[str]) -> int:

    matrix = [list(line) for line in diagnostic_report]
    valid_lines_oxy = [True] * len(matrix)
    valid_lines_C02 = [True] * len(matrix)

    transposed_matrix = list(map(list, zip(*matrix)))

    for i, line in enumerate(transposed_matrix):

        zeroes_oxy = sum(bit == "0" and valid_lines_oxy[j] for j, bit in enumerate(line))
        ones_oxy = sum(bit == "1" and valid_lines_oxy[j] for j, bit in enumerate(line))

        most_common_bit = str((ones_oxy >= zeroes_oxy) * 1)

        for j, l in enumerate(matrix):
            if valid_lines_oxy[j] and l[i] != most_common_bit:
                valid_lines_oxy[j] = False

        if sum(x * 1 for x in valid_lines_oxy) == 1:
            oxygen_generator_rating = "".join(matrix[valid_lines_oxy.index(True)])

        zeroes_C02 = sum(bit == "0" and valid_lines_C02[j] for j, bit in enumerate(line))
        ones_C02 = sum(bit == "1" and valid_lines_C02[j] for j, bit in enumerate(line))

        least_common_bit = str((ones_C02 < zeroes_C02) * 1)

        for j, l in enumerate(matrix):
            if valid_lines_C02[j] and l[i] != least_common_bit:
                valid_lines_C02[j] = False

        if sum(x * 1 for x in valid_lines_C02) == 1:
            C02_scrubber_rating = "".join(matrix[valid_lines_C02.index(True)])

    return int(oxygen_generator_rating, 2) * int(C02_scrubber_rating, 2)


if __name__ == "__main__":

    data = aocd.get_data(day=4, year=2021, session="")
    diagnostic_report = data.splitlines()

    print("Part 1:", Day3Q1(diagnostic_report))
    print("Part 2:", Day3Q2(diagnostic_report))
