# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
number = input("Please choose a number")

# Convert the input string into integer.
number = int(number)

# Checks if the number is a multiple of ten.
if number % 10 == 0:
	print("Your number is a multiple of ten")
else:
	print("Your number is NOT a multiple of ten")