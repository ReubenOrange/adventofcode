from collections.abc import Iterable
import re


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def check_passport_validityQ1(passport):
    #cid not required
    required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    return all(field in passport for field in required_fields)

def check_passport_validityQ2(passport):
    """
    Conditions of validity:
    Required fields present:  ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """

    #cid not required
    required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    required_fields_present = all(field in passport for field in required_fields)

    if required_fields_present:
        bry_check = int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002
        iyr_check = int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
        eyr_check = int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030
        hgt_check = bool(re.match("(1[5-8][0-9]|19[0-3])cm",passport["hgt"])) or bool(re.match("(59|6[0-9]|7[0-6])in",passport["hgt"]))
        hcl_check = bool(re.match("(#[0-9a-f]{6})",passport["hcl"]))
        ecl_check = passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
        pid_check = bool(re.match(r"(?=.*\b(\d{9})\b)",passport["pid"])) #taken from Josh's solution

        return (bry_check and iyr_check and eyr_check and hgt_check and hcl_check and ecl_check and pid_check)

    else: 
        return False


def create_list_of_passport_dicts():
    input = [line for line in open("input.txt")]

    passport_list = []
    add_new_entry = True
    list_position = 0

    #create a list of the passports, using the \n character to delimit them
    #this will be a list of strings, some of which will be nested in lists
    for line in input:
        if add_new_entry:
            passport_list.append(line.split())
            add_new_entry = False
        elif line == "\n":
            add_new_entry = True
            list_position += 1
        else:
            passport_list[list_position].append(line.split())
    
    #flatten out the passport list, so that each list element is an iterator of strings, one string for each passport field
    flat_passport_list = []
    for passport in passport_list:
        flat_passport_list.append(flatten(passport))
    
    #turn each of the passports into a dictionary
    list_of_passport_dicts = []
    for passport in flat_passport_list:
        passport_dict = {}
        for item in passport:
            passport_dict[item.split(":")[0]] = item.split(":")[1]
        list_of_passport_dicts.append(passport_dict)
    
    return list_of_passport_dicts


def Day4Q1():

    list_of_passport_dicts = create_list_of_passport_dicts()

    #count the number of passports that have all the required fields
    num_valid_passports = 0
    for passport in list_of_passport_dicts:
        if check_passport_validityQ1(passport):
            num_valid_passports += 1

    
    print("Q1:")
    print("Number of passports: " + str(len(list_of_passport_dicts)))
    print("Number of valid passports: " + str(num_valid_passports))

def Day4Q2():

    list_of_passport_dicts = create_list_of_passport_dicts()

    #count the number of passports that have all the required fields
    num_valid_passports = 0
        
    for passport in list_of_passport_dicts:
        if check_passport_validityQ2(passport):
            num_valid_passports += 1
    
    print("Q2:")
    print("Number of passports: " + str(len(list_of_passport_dicts)))
    print("Number of valid passports: " + str(num_valid_passports))


def testing():

    valid_test1 = {"pid":"087499704","hgt":"74in","ecl":"grn","iyr":"2012","eyr":"2030","byr":"1980","hcl":"#623a2f"}
    valid_test2 = {"eyr":"2029","ecl":"blu","cid":"129","byr":"1989","iyr":"2014","pid":"896056539","hcl":"#a97842","hgt":"165cm"}
    valid_test3 = {"hcl":"#888785","hgt":"164cm","byr":"2001","iyr":"2015","cid":"88","pid":"545766238","ecl":"hzl","eyr":"2022"}
    valid_test4 = {"iyr":"2010","hgt":"158cm","hcl":"#b6652a","ecl":"blu","byr":"1944","eyr":"2021","pid":"093154719"}

    invalid_test1 = {"eyr":"1972","cid":"100","hcl":"#18171d","ecl":"amb","hgt":"170","pid":"186cm","iyr":"2018","byr":"1926"}
    invalid_test2 = {"iyr":"2019","hcl":"#602927","eyr":"1967","hgt":"170cm","ecl":"grn","pid":"012533040","byr":"1946"}
    invalid_test3 = {"hcl":"dab227","iyr":"2012","ecl":"brn","hgt":"182cm","pid":"021572410","eyr":"2020","byr":"1992","cid":"277"}
    invalid_test4 = {"hgt":"59cm","ecl":"zzz","eyr":"2038","hcl":"74454a","iyr":"2023","pid":"3556412378","byr":"2007"}
    invalid_test5 = {"byr":"1971","iyr":"2012","eyr":"2039","hgt":"172in","hcl":"17106b","ecl":"gry","pid":"170cm","cid":"339"}
    
    print("Valid tests (should return True):")
    print(check_passport_validityQ2(valid_test1))
    print(check_passport_validityQ2(valid_test2))
    print(check_passport_validityQ2(valid_test3))
    print(check_passport_validityQ2(valid_test4))

    print("Invalid tests (should return False):")
    print(check_passport_validityQ2(invalid_test1))
    print(check_passport_validityQ2(invalid_test2))
    print(check_passport_validityQ2(invalid_test3))
    print(check_passport_validityQ2(invalid_test4))
    print(check_passport_validityQ2(invalid_test5))


if __name__ == "__main__":
#    testing()
    Day4Q1()
    Day4Q2()