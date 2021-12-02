import aocd
import typing as t

def Day1Q1(depths: t.List[int]) -> int:

    return sum(1 for i in range(1, len(depths)) if depths[i] > depths[i-1])


def Day1Q2(depths: t.List[int]) -> int:
        
    return sum(1 for i in range(3, len(depths)) if sum(depths[i-2:i+1])>sum(depths[i-3:i]))


if __name__ == "__main__":
    depths = [int(x) for x in aocd.get_data(day=1, year=2021).splitlines()]
    
    print("Part 1:", Day1Q1(depths))
    print("Part 2:", Day1Q2(depths))
