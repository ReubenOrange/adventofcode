#%%
def Day5Q1():

    input = [line.strip() for line in open("input.txt")]

    max_seat_id = 0

    for seat in input:
        row = int(seat[0:7].replace("B","1").replace("F","0"),2)
        column = int(seat[7:10].replace("R","1").replace("L","0"),2)
        seat_id = row * 8 + column
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        #print("row: ", row)
        #print("column: ", column)
        #print("seat_id: ", seat_id)
    
    return max_seat_id

def Day5Q2():

    input = {int(line.strip().replace("B","1").replace("R","1").replace("F","0").replace("L","0"),2) for line in open("input.txt")}

    for i in range(min(input),max(input)):
        if i not in input:
            return i


if __name__ == "__main__":
    print("Q1 - Max seat id: ", Day5Q1())
    print("Q2 - Missing seat id:", Day5Q2())
# %%
