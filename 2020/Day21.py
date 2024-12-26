import aocd
import typing as t
import re
from collections import defaultdict


class Food:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

    def __str__(self):
        return "ingredients: %s \nallergens: %s \n" % (self.ingredients, self.allergens)


def Day21Q(food_list: t.List[Food]) -> int:

    # create allergen dictionary where the key is the name of the allergen and the value is a set of possible ingredients
    allergen_dict = {}
    for f in food_list:
        for a in f.allergens:
            if a in allergen_dict:
                # allergen_dict[a] = allergen_dict[a].intersection(f.ingredients)
                allergen_dict[a] = allergen_dict[a] & f.ingredients
            else:
                allergen_dict[a] = f.ingredients

    known_allergens = set(x for x in allergen_dict.keys() if len(allergen_dict[x]) == 1)

    # Loop through the allegen_dict trimming off foods that map to only one allergen until all foods map to only one allergen
    while True:
        known_allergens = set(x for x in allergen_dict.keys() if len(allergen_dict[x]) == 1)
        for a in allergen_dict:
            for f in known_allergens:
                if len(allergen_dict[a]) > 1:
                    allergen_dict[a].discard(next(iter(allergen_dict[f])))

        if len(known_allergens) == len(allergen_dict):
            break

    known_foods = set(next(iter(allergen_dict[x])) for x in known_allergens)

    # ans = 0
    # for f in food_list:
    #    for i in f.ingredients:
    #        if i not in known_foods:
    #            ans += 1

    # Sum of ingredients that can't contain any of the listed allergens
    ans = sum(1 for f in food_list for i in f.ingredients if i not in known_foods)

    yield ans

    ans2 = ",".join(next(iter(allergen_dict[a])) for a in sorted(allergen_dict))

    yield ans2


if __name__ == "__main__":

    data = aocd.get_data(day=21, year=2020)

    food_list = []

    for line in data.splitlines():

        i1, a1 = line.split(" (contains ")
        i1 = set(i1.split())
        a1 = set(a1[:-1].split(", "))

        food_list.append(Food(i1, a1))

    part = 1
    for ans in Day21Q(food_list):
        print("Part %s: %s" % (str(part), str(ans)))
        part += 1
