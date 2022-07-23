def addition(x,y):
	try:
		result = int(x) + int(y)
	except ValueError:
		print("One of your inputs is not a number.")
	else:
		print(result)

first_number = input("Choose first number:")
second_number = input("Choose second number:")
addition(first_number,second_number)