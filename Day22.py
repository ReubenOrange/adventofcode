import aocd
import typing as t


def Day22Q1(p1: t.List[int], p2: t.List[int]) -> int:

    while len(p1) > 0 and len(p2) > 0:

        c1 = p1[0]
        c2 = p2[0]

        p1 = p1[1:]
        p2 = p2[1:]

        # Assume all cards are unique, so c1 != c2 for all c
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    if len(p1) > 0:
        p = p1
    else:
        p = p2

    ans = 0

    for i, v in enumerate(p[::-1], 1):
        ans += i * v

    return ans


def recursive_game(
    p1: t.List[int],
    p2: t.List[int],
    game_counter: int,
    round_counter: int,
    max_game: int,
    rounds_tracker: t.List[t.Tuple[t.Tuple, t.Tuple]],
) -> t.Tuple[t.List[int], t.List[int]]:

    print("=== Game {} ===\n".format(game_counter))

    print("-- Round {} (Game {}) --".format(round_counter, game_counter))
    print("Player 1's deck: " + ", ".join(str(p) for p in p1))
    print("Player 2's deck: " + ", ".join(str(p) for p in p2))

    c1 = p1[0]
    c2 = p2[0]
    print("Player 1 plays:", c1)
    print("Player 2 plays:", c2)

    p1 = p1[1:]
    p2 = p2[1:]

    if c1 > len(p1) or c2 > len(p2):
        if c1 > c2:
            print("Player 1 wins round {} of game {}".format(round_counter, game_counter))
            p1.append(c1)
            p1.append(c2)
        else:
            print("Player 2 wins round {} of game {}".format(round_counter, game_counter))
            p2.append(c2)
            p2.append(c1)
    else:
        print("Playing a sub-game to determine the winner...\n")
        max_game += 1
        recursive_game(p1[:c1], p2[:c2], max_game, 1, max_game, rounds_tracker)
        print("...anyway, back to game {}.".format(game_counter))

    if len(p1) == 0 or (tuple(p1), tuple(p2)) in rounds_tracker:
        print("The winner of game {} is player 2!".format(game_counter))
        return p1, p2

    if len(p2) == 0:
        print("The winner of game {} is player 1!".format(game_counter))
        return p1, p2

    # This will keep track of the rounds already played
    rounds_tracker.append((tuple(p1), tuple(p2)))
    recursive_game(p1, p2, game_counter, round_counter + 1, max_game, rounds_tracker)


def Day22Q2(p1: t.List[int], p2: t.List[int]) -> int:

    p1, p2 = recursive_game(p1, p2, 1, 1, 1, [])


if __name__ == "__main__":

    data = aocd.get_data(
        day=22,
        year=2020
    )

    p1, p2 = data.split("\n\n")

    p1 = p1.splitlines()[1:]
    p2 = p2.splitlines()[1:]

    p1 = list(map(int, p1))
    p2 = list(map(int, p2))

    # Treat both p1 and p2 as a stack

    # print("Part 1:", Day22Q1(p1, p2))
    print("Part 2:", Day22Q2(p1, p2))
