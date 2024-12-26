import aocd
import typing as t
import re

# https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
def push(t.list: obj, t.list: l, int: depth) -> None:
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)


# https://stackoverflow.com/questions/4284991/parsing-nested-parentheses-in-python-grab-content-by-level
def parse_parentheses(s: str) -> t.List:
    groups = []
    depth = 0

    try:
        for char in s:
            if char == "(":
                push([], groups, depth)
                depth += 1
            elif char == ")":
                depth -= 1
            else:
                push(char, groups, depth)
    except IndexError:
        raise ValueError("Parentheses mismatch")

    if depth > 0:
        raise ValueError("Parentheses mismatch")
    else:
        return groups


def paren_parse(equation_list: t.List) -> t.List:

    num_letters = 0.5 * len(equation_list) + 0.5

    num_prepend_parens = int(max(num_letters - 1, 1))

    parsed_equation_list = []

    parsed_equation_list.append("(" * num_prepend_parens)

    for i in range(0, len(equation_list)):

        if isinstance(equation_list[i], list) and (i == len(equation_list) - 1 or i == 0):
            parsed_equation_list.append(paren_parse(equation_list[i]))
        elif (
            isinstance(equation_list[i], list)
            and (i % 2 == 0)
            and (i != 0)
            and i != len(equation_list) - 1
        ):
            parsed_equation_list.append(paren_parse(equation_list[i]) + ")")
        elif isinstance(equation_list[i], list):
            parsed_equation_list.append("(" + paren_parse(equation_list[i]))
        elif (i % 2 == 0) and (i != 0) and i != len(equation_list) - 1:
            parsed_equation_list.append(equation_list[i] + ")")
        else:
            parsed_equation_list.append(equation_list[i])

    return "".join(parsed_equation_list) + ")"


def Day18Q1(equations: t.List) -> int:

    # a + b --> (a+b)
    # a + b + c --> ((a+b)+c)
    # a + b + c + d --> (((a+b)+c)+d)
    # a + b + c + d + e --> ((((a+b)+c)+d)+e)

    total = 0

    for equation in equations:
        equation_list = parse_parentheses(equation.replace(" ", ""))
        parsed_equation = paren_parse(equation_list)
        total += eval(parsed_equation)

    return total


# global variables
PRECEDENCE = {"+": 2, "*": 1}
OP_LIST = list(PRECEDENCE.keys())


def Day18Q2(equations: t.List) -> int:

    # Going to take a different tact, and try to use the algorithm described here:
    # https://en.wikipedia.org/wiki/Operator-precedence_parser

    total = 0

    for equation in equations:
        equation_list = parse_parentheses(equation.replace(" ", ""))
        result, _ = parse_expression(equation_list[0], 0, equation_list, 0)
        total += result

    return total


def parse_expression(lhs: str, min_precedence: int, tokens: t.List, pointer: int) -> (int, int):

    if type(lhs) is list:
        lhs, _ = parse_expression(lhs[0], 0, lhs, 0)

    lookahead = get_lookahead(tokens, pointer)

    while (lookahead in OP_LIST) and (PRECEDENCE[lookahead] >= min_precedence):
        op = lookahead
        # advance to next token that is a number
        pointer += 2
        rhs = tokens[pointer]
        if type(rhs) is list:
            rhs, _ = parse_expression(rhs[0], 0, rhs, 0)
            rhs = str(rhs)

        lookahead = get_lookahead(tokens, pointer)
        while (lookahead in OP_LIST) and (PRECEDENCE[lookahead] > PRECEDENCE[op]):
            rhs, pointer = parse_expression(rhs, PRECEDENCE[lookahead], tokens, pointer)
            rhs = str(rhs)
            lookahead = get_lookahead(tokens, pointer)
        lhs = eval(str(lhs) + op + str(rhs))
    return int(lhs), pointer


def get_lookahead(tokens: t.List, pointer: int) -> str:
    if pointer + 1 >= len(tokens):
        return None
    else:
        return tokens[pointer + 1]


if __name__ == "__main__":

    equations = [x.strip() for x in aocd.get_data(day=18, year=2020).splitlines()]

    print("Part 1:", Day18Q1(equations))
    print("Part 2:", Day18Q2(equations))
