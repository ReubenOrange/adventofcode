#%%
import typing as t

import aocd
import re

instruction_re = re.compile(r"(?P<action>\w{3}) (?P<size>[+-]\d+)")


def parse_instruction(line):
    match = instruction_re.match(line).groupdict()
    return match["action"], int(match["size"])


def Day8Q1(instructions: t.List[str]) -> int:

    positions_visited = set()

    accumulator = 0
    position = 0
    set_size = 0
    previous_set_size = -1

    while set_size > previous_set_size:

        previous_set_size = len(positions_visited)
        positions_visited.add(position)
        current_instruction = instructions[position]
        action, size = parse_instruction(current_instruction)

        if action == "acc":
            accumulator += size
            position += 1
        elif action == "jmp":
            position = position + size
        else:
            position += 1

        set_size = len(positions_visited)

    if action == "acc":
        accumulator -= size

    return accumulator


def Day8Q2(instructions: t.List[str]) -> int:

    for i in range(len(instructions)):
        instructions_copy = instructions.copy()
        action, size = parse_instruction(instructions_copy[i])
        sign = lambda x: ("+", "-")[x < 0]
        if action == "jmp":
            instructions_copy[i] = "nop " + sign(size) + str(abs(size))
        elif action == "nop":
            instructions_copy[i] = "jmp " + sign(size) + str(abs(size))
        else:
            continue

        positions_visited = set()
        accumulator = 0
        position = 0
        set_size = 0
        previous_set_size = -1

        while set_size > previous_set_size:

            previous_set_size = len(positions_visited)
            positions_visited.add(position)
            current_instruction = instructions_copy[position]
            action, size = parse_instruction(current_instruction)

            if action == "acc":
                accumulator += size
                position += 1
            elif action == "jmp":
                position = position + size
            else:
                position += 1

            set_size = len(positions_visited)

            if position >= len(instructions):
                # print("Action: ", action)
                # print("Size: ", size)
                # print("Position: ", position)
                # print("Instruction altered: ", i)
                return accumulator


if __name__ == "__main__":
    data = aocd.get_data(day=8, year=2020).splitlines()
    print("Part 1: ", Day8Q1(data))
    print("Part 2: ", Day8Q2(data))
# %%
