import aocd
import typing as t
import re


def merge_intervals(intervals: t.List[tuple]) -> t.List[tuple]:
    result = []
    (start_candidate, stop_candidate) = intervals[0]
    for (start, stop) in intervals[1:]:
        if start <= stop_candidate + 1:
            stop_candidate = max(stop, stop_candidate)
        else:
            result.append((start_candidate, stop_candidate))
            (start_candidate, stop_candidate) = (start, stop)
    result.append((start_candidate, stop_candidate))
    return result


def DayQ1(data: t.List[str]) -> int:

    y = 2000000
    impossible_points_num = 0
    intervals = []

    for line in data:

        sx, sy, bx, by = [
            int(x)
            for x in re.findall("x=(-*\d+), y=(-*\d+):.*x=(-*\d+), y=(-*\d+)", line)[0]
        ]

        md = abs(sx - bx) + abs(sy - by)

        # a = |x2-x1|+|y2-y1|
        # x2 = x1 +- (a - |y2 - y1|)
        intx1 = sx - (md - abs(y - sy))
        intx2 = sx + (md - abs(y - sy))

        if sy - md <= y <= sy + md:
            intervals.append((min(intx1, intx2), max(intx1, intx2)))

    merged_intervals = merge_intervals(sorted(intervals))

    impossible_points_num = sum(
        abs(interval[1] - interval[0]) for interval in merged_intervals
    )

    return impossible_points_num


def DayQ2(data: t.List[str]) -> int:

    # for every line from the lowest y value, to the highest y value, check that the intervals are all continuous

    miny = 0
    maxy = 4000000

    sb_list = []

    for line in data:

        sx, sy, bx, by = [
            int(x)
            for x in re.findall("x=(-*\d+), y=(-*\d+):.*x=(-*\d+), y=(-*\d+)", line)[0]
        ]

        md = abs(sx - bx) + abs(sy - by)

        sb_list.append([sx, sy, bx, by, md])

    for i in range(miny, maxy + 1):

        intervals = []

        for sx, sy, bx, by, md in sb_list:

            if abs(sy - i) < md:
                intx1 = sx - (md - abs(i - sy))
                intx2 = sx + (md - abs(i - sy))
                intervals.append((min(intx1, intx2), max(intx1, intx2)))

        merged_intervals = merge_intervals(sorted(intervals))

        if len(merged_intervals) > 1:
            return 4000000 * (merged_intervals[0][1] + 1) + i


def Day2Q2_take2(data: t.List[str]) -> int:

    # Attempt to do a faster solution by looking at the projection of the diamonds onto the y axis. But it didn't work.
    pgs = []
    ngs = []
    miny = 0
    maxy = 0

    for line in data:

        sx, sy, bx, by = [
            int(x)
            for x in re.findall("x=(-*\d+), y=(-*\d+):.*x=(-*\d+), y=(-*\d+)", line)[0]
        ]

        md = abs(sx - bx) + abs(sy - by)

        ts = (sx, sy - md)
        bs = (sx, sy + md)
        rs = (sx + md, sy)
        ls = (sx - md, sy)

        # Let's put a wall at the position of negative 10,000,000, and look at the shadow cast on it from the diamonds.
        # Projecting down to that wall, for the line extending from ts (top) to ls (left). Every 1 we go down and left, x value decreases by
        # 1, and the y value increases by 1. So the line will intersect the wall at (-10M, 10M + sy - sx + md ). This is the top left of the
        # diamond line. Now we need to find the bottor right of the diamond:  (-10M, )

        # (x1, y1) = (sx - md, sy), (x2, y2) = (sx, sy - md)
        y_pg1 = sy + (((sy - md) - (sy)) / ((sx) - (sx - md))) * (0 - (sx - md))

        y_pg1 = sy + sx - md
        y_pg2 = sy + sx + md
        y_ng1 = sy - sx - md
        y_ng2 = sy - sx + md

        pgs.append((y_pg1, y_pg2))
        ngs.append((y_ng1, y_ng2))

        # y = mx + c
        # y - y1 = m(x-x1)
        # m = (y2-y1)/(x2-x1)

        # If, x = 0
        # y = y1 + ((y2-y1)/(x2-x1))*(0-x1)

        # Looking for 2 lines that have a difference of 2 in their y intercepts

        maxy = max(maxy, sy + md)
        miny = min(miny, sy - md)

        # Okay I think I know what is the bug now. We're projecting out the diamond onto the y axis, but some of the diamonds also
        # intersect with the y axis so the calculation won't return the right interval. Either we need to move that line that we're
        # looking at back more to the left so that it doesn't intersect with any of the diamonds. Or use smaller intervals including a
        # subset of the projection and the intersection


if __name__ == "__main__":

    data = aocd.get_data(day=15, year=2022).split("\n")

    test_data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split(
        "\n"
    )

    print("Part 1:", DayQ1(data))
    print("Part 2:", DayQ2(data))

    # print("Part 2:", Day2Q2_take2(test_data))
