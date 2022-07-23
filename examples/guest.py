filename = 'guest.txt'

while True:
	name = input("What is your name?")
	
	# Print greeting to visitor
	print(f"Welcome, {name}!\n")

	# Record visitor's name in text file
	with open(filename,'a') as file_object:
		file_object.write(f"{name.title()} has visited this page.\n")

	# Check if there are other visitors
	response = input("Are there any other visitors? y/n")
	if response == 'n':
		break