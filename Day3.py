
def Day3Q1():

    tree_rows = [row for row in open("input.txt")]
    trees_hit = 0
    tree_column = 0
    last_column = len(tree_rows[0].strip())

    for row in tree_rows:
        if row[tree_column] == "#":
            trees_hit += 1
        tree_column = (tree_column + 3) % last_column

    print("Part 1, trees hit: " + str(trees_hit))


def Day3Q2():

    tree_rows = [row for row in open("input.txt")]
    slopes = [1, 3, 5, 7, 0.5]

    # dictionary to track trees hit for each slope value
    trees_hit_per_slope = {1: 0, 3: 0, 5: 0, 7: 0, 0.5: 0}
    tree_column = 0
    last_column = len(tree_rows[0].strip())

    for slope in slopes:
        for row in tree_rows:
            # check tree_column is a whole number (for decimal slopes)
            if tree_column % 1 == 0:
                if row[int(tree_column)] == "#":
                    trees_hit_per_slope[slope] += 1
            tree_column = (tree_column + slope) % last_column
        tree_column = 0

    # multiply trees hit together for each slope
    trees_hit_multi = 1
    for slope in trees_hit_per_slope:
        print("Slope: " + str(slope) + ", Trees hit: " + str(trees_hit_per_slope[slope]))
        trees_hit_multi = trees_hit_multi * trees_hit_per_slope[slope]

    print("Part 2, trees hit:" + str(trees_hit_multi))


if __name__ == "__main__":
    Day3Q1()
    Day3Q2()
