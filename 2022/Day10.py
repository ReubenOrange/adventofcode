import aocd
import typing as t
from math import floor


def Day2Q1(data: t.List[str]) -> int:

    cycle = 0
    instructions = []
    signal = [0]
    X = 1

    for line in data:
        if line[:4] == "noop":
            instructions.append(("noop", 0))
        else:
            instructions.append((line.split(" ")[0], int(line.split(" ")[1])))

    for I in instructions:

        if I[0] == "noop":
            cycle += 1  # cycle that is happening right now
            signal.append(cycle * X)

        if I[0] == "addx":
            cycle += 1
            signal.append(cycle * X)
            cycle += 1
            signal.append(cycle * X)

            X += I[1]

    return (
        signal[20] + signal[60] + signal[100] + signal[140] + signal[180] + signal[220]
    )


def Day2Q2(data: t.List[str]) -> int:

    instructions = []

    for line in data:
        if line[:4] == "noop":
            instructions.append(("noop", 0))
        else:
            instructions.append((line.split(" ")[0], int(line.split(" ")[1])))

    cycle = 0
    X = 1
    picture = []

    for I in instructions:

        if I[0] == "noop":
            cycle += 1  # cycle that is happening right now
            print("Start cycle   {}: begin executing {}{}".format(cycle, I[0], I[1]))
            print(
                "During cycle  {}: CRT draws pixel in position {}".format(
                    cycle, (cycle - 1) % 40
                )
            )
            picture.append(
                "#" if (((cycle - 1) % 40) - 1) <= X <= ((cycle) % 40) else "."
            )
            print(
                "Current CRT row: {}".format("".join(picture[floor(cycle / 40) * 40 :]))
            )
            print("End of cycle  {}: finish executing {}{}".format(cycle, I[0], I[1]))

        if I[0] == "addx":
            cycle += 1
            print("Start cycle   {}: begin executing {}{}".format(cycle, I[0], I[1]))
            print(
                "During cycle  {}: CRT draws pixel in position {}".format(
                    cycle, (cycle - 1) % 40
                )
            )
            picture.append(
                "#" if (((cycle - 1) % 40) - 1) <= X <= ((cycle) % 40) else "."
            )
            print(
                "Current CRT row: {}".format("".join(picture[floor(cycle / 40) * 40 :]))
            )

            cycle += 1
            print(
                "During cycle  {}: CRT draws pixel in position {}".format(
                    cycle, (cycle - 1) % 40
                )
            )
            picture.append(
                "#" if (((cycle - 1) % 40) - 1) <= X <= ((cycle) % 40) else "."
            )
            print(
                "Current CRT row: {}".format("".join(picture[floor(cycle / 40) * 40 :]))
            )
            X += I[1]
            print(
                "End of cycle  {}: finish executing {} {} (Register X is now {})".format(
                    cycle, I[0], I[1], X
                )
            )

    print("********************************")

    final_picture = ""

    for i in range(floor(len(picture) / 40)):
        final_picture += "\n" + "".join(picture[i * 40 : (i + 1) * 40])

    return final_picture


if __name__ == "__main__":

    data = aocd.get_data(
        day=10,
        year=2022,
    ).splitlines()

    # data = "addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop\n".splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
