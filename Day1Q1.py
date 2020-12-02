f = open("input.txt", "r")
input = f.read()
split_input_string = input.split()
split_input_int = [int(i) for i in split_input_string]

answer_tuple = (0,0)
remainder_set = set()

for x in split_input_int:
    remainder_set.add(2020-x)
    if x in remainder_set:
        answer_tuple = (x, 2020-x)
        break

print("Answer tuple: " + str(answer_tuple))
print("Multiplied: " + str(answer_tuple[0] * answer_tuple[1]))
