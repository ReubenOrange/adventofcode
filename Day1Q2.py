f = open("input.txt", "r")
input = f.read()
split_input_string = input.split()
split_input_int = [int(i) for i in split_input_string] 

answer_tuple = (0,0)

for x in split_input_int:
    for y in split_input_int:
        for z in split_input_int:
            if x+y+z == 2020:
                answer_tuple = (x,y,z)
                break                

print("Answer tuple: " + str(answer_tuple))
print("Multiplied: " + str(answer_tuple[0] * answer_tuple[1] * answer_tuple[2]))