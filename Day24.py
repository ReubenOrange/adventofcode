import aocd
import typing as t
from collections import Counter


def Day24Q(tile_lines: t.List) -> int:

    moves = set()
    M = {"e": (1, 0), "w": (-1, 0), "ne": (0, 1), "nw": (-1, 1), "se": (1, -1), "sw": (0, -1)}

    for line in tile_lines:

        i = 0
        move = (0, 0)

        while i < len(line):

            if line[i] == "n" or line[i] == "s":
                dir = line[i] + line[i + 1]
                i += 1
            else:
                dir = line[i]

            move = tuple(sum(x) for x in zip(move, M[dir]))
            i += 1

        moves ^= set([move])

    # change to yield
    yield len(moves)

    d = [v for k, v in M.items()]
    b = moves.copy()

    for i in range(1, 101):

        b_add = set()
        b_remove = set()

        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        for tile in b:
            b_n = 0
            for dd in d:
                n = tuple(sum(x) for x in zip(tile, dd))
                b_n += 1 if n in b else 0
            if b_n == 0 or b_n > 2:
                b_remove |= set([tile])

        # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        for tile in b:
            for dd in d:
                n = tuple(sum(x) for x in zip(tile, dd))
                if n not in b:  # if neighbour is white
                    b_n = 0
                    for ddd in d:
                        nn = tuple(sum(x) for x in zip(n, ddd))
                        b_n += 1 if nn in b else 0
                    if b_n == 2:
                        b_add |= set([n])

        # print("b:", b)
        b |= b_add
        b -= b_remove
        # print("b_add:", b_add)
        # print("b_remove:", b_remove)

        # print("Day {}: {}".format(i, len(b)))

    # Short version of this (with help from: https://github.com/mebeim/aoc/tree/master/2020#day-24---lobby-layout):

    # b = moves.copy()
    # for _ in range(100):
    #    near = Counter((x + dx, y + dy) for x, y in b for dx, dy in d)
    #    b = set(p for p, n in near.items() if n == 2 or n == 1 and p in b)

    yield len(b)


if __name__ == "__main__":

    data = aocd.get_data(day=24, year=2020)

    # data = open("./sample.txt", "r").read()

    tile_lines = data.splitlines()

    part = 1
    for ans in Day24Q(tile_lines):
        print("Part %s: %s" % (str(part), str(ans)))
        part += 1
