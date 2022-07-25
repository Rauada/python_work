print("Enter 'q' at any time to quit.\n")

while True:
	try:
		x = input("\nChoose first number:")
		if x == 'q':
			break
		x = int(x)

		y = input("\nChoose second number:")
		if y == 'q':
			break
		y = int(y)
	except ValueError:
		print("One of your inputs is not a number.")
	else:
		sum = int(x) + int(y)
		print(sum)