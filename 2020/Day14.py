import aocd
import typing as t
import re
import copy


def set_bit(v, index, x):
    mask = 1 << index
    v &= ~mask
    if x:
        v |= mask
    return v


def Day14Q1(docking_input: t.List[str]) -> int:

    mask = ""
    pattern = re.compile(r"mem\[(?P<mem_address>\d+)\] = (?P<value>\d+)")
    memory_dict = {}

    for line in docking_input:
        if line[0:4] == "mask":
            mask = "0b" + line[7:]
        else:
            line_dict = pattern.match(line).groupdict()
            mem_address = line_dict["mem_address"]
            value = format(int(line_dict["value"]), "#038b")
            result = "0b"
            for i, character in enumerate(mask[2:]):
                if character == "X":
                    result += value[i + 2]
                else:
                    result += character
            memory_dict[mem_address] = result

    return sum(int(value, 2) for value in memory_dict.values())


def Day14Q2(docking_input: t.List[str]) -> int:

    mask = ""
    pattern = re.compile(r"mem\[(?P<mem_address>\d+)\] = (?P<value>\d+)")

    masked_input = []

    # first create a new input that is the every input line with the corresponding mask applied
    for line in docking_input:
        if line[0:4] == "mask":
            mask = "0b" + line[7:]
        else:
            masked_line = []
            line_dict = pattern.match(line).groupdict()
            mem_address = format(int(line_dict["mem_address"]), "#038b")
            value = line_dict["value"]
            for i, character in enumerate(mask):
                if character == "X":
                    masked_line.append("X")
                elif character == "1":
                    masked_line.append("1")
                else:
                    masked_line.append(mem_address[i])

            masked_input.append([masked_line, value])

    memory_dict = {}

    for line in masked_input:
        dict_keys = [[]]
        for character in line[0]:
            if character == "X":
                copy1 = copy.deepcopy(dict_keys)
                copy2 = copy.deepcopy(dict_keys)

                for i in range(len(dict_keys)):
                    copy1[i].append("0")
                    copy2[i].append("1")

                dict_keys = copy1 + copy2
            else:
                for i in range(len(dict_keys)):
                    dict_keys[i].append(character)

        for key in dict_keys:
            memory_dict["".join(key)] = line[1]

    return sum(int(value) for value in memory_dict.values())


if __name__ == "__main__":
    docking_input = aocd.get_data(day=14, year=2020).splitlines()

    print("Part 1:", Day14Q1(docking_input))
    print("Part 2:", Day14Q2(docking_input))
