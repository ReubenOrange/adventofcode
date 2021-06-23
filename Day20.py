import aocd
import typing as t
import re
from collections import defaultdict
import math

BoxDict = t.Dict[int, t.List[str]]
EdgesSet = t.Set[t.Tuple]
EdgesDict = t.DefaultDict[str, t.List[int]]  # edge string is the key, value is a list of box ids
NeighboursDict = t.DefaultDict[int, t.Set[int]]


def create_box_dict(data: str) -> BoxDict:

    boxes = data.split("\n\n")

    box_dict = {}

    tile_re = re.compile(r"Tile (\d+):")

    for box in boxes:
        box_list = box.splitlines()

        box_dict[int(tile_re.match(box_list[0]).group(1))] = box_list[1:]

    return box_dict


def create_edges_dict(box_dict: BoxDict) -> EdgesDict:

    edges_dict = defaultdict(list)

    for key, box in box_dict.items():
        edges_dict[box[0]].append(key)
        edges_dict[box[-1]].append(key)
        edges_dict[box[0][::-1]].append(key)
        edges_dict[box[-1][::-1]].append(key)

        left_side = ""
        right_side = ""

        for line in box:
            left_side += line[0]
            right_side += line[-1]

        edges_dict[left_side].append(key)
        edges_dict[right_side].append(key)
        edges_dict[left_side[::-1]].append(key)
        edges_dict[right_side[::-1]].append(key)

    return edges_dict


# TODO: create another function like this for the top left corner piece to find two transformations
# Goal to find how box2 could be rotated or flipped to match up with box 1

# All the possible flips and rotations form the dihedral group of order 8:
# ["","R","RR","RRR","F","RF","RRF","RRRF"]

# R = rotate list of lists 90 degrees clockwise: zip(*reversed(your_list))
# F = flip list of lists along vertical axis: reversed(your_list)

# Returns the transformation that needs to be perfomed on box2 for it to line up with box1
# with the left or top side of box2 lining up with the right or bottom side of box1
def find_matching_edge(box1: t.List[str], box2: t.List[str], rel_pos_box2: str) -> str:

    edges_dict = defaultdict(list)

    edges_list = []
    left_side = ""
    right_side = ""

    for line in box2:
        left_side += line[0]
        right_side += line[-1]

    # [top, right, bottom, left, top_inv, right_inv, bottom_inv, left_inv]
    edges_list.append(box2[0])
    edges_list.append(right_side)
    edges_list.append(box2[-1])
    edges_list.append(left_side)
    edges_list.append(box2[0][::-1])
    edges_list.append(right_side[::-1])
    edges_list.append(box2[-1][::-1])
    edges_list.append(left_side[::-1])

    box1_right_side = "".join(line[-1] for line in box1)
    box1_bottom_side = box1[-1]

    # match index to rotation required mapping:
    # [top, right, bottom, left, top_inv, right_inv, bottom_inv, left_inv]
    # R is a rotation clockwise, F is a reflection in the vertical axis
    if rel_pos_box2 == "right":
        for edge in range(len(edges_list)):
            if edge == box1_right_side:
                match_index = edge
                break
        transformations = ["RF", "F", "R", "", "RRR", "RR", "RRRF", "RRF"]
    elif rel_pos_box2 == "bottom":
        for edge in range(len(edges_list)):
            if edge == box1_bottom_side:
                match_index = edge
                break
        transformations = ["", "RRR", "RRF", "RF", "F", "RRRF", "RR", "R"]

    return transformations[match_index]


# Rewrote this one as a generator function with some help from:
# https://github.com/mebeim/aoc/tree/master/2020#day-20---jurassic-jigsaw
def poss(box: t.List[t.List[str]]) -> t.List[t.List[t.List[str]]]:

    orientations = []

    # R = rotate list of lists 90 degrees clockwise: zip(*reversed(your_list))
    # F = flip list of lists along vertical axis: ??? reversed(your_list)
    # All the possible flips and rotations form the dihedral group of order 8:
    # ["","R","RR","RRR","F","RF","RRF","RRRF"]

    orientations.append(box)
    orientations.append(list(zip(*reversed(box))))
    orientations.append(list(zip(*reversed(list(zip(*reversed(box)))))))
    orientations.append(list(zip(*reversed(list(zip(*reversed(list(zip(*reversed(box))))))))))
    orientations.append(list(reversed(box)))
    orientations.append(list(reversed(list(zip(*reversed(box))))))
    orientations.append(list(reversed(list(zip(*reversed(list(zip(*reversed(box)))))))))
    orientations.append(
        list(reversed(list(zip(*reversed(list(zip(*reversed(list(zip(*reversed(box)))))))))))
    )

    return orientations


# Rewrote the poss function as a generator function with some help from:
# https://github.com/mebeim/aoc/tree/master/2020#day-20---jurassic-jigsaw
def poss_gen(box: t.List[t.List[str]]) -> t.Generator:

    yield from orientations(box)
    yield from orientations(box[::-1])


def orientations(box: t.List[t.List[str]]) -> t.Generator:
    yield box
    for _ in range(3):
        # rotate 90 degrees
        box = list(zip(*reversed(box)))
        yield box


# Loops through all of the edges in edges_dict, then loops though the (two) ids using each one
# in turn to be the dictionary key for the neighbours_dict and the other to be the value, ending up
# with a dictionary mapping each box id with its 2, 3 or 4 neighbours. We know they are neighbours
# because they share an edge, but we don't know what edge they share, we are not recording that
# infomation in the neighbours dictionary.
def create_neighbours_dict(edges_dict: EdgesDict) -> NeighboursDict:

    neighbours_dict = defaultdict(set)

    for edge, box_key_list in edges_dict.items():

        for box_key_outer in box_key_list:
            for box_key_inner in box_key_list:
                if box_key_inner != box_key_outer:
                    neighbours_dict[box_key_outer].add(box_key_inner)

    return neighbours_dict


# Does the boundary of p1 match p2, assuming p2 is in the direction of (dr,dc)?
def matches(p1: t.List[str], p2: t.List[str], dr: int, dc: int) -> bool:
    C = len(p1[0])
    R = len(p1)
    if dr == -1:  # up, so top of p1 should match bottom
        for c in range(C):
            if p1[0][c] != p2[R - 1][c]:
                return False
        return True
    elif dc == 1:  # right, so right of p1 should match left of p2
        for r in range(R):
            if p1[r][C - 1] != p2[r][0]:
                return False
        return True
    elif dr == 1:
        for c in range(C):
            if p1[R - 1][c] != p2[0][c]:
                return False
        return True
    elif dc == -1:
        for r in range(R):
            if p1[r][0] != p2[r][C - 1]:
                return False
        return True
    else:
        assert False


def build_image(neighbours_dict: NeighboursDict, box_dict: BoxDict) -> t.List[t.List[str]]:

    # With some help from:
    # https://www.youtube.com/watch?v=H0rTE9r9YmQ&ab_channel=JonathanPaulson
    GR = int(len(neighbours_dict) ** 0.5)  # number of puzzle peices in each row
    GC = int(len(neighbours_dict) ** 0.5)
    R = 10  # pixels within a puzzle peice row
    C = 10

    D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    corner_piece = [key for key, value in neighbours_dict.items() if len(value) == 2][0]

    PLACE = [[None for _ in range(GC)] for _ in range(GR)]

    PLACE[0][0] = corner_piece
    PLACE[0][1], PLACE[1][0] = neighbours_dict[corner_piece]

    USED = set()
    USED.add(PLACE[0][0])
    USED.add(PLACE[1][0])
    USED.add(PLACE[0][1])

    while True:
        if len(USED) == GC * GR:
            break
        for r in range(GR):
            for c in range(GC):
                if PLACE[r][c] is not None:
                    continue
                opts = set([k for k in neighbours_dict.keys() if k not in USED])
                for dr, dc in D:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < GR and 0 <= cc < GC and PLACE[rr][cc]:
                        opts = opts & neighbours_dict[PLACE[rr][cc]]
                if len(opts) == 1:
                    chosen = list(opts)[0]
                    PLACE[r][c] = chosen
                    assert chosen not in USED
                    USED.add(chosen)

    # PLACE is now a grid of pieces unoriented, next step is to orient them and place the result in PIECES

    PIECES = [[None for _ in range(12)] for _ in range(12)]

    for r in range(GR):
        for c in range(GC):
            opts = poss(box_dict[PLACE[r][c]])
            for dr, dc in D:
                rr, cc = r + dr, c + dc
                if 0 <= rr < GR and 0 <= cc < GC:
                    ok_nbr = list()
                    opts_nbr = poss(box_dict[PLACE[rr][cc]])
                    for o1 in opts:
                        for o2 in opts_nbr:
                            if matches(o1, o2, dr, dc):
                                ok_nbr.append(o1)
                    # assert len(ok_nbr) == 1
                    opts = ok_nbr
            assert len(opts) == 1
            PIECES[r][c] = opts[0]

    # IMAGE is the final puzzle picture with the peice borders removed
    IMAGE = [[None for _ in range(GC * (C - 2))] for _ in range(GR * (R - 2))]

    for r in range(GR):
        for c in range(GC):
            T = PIECES[r][c]
            for rr in range(1, len(T) - 1):
                for cc in range(1, len(T[rr]) - 1):
                    IMAGE[r * (R - 2) + (rr - 1)][c * (C - 2) + (cc - 1)] = T[rr][cc]

    return IMAGE


def water_roughness(image: t.List[t.List[str]]) -> int:

    # sea monster
    M = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

    MR = len(M)
    MC = len(M[0])

    for row in M:
        assert len(row) == MC

    IR = len(image)
    IC = len(image[0])

    for row in image:
        assert len(row) == IC

    for IM in poss_gen(image):

        assert len(IM) == IR
        assert len(IM[0]) == IC
        IS_M = [[False for _ in range(IC)] for _ in range(IR)]
        has_monster = False

        for r in range(IR):
            for c in range(IC):
                is_monster = True
                for mr in range(MR):
                    for mc in range(MC):
                        outside_range = not (0 <= r + mr < IR and 0 <= c + mc < IC)
                        if outside_range:
                            is_monster = False
                        else:
                            not_monster_part = M[mr][mc] == "#" and IM[r + mr][c + mc] != "#"
                            if not_monster_part:
                                is_monster = False

                if is_monster:
                    has_monster = True
                    for mr in range(MR):
                        for mc in range(MC):
                            if M[mr][mc] == "#":
                                IS_M[r + mr][c + mc] = True

        # Assumes only one orientation has sea monsters
        if has_monster:
            # Print the final picture with the sea monsters highlighted as 'O'
            for row in IS_M:
                row_pr = ""
                for col in row:
                    if col:
                        row_pr += "O"
                    else:
                        row_pr += "."
                print(row_pr)
            ans = 0
            # Does not assume that sea monsters can not overlap
            for r in range(IR):
                for c in range(IC):
                    if IM[r][c] == "#" and not IS_M[r][c]:
                        ans += 1
            return ans


def Day20Q2(data: str) -> int:

    box_dict = create_box_dict(data)

    edges_dict = create_edges_dict(box_dict)

    neighbours_dict = create_neighbours_dict(edges_dict)

    pieces = build_image(neighbours_dict, box_dict)

    return water_roughness(pieces)


def Day20Q1(data: str) -> int:

    box_dict = create_box_dict(data)

    edges_dict = create_edges_dict(box_dict)

    neighbours_dict = create_neighbours_dict(edges_dict)

    two_neighbours_list = [key for key, value in neighbours_dict.items() if len(value) == 2]

    return math.prod(two_neighbours_list)


if __name__ == "__main__":

    data = aocd.get_data(
        day=20,
        year=2020,
        session="53616c7465645f5f3d94ce9f37a112b8c3d011d6c5ab84a43bc41aeaa4038fb639db62b3ad64c5eebce715096e4d0dae",
    )

    print("Part 1:", Day20Q1(data))
    print("Part 2:", Day20Q2(data))
