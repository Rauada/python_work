# if age < 3 => free
# if 3 <= age < 12 => $10
# if age >= 12 => $15

prompt = "\nWhat is your age?"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	age = input(prompt)
	if age == 'quit':
		break 
	elif age < 3:
		print("Your ticket is free.")
	elif age < 12:
		print("Your ticket costs $10 dollars.")
	else:
		print("Your ticker costs $15 dollars.")
