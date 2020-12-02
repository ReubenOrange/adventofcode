import re

def Day2Q1():

	lines = [line.strip() for line in open('input.txt')]

	#counter = 0
	num_valid_passwords = 0

	for line in lines:


		lower_bound = re.search("([0-9]+)-",line).group(1)
		
		upper_bound = re.search("-([0-9]+)",line).group(1)
		
		policy = re.search(" (.):",line).group(1)

		letter_count = 0 #count the number of times the policy letter appears in the password

		password = re.search(": (.*)",line).group(1)
		print(password)

		for letter in password:
			if letter == policy:
				letter_count += 1
		
		if letter_count > lower_bound and letter_count < upper_bound:
			num_valid_passwords += 1

		break

	print("Number of valid passwords: " + str(num_valid_passwords))







		#do the check

	print(lower_bound)
	print(upper_bound)
	print(type(lower_bound))


if __name__ == "__main__":
	Day2Q1()
