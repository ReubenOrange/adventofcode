f = open("Day1Input.txt", "r")

sum = 0
x1_list = []
x2_list = []

for line in f.readlines():
    # x1, x2 = 
    x1, x2 = line.split()
    x1_list += [int(x1)]
    x2_list += [int(x2)]
    # print(x1, x2)

x1_list.sort()
x2_list.sort()

for x1, x2 in zip(x1_list, x2_list):
    sum += abs(x1 - x2)
    
print(sum)




f = open("Day1Input.txt", "r")

x1_list = []
x2_list = []

for line in f.readlines():
    x1, x2 = line.split()
    x1_list += [int(x1)]
    x2_list += [int(x2)]

sim_score = 0

for x1 in x1_list:
    for x2 in x2_list:
        if x1 == x2:
            sim_score += x1
    
print("similarity score: ", sim_score)
