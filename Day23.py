import aocd
import typing as t


def Day23Q1(l: t.List[int]) -> str:

    pos = 0
    label = 0

    for x in range(100):

        label = l[pos]

        pick_up1 = (pos + 1) % len(l)
        pick_up2 = (pos + 2) % len(l)
        pick_up3 = (pos + 3) % len(l)

        l1 = l[pick_up1]
        l2 = l[pick_up2]
        l3 = l[pick_up3]
        l.remove(l1)
        l.remove(l2)
        l.remove(l3)

        new_des = label - 1

        while new_des not in l:

            if new_des < 1:
                new_des = max(l)
            if new_des not in l:
                new_des -= 1

        new_pos = (l.index(new_des) + 1) % len(l)

        l = l[:new_pos] + [l1] + [l2] + [l3] + l[new_pos:]

        # print(l)

        pos = (l.index(label) + 1) % len(l)

        # print(pos)

    pos = l.index(1)

    new_l = l[pos:] + l[:pos]

    return "".join(str(x) for x in new_l[1:])


# With some help from JonathanPaulson:
# https://www.youtube.com/watch?v=62chpxJA9pQ
# Didn't end up using the linked list class though
class LinkedList(object):
    def __init__(
        self,
    ):
        self.head = None
        self.D = {}

    def append(self, x):
        if self.head is None:
            self.head = Node(self, x, head, head)
        else:
            node = Node(x, None, None)
            node.next = head
            node.prev = head.prev
            head.prev.next = node
            head.prev = node
            self.D[x] = node


class Node(object):
    def __init__(self):
        def __init__(self, parent, v, prev, next_):
            self.parent = parent
            self.v = v
            self.prev = prev
            self.next = next_


def Day23Q2(l: t.List[int]) -> str:

    # I tried to solve this problem without using a linked list by finding a pattern in which
    # elements were updated each time. It seemed like a pattern was emerging but the number of
    # elements needing to be updated ended up growing like O(n), so I'm using a linked list now
    # and taking advantage of all the numbers from 1 to 1M being used so that we can use the
    # index of a python list like a dictionary pointing to each of the nodes in an array that
    # stores the value of the cup that is next.

    orig_len = len(l)
    nmoves = 10000000
    ncups = 1000000

    l = l + list(range(max(l) + 1, ncups + 1))

    # N is the array of next cups. It is one element longer than l so that we can use the actual
    # cup number as the index rather than offsetting by 1. This means element 0 of the array will
    # just not be used.
    N = [None for i in range(len(l) + 1)]
    # create N for the original setup
    for i in range(orig_len):
        N[l[i]] = l[(i + 1) % orig_len]
    N[l[orig_len - 1]] = orig_len + 1
    # fill N for the remaining million or so cups
    for i in range(orig_len + 1, len(l)):
        N[i] = i + 1
    # complete the loop, setting the next value for the last cup to the first cup
    N[-1] = l[0]

    cur = l[0]

    for _ in range(nmoves):

        pick_up = N[cur]
        N[cur] = N[N[N[pick_up]]]

        l1 = pick_up
        l2 = N[pick_up]
        l3 = N[N[pick_up]]

        # cur = 3
        # pick_up = N[cur] = N[3] = 8
        # N[cur] = 2

        dest = ncups if cur == 1 else cur - 1
        while dest in [l1, l2, l3]:
            dest = ncups if dest == 1 else dest - 1

        # insert the 3 cups at the destination
        N[l3] = N[dest]
        N[dest] = l1
        cur = N[cur]

    ans = N[1] * N[N[1]]

    return ans


if __name__ == "__main__":

    data = aocd.get_data(day=23, year=2020)

    # data = "389125467"

    l = [int(x) for x in data]

    print("Part 1:", Day23Q1(l.copy()))
    print("Part 2:", Day23Q2(l.copy()))