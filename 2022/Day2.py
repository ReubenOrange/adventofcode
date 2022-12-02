import aocd
import typing as t


def Day2Q1(data: t.List[str]) -> int:

    # A = X = rock = 1
    # B = Y = paper = 2
    # C = Z = scissors = 3

    m = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    moves = [[m[x[0]], m[x[1]]] for x in [z.split() for z in data]]

    # 2 is a win
    # 1 is a loss
    # 0 is a draw
    score = [3, 0, 6]

    # You go rock, I go paper, I win
    # (1 - 2) % 3 = 2
    # You go paper, I go scissors, I win
    # (2 - 3) % 3 = 2
    # You go scissors, I go rock, I win
    # (3 - 1) % 3 = 2

    # You go rock, I go scissors, I lose
    # (1 - 3) % 3 = 1
    # You go paper, I go rock, I lose
    # (2 - 1) % 3 = 1
    # You go scissors, I go paper, I lose
    # (3 - 2) % 3 = 1

    return sum(score[(move[0] - move[1]) % 3] + move[1] for move in moves)


def Day2Q2(data: t.List[str]) -> int:

    # A = rock = 1 -> W = 2, L = 3, D = 1
    # B = paper = 2 -> W = 3, L = 1, D = 2
    # C = scissors = 3 -> W = 1, L = 2, D = 3

    # X = Lose -> (move[0] - 2) % 3 + 1
    # Y = Draw -> (move[0] - 1) % 3 + 1
    # Z = Win ->  (move[0] - 0) % 3 + 1

    m = {"A": 1, "B": 2, "C": 3, "X": 2, "Y": 1, "Z": 0}

    score = [3, 0, 6]

    return sum(score[(move[0] - move[1]) % 3] + move[1] for move in moves)


if __name__ == "__main__":

    data = aocd.get_data(
        day=2,
        year=2022,
    ).splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
