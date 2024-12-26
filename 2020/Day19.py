"""
0: 4 1 5
1: 2 3 | 3 2
2: a a | b b
3: a b | b a
4: "a"
5: "b"

Can be turned into regex:
(a)((aa|bb)(ab|ba)|(ab|ba)(aa|bb))(b)
Add a ^ and $ start and end of the line respectively to match the full line

Otherwise, one could also build up a list of matches:

4: "a"
5: "b"
3: ["ab","ba"]
2: ["aa","ba"]
1: ["aaab","aaab","baab","baba","abaa","abbb","baaa","babb"]
0: 
"""

import aocd
import re
import typing as t

Rules = t.Dict[int, str]
Messages = t.List[str]
InputData = t.Tuple[Rules, Messages]


def parse_input(data: str) -> InputData:
    rules: Rules = {}
    messages: Messages = []

    rules_str, messages_str = data.split("\n\n")

    rules_re = re.compile(r"(?P<rule_num>\d+): (?P<rule>.*)$")

    for line in rules_str.splitlines():
        rules_match = rules_re.match(line).groupdict()
        rules[rules_match["rule_num"]] = rules_match["rule"]

    for line in messages_str.splitlines():
        messages.append(line)

    return rules, messages


def create_re_non_looping(rules: Rules, start_rule: str) -> str:

    final_re_rule_length = -1
    new_re_rule_length = 0

    rule_tok = re.findall(r"\d+|[\|ab]", rules[start_rule])

    while new_re_rule_length > final_re_rule_length:

        final_re_rule_length = new_re_rule_length
        new_re_rule = ""
        for element in rule_tok:
            if element not in ["(", ")", "|", "a", "b"]:
                new_re_rule += "( "
                new_re_rule += rules[element]
                new_re_rule += " )"
            else:
                new_re_rule += element

        rule_tok = re.findall(r"\d+|[\|\(\)ab]", new_re_rule)
        new_re_rule_length = len(rule_tok)

    final_re_rule = "".join(rule_tok).replace(" ", "").replace("(a)", "a").replace("(b)", "b")

    return final_re_rule


def Day19Q1(rules: Rules, messages: Messages) -> int:

    final_re_rule = "^" + create_re_non_looping(rules, "0") + "$"

    # print(final_re_rule)

    matches = 0

    for message in messages:
        if re.match(final_re_rule, message):
            matches += 1

    return matches


def Day19Q2(rules: Rules, messages: Messages) -> int:

    # rules["8"] = "42 | 42 8"
    # rules["11"] = "42 31 | 42 11 31"

    re_rule_42 = create_re_non_looping(rules, "42")
    re_rule_31 = create_re_non_looping(rules, "31")

    # print("Rule 42:", re_rule_42)
    # print("Rule 31:", re_rule_31)

    """
    If:
    rule 31 = X
    rule 42 = Y

    then:
    rule 8 = Y | Y 8 --> (Y)^n 
    rule 11 = Y X | Y 11 X --> (Y)^m (X)^m
    where n,m are a integers > 0
    
    therefore:
    rule 0 = 8 11 -> ((Y)^n) ((Y)^m (X)^m)
    """

    X = "(" + re_rule_31 + ")"
    Y = "(" + re_rule_42 + ")"

    # re_rule_0 = "(" + Y + ")(" + Y + X + ")"
    # print("re_rule_0:", re_rule_0)

    matched_messages = set()
    matches = 0

    # setting n and m to 10 should be enough to find all matches

    for m in range(1, 10):
        for n in range(1, 10):
            re_rule = "^(" + Y * n + ")(" + Y * m + X * m + ")" + "$"
            for message in messages:
                if re.match(re_rule, message) and message not in matched_messages:
                    matches += 1
                    matched_messages.add(message)
                    # print(f"m: {m}, n: {n}, match found: {message}")

    return matches


# tokenize('(1 + 2) * 3') -> ['(', '1', '+', '2', ')', '*', '3']
def tokenize(expr):
    return re.findall(r"\d+|[\|ab]", expr)


if __name__ == "__main__":

    data = aocd.get_data(day=19, year=2020)

    rules, messages = parse_input(data)

    print("Part 1:", Day19Q1(rules, messages))
    print("Part 2:", Day19Q2(rules, messages))
