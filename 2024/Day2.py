import aocd
import typing as t


def Q1(reports: t.List[str]) -> int:

    safe = 0

    for report in reports:

        levels = [int(x) for x in report.split()]
        inc = True
        desc = True
        gradual = True

        for i, level in enumerate(levels):

            if i == 0:
                continue

            if not (levels[i] > levels[i - 1] and inc):
                inc = False

            if not (levels[i] < levels[i - 1] and desc):
                desc = False

            if not (1 <= abs(levels[i] - levels[i - 1]) <= 3):
                gradual = False

        if (inc or desc) and gradual:
            safe += 1

    return safe


def Q2(reports: t.List[str]) -> int:

    safe = 0

    for report in reports:

        levels = [int(x) for x in report.split()]

        damped_safe = []

        for j in range(len(levels)):

            damped = [levels[l] for l in range(len(levels)) if l != j]

            inc = True
            desc = True
            gradual = True

            for i in range(len(damped)):

                if i == 0:
                    continue

                if not (damped[i] > damped[i - 1] and inc):
                    inc = False

                if not (damped[i] < damped[i - 1] and desc):
                    desc = False

                if not (1 <= abs(damped[i] - damped[i - 1]) <= 3):
                    gradual = False

            damped_safe += [(inc or desc) and gradual]

        safe += any(damped_safe)

    return safe


if __name__ == "__main__":

    reports = aocd.get_data(day=2, year=2024).split("\n")

    print("Part 1:", Q1(reports))

    print("Part 2:", Q2(reports))
