import aocd
import typing as t
from collections import Counter


def Day8Q1(data: t.List[str]) -> int:

    count1478 = 0

    for line in data:
        _, output = line.split(" | ")
        for display in output.split():
            if len(display) in [2, 3, 4, 7]:
                count1478 += 1

    return count1478


def Day8Q2(data: t.List[str]) -> str:

    # Example:
    # cdbga acbde eacdfbg adbgf gdebcf bcg decabf cg ebdgac egca | geac ceag faedcb cg
    # bottom right appears 9 times, so bottom right must be c
    # top left appears 6 times, so top left must be e
    # bottom left appears 4 times, so bottom left must be f
    # one has 2 segments, cg, c is already taken, so top right must be g
    # seven has 3 segments, bcg, cg are already taken, so top must be b
    # four has 4 segments, egca, ecg are already taken, so middle must be a
    # 8 has 7 segments, eacdfbg, abcefg are already taken, so bottom must be d

    # [top, top left, top right, middle, bottom left, bottom right, bottom]
    # Stores which segments are on for each number 0-9
    display_list = [
        (1, 1, 1, 0, 1, 1, 1),
        (0, 0, 1, 0, 0, 1, 0),
        (1, 0, 1, 1, 1, 0, 1),
        (1, 0, 1, 1, 0, 1, 1),
        (0, 1, 1, 1, 0, 1, 0),
        (1, 1, 0, 1, 0, 1, 1),
        (1, 1, 0, 1, 1, 1, 1),
        (1, 0, 1, 0, 0, 1, 0),
        (1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 0, 1, 1),
    ]

    sum_all = 0

    for line in data:

        input, output = line.split(" | ")

        input_dict = {frozenset(x): len(x) for x in input.split()}
        char_counter = Counter(input.replace(" ", ""))

        # [top, top left, top right, middle, bottom left, bottom right, bottom]
        letter_pos = [None] * 7
        for c in char_counter:
            if char_counter[c] == 9:
                letter_pos[5] = c
            if char_counter[c] == 6:
                letter_pos[1] = c
            if char_counter[c] == 4:
                letter_pos[4] = c

        while None in letter_pos:
            for k, v in input_dict.items():
                if v == 2:
                    for c in k:
                        if c not in letter_pos:
                            letter_pos[2] = c
            for k, v in input_dict.items():
                if v == 3:
                    for c in k:
                        if c not in letter_pos:
                            letter_pos[0] = c
            for k, v in input_dict.items():
                if v == 4:
                    for c in k:
                        if c not in letter_pos:
                            letter_pos[3] = c
            for k, v in input_dict.items():
                if v == 7:
                    for c in k:
                        if c not in letter_pos:
                            letter_pos[6] = c

        output_list = output.split()
        mult = 1000
        sum_line = 0

        for n in output_list:
            temp_list = [0] * 7
            for l in n:
                temp_list[letter_pos.index(l)] = 1
            display_num = display_list.index(tuple(temp_list))
            sum_line += int(display_num * mult)
            mult /= 10

        sum_all += sum_line

    return sum_all


if __name__ == "__main__":

    data = aocd.get_data(day=8, year=2021).splitlines()

    print("Part 1:", Day8Q1(data))
    print("Part 2:", Day8Q2(data))
