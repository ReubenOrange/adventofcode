import re

def Day2Q1():

	lines = [line.strip() for line in open('input.txt')]

	num_valid_passwords = 0

	for line in lines:

		lower_bound = int(re.search("([0-9]+)-",line).group(1))
		upper_bound = int(re.search("-([0-9]+)",line).group(1))
		policy = re.search(" (.):",line).group(1)
		password = re.search(": (.*)",line).group(1)

		letter_count = 0 #count the number of times the policy letter appears in the password

		for letter in password:
			if letter == policy:
				letter_count += 1
		
		#if letter count is between upper and lower bound, increment number of valid passwords by 1
		if letter_count >= lower_bound and letter_count <= upper_bound:
			num_valid_passwords += 1

	print("Number of valid passwords: " + str(num_valid_passwords))


def Day2Q2():

	lines = [line.strip() for line in open('input.txt')]

	num_valid_passwords = 0

	for line in lines:
		position1 = int(re.search("([0-9]+)-",line).group(1))
		position2 = int(re.search("-([0-9]+)",line).group(1))
		policy = re.search(" (.):",line).group(1)
		password = re.search(": (.*)",line).group(1)

		#returning true/false if the policy letter is in position 1/2
		position1_check = password[position1-1] == policy

		position2_check = password[position2-1] == policy

		if (not position1_check and position2_check) or (not position2_check and position1_check):
			num_valid_passwords += 1

	print("Number of valid passwords: " + str(num_valid_passwords))



if __name__ == "__main__":
	Day2Q1()
	Day2Q2()
