import aocd
import typing as t
from copy import deepcopy


def Day11Q1(data: t.List[t.List[int]]) -> int:

    num_flashes = 0

    for step in range(100):

        flashed = [[False for x in range(len(data[0]))] for y in range(len(data))]

        for y in range(len(data)):
            for x in range(len(data[0])):
                data[y][x] += 1

        still_flashing = True
        while still_flashing:
            still_flashing = False

            for y in range(len(data)):
                for x in range(len(data[0])):
                    if data[y][x] > 9 and not flashed[y][x]:
                        flashed[y][x] = "pending"
                        num_flashes += 1

            for y in range(len(flashed)):
                for x in range(len(flashed[0])):
                    if flashed[y][x] == "pending":
                        if y - 1 >= 0 and x - 1 >= 0:
                            data[y - 1][x - 1] += 1
                        if y - 1 >= 0:
                            data[y - 1][x] += 1
                        if y - 1 >= 0 and x + 1 < len(flashed[0]):
                            data[y - 1][x + 1] += 1
                        if x - 1 >= 0:
                            data[y][x - 1] += 1
                        if x + 1 < len(flashed[0]):
                            data[y][x + 1] += 1
                        if x - 1 >= 0 and y + 1 < len(flashed):
                            data[y + 1][x - 1] += 1
                        if y + 1 < len(flashed):
                            data[y + 1][x] += 1
                        if x + 1 < len(flashed[0]) and y + 1 < len(flashed):
                            data[y + 1][x + 1] += 1
                        flashed[y][x] = True
                        still_flashing = True

        for y in range(len(flashed)):
            for x in range(len(flashed[0])):
                if flashed[y][x]:
                    data[y][x] = 0

    return num_flashes


def Day11Q2(data: t.List[t.List[int]]) -> int:

    # Pretty much identical code to Q1
    num_flashes = 0
    step_flashes = 0
    step = 0

    while step < 100000:

        step += 1
        step_flashes = 0
        flashed = [[False for x in range(len(data[0]))] for y in range(len(data))]

        for y in range(len(data)):
            for x in range(len(data[0])):
                data[y][x] += 1

        still_flashing = True
        while still_flashing:
            still_flashing = False

            for y in range(len(data)):
                for x in range(len(data[0])):
                    if data[y][x] > 9 and not flashed[y][x]:

                        flashed[y][x] = "pending"
                        num_flashes += 1

            for y in range(len(flashed)):
                for x in range(len(flashed[0])):
                    if flashed[y][x] == "pending":
                        if y - 1 >= 0 and x - 1 >= 0:
                            data[y - 1][x - 1] += 1
                        if y - 1 >= 0:
                            data[y - 1][x] += 1
                        if y - 1 >= 0 and x + 1 < len(flashed[0]):
                            data[y - 1][x + 1] += 1
                        if x - 1 >= 0:
                            data[y][x - 1] += 1
                        if x + 1 < len(flashed[0]):
                            data[y][x + 1] += 1
                        if x - 1 >= 0 and y + 1 < len(flashed):
                            data[y + 1][x - 1] += 1
                        if y + 1 < len(flashed):
                            data[y + 1][x] += 1
                        if x + 1 < len(flashed[0]) and y + 1 < len(flashed):
                            data[y + 1][x + 1] += 1
                        flashed[y][x] = True
                        still_flashing = True

        for y in range(len(flashed)):
            for x in range(len(flashed[0])):
                if flashed[y][x]:
                    data[y][x] = 0
                    step_flashes += 1

        if step_flashes == len(data) * len(data[0]):
            return step


if __name__ == "__main__":

    data = [[int(x) for x in y] for y in open("input.txt").read().splitlines()]

    print("Part 1:", Day11Q1(deepcopy(data)))
    print("Part 2:", Day11Q2(deepcopy(data)))