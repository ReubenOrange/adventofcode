import aocd

import typing as t


def Day11Q1(seat_layout: t.List[t.List]) -> int:

    new_layout = []
    occupied_seats = sum(x.count("#") for x in seat_layout)
    new_occupied_seats = None

    # do while there is a change in the number of empty seats:
    while occupied_seats != new_occupied_seats:

        occupied_seats = sum(x.count("#") for x in seat_layout)
        new_layout = [x[:] for x in seat_layout]
        for i in range(len(seat_layout)):
            for j in range(len(seat_layout[i])):
                adjacent_seats = []
                if i - 1 >= 0 and j - 1 >= 0:
                    adjacent_seats.append(seat_layout[i - 1][j - 1])
                if i - 1 >= 0:
                    adjacent_seats.append(seat_layout[i - 1][j])
                if i - 1 >= 0 and j + 1 < len(seat_layout[i]):
                    adjacent_seats.append(seat_layout[i - 1][j + 1])
                if j - 1 >= 0:
                    adjacent_seats.append(seat_layout[i][j - 1])
                if j + 1 < len(seat_layout[i]):
                    adjacent_seats.append(seat_layout[i][j + 1])
                if i + 1 < len(seat_layout) and j - 1 >= 0:
                    adjacent_seats.append(seat_layout[i + 1][j - 1])
                if i + 1 < len(seat_layout):
                    adjacent_seats.append(seat_layout[i + 1][j])
                if i + 1 < len(seat_layout) and j + 1 < len(seat_layout[i]):
                    adjacent_seats.append(seat_layout[i + 1][j + 1])

                # update seat layout based on adjacent seats
                if seat_layout[i][j] == "#" and adjacent_seats.count("#") >= 4:
                    new_layout[i][j] = "L"
                if seat_layout[i][j] == "L" and adjacent_seats.count("#") == 0:
                    new_layout[i][j] = "#"
        new_occupied_seats = sum(x.count("#") for x in new_layout)
        # string_list = ["".join(x) for x in new_layout]
        # bulk_string = "\n".join(string_list)
        # print(bulk_string)
        # print()
        # print(occupied_seats)
        seat_layout = [x[:] for x in new_layout]

    return occupied_seats

def Day11Q2(seat_layout: t.List[t.List]) -> int:
    new_layout = []
    occupied_seats = sum(x.count("#") for x in seat_layout)
    new_occupied_seats = None
    while occupied_seats != new_occupied_seats:

        occupied_seats = sum(x.count("#") for x in seat_layout)
        new_layout = [x[:] for x in seat_layout]
        for i in range(len(seat_layout)):
            for j in range(len(seat_layout[i])):
                visible_seats = []
                
                #check up left
                k = 0
                while i - 1 - k >= 0 and j - 1 - k >= 0:
                    if seat_layout[i - 1 - k][j - 1 - k] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i - 1 - k][j - 1 - k])
                        break
                
                #check up
                k = 0
                while i - 1 - k >= 0:
                    if seat_layout[i - 1 - k][j] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i - 1 - k][j])
                        break

                #check up right
                k = 0
                while i - 1 - k >= 0 and j + 1 + k < len(seat_layout[i]):
                    if seat_layout[i - 1 - k][j + 1 + k] == ".":
                        k+=1
                    else:
                        visible_seats.append(seat_layout[i - 1 - k][j + 1 + k])
                        break
                
                #check left
                k = 0
                while j - 1 - k >= 0:
                    if seat_layout[i][j - 1 - k] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i][j - 1 - k])
                        break
                
                #check right
                k = 0
                while j + 1 + k < len(seat_layout[i]):
                    if seat_layout[i][j + 1 + k] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i][j + 1 + k])
                        break
                
                #check down left
                k = 0
                while i + 1 + k < len(seat_layout) and j - 1 - k >= 0:
                    if seat_layout[i + 1 + k][j - 1 - k] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i + 1 + k][j - 1 - k])
                        break
                
                #check down
                k = 0
                while i + 1 + k < len(seat_layout):
                    if seat_layout[i + 1 + k][j] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i + 1 + k][j])
                        break
                
                #check down right
                k = 0
                while i + 1 + k < len(seat_layout) and j + 1 + k < len(seat_layout[i]):
                    if seat_layout[i + 1 + k][j + 1 + k] == ".":
                        k += 1
                    else:
                        visible_seats.append(seat_layout[i + 1 + k][j + 1 + k])
                        break

                if seat_layout[i][j] == "#" and visible_seats.count("#") >= 5:
                    new_layout[i][j] = "L"
                if seat_layout[i][j] == "L" and visible_seats.count("#") == 0:
                    new_layout[i][j] = "#"

        new_occupied_seats = sum(x.count("#") for x in new_layout)
        # This part is to print the seat layout in the terminal
        # string_list = ["".join(x) for x in new_layout]
        # bulk_string = "\n".join(string_list)
        # print(bulk_string)
        # print()
        # print(occupied_seats)
        seat_layout = [x[:] for x in new_layout]


            
                    

    return occupied_seats



if __name__ == "__main__":
    seat_layout = [list(x) for x in aocd.get_data(day=11, year=2020).splitlines()]

    print("Part 1: ", Day11Q1(seat_layout))
    print("Part 2: ", Day11Q2(seat_layout))
