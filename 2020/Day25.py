import aocd
import typing as t


def find_loop_size(subject_number: int, target: int) -> int:

    value = 1
    loop_counter = 0

    while value != target:

        loop_counter += 1
        if loop_counter > 10000000:
            print("Did not find loop size")
            break
        # if loop_counter % 100000 == 0:
        #    print("loop counter at:", loop_counter)

        value *= subject_number
        value = value % 20201227

    return loop_counter


def transform(subject_number: int, loop_size: int) -> int:

    value = 1

    for _ in range(loop_size):

        value *= subject_number
        value = value % 20201227

    return value


def Day25Q1(card: t.List, door: t.List) -> int:

    value = 1
    subject_number = 7

    loop_size = 1  # we don't know what this value should be yet

    card_loop_size = find_loop_size(subject_number, card)
    door_loop_size = find_loop_size(subject_number, door)

    # print("card_loop_size:", card_loop_size)
    # print("door_loop_size:", door_loop_size)

    if card_loop_size < door_loop_size:
        ans = transform(door, card_loop_size)
    else:
        ans = transform(card, door_loop_size)

    return ans


if __name__ == "__main__":

    data = aocd.get_data(
        day=25,
        year=2020,
        session="53616c7465645f5f3d94ce9f37a112b8c3d011d6c5ab84a43bc41aeaa4038fb639db62b3ad64c5eebce715096e4d0dae",
    )

    card, door = (int(x) for x in data.splitlines())

    # card, door = 5764801, 17807724

    # print("card:", card)
    # print("door:", door)

    print("Part 1:", Day25Q1(card, door))
    print("Part 2:", "Thanks reindeer!")
