import aocd
import typing as t
from anytree import Node, RenderTree, PreOrderIter


def find_sum(my_node):

    if len(my_node.children) == 0:
        my_node.total_sum = sum(my_node.files)
        return sum(my_node.files)

    my_node.total_sum = sum(my_node.files) + sum(find_sum(x) for x in my_node.children)

    return sum(my_node.files) + sum(find_sum(x) for x in my_node.children)


def find_total(my_node):

    if len(my_node.children) == 0 and my_node.total_sum <= 100000:
        return my_node.total_sum

    if my_node.total_sum <= 100000:
        return my_node.total_sum + sum(find_total(x) for x in my_node.children)
    else:
        return sum(find_total(x) for x in my_node.children)


def find_smallest_to_delete(my_node, current_smallest, min_sum):

    if len(my_node.children) == 0:
        return my_node

    for child in my_node.children:

        if (
            min_sum
            <= find_smallest_to_delete(child, current_smallest, min_sum).total_sum
            < current_smallest.total_sum
        ):
            current_smallest = child

    return current_smallest


def build_tree(data):

    root = Node("", files=[], total_sum=0)

    current = root

    for line in data[1:]:

        if line[:4] == "$ ls":
            continue

        if line[:7] == "$ cd ..":
            current = current.parent
            continue

        if line[:4] == "$ cd":
            for child in current.children:
                if child.name == line.split(" ")[2]:
                    current = child
                    break
            continue

        if line[:3] == "dir" and not line.split(" ")[1] in [
            current.children[x].name for x in range(len(current.children))
        ]:
            x = Node(line.split(" ")[1], parent=current, files=[], total_sum=0)
        else:
            current.files.append(int(line.split(" ")[0]))

    return root


def Day2Q1(data: t.List[str]) -> int:

    root = build_tree(data)

    # go through tree adding the total sum field to each directory
    find_sum(root)

    return find_total(root)


def Day2Q2(data: t.List[str]) -> int:

    root = build_tree(data)

    # go through tree adding the total sum field to each directory
    find_sum(root)

    node_to_delete_size = root.total_sum

    space_we_need = 30000000 - (70000000 - root.total_sum)

    for node in PreOrderIter(root):
        if space_we_need <= node.total_sum < node_to_delete_size:
            node_to_delete_size = node.total_sum

    return node_to_delete_size


if __name__ == "__main__":

    data = aocd.get_data(
        day=7,
        year=2022,
    ).splitlines()

    # test_data = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k".splitlines()

    print("Part 1:", Day2Q1(data))
    print("Part 2:", Day2Q2(data))
