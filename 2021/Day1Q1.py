import aocd
import typing as t

def Day1Q1(depths: t.List[int]) -> int:

    return sum(1 for i in range(1, len(depths)) if depths[i] > depths[i-1])


def Day1Q2(depths: t.List[int]) -> int:
        
    return sum(1 for i in range(3, len(depths)) if sum(depths[i-2:i+1])>sum(depths[i-3:i]))


if __name__ == "__main__":
    depths = [int(x) for x in aocd.get_data(day=1, year=2021, session="53616c7465645f5f5af8cd657c485ceed35a06c32ed70e555593e1b9083e2a90298bf1916bd09a8c90e2a61a555ae992").splitlines()]
    
    print("Part 1:", Day1Q1(depths))
    print("Part 2:", Day1Q2(depths))
