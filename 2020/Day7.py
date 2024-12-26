"""
create a bag object which contains:
- bag name
- list of bags that bag can contains

- go through each bag list and create a list of bags that can contain gold directly
- for each of those, go through which bags can contain them (function for this?)
- continue until all have been checked

"""
import aocd
import re


class Bag:
    def __init__(self, colour, can_contain_list):
        self.colour = colour
        self.can_contain_list = can_contain_list

    def __str__(self):
        return (
            "Bag colour: " + str(self.colour) + " | Can contain list: " + str(self.can_contain_list)
        )


def create_bag_list(is_numbered):

    data = aocd.get_data(day=7, year=2020).split("\n")

    bag_list = []

    for bag in data:
        if re.search(r"(.+?)(?= bags)", bag):
            colour = re.search(r"(.+?)(?= bags)", bag).group(0)
        else:
            colour = ""

        if re.search(r"contain \d* (.*)\.", bag):
            can_contain_list = re.search(r"contain \d* (.*)\.", bag).group(0).split(", ")
        else:
            can_contain_list = []

        for i in range(len(can_contain_list)):
            can_contain_list[i] = (
                can_contain_list[i]
                .replace("contain ", "")
                .replace(".", "")
                .replace(" bags", "")
                .replace(" bag", "")
            )
            if is_numbered:
                can_contain_list[i] = re.search(r"\d* (.*)", can_contain_list[i]).group(0)
            else:
                can_contain_list[i] = re.search(r"\d* (.*)", can_contain_list[i]).group(1)

        bag_list.append(Bag(colour, can_contain_list))

    return bag_list


def Day7Q1():

    bag_list = create_bag_list(is_numbered=False)

    set_size = 1
    previous_set_size = 0
    can_contain_gold_set = set(["shiny gold"])

    while set_size > previous_set_size:
        previous_set_size = len(can_contain_gold_set)
        for bag in bag_list:
            for inner_bag in bag.can_contain_list:
                add_to_can_contain_gold_set = set()
                if inner_bag in can_contain_gold_set:
                    add_to_can_contain_gold_set.add(bag.colour)
                can_contain_gold_set = can_contain_gold_set.union(add_to_can_contain_gold_set)
        set_size = len(can_contain_gold_set)
    can_contain_gold_set.remove("shiny gold")

    return len(can_contain_gold_set)


def Day7Q2():

    bag_list = create_bag_list(is_numbered=True)

    dict_size = 1
    previous_dict_size = 0

    number_of_bags_dict = {"shiny gold": 1}
    number_of_bags_counter = 0
    previous_counter = -1

    while number_of_bags_counter > previous_counter:
        previous_counter = number_of_bags_counter
        add_to_bag_dict = {}
        for bag in bag_list:
            if bag.colour in number_of_bags_dict:
                for inner_bag in bag.can_contain_list:
                    bag_name = re.search(r"\d* (.*)", inner_bag).group(1)
                    bag_qty = int(re.search(r"(\d*)", inner_bag).group(1))
                    if bag_name in add_to_bag_dict:
                        add_to_bag_dict[bag_name] = (
                            add_to_bag_dict[bag_name] + bag_qty * number_of_bags_dict[bag.colour]
                        )
                    else:
                        add_to_bag_dict[bag_name] = bag_qty * number_of_bags_dict[bag.colour]
        number_of_bags_dict = add_to_bag_dict
        number_of_bags_counter += sum(number_of_bags_dict.values())

        dict_size = sum(number_of_bags_dict.values())

    return number_of_bags_counter


if __name__ == "__main__":
    print("Part 1: ", Day7Q1())
    print("Part 2: ", Day7Q2())
