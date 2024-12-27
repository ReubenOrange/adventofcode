import aocd
import typing as t

def Day1Q1(rations: t.List[str]) -> int:

    return max([sum(int(snack) for snack in elf.split()) for elf in rations])
    


def Day1Q2(rations: t.List[str]) -> int:

    sorted_elf_rations = sorted([sum(int(snack) for snack in elf.split()) for elf in rations])    
    return sum(sorted_elf_rations[-3:])



if __name__ == "__main__":

    rations = aocd.get_data(day=1, year=2022).split("\n\n")

    print("Part 1:", Day1Q1(rations))
    print("Part 2:", Day1Q2(rations))